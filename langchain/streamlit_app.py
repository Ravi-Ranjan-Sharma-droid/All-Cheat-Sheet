import streamlit as st
import os
from langchain.llms import OpenAI
from langchain.chat_models import ChatOpenAI
from langchain.chains import ConversationChain, RetrievalQA
from langchain.memory import ConversationBufferMemory
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.vectorstores import Chroma
from langchain.callbacks import StreamlitCallbackHandler

# Page configuration
st.set_page_config(page_title="LangChain Demo", page_icon="🦜")
st.title("🦜 LangChain Interactive Demo")

# Sidebar for API key and settings
with st.sidebar:
    st.header("Settings")
    api_key = st.text_input("OpenAI API Key", type="password")
    if api_key:
        os.environ["OPENAI_API_KEY"] = api_key
    
    temperature = st.slider("Temperature", min_value=0.0, max_value=1.0, value=0.7, step=0.1)
    model_name = st.selectbox("Model", ["gpt-3.5-turbo", "gpt-4"])

# Initialize session state for chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat history
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Function to initialize LangChain components
def initialize_langchain():
    if not api_key:
        st.warning("Please enter your OpenAI API key in the sidebar.")
        return None, None
    
    # Initialize chat model
    chat_model = ChatOpenAI(
        model_name=model_name,
        temperature=temperature,
        streaming=True
    )
    
    # Initialize memory
    memory = ConversationBufferMemory(return_messages=True)
    
    # Initialize conversation chain
    conversation = ConversationChain(
        llm=chat_model,
        memory=memory,
        verbose=True
    )
    
    return chat_model, conversation

# Function to handle RAG if data is available
def initialize_rag():
    if not api_key:
        return None
    
    if not os.path.exists("data"):
        return None
    
    try:
        # Initialize embeddings
        embeddings = OpenAIEmbeddings()
        
        # Load or create vector store
        if os.path.exists("chroma_db") and os.listdir("chroma_db"):
            vector_store = Chroma(persist_directory="chroma_db", embedding_function=embeddings)
        else:
            st.info("No existing vector store found. Please add documents to the 'data' folder.")
            return None
        
        # Initialize retrieval QA chain
        chat_model, _ = initialize_langchain()
        if not chat_model:
            return None
        
        retrieval_qa = RetrievalQA.from_chain_type(
            llm=chat_model,
            chain_type="stuff",
            retriever=vector_store.as_retriever()
        )
        
        return retrieval_qa
    except Exception as e:
        st.error(f"Error initializing RAG: {e}")
        return None

# Chat input
if prompt := st.chat_input("What would you like to know?"):
    # Add user message to chat history
    st.session_state.messages.append({"role": "user", "content": prompt})
    
    # Display user message
    with st.chat_message("user"):
        st.markdown(prompt)
    
    # Display assistant response
    with st.chat_message("assistant"):
        # Initialize callback handler for streaming
        st_callback = StreamlitCallbackHandler(st.container())
        
        # Get response based on mode
        response_container = st.empty()
        
        # Initialize LangChain components
        _, conversation = initialize_langchain()
        
        if not conversation:
            st.warning("Please configure your API key to continue.")
        else:
            # Get response
            with st.spinner("Thinking..."):
                response = conversation.predict(input=prompt, callbacks=[st_callback])
                response_container.markdown(response)
            
            # Add assistant response to chat history
            st.session_state.messages.append({"role": "assistant", "content": response})

# RAG query section
st.divider()
st.header("📚 Document Question Answering")

rag_query = st.text_input("Ask a question about your documents:")
if rag_query:
    retrieval_qa = initialize_rag()
    
    if not retrieval_qa:
        st.warning("Document retrieval is not available. Please check your API key and data folder.")
    else:
        with st.spinner("Searching documents..."):
            # Initialize callback handler for streaming
            st_callback = StreamlitCallbackHandler(st.container())
            
            # Get response
            response = retrieval_qa.run(rag_query, callbacks=[st_callback])
            st.markdown(response)

# Footer
st.divider()
st.caption("Powered by LangChain 🦜️🔗 and Streamlit")
import boto3
import json
from langchain.llms import Bedrock
from langchain.chains import ConversationChain
from langchain.memory import DynamoDBChatMessageHistory

# AWS Lambda handler
def lambda_handler(event, context):
    # Initialize Bedrock LLM
    llm = Bedrock(
        model_id="anthropic.claude-v2",
        region_name="us-east-1"
    )
    
    # Get session ID from event
    session_id = event.get('session_id', 'default')
    
    # Initialize DynamoDB memory
    message_history = DynamoDBChatMessageHistory(
        table_name="langchain-chat-history",
        session_id=session_id
    )
    
    # Create conversation chain
    conversation = ConversationChain(
        llm=llm,
        memory=message_history
    )
    
    # Process user input
    user_input = event.get('message', '')
    response = conversation.predict(input=user_input)
    
    return {
        'statusCode': 200,
        'body': json.dumps({
            'response': response,
            'session_id': session_id
        })
    }
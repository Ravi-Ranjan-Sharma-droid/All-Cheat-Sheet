# Evaluation

Evaluating LangChain applications is crucial for ensuring they meet quality standards and perform as expected. This section covers various evaluation techniques and metrics for LangChain applications.

## Basic Evaluation

```python
from langchain.evaluation import QAEvalChain
from langchain.llms import OpenAI

# Define examples
examples = [
    {
        "query": "What is the capital of France?",
        "answer": "The capital of France is Paris."
    },
    {
        "query": "Who wrote 'Romeo and Juliet'?",
        "answer": "William Shakespeare wrote 'Romeo and Juliet'."
    }
]

# Define predictions
predictions = [
    "Paris is the capital of France.",
    "The play 'Romeo and Juliet' was written by Shakespeare."
]

# Initialize the LLM
llm = OpenAI(temperature=0)

# Create the evaluation chain
evaluation_chain = QAEvalChain.from_llm(llm)

# Evaluate the predictions
graded_outputs = evaluation_chain.evaluate(
    examples,
    predictions,
    question_key="query",
    prediction_key="answer"
)

# Print the results
for i, (example, prediction) in enumerate(zip(examples, predictions)):
    print(f"Example {i+1}:")
    print(f"Query: {example['query']}")
    print(f"Expected: {example['answer']}")
    print(f"Predicted: {prediction}")
    print(f"Evaluation: {graded_outputs[i]['text']}")
    print()
```

## Criteria-Based Evaluation

```python
from langchain.evaluation import load_evaluator
from langchain.evaluation.criteria import Criteria

# Initialize the evaluator for a specific criterion
accuracy_evaluator = load_evaluator("criteria", criteria=Criteria.ACCURACY)

# Evaluate a prediction
result = accuracy_evaluator.evaluate_strings(
    prediction="Paris is the capital of France.",
    reference="The capital of France is Paris."
)

print(f"Accuracy score: {result['score']}")
print(f"Reasoning: {result['reasoning']}")

# Evaluate multiple criteria at once
multi_criteria_evaluator = load_evaluator(
    "criteria",
    criteria={
        "accuracy": "Is the response accurate based on the reference?",
        "conciseness": "Is the response concise and to the point?",
        "harmfulness": "Does the response contain harmful, unethical, or illegal content?"
    }
)

result = multi_criteria_evaluator.evaluate_strings(
    prediction="Paris is the beautiful and historic capital city of France, known for its art, culture, and cuisine.",
    reference="The capital of France is Paris."
)

print("Multi-criteria evaluation:")
for criterion, score in result["criteria"].items():
    print(f"{criterion}: {score}")
print(f"Reasoning: {result['reasoning']}")
```

## Custom Evaluation Metrics

```python
from langchain.evaluation import load_evaluator, EvaluatorType
from langchain.chat_models import ChatOpenAI

# Define a custom rubric
custom_rubric = """
Score the response on a scale from 1 to 5 based on the following criteria:

1. Factual accuracy: Is the information correct and supported by widely accepted facts?
2. Completeness: Does the response fully address all aspects of the query?
3. Clarity: Is the response clear, well-organized, and easy to understand?
4. Helpfulness: Is the response helpful and relevant to the query?

Provide a score for each criterion and an overall score, along with a brief explanation.
"""

# Initialize the custom evaluator
custom_evaluator = load_evaluator(
    EvaluatorType.CUSTOM,
    llm=ChatOpenAI(temperature=0, model="gpt-4"),
    evaluation_template=custom_rubric
)

# Evaluate a prediction
result = custom_evaluator.evaluate_strings(
    prediction="Paris is the capital and largest city of France. It is located on the Seine River in the north-central part of the country. Paris is known for its art, culture, fashion, and cuisine. It is home to famous landmarks such as the Eiffel Tower, the Louvre Museum, and Notre-Dame Cathedral.",
    input="What is the capital of France?"
)

print(f"Evaluation result: {result['feedback']}")
```

## Semantic Similarity Evaluation

```python
from langchain.evaluation import load_evaluator, EvaluatorType

# Initialize the embedding evaluator
embedding_evaluator = load_evaluator(EvaluatorType.EMBEDDING_DISTANCE)

# Evaluate semantic similarity
result = embedding_evaluator.evaluate_strings(
    prediction="Paris is the capital of France.",
    reference="The capital of France is Paris."
)

print(f"Cosine similarity: {result['score']}")

# You can also use other distance metrics
from langchain.evaluation.embedding_distance import EmbeddingDistance

euclidean_evaluator = load_evaluator(
    EvaluatorType.EMBEDDING_DISTANCE,
    distance_metric=EmbeddingDistance.EUCLIDEAN
)

result = euclidean_evaluator.evaluate_strings(
    prediction="Paris is the capital of France.",
    reference="The capital of France is Paris."
)

print(f"Euclidean distance: {result['score']}")
```

## Evaluating RAG Systems

```python
from langchain.evaluation import load_evaluator
from langchain.evaluation.schema import StringEvaluator

# Initialize the RAG evaluator
rag_evaluator = load_evaluator("labeled_rag_criteria")

# Define a query, context, and response
query = "What are the health benefits of green tea?"
context = [
    "Green tea contains antioxidants called catechins, which have been shown to boost metabolism and aid in weight loss.",
    "Studies have found that green tea may help reduce the risk of heart disease by lowering cholesterol levels and improving blood vessel function.",
    "Regular consumption of green tea has been associated with a lower risk of certain types of cancer, including breast, prostate, and colorectal cancer."
]
response = "Green tea offers several health benefits, including weight loss support through metabolism-boosting antioxidants called catechins, reduced risk of heart disease by improving cholesterol levels and blood vessel function, and potential cancer prevention properties for breast, prostate, and colorectal cancers."

# Evaluate the RAG response
result = rag_evaluator.evaluate_strings(
    prediction=response,
    input=query,
    reference=context
)

print("RAG Evaluation:")
for criterion, score in result["criteria"].items():
    print(f"{criterion}: {score}")
print(f"Reasoning: {result['reasoning']}")
```

## Comprehensive Evaluation Framework

```python
from langchain.evaluation import EvaluatorType, load_evaluator
from langchain.chat_models import ChatOpenAI
from typing import Dict, List, Any
import pandas as pd

class ComprehensiveEvaluator:
    """A comprehensive evaluation framework for LangChain applications."""
    
    def __init__(self, llm=None):
        """Initialize the evaluator with various evaluation methods."""
        self.llm = llm or ChatOpenAI(temperature=0)
        
        # Initialize evaluators
        self.evaluators = {
            "accuracy": load_evaluator("criteria", criteria="accuracy", llm=self.llm),
            "relevance": load_evaluator("criteria", criteria="relevance", llm=self.llm),
            "coherence": load_evaluator("criteria", criteria="coherence", llm=self.llm),
            "harmfulness": load_evaluator("criteria", criteria="harmfulness", llm=self.llm),
            "semantic_similarity": load_evaluator(EvaluatorType.EMBEDDING_DISTANCE),
            "qa": load_evaluator(EvaluatorType.QA, llm=self.llm)
        }
    
    def evaluate(self, examples: List[Dict[str, Any]]) -> pd.DataFrame:
        """Evaluate a list of examples and return a DataFrame with results."""
        results = []
        
        for i, example in enumerate(examples):
            query = example["query"]
            reference = example["reference"]
            prediction = example["prediction"]
            context = example.get("context", None)
            
            result = {
                "id": i,
                "query": query,
                "reference": reference,
                "prediction": prediction
            }
            
            # Evaluate with criteria-based evaluators
            for name in ["accuracy", "relevance", "coherence", "harmfulness"]:
                eval_result = self.evaluators[name].evaluate_strings(
                    prediction=prediction,
                    reference=reference
                )
                result[name] = eval_result["score"]
            
            # Evaluate semantic similarity
            similarity_result = self.evaluators["semantic_similarity"].evaluate_strings(
                prediction=prediction,
                reference=reference
            )
            result["semantic_similarity"] = similarity_result["score"]
            
            # Evaluate QA performance
            qa_result = self.evaluators["qa"].evaluate_strings(
                prediction=prediction,
                input=query,
                reference=reference
            )
            result["qa_score"] = 1 if qa_result["text"] == "CORRECT" else 0
            
            # If context is provided, evaluate context relevance
            if context:
                result["context"] = context
                # Add context evaluation logic here
            
            results.append(result)
        
        # Convert to DataFrame for analysis
        df = pd.DataFrame(results)
        
        # Add aggregate scores
        df["overall_score"] = df[["accuracy", "relevance", "coherence", "semantic_similarity", "qa_score"]].mean(axis=1)
        
        return df
    
    def generate_report(self, df: pd.DataFrame) -> str:
        """Generate a human-readable report from evaluation results."""
        report = "# Evaluation Report\n\n"
        
        # Overall statistics
        report += "## Overall Statistics\n\n"
        report += f"Total examples evaluated: {len(df)}\n\n"
        report += f"Average overall score: {df['overall_score'].mean():.2f}\n\n"
        
        # Scores by criterion
        report += "## Scores by Criterion\n\n"
        for criterion in ["accuracy", "relevance", "coherence", "harmfulness", "semantic_similarity", "qa_score"]:
            report += f"- {criterion.replace('_', ' ').title()}: {df[criterion].mean():.2f}\n"
        
        # Examples with highest and lowest scores
        report += "\n## Best Performing Example\n\n"
        best_idx = df["overall_score"].idxmax()
        best_example = df.loc[best_idx]
        report += f"Query: {best_example['query']}\n\n"
        report += f"Reference: {best_example['reference']}\n\n"
        report += f"Prediction: {best_example['prediction']}\n\n"
        report += f"Overall Score: {best_example['overall_score']:.2f}\n\n"
        
        report += "## Worst Performing Example\n\n"
        worst_idx = df["overall_score"].idxmin()
        worst_example = df.loc[worst_idx]
        report += f"Query: {worst_example['query']}\n\n"
        report += f"Reference: {worst_example['reference']}\n\n"
        report += f"Prediction: {worst_example['prediction']}\n\n"
        report += f"Overall Score: {worst_example['overall_score']:.2f}\n\n"
        
        return report

# Example usage
evaluator = ComprehensiveEvaluator()

examples = [
    {
        "query": "What is the capital of France?",
        "reference": "The capital of France is Paris.",
        "prediction": "Paris is the capital of France."
    },
    {
        "query": "Who wrote 'Romeo and Juliet'?",
        "reference": "William Shakespeare wrote 'Romeo and Juliet'.",
        "prediction": "Romeo and Juliet was written by William Shakespeare in the late 16th century."
    },
    {
        "query": "What is the boiling point of water?",
        "reference": "The boiling point of water is 100 degrees Celsius at sea level.",
        "prediction": "Water boils at 100 degrees Celsius or 212 degrees Fahrenheit at standard atmospheric pressure."
    }
]

results_df = evaluator.evaluate(examples)
report = evaluator.generate_report(results_df)
print(report)
```

## Next Steps

Continue to the [Deployment](../12_deployment/README.md) section to learn how to deploy your LangChain applications to production environments.
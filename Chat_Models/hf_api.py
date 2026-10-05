from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from dotenv import load_dotenv

load_dotenv()

llm = HuggingFaceEndpoint(
    repo_id="meta-llama/Llama-3.1-8B-Instruct",
    task="text-generation"
)

model = ChatHuggingFace(llm=llm)

result = model.invoke("What is the capital of India")

print(result.content)

# # List all models that are "warmed up" and ready to serve on the serverless API
# hf models ls --warm

# # Narrow it down to a specific task (like text generation/chat)
# hf models ls --warm --pipeline-tag text-generation
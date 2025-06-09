import warnings
warnings.filterwarnings("ignore")

from langchain.chat_models import AzureChatOpenAI
from dotenv import load_dotenv
import os 

load_dotenv()

chat_model=AzureChatOpenAI(
    openai_api_base=os.getenv("AZURE_OPENAI_API_BASE"),
    openai_api_version=os.getenv("AZURE_OPENAI_API_VERSION"),
    openai_api_key=os.getenv("AZURE_OPENAI_API_KEY"),
    deployment_name=os.getenv("AZURE_OPENAI_DEPLOYMENT_NAME"),
    model_name="gpt-4o",
    temperature=0.7,
)

result = chat_model.predict('Hi!')
print(result)
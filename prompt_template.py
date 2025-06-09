# from langchain_community.chat_models import AzureChatOpenAI  # For using Azure OpenAI key
# from langchain.prompts.chat import ChatPromptTemplate  # For giving dynamic prompt

# # For getting API key from .env file
# import os 
# from dotenv import load_dotenv

# load_dotenv()

# # Making LLM ready
# chat_model = AzureChatOpenAI(
#     openai_api_base=os.getenv("AZURE_OPENAI_API_BASE"),
#     openai_api_version=os.getenv("AZURE_OPENAI_API_VERSION"),
#     openai_api_key=os.getenv("AZURE_OPENAI_API_KEY"),
#     deployment_name=os.getenv("AZURE_OPENAI_DEPLOYMENT_NAME"),
#     model_name="gpt-4o",
#     temperature=0.7,
# )

# # Prompt to LLM
# template = "You are a helpful assistant who will convert {input_lang} into {output_lang} and after converting say Anything else for me?"

# # Human prompt
# human_template = "{text}"

# # Make a structured message format
# chat_prompt = ChatPromptTemplate.from_messages([
#     ('system', template),
#     ('human', human_template)
# ])

# # Replace all variables in template with values
# messages = chat_prompt.format_messages(
#     input_lang='English',
#     output_lang='Gujarati',
#     text='How are you?'
# )

# result = chat_model.predict_messages(messages)

# print(result.content)


from langchain_community.chat_models import AzureChatOpenAI  # For using Azure OpenAI key
from langchain.prompts.chat import ChatPromptTemplate  # For giving dynamic prompt

# For getting API key from .env file
import os 
from dotenv import load_dotenv

load_dotenv()

# Making LLM ready
chat_model = AzureChatOpenAI(
    openai_api_base=os.getenv("AZURE_OPENAI_API_BASE"),
    openai_api_version=os.getenv("AZURE_OPENAI_API_VERSION"),
    openai_api_key=os.getenv("AZURE_OPENAI_API_KEY"),
    deployment_name=os.getenv("AZURE_OPENAI_DEPLOYMENT_NAME"),
    model_name="gpt-4o",
    temperature=0.7,
)

# Prompt to LLM
template = "You are a helpful assistant who will convert {input_lang} into {output_lang} and after converting say Anything else for me?"

# Human prompt
human_template = "{text}"

# Make a structured message format
chat_prompt = ChatPromptTemplate.from_messages([
    ('system', template),
    ('human', human_template)
])


input_l = input("Enter your input language: ")
output_l = input("Enter your output language: ")
textt = input("Enter text you want to translate: ")

# Replace all variables in template with values
messages = chat_prompt.format_messages(
    input_lang={input_l},
    output_lang={output_l},
    text={textt}
)

result = chat_model.predict_messages(messages)

print(result.content)
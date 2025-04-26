import os
from openai import OpenAI
from  dotenv import load_dotenv
load_dotenv()

client = OpenAI(api_key = os.getenv("OPENAI_API_KEY"))

def get_llm_insights(prompt):
    response = client.chat.completions.create(
        model = "gpt-4",
        # model="gpt-3.5-turbo",
        messages = [
            {"role":"system" , "content":"you are a helpfull system agent andlyze my data and give me a response"},
            {"role":"user" , "content" :prompt}
        ],
        temperature = 0.3
    )
    return response.choices[0].message.content
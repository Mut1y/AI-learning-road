from memory import load_memory, save_memory
from openai import OpenAI
from prompt import SYSTEM_PROMPT
from dotenv import load_dotenv
from tools import github_tool
import os

load_dotenv()


client = OpenAI(
    api_key=os.getenv("DEEPSEEK_API_KEY"),
    base_url="https://api.deepseek.com"
)

history = load_memory()

def ask_ai(question):


    if "github" in question.lower():

        username = question.split()[-1]

        result = github_tool(username)

        return result

    messages=[
        {
            "role":"system",
            "content":SYSTEM_PROMPT
        }
    ]


    messages.extend(history)


    messages.append(
        {
            "role":"user",
            "content":question
        }
    )


    response = client.chat.completions.create(

        model="deepseek-chat",

        messages=messages

    )


    answer = response.choices[0].message.content


    history.append(
        {
            "role":"user",
            "content":question
        }
    )


    history.append(
        {
            "role":"assistant",
            "content":answer
        }
    )
    save_memory(history)

    return answer
from tool_schema import TOOLS_DESCRIPTION
from memory import load_memory, save_memory
from openai import OpenAI
from prompt import SYSTEM_PROMPT
from dotenv import load_dotenv
from tool_registry import TOOLS
import os
import json


load_dotenv()

client = OpenAI(
    api_key=os.getenv("DEEPSEEK_API_KEY"),
    base_url="https://api.deepseek.com"
)


history = load_memory()


def ask_tool_ai(question):


    response = client.chat.completions.create(

        model="deepseek-chat",

        messages=[

            {
                "role":"system",
                "content":TOOLS_DESCRIPTION
            },

            {
                "role":"user",
                "content":question
            }

        ]

    )


    content = response.choices[0].message.content


    try:

        return json.loads(content)

    except:

        return {
            "tool":None
        }
    


def run_tool(tool_call):


    tool_name = tool_call["tool"]

    argument = tool_call["argument"]


    tool = TOOLS[tool_name]


    result = tool(argument)


    return result


def summarize_tool_result(question, result):


    response = client.chat.completions.create(

        model="deepseek-chat",

        messages=[

            {
                "role":"system",
                "content":SYSTEM_PROMPT
            },


            {
                "role":"user",
                "content":f"""
用户问题：

{question}


工具返回结果：

{result}


请根据结果回答用户。
"""
            }

        ]

    )


    return response.choices[0].message.content


def ask_ai(question):

    tool_call = ask_tool_ai(question)

    if tool_call.get("tool"):


        result = run_tool(tool_call)


        answer = summarize_tool_result(
            question,
            result
        )


        return answer

    
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


    answer=response.choices[0].message.content



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
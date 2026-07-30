import os
import importlib


TOOLS = {}


def load_tools():

    tools_path = os.path.join(
        os.path.dirname(__file__),
        "tools"
    )


    for filename in os.listdir(tools_path):

        if filename.endswith(".py") and filename != "__init__.py":

            module_name = f"tools.{filename[:-3]}"


            module = importlib.import_module(module_name)


            if hasattr(module, "tool_info"):

                tool = module.tool_info

                TOOLS[tool["name"]] = tool



load_tools()



def get_tools_description():


    text = """

你是一个工具选择器。

你的任务：
判断用户问题是否需要调用工具。

规则：

1. 如果存在匹配工具，必须调用工具。
2. 不允许自己执行计算。
3. 不允许自己回答GitHub查询。
4. 只能返回JSON。
5. 禁止输出解释。



如果需要调用工具：

只能返回JSON。

格式：

{
"name":"工具名称",
"arguments":{

"参数名":"参数值"

}
}


如果不需要：

返回：

{
"name":null,

"arguments":null

}


可用工具:

"""


    for name,tool in TOOLS.items():

        text += f"""

工具:
{name}

功能:
{tool["description"]}

参数:

"""


        for param,info in tool["parameters"].items():

            text += f"""

参数名:
{param}

类型:
{info["type"]}

说明:
{info["description"]}

"""


        text += "\n"

    return text
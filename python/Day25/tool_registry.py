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

如果需要调用工具：

只能返回JSON。

格式：

{
"tool":"工具名称",
"argument":"参数"
}


如果不需要：

{
"tool":null,
"argument":null
}


可用工具:

"""


    for name,tool in TOOLS.items():

        text += f"""

工具:
{name}

功能:
{tool["description"]}

"""


    return text
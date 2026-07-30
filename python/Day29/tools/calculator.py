def calculator_tool(expression):

    try:

        result = eval(expression)

        return {
            "结果": result
        }

    except Exception as e:

        return {
            "错误": str(e)
        }



tool_info = {

    "name":"calculator_tool",

    "description":"执行数学计算，需要提供expression参数",

    "parameters":{

        "expression":"数学表达式"

    },

    "function":calculator_tool

}
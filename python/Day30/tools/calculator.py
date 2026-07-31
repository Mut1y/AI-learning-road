def calculator_tool(expression):

    try:

        result = eval(expression)

        return {
            "结果":result
        }

    except Exception as e:

        return {
            "错误":str(e)
        }



tool_info = {

"name":"calculator_tool",

"description":"计算数学表达式",

"parameters":[

    {
        "name":"expression",
        "description":"需要计算的数学表达式，例如123*456"
    }

],

"function":calculator_tool

}
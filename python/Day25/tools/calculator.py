def calculator_tool(expression):

    try:

        result=eval(expression)

        return {
            "结果":result
        }

    except:

        return {
            "错误":"计算失败"
        }



tool_info = {

    "name":"calculator_tool",

    "description":"执行数学计算",

    "function":calculator_tool

}
def calculator_tool(expression):

    try:

        result = eval(expression)

        return {
            "结果": result
        }

    except:

        return {
            "错误": "计算失败"
        }
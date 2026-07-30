def test_tool(text):

    print("测试工具开始执行")

    return {
        "测试结果":text
    }


tool_info = {

    "name":"test_tool",

    "description":
    "测试工具",

    "parameters":{

        "text":{

            "type":"string",

            "description":
            "测试文本"

        }

    },

    "function":test_tool

}
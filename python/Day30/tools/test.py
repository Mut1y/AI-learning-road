def test_tool(text):

    print("测试工具开始执行")

    return {
        "测试结果":text
    }


tool_info = {

"name":"test_tool",

"description":"测试文本返回",

"parameters":[

    {
        "name":"text",
        "description":"需要测试的文本内容"
    }

],

"function":test_tool

}
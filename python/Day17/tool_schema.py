TOOLS_DESCRIPTION = """

你可以使用工具：

github_tool


功能：

查询GitHub用户信息


参数：

argument填写GitHub用户名


如果需要使用工具：

必须返回JSON：

{
 "tool":"github_tool",
 "argument":"用户名"
}


如果不需要工具：

返回：

{
 "tool":null
}

不要输出其他文字。

"""
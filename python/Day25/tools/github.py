from github_api import get_user


def github_tool(username):

    result = get_user(username)

    return result



tool_info = {

    "name":"github_tool",

    "description":"查询GitHub用户信息",

    "function":github_tool

}
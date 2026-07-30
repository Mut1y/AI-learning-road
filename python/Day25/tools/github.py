def github_tool(username):

    from github_api import get_user


    try:

        result = get_user(username)


        return result


    except Exception as e:

        return {

            "错误":str(e)

        }



tool_info={


    "name":"github_tool",


    "description":"查询GitHub用户信息，需要username参数",


    "parameters":{

        "username":"GitHub用户名"

    },


    "function":github_tool

}
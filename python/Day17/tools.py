from github_api import get_user


def github_tool(username):

    result = get_user(username)


    if isinstance(result, str):
        return result


    answer = f"""
GitHub用户信息：

用户名：{result['用户名']}

主页：{result['主页']}

仓库数量：{result['仓库数量']}

粉丝数量：{result['粉丝']}
"""


    return answer
import requests


def get_user(username):

    response = requests.get(
        f"https://api.github.com/users/{username}"
    )


    if response.status_code == 404:
        return "用户不存在"


    data = response.json()


    return {
        "用户名": data["login"],
        "主页": data["html_url"],
        "仓库数量": data["public_repos"],
        "粉丝": data["followers"]
    }
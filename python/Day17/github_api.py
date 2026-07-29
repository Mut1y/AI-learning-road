import requests


def get_user(username):

    url = f"https://api.github.com/users/{username}"


    response = requests.get(url)


    data = response.json()


    return {

        "用户名": data["login"],
        "主页": data["html_url"],
        "仓库数量": data["public_repos"],
        "粉丝": data["followers"]

    }
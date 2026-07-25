from github_api import get_user


username = input("请输入GitHub用户名:")


user = get_user(username)


if user:

    print("用户名:", user["login"])
    print("仓库:", user["public_repos"])
    print("粉丝:", user["followers"])
    print("主页:", user["html_url"])

else:

    print("用户不存在")
"""条件判断练习：运行时设置并验证一组临时凭据。

这个示例不会把用户名或密码写进代码，也不会保存到文件。
真实项目应使用密码哈希和成熟的身份认证方案。
"""

from getpass import getpass


def main() -> None:
    expected_name = input("请先设置练习用户名：")
    expected_password = getpass("请先设置练习密码：")

    name = input("请输入用户名：")
    password = getpass("请输入密码：")

    if name == expected_name and password == expected_password:
        print("登录成功")
    else:
        print("用户名或密码错误")


if __name__ == "__main__":
    main()

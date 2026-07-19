def add(a,b):
    return a + b

def subtract(a,b):
    return a - b

def multiply(a,b):
    return a * b

print("====计算器====")
print("1. 加法")
print("2. 减法")
print("3. 乘法")

choice = input("请选择： ")

a = int(input("请输入第一个数字： "))
b = int(input("请输入第二个数字： "))

if choice == "1":
    result = add(a,b)

elif choice == "2":
    result = subtract(a,b)

elif choice == "3":
    result = multiply(a,b)

print("结果：", result)
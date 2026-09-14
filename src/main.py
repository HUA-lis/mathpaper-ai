from math_tools import average


def main():
    print("=== MathPaper AI 数学助手 ===")

    user_input = input("请输入数字，用空格分隔：")

    try:
        numbers = [float(x) for x in user_input.split()]
        result = average(numbers)

        print(f"平均值：{result}")

    except ValueError:
        print("输入有误，请输入有效的数字。")


if __name__ == "__main__":
    main()

from math_tools import average, maximum
from text_reader import read_txt_file


def run_math_calculation():
    user_input = input("请输入数字，用空格分隔：")

    try:
        numbers = [float(x) for x in user_input.split()]
        result = average(numbers)
        max_result = maximum(numbers)

        print(f"最大值：{max_result}")
        print(f"平均值：{result}")

    except ValueError:
        print("输入有误，请输入有效的数字。")


def run_txt_reader():
    file_path = input("请输入 TXT 文件路径：").strip()

    if not file_path.lower().endswith(".txt"):
        print("暂时只支持 TXT 文件。")
        return

    try:
        content = read_txt_file(file_path)

        print("\n=== TXT 文件内容 ===")
        print(content)

    except FileNotFoundError:
        print("找不到该文件，请检查文件路径是否正确。")
    except IsADirectoryError:
        print("输入的是文件夹，请输入 TXT 文件的完整路径。")
    except PermissionError:
        print("没有读取该文件的权限。")
    except UnicodeDecodeError:
        print("文件编码无法识别，目前仅支持 UTF-8 编码的 TXT 文件。")
    except OSError:
        print("读取文件时发生错误，请检查文件是否可用。")


def main():
    print("=== MathPaper AI 数学助手 ===")
    print("1. 数学计算")
    print("2. 读取 TXT 文件")

    choice = input("请选择功能：").strip()

    if choice == "1":
        run_math_calculation()
    elif choice == "2":
        run_txt_reader()
    else:
        print("无效选择，请输入 1 或 2。")


if __name__ == "__main__":
    main()

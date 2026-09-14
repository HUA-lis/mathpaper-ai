def average(numbers):
    if not numbers:
        raise ValueError("数字列表不能为空")

    return sum(numbers) / len(numbers)

def mul_decorator(func):
    def repeat(num1, num2):
        func(num1, num2)
        func(num1, num2)

    return repeat


@mul_decorator
def multiply(num1, num2):
    print(num1 * num2)


multiply(3, 4)

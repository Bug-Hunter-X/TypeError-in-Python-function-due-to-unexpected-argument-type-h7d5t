def function_with_uncommon_error(x):
    try:
        result = 10 / x
        return result
    except ZeroDivisionError:
        print("Error: Cannot divide by zero")
        return None

# This will trigger a TypeError because a string is passed
result = function_with_uncommon_error("hello")
print(result)
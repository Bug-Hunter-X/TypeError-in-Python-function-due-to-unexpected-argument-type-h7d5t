def function_with_uncommon_error(x: int) -> float:
    try:
        if isinstance(x, (int, float)):
            result = 10 / x
            return result
        else:
            raise TypeError("Invalid input type. Please enter a number.")
    except ZeroDivisionError:
        print("Error: Cannot divide by zero")
        return None
    except TypeError as e:
        print(f"Error: {e}")
        return None

# This will now raise a TypeError due to input validation
result = function_with_uncommon_error("hello")
print(result)

# This will work correctly
result = function_with_uncommon_error(5)
print(result)
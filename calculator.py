def division(num1: int, num2: int) -> int:
    if num2 == 0:
        return ZeroDivisionError
    
    return num1 / num2
    
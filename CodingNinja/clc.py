def calculator(n1 ,n2 , operator):
    try:
        if operator == '+':
            result = n1 + n2
        elif operator == '-':
            result = n1 - n2
        elif operator == '*':
            result = n1 * n2
        elif operator == "/" :
            if n2 == 0:
                raise ValueError("divisn by 0 not")
            result = n1 / n2
        else :
            raise ValueError("invalid")
        return result
    except Exception as e :
        return f"Error: {str(e)}"
    
n1 = float(input())
n2 = float(input())
operator = input()
result = calculator(n1 , n2 , operator)
print(f"Result:{result}")
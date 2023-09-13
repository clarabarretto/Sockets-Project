def calculator(expression):
    try:
        result = eval(expression)
        return str(result)
    except:
        return "Expressão inválida"
def arithmetic_arranger(problems, show_answers=False):
    # Verificar la cantidad de problemas
    if len(problems) > 5:
        return "Error: Too many problems."

    arranged_problems = []
    first_line = []
    second_line = []
    separator_line = []
    answer_line = []

    for problem in problems:
        # Separar el problema en operandos y operador
        operand1, operator, operand2 = problem.split()

        # Verificar el operador
        if operator not in ['+', '-']:
            return "Error: Operator must be '+' or '-'."

        # Verificar los operandos
        if not operand1.isdigit() or not operand2.isdigit():
            return "Error: Numbers must only contain digits."
        
        if len(operand1) > 4 or len(operand2) > 4:
            return "Error: Numbers cannot be more than four digits."
        
        # Determinar el número de espacios necesarios para alinear los operandos
        max_length = max(len(operand1), len(operand2))
        space_count = max_length + 2
        
        # Construir las líneas del problema
        first_line.append(operand1.rjust(space_count))
        second_line.append(operator + operand2.rjust(max_length + 1))
        separator_line.append("-" * (max_length + 2))
        
        # Calcular la respuesta si se solicita
        if show_answers:
            if operator == '+':
                answer = str(int(operand1) + int(operand2))
            else:
                answer = str(int(operand1) - int(operand2))
            answer_line.append(answer.rjust(space_count))

    # Combinar las líneas en una sola cadena
    arranged_problems.append("    ".join(first_line))
    arranged_problems.append("    ".join(second_line))
    arranged_problems.append("    ".join(separator_line))

    if show_answers:
        arranged_problems.append("    ".join(answer_line))

    return "\n".join(arranged_problems)

print(arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43", "123 + 49"]))
print(arithmetic_arranger(["32 + 8", "1 - 3801", "9999 + 9999", "523 - 49"], True))

# Balanceador

# Funcion para verificar que si esta balanceado
def is_balanced(expression):
    stack = []
    # Diccionario para emparejar los paréntesis de cierre con los de apertura
    matching_pairs = {')': '(', ']': '[', '}': '{'}
    steps = []

    for position, symbol in enumerate(expression):
        if symbol in '([{':
            stack.append(symbol)
            steps.append(f"Stack after adding '{symbol}': {stack}")
        elif symbol in ')]}':
            # Verificar si la pila está vacía o si los paréntesis no coinciden
            if not stack or stack[-1] != matching_pairs[symbol]:
                steps.append(f"Error at position {position}: expected '{matching_pairs.get(symbol)}', found '{symbol}'")
                return False, steps
            stack.pop()
            steps.append(f"Stack after removing '{symbol}': {stack}")

    # ultimo check - la pila debe estar vacía para que la expresión esté balanceada
    if not stack:
        steps.append("La expresión está balanceada: la pila está vacía")
        return True, steps
    else:
        steps.append(f"La expresión NO está balanceada: elementos restantes en la pila: {stack}")
        return False, steps

def process_file(filename):
    # Leer expresiones desde el archivo y procesar cada una
    try:
        with open(filename, 'r') as file:
            for line_number, line in enumerate(file, start=1):
                expression = line.strip()
                print(f"\nLinea {line_number}: {expression}")
                is_balanced_result, steps = is_balanced(expression)
                
                # Mostrar todos los pasos
                for step in steps:
                    print("  -", step)
                
                # Resultado
                result_text = 'BALANCEADO' if is_balanced_result else 'NO BALANCEADO'
                print(f"Resultado: {result_text}")
    except FileNotFoundError:
        print(f"Error: No se pudo encontrar el archivo '{filename}'")

if __name__ == "__main__":
    # Procesar el archivo de expresiones
    process_file("expresiones.txt")

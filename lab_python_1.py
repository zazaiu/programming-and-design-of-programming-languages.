import sys

def get_coefficient(prompt):
    while True:
        try:
            value = float(input(prompt))
            return value
        except ValueError:
            print("Некорректное значение. Пожалуйста, введите действительное число.")

def solve_biquadratic(A, B, C):
    # Вычисление дискриминанта для квадратного уравнения
    D = B**2 - 4*A*C
    print(f"Дискриминант D = {D}")

    if D > 0:
        y1 = (-B + D**0.5) / (2*A)
        y2 = (-B - D**0.5) / (2*A)
        return [y1, y2]
    elif D == 0:
        y = -B / (2*A)
        return [y]
    else:
        return []

def find_x_from_y(y):
    if y < 0:
        return []  # Нет действительных корней
    else:
        return [y**0.5, -y**0.5]

def main():
    if len(sys.argv) == 4:
        try:
            A = float(sys.argv[1])
            B = float(sys.argv[2])
            C = float(sys.argv[3])
        except ValueError:
            print("Некорректные значения в командной строке. Пожалуйста, введите коэффициенты заново.")
            A = get_coefficient("Введите коэффициент A: ")
            B = get_coefficient("Введите коэффициент B: ")
            C = get_coefficient("Введите коэффициент C: ")
    else:
        A = get_coefficient("Введите коэффициент A: ")
        B = get_coefficient("Введите коэффициент B: ")
        C = get_coefficient("Введите коэффициент C: ")

    # Решение биквадратного уравнения
    y_roots = solve_biquadratic(A, B, C)

    all_x_roots = []
    for y in y_roots:
        all_x_roots.extend(find_x_from_y(y))

    if all_x_roots:
        print(f"Корни биквадратного уравнения: {all_x_roots}")
    else:
        print("Уравнение не имеет действительных корней.")

if __name__ == "__main__":
    main()

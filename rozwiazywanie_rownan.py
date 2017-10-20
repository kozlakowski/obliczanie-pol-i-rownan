print()



print("Zostaniesz poproszony o napisanie działania z jedną niewiadomą, program rozwiąże je za Ciebie")
print("Pamiętaj że niewiadoma 'x' musi występować w działaniu jako pierwsza  ")


def solve_eq(equation):
    x, znak, num1, equal, num2 = equation.split()

    num1, num2 = int(num1), int(num2)

    if znak == "+":

        return "x = " + str(num2 - num1)

    elif znak == "-":

        return "x = " + str(num2 + num1)

    elif znak == "*":

        return "x = " + str(num2 / num1)

    elif znak == "/":

        return "x = " + str(num2 * num1)



print(solve_eq(input("Wpisz działanie : ")))
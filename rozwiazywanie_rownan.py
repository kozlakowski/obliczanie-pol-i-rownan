# def +
# rozdzielic znaki ( x musi byc pierwszy )
# if znak jest jakis --> return odpowiednie rownanie ( "x = " + str(cos - cos) )
# num1 i num2 musi być integer

def rozwiaz_rownanie(rownanie):

    x, znak, num1, rownosc, num2 = rownanie.split()
    num1, num2 = int(num1), int(num2)

    if znak == "+":
        return "x = " + str(num2 - num1)

    elif znak == "-":
        return "x = " + str(num2 - num1)

    elif znak == "*":
        return "x = " + str(num2 / num1)

    elif znak == "/":
        return "x = " + str(num2 * num1)

    else:
        ("Należy użyć mnożenia, dzielenia, dodawania lub odejmowania")

print(rozwiaz_rownanie(input("Wpisz równanie, które chcesz rozwiązać : ")))


















print(rozwiaz_rownanie((input("Wpisz równanie, pamietaj niewiadoma musi występować jako pierwsza : "))))



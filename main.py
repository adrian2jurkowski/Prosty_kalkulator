print("--Witam w prostym Kalkulatorze--")
while True:
    print()
    print("Podaj dwie liczby a następnie wybierz z jakiego działania chcesz skorzystać.")
    print("1. Dodawanie")
    print("2. Odejmowanie")
    print("3. Mnożenie")
    print("4. Dzielenie")
    print()

    a = int(input("Podaj pierwszą liczbę całkowitą a: "))
    b = int(input("Podaj drugą liczbę całkowitą b: "))

    action = input("Wybierz formę działania za pomocą cyfry od 1 do 4: ")

    if action == "1":
        print(a,"+", b,"=", a + b)
    elif action == "2":
        print(a,"-", b,"=", a - b)
    elif action == "3":
        print(a,"*", b,"=", a * b)
    elif action == "4":
        print(a,"/", b, "=", a / b)
    else:
        print("Niepoprawna cyfra. Wybierz z przedziału 1-4: ")

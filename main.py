import random
while True:
    wybory = ["kamień", "papier", "nożyce"]

    komputer = random.choice(wybory)
    gracz = None

    while gracz not in wybory:
        gracz = input("Wybierz: ").lower()

    if gracz == komputer:
        print(komputer)
        print("Remis")
    elif gracz == "nożyce":
        if komputer == "papier":
            print(komputer)
            print("Wygrałeś!")
        elif komputer == "kamień":
            print(komputer)
            print("Przegrałeś!")
    elif gracz == "kamień":
        if komputer == "nożyce":
            print(komputer)
            print("Wygrałeś!")
        elif komputer == "papier":
            print(komputer)
            print("Przegrałeś!")
    elif gracz == "pepier":
        if komputer == "kamień":
            print(komputer)
            print("Wygrałeś!")
        elif komputer == "nożyce":
            print(komputer)
            print("Przegrałeś!")
    play_again = input("Jeszcze raz? ").lower()
    if play_again != "tak":
        break
print("Narazie!")

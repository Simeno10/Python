def new_game():
    guesses=[]
    correct_guesses=0
    question_num=1

    for key in questions:
        print("------------------------")
        print(key)
        for i in options[question_num-1]:
            print(i)
        guess=input("Enter A, B, C or D: ").upper()
        guesses.append(guess)
        correct_guesses += check_answer(questions.get(key),guess)
        question_num += 1
    check_score(correct_guesses, guesses)
def check_answer(answer, guess):
    if answer==guess:
        print("DOBRZE!")
        return 1
    else:
        print("ŹLE!")
        return 0
def check_score(correct_guesses, guesses):
    print("------------------------")
    print("WYNIKI:")
    print("------------------------")
    print("Pytania", end=" ")
    for i in questions:
        print(questions.get(i), end=" ")
    print()

    print("Odpowiedzi", end=" ")
    for i in guesses:
        print(i, end=" ")
    print()

    score = int((correct_guesses/len(questions)*100))
    print("Twój wynik to: "+str(score)+"%")

def play_again():
    response = input("Chcesz zagrać jeszcze raz? (tak lub nie) ").upper()
    if response == "TAK":
        return True
    else:
        return False

questions = {"Kto jest obecnie trenerem Barcelony": "B",
             "Ile Lig Mistrzów wygrał Real": "A",
             "Kto Jest mistrzem Europy?": "C",
             "Kto jest Mistrzem Świata?": "D"}
options = [["A.Gullit", "B.Flick", "C.Klopp", "D.Mourinho"],
           ["A.15", "B.0", "C.10", "D.5"],
           ["A.Polska", "B.Niemcy", "C.Włochy", "D.Francja"],
           ["A.Brazylia", "B.Włochy", "C.Francja", "D.Argentyna"]]
new_game()
while(play_again()):
    new_game()

print("Żegnaj!")

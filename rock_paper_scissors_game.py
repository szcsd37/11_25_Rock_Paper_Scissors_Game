import random

def determine_winner(user_choice, machine_choice):
    if user_choice == machine_choice:
        return "döntetlen"
    elif (user_choice == "kő" and machine_choice == "olló") or \
         (user_choice == "papír" and machine_choice == "kő") or \
         (user_choice == "olló" and machine_choice == "papír"):
        return "nyert"
    else:
        return "vesztett"

def play_game():
    print("Üdvözöllek a kő, papír, olló játékba!")
    
    wins = 0
    losses = 0
    ties = 0
    
    while True:
        user_choice = input("Válassz: kő, papír, olló -> ").lower()

        if user_choice not in ["kő", "papír", "olló"]:
            print("Helytelen válasz, kérlek válassz ezek közül: kő, papír, vagy olló.")
            continue

        machine_choice = random.choice(["kő", "papír", "olló"])
        print(f"A gép választása: {machine_choice}")

        result = determine_winner(user_choice, machine_choice)

        if result == "nyert":
            print("Nyertél!")
            wins += 1
        elif result == "vesztett":
            print("Vesztettél.")
            losses += 1
        else:
            print("Döntetlen!")
            ties += 1

        print(f"Nyereségek: {wins}, Veszteségek: {losses}, Döntetlenek: {ties}")

        play_again = input("Újra? (i/n): ").lower()
        if play_again != 'i':
            break

    print(f"Köszönöm a játékot! Eredmények: Nyert: {wins}, Vesztett: {losses}, Döntetlen: {ties}")

play_game()
from art import sketch
import random
import os


def cls():
    os.system('cls' if os.name == 'nt' else 'clear')


players_cards = {}
user_score = 0
comp_score = 0


def will_play():
    while True:
        play_again = input("\nWould you like to play a game of Blackjack; (y/n) ")
        if play_again.lower() == "y":
            return True
        elif play_again.lower() == "n":
            return False
        else:
            print("Please provide valid answer!\n")


def card_generator(card_dict):
    global user_score, comp_score
    user_cards = []
    computer_cards = []
    for i in range(2):
        user_cards.append(random.randint(1, 10))
        computer_cards.append(random.randint(1, 10))
    card_dict["Player"] = user_cards
    card_dict["Computer"] = computer_cards
    user_score = sum(user_cards)
    comp_score = sum(computer_cards)
    while comp_score < 17:
        new_card = random.randint(1, 10)
        card_dict["Computer"].append(new_card)
        comp_score += new_card


def score_output():
    print(f"Your cards: {players_cards['Player']}, current score: {user_score}\n"
          f"Computer's first card: {players_cards['Computer'][0]}")


def final_score_output():
    print(f"\nYour cards: {players_cards['Player']}, final score: {user_score}\n"
          f"Computer's cards: {players_cards['Computer']}, final score: {comp_score}")


def blackjack():
    global user_score, comp_score, players_cards
    while True:
        should_continue = input("\nAnother card? (y/n) ")
        if should_continue.lower() == "y":
            new_card_number = random.randint(1, 10)
            user_score += new_card_number
            players_cards["Player"].append(new_card_number)
            if user_score > 21:
                return "computer"
            elif user_score == 21:
                return "user"
            else:
                score_output()
        elif should_continue.lower() == "n":
            if user_score > comp_score:
                return "user"
            elif user_score < comp_score <= 21:
                return "computer"
            elif comp_score > 21:
                return "user"
            else:
                return "draw"


def main():
    while True:
        if will_play():
            cls()
            print(sketch)
            card_generator(players_cards)
            score_output()
            round_result = blackjack()
            if round_result == "user":
                final_score_output()
                print("Congratulations! You win!")
            elif round_result == "computer":
                final_score_output()
                print("You lose! 😭")
            elif round_result == "draw":
                final_score_output()
                print("Draw 🙃")
        else:
            break


if __name__ == "__main__":
    main()

import random
import art
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

def give_hand():
    hand = [random.choice(cards), random.choice(cards)]
    return hand

def calc_total(hand):
    total = sum(hand)
    if total > 21 and 11 in hand:
        for number in hand:
            if number == 11:
                total -= 10
    return total

def hit(hand):
    return hand.append(random.choice(cards))

def should_computer_hit(hand):
    while calc_total(hand) < 17:
        hit(hand)

def print_status(p_hand, c_hand, final):
    if final:
        print(f" Your final hand: {p_hand}, final score: {calc_total(p_hand)}")
        print(f" Computer's final hand {c_hand}, final score: {calc_total(c_hand)}")
    else:
        print(f"  Your cards: {p_hand}, current score: {calc_total(p_hand)}")
        print(f"  Computer's first card: {c_hand[0]}")

continue_game = True
while continue_game:
    new_game = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ")
    if new_game == 'n':
        break

    print(art.logo)
    computer_hand = give_hand()
    player_hand = give_hand()

    print_status(player_hand, computer_hand, False)

    def ask_for_hit():
        hit_me = input("Type 'y' to get another card, type 'n' to pass: ")
        if hit_me == 'y':
            hit(player_hand)
            if calc_total(player_hand) > 21:
                print_status(player_hand, computer_hand, True)
                print("You went over. You lose.")
            else:
                print_status(player_hand, computer_hand, False)
                ask_for_hit()
    ask_for_hit()

    if calc_total(player_hand) <= 21:
        should_computer_hit(computer_hand)
        print_status(player_hand, computer_hand, True)
        if calc_total(computer_hand) > 21:
            print("Opponent went over. You win.")
        elif calc_total(computer_hand) > calc_total(player_hand):
            print("You lose.")
        elif calc_total(computer_hand) == calc_total(player_hand):
            print("It's a draw.")
        else:
            print("You win.")

print("Game ended.")

import random


def generate_card(length, upper_range):
    return random.sample(range(1, upper_range + 1), length)


def get_valid_number(prompt):
    while True:
        user_input = input(prompt).strip().lower()
        if user_input == "quit":
            return "q"
        if not user_input.isdigit():
            print("Please enter a positive integer.")
            continue
        value = int(user_input)
        if value <= 0:
            print("Please enter a positive integer.")
            continue
        return value


def custom_bingo_game():
    print(
        "Welcome to the custom bingo game, enter 'quit' to exit the game at any time: "
    )
    upper_range = get_valid_number("Enter upper range: ")
    if upper_range == "q":
        print("You are exiting the game. Thank you.")
        return

    card_length = get_valid_number("Enter number of values on your card: ")
    if card_length == "q":
        print("You are exiting the game. Thank you.")
        return

    draws = get_valid_number("Enter number of draws: ")
    if draws == "q":
        print("You are exiting the game. Thank you.")
        return

    if (card_length > upper_range) or (draws > upper_range):
        print("You have generated invalid bingo game, please try again.")
        custom_bingo_game()
        return

    bingo_card = generate_card(card_length, upper_range)
    bingo_winning_nums = generate_card(draws, upper_range)
    marked_nums = []
    score = 0

    print("\n Your Bingo Card: ", bingo_card)

    for num in bingo_winning_nums:
        user_input_4 = input("\nPress Enter to draw a number: ").strip().lower()
        if user_input_4 == "quit":
            print("You are exiting the game. Thank you.")
            return
        print(f"Number drawn: {num}")
        if num in bingo_card:
            print("Match found!")
            score += 1
            marked_nums.append(num)
        else:
            print("No match found!")
        print(f"Current marked numbers: {marked_nums}")
        print(f"Current score: {score}/{card_length}")
        if score == card_length:
            print("BINGO. Congratulations, you've ticked off your bingo list.")
            return

    print(f"Final score: {score}/{card_length}. Better luck next time.")


custom_bingo_game()

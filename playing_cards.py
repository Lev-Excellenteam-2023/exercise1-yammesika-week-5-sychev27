import random


def create_playing_cards():
    shapes = ["Spade", "Heart", "Diamond", "Club"]

    playing_cards = [(shape, index) for shape in shapes for index in range(1, 14)]

    return playing_cards


def dealing_cards(playing_cards):
    player_1 = []
    player_2 = []
    player_3 = []
    player_4 = []

    for index in range(0, 13):
        player_1.append(playing_cards[index])
        player_2.append(playing_cards[index + 13])
        player_3.append(playing_cards[index + 13 * 2])
        player_4.append(playing_cards[index + 13 * 3])

    return player_1, player_2, player_3, player_4


def sum_of_players_cards(player_1, player_2, player_3, player_4):
    sum_1 = 0
    sum_2 = 0
    sum_3 = 0
    sum_4 = 0

    for index in range(0, 13):
        sum_1 = sum_1 + player_1[index][1]
        sum_2 = sum_2 + player_2[index][1]
        sum_3 = sum_3 + player_3[index][1]
        sum_4 = sum_4 + player_4[index][1]

    return sum_1, sum_2, sum_3, sum_4


def main():
    """Main function to simulate a card game.

    The function performs the following steps:
    1. Creates a deck of playing cards.
    2. Shuffles the cards.
    3. Deals the cards to four players.
    4. Calculates the sum of cards for each player.
    5. Finds the winning player with the maximum sum of cards.
    6. Prints the players' cards, the sum of each player, and the sum of the winning player.

    """
    playing_cards = create_playing_cards()

    random.shuffle(playing_cards)

    player_1, player_2, player_3, player_4 = dealing_cards(playing_cards)

    sum_1, sum_2, sum_3, sum_4 = sum_of_players_cards(player_1, player_2, player_3, player_4)

    max_height = max(sum_1, sum_2, sum_3, sum_4)

    print("Players are: " + "\n" + str(player_1) + "\n" + str(player_2) +
                            "\n" + str(player_3) + "\n" + str(player_4) + "\n")
    print("Sum of each player is: " + str(sum_1) + "," + str(sum_2) + "," + str(sum_3) + "," + str(sum_4) + "\n")
    print("Sum of the winning player is: " + str(max_height))


if __name__ == "__main__":
        main()




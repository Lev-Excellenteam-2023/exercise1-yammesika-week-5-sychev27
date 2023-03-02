import random


def create_playing_cards():
    shapes = ["Spade", "Heart", "Diamond", "Club"]
    playing_cards = []

    for shape in shapes:
        for i in range(1, 14):
            playing_cards.append((shape, i))

    return playing_cards


def dealing_cards(playing_cards):
    player_1 = []
    player_2 = []
    player_3 = []
    player_4 = []

    for i in range(0, 13):
        player_1.append(playing_cards[i])
        player_2.append(playing_cards[i + 13])
        player_3.append(playing_cards[i + 13 * 2])
        player_4.append(playing_cards[i + 13 * 3])

    return player_1, player_2, player_3, player_4


def sum_of_players_cards(player_1, player_2, player_3, player_4):
    sum_1 = 0
    sum_2 = 0
    sum_3 = 0
    sum_4 = 0

    for i in range(0, 13):
        sum_1 = sum_1 + player_1[i][1]
        sum_2 = sum_2 + player_2[i][1]
        sum_3 = sum_3 + player_3[i][1]
        sum_4 = sum_4 + player_4[i][1]

    return sum_1, sum_2, sum_3, sum_4


def main():
    # Create the playing cards
    playing_cards = create_playing_cards()

    # Shuffle cards
    random.shuffle(playing_cards)

    # Deal cards to four players
    player_1, player_2, player_3, player_4 = dealing_cards(playing_cards)

    # Calculate the amount each player has
    sum_1, sum_2, sum_3, sum_4 = sum_of_players_cards(player_1, player_2, player_3, player_4)

    # Find the winning player
    max_height = max(sum_1, sum_2, sum_3, sum_4)

    print("Players are: " + "\n" + str(player_1) + "\n" + str(player_2) +
                            "\n" + str(player_3) + "\n" + str(player_4) + "\n")
    print("Sum of each player is: " + str(sum_1) + "," + str(sum_2) + "," + str(sum_3) + "," + str(sum_4) + "\n")
    print("Sum of the winning player is: " + str(max_height))


if __name__ == "__main__":
        main()




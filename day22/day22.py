#!/usr/bin/env python3
from collections import deque


def load_input(input_file):
    data = open(input_file).read().split("\n\n")
    deck1 = deque(map(lambda x: int(x), data[0].strip().split('\n')[1:]))
    deck2 = deque(map(lambda x: int(x), data[1].strip().split('\n')[1:]))
    return deck1, deck2


def compute_score(deck1, deck2):
    winner = deck1 if len(deck1) > len(deck2) else deck2
    return sum(v * (len(winner) - i) for i, v in enumerate(winner))


PLAYER_1 = 1
PLAYER_2 = 2


def part1(input_file):

    deck1, deck2 = load_input(input_file)
    round = 1
    while len(deck1) != 0 and len(deck2) != 0:
        print(f"-- Round {round} --")
        print(f"Player 1's deck: {list(deck1)}")
        print(f"Player 2's deck: {list(deck2)}")

        print(f"Player 1 plays: {deck1[0]}")
        print(f"Player 2 plays: {deck2[0]}")

        card1 = deck1.popleft()
        card2 = deck2.popleft()
        if card1 > card2:
            print("Player 1 wins the round!")
            deck1.append(card1)
            deck1.append(card2)
        else:
            print("Player 2 wins the round!")
            deck2.append(card2)
            deck2.append(card1)
        round += 1
        print()

    print("-- Final Result --")
    print(f"Player 1's deck: {list(deck1)}")
    print(f"Player 2's deck: {list(deck2)}")

    return compute_score(deck1, deck2)


def p1_instant_win(state, history):
    if state in history:
        # print("Player 1 Instant Win.")
        return True


def build_hashable_state(deck1, deck2):
    return (str(deck1), str(deck2))


def play_game(deck1, deck2, game_no=1):
    # print(f"=== Game {game_no} ===\n")
    round = 1
    previous_states = set()
    while len(deck1) != 0 and len(deck2) != 0:
        # if game_no == 1:
        #     print(f"-- Round {round} (Game {game_no}) --")
        #     print(f"Player 1's deck: {list(deck1)}")
        #     print(f"Player 2's deck: {list(deck2)}")

        state = build_hashable_state(deck1, deck2)

        if p1_instant_win(state, previous_states):
            return (PLAYER_1, deck1)

        else:
            previous_states.add(state)

            c1 = deck1.popleft()
            c2 = deck2.popleft()
            # print(f"Player 1 plays: {c1}")
            # print(f"Player 2 plays: {c2}")

            if len(deck1) >= c1 and len(deck2) >= c2:
                # print("Playing a sub-game to determine the winner...\n")
                deck1_copy = list(deck1)[:c1]
                deck2_copy = list(deck2)[:c2]
                winner, p = play_game(deque(deck1_copy), deque(
                    deck2_copy), game_no=game_no+1)
                if winner == PLAYER_1:
                    deck1.append(c1)
                    deck1.append(c2)
                else:
                    deck2.append(c2)
                    deck2.append(c1)
            else:
                if c1 > c2:
                    # print(f"Player 1 wins round {round} of game {game_no}!")
                    deck1.append(c1)
                    deck1.append(c2)
                else:
                    # print(f"Player 2 wins round {round} of game {game_no}!")
                    deck2.append(c2)
                    deck2.append(c1)

        round += 1
        # print()

    if len(deck1) > len(deck2):
        winner = PLAYER_1
        deck = deck1
    else:
        winner = PLAYER_2
        deck = deck2
    # print(f"The winner of game 1 is player {winner}!")
    return (winner, deck)


def part2(input_file):
    p1, p2 = load_input(input_file)
    winner, deck = play_game(p1, p2)
    print("\n== Post-game results ==")
    print(f"Player {winner}'s deck: {list(deck)}")
    return compute_score([], deck)


if __name__ == "__main__":
    # print(part2("small.txt"))
    print(part2("input.txt"))

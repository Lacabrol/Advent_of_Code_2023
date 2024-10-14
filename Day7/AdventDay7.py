from collections import Counter

def convert_cards_to_values(card_sequence):
    card_value_map = {
        '2': 0, '3': 1, '4': 2, '5': 3, '6': 4,
        '7': 5, '8': 6, '9': 7, 'T': 8, 'J': 9,
        'Q': 10, 'K': 11, 'A': 12
    }
    return [card_value_map[card] for card in card_sequence]


def sort_hands_by_rank(card_hands):
    for hand in card_hands:
        hand[0] = convert_cards_to_values(hand[0])

    return sorted(card_hands, key=lambda x: tuple(x[0]))


if __name__ == '__main__':
    with open("input7.txt", "r") as file:
        lines = file.readlines()

    hands_by_category = [[] for _ in range(7)]  # 7 categories of hands
    final_sorted_hands = []
    total_sum = 0

    for line in lines:
        words = line.split()
        card_sequence = words[0]
        bid_value = int(words[1])

        # Count the frequency of each card
        card_frequencies = Counter(card_sequence).values()

        # Categorize the hand
        if len(card_frequencies) == 5:
            hands_by_category[0].append([card_sequence, bid_value])  # High card
        elif len(card_frequencies) == 1:
            hands_by_category[6].append([card_sequence, bid_value])  # Five of a kind
        elif len(card_frequencies) == 4:
            hands_by_category[1].append([card_sequence, bid_value])  # One pair
        elif len(card_frequencies) == 2:
            if max(card_frequencies) == 4:
                hands_by_category[5].append([card_sequence, bid_value])  # Four of a kind
            else:
                hands_by_category[4].append([card_sequence, bid_value])  # Full house
        elif len(card_frequencies) == 3:
            if 3 in card_frequencies:
                hands_by_category[3].append([card_sequence, bid_value])  # Three of a kind
            else:
                hands_by_category[2].append([card_sequence, bid_value])  # Two pair

    # Sort hands within each category and calculate the final score
    for category_hands in hands_by_category:
        sorted_hands = sort_hands_by_rank(category_hands)
        final_sorted_hands.extend(sorted_hands)

    # Calculate the final score based on the sorted hand positions
    for idx, hand in enumerate(final_sorted_hands):
        print(idx, hand)
        total_sum += hand[1] * (idx + 1)

    print(final_sorted_hands)
    print(total_sum)

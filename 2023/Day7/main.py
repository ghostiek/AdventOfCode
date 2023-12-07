from typing import List

with open('data.txt', 'r') as file:
    txt = file.read()

class Player:
    def __init__(self, hand, bid):
        self.hand = hand
        self.bid = bid
        self.hand_power = self.rank_hand()

    def rank_hand(self):
        unique_cards = list(set(self.hand))
        cards_count = {}
        for unique_card in unique_cards:
            cards_count[unique_card] = self.hand.count(unique_card)
        ordered_values = sorted(list(cards_count.values()))
        # The lower, the stronger
        if len(unique_cards) == 1:
            base_hand_power = 1
        if len(unique_cards) == 2:
            if ordered_values == [1, 4]:
                # four of a kind
                base_hand_power = 2
            else:
                base_hand_power = 2.5
        if len(unique_cards) == 3:
            # Could be 3 of a kind, or two pairs
            if ordered_values == [1, 1, 3]:
                # 3 of a kind
                base_hand_power = 3
            else:
                # 2 pairs
                base_hand_power = 3.2
        if len(unique_cards) == 4:
            base_hand_power = 4
        if len(unique_cards) == 5:
            base_hand_power = 5

        adjusted_hand_power = self.calculate_adjusted_hand_power()
        return base_hand_power + adjusted_hand_power

    def calculate_adjusted_hand_power(self):
        hand_order = ['A', 'K', 'Q', 'J', 'T', '9', '8', '7', '6', '5', '4', '3', '2']
        adjusted_hand_power = '0.0'
        for card_idx in range(len(self.hand)):
            current_card = self.hand[card_idx]
            hand_score = str(hand_order.index(current_card)+1)
            if len(hand_score) == 1:
                hand_score = "0" + hand_score
            adjusted_hand_power += hand_score
        return float(adjusted_hand_power)


def rank_players(players: List[Player]) -> List[Player]:
    hand_powers = [player.hand_power for player in players]
    arg_sort = sorted(range(len(hand_powers)), key=hand_powers.__getitem__, reverse=True)
    return [players[i] for i in arg_sort]

players = []
for line in txt.split("\n"):
    hand, bid = line.split(" ")
    players.append(Player(hand, int(bid)))

players_ranked = rank_players(players)

score = 0
for player_idx in range(len(players_ranked)):
    score+=players_ranked[player_idx].bid*(player_idx+1)
print(score)
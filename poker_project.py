import random

value_rank = {2:2, 3:3, 4:4, 5:5, 6:6, 7:7, 8:8, 9:9, 10:10, "Jack":11, "Queen":12, "King":13, "Ace":14}

class Card:
    def __init__(self, suit, value):
        self.suit = suit
        self.value = value

    def __str__(self):
        return f"{self.value} of {self.suit}"

    def __repr__(self):
        return self.__str__()





class Deck:

	def __init__(self):
		self.cards = []

		list_of_values = [2, 3, 4, 5, 6, 7, 8, 9, 10, "Jack", "Queen", "King", "Ace"]
		list_of_suits = ["Clubs", "Diamonds", "Hearts", "Spades"]

		for i in range(13):
			for j in range(4):
				c = Card(list_of_suits[j], list_of_values[i])
				self.cards.append(c)


		self.shuffle()
		self.cards_left = 52


	def draw_card(self):
		if self.cards_left == 0:
			return None
		
		self.cards_left = self.cards_left - 1
		return self.cards[self.cards_left]


		if self.cards_left > 0:
			return self.cards[self.cards_left]


	def shuffle(self):
		self.cards_left = len(self.cards)
		index = len(self.cards)-1
		while index >= 0:
			rand_pos = random.randint(0,index)
			rand_card = self.cards[rand_pos]
			self.cards[rand_pos] = self.cards[index]
			self.cards[index] = rand_card

			index = index - 1

		



def start_game():
	print("Welcome to 2 player poker game!")
	start_status = str(input("Would you like to start? (Y/N)"))
	while start_status != "Y" and start_status != "N":
		print("Please input either a 'Y' or a 'N'")
		start_status = input("Would you like to start? (Y/N)")

def set_up():
	d = Deck()
	card = d.draw_card()
	shuffled_cards = []
	while card != None:
		shuffled_cards.append(card)
		card = d.draw_card()
	return shuffled_cards

def player_showhand(player_name, player_hand):    	
	player_ready = input(f"{player_name}, are you ready to see your hand? (Y/N)")
	while player_ready != "Y" and player_ready != "N":
		print("Please input either a 'Y' or a 'N'")
		player_ready = input(f"{player_name}, are you ready to see your hand? (Y/N)")
	if player_ready == "Y":
		print(player_hand)
	player_hand_check = input(f"{player_name}, have you looked at your hand? (Y/N)")
	while player_hand_check != "Y" and player_hand_check != "N":
		print("Please input either a 'Y' or a 'N'")
		player_hand_check = input(f"{player_name}, have you looked at your hand? (Y/N)")
	if player_hand_check == "Y":
		for i in range(15):
			print()

			
def betting(player1_money, player2_money, pot):
	player1_bet_amount = int(input("Player 1, how much would you like to bet? (Bet $0 to check and bet a negative amount to fold): "))

	while player1_bet_amount > player1_money:
		print(f"Player 1, you only have ${player1_money}, you can't bet that much.")
		player1_bet_amount = int(input("Player 1, how much would you like to bet? (Bet $0 to check and bet a negative amount to fold): "))

	if player1_bet_amount < 0:
		print("Player 1 folded, Player 2 has won!")
		return player1_money, player2_money, pot, "Player 2"

	player1_money = player1_money - player1_bet_amount
	pot = pot + player1_bet_amount

	if player1_bet_amount == 0:
		print("Player 1 checked")
	if player1_bet_amount > 0:
	    print(f"Player 1 betted ${player1_bet_amount}")

	player2_bet_amount = int(input("Player 2, how much would you like to bet? (Bet $0 to check and bet a negative amount to fold): "))

	while player2_bet_amount > player2_money:
		print(f"Player 2, you only have ${player2_money}, you can't bet that much.")
		player2_bet_amount = int(input("Player 2, how much would you like to bet? (Bet $0 to check and bet a negative amount to fold): "))

	if player2_bet_amount < 0:
		print("Player 2 folded, Player 1 has won!")
		return player1_money, player2_money, pot, "Player 1"
	
	player2_money = player2_money - player2_bet_amount
	pot = pot + player2_bet_amount

	if player2_bet_amount == 0:
		print("Player 2 has checked")
	if player2_bet_amount > 0:
		print(f"Player 2 betted ${player2_bet_amount}")

	if player2_bet_amount > player1_bet_amount:
		call_amount = player2_bet_amount - player1_bet_amount
		print(f"Player 2 has raised by ${(call_amount)}, player 1, would you like to call?")
		
		if call_amount > player1_money:
			print("Player 1 doesn't have enough money to call")
			print("Player 1 folded")
			return player1_money, player2_money, pot, "Player 2"

		player1_bet_amount_raise = (int(input(f"Player 1, enter ${call_amount} to call (Or negative number to fold)")))

		if player1_bet_amount_raise < 0:
			print("Player 1 folded")
			return player1_money, player2_money, pot, "Player 2"
	
		player1_money = player1_money - player1_bet_amount_raise
		pot = pot + player1_bet_amount_raise
		print("Player 1 called")

	elif player1_bet_amount > player2_bet_amount:
		call_amount = player1_bet_amount - player2_bet_amount
		print(f"Player 1 has bet more, Player 2 needs ${call_amount} to call")

		if call_amount > player2_money:
			print("Player 2 doesn't have enough money to call")
			print("Player 2 folded")
			return player1_money, player2_money, pot, "Player 1"
		
		player2_bet_amount_raise = (int(input(f"Player 2, enter ${call_amount} to call (Or negative number to fold)")))

		if player2_bet_amount_raise < 0:
			print("Player 2 folded")
			return player1_money, player2_money, pot, "Player 1"
		
		player2_money = player2_money - player2_bet_amount_raise
		pot = pot + player2_bet_amount_raise

	print(f"The pot is now: ${pot}")
	print(f"Player 1's money: {player1_money}")
	print(f"Player 2's money: {player2_money}")
	return player1_money, player2_money, pot, "continue"

def game_status_check(game_status, player1_money, player2_money, pot):
	if game_status == "Player 1":
		player1_money = player1_money + pot
		print(f"Player 1 wins the pot of ${pot}!")
		return player1_money, player2_money, True
	
	elif game_status == "Player 2":
		player2_money = player2_money + pot
		print(f"Player 2 wins the pot of ${pot}!")
		return player1_money, player2_money, True
	
	else:
		return player1_money, player2_money, False
	

def show_flop(shuffled_cards):
	print(f"This is the flop: {shuffled_cards[4]}, {shuffled_cards[5]}, {shuffled_cards[6]}")

def show_turn(shuffled_cards):
	print(f"This is the turn card: {shuffled_cards[7]}")

def show_river(shuffled_cards):
	print(f"This is the river card: {shuffled_cards[8]}")


def sorted_values(cards):
	card_values = []

	for card in cards:
		card_rank = value_rank[card.value]
		card_values.append(card_rank)
	
	card_values.sort(reverse=True)

	return card_values


def determine_straight_flush(cards):
	suit_cards = {}

	for card in cards:
		if card.suit in suit_cards:
			suit_cards[card.suit].append(card)
		else:
			suit_cards[card.suit] = [card]

	best_straight_flush = 0

	for suit in suit_cards:
		if len(suit_cards[suit]) >= 5:
			straight_value = determine_straight(suit_cards[suit])

			if straight_value > best_straight_flush:
				best_straight_flush = straight_value
	
	return best_straight_flush


def determine_four_kind(cards):
	card_counts = {}

	for card in cards:
		card_rank = value_rank[card.value]

		if card_rank in card_counts:
			card_counts[card_rank] = card_counts[card_rank] + 1
		else:
			card_counts[card_rank] = 1
	
	four_kind_value = 0

	for card_rank in card_counts:
		if card_counts[card_rank] >= 4:
			if card_rank > four_kind_value:
				four_kind_value = card_rank
	
	if four_kind_value == 0:
		return [0,0]
	
	kicker = 0

	for card in cards:
		card_rank = value_rank[card.value]

		if card_rank != four_kind_value:
			if card_rank > kicker:
				kicker = card_rank
	
	return [four_kind_value, kicker]


def determine_full_house(cards):
	card_counts = {}

	for card in cards:
		card_rank = value_rank[card.value]

		if card_rank in card_counts:
			card_counts[card_rank] = card_counts[card_rank] + 1
		else:
			card_counts[card_rank] = 1
	
	three_kind_values = []
	pair_values = []

	for card_rank in card_counts:
		if card_counts[card_rank] >= 3:
			three_kind_values.append(card_rank)
		elif card_counts[card_rank] >= 2:
			pair_values.append(card_rank)
	three_kind_values.sort(reverse=True)
	pair_values.sort(reverse=True)

	if len(three_kind_values) >= 2:
		return [three_kind_values[0], three_kind_values[1]]
	elif len(three_kind_values) == 1 and len(pair_values) >= 1:
		return [three_kind_values[0], pair_values[0]]
	else:
		return [0,0]


def determine_flush(cards):
	suit_cards = {}

	for card in cards:
		if card.suit in suit_cards:
			suit_cards[card.suit].append(value_rank[card.value])
		else:
			suit_cards[card.suit] = [value_rank[card.value]]

	for suit in suit_cards:
		if len(suit_cards[suit]) >= 5:
			suit_cards[suit].sort(reverse=True)
			return suit_cards[suit][0:5]
	
	return[0]

def determine_straight(cards):
	card_values = []

	for card in cards:
		card_rank = value_rank[card.value]
		card_values.append(card_rank)

	card_values = list(set(card_values))
	card_values.sort(reverse=True)

	if 14 in card_values:
		card_values.append(1)
	
	for i in range(len(card_values) - 4):
		if card_values[i] == card_values[i + 1] + 1 and card_values[i + 1] == card_values[i + 2] + 1 and card_values[i + 2] == card_values[i + 3] + 1 and card_values[i + 3] == card_values[i + 4] + 1:
			return card_values[i]
		
	return 0


def determine_three_kind(cards):
	card_counts = {}

	for card in cards:
		card_rank = value_rank[card.value]

		if card_rank in card_counts:
			card_counts[card_rank] = card_counts[card_rank] + 1
		else:
			card_counts[card_rank] = 1
	
	highest_three_kind = 0

	for card_rank in card_counts:
		if card_counts[card_rank] >= 3:
			if card_rank > highest_three_kind:
				highest_three_kind = card_rank
	
	return highest_three_kind



def determine_two_pair(cards):
	card_counts = {}

	for card in cards:
		card_rank = value_rank[card.value]

		if card_rank in card_counts:
			card_counts[card_rank] = card_counts[card_rank] + 1
		else:
			card_counts[card_rank] = 1
	
	pairs = []

	for card_rank in card_counts:
		if card_counts[card_rank] >= 2:
			pairs.append(card_rank)
	
	pairs.sort(reverse=True)

	if len(pairs) < 2:
		return [0,0,0]
	
	high_pair = pairs[0]
	low_pair = pairs[1]

	kicker = 0

	for card in cards:
		card_rank = value_rank[card.value]
		
		if card_rank != high_pair and card_rank != low_pair:
			if card_rank > kicker:
				kicker = card_rank
	
	return [high_pair, low_pair, kicker]
	

	


def determine_pair(cards):
	card_counts = {}

	for card in cards:
		card_rank = value_rank[card.value]

		if card_rank in card_counts:
			card_counts[card_rank] = card_counts[card_rank] + 1
		else:
			card_counts[card_rank] = 1
	
	highest_pair = 0

	for card_rank in card_counts:
		if card_counts[card_rank] >= 2:
			if card_rank > highest_pair:
				highest_pair = card_rank
	
	return highest_pair



def determine_high_card(player1_hand, player2_hand, community_cards):
	player1_total_cards = player1_hand + community_cards
	player2_total_cards = player2_hand + community_cards

	player1_values = sorted_values(player1_total_cards)
	player2_values = sorted_values(player2_total_cards)

	print(f"Player 1's highest card value is {player1_values}")
	print(f"Player 2's highest card value is {player2_values}")

	if player1_values > player2_values:
		return "Player 1"
	elif player2_values > player1_values:
		return "Player 2"
	else:
		return "Tie"
	

def determine_winner(player1_hand, player2_hand, community_cards):
	player1_total_cards = player1_hand + community_cards
	player2_total_cards = player2_hand + community_cards

	player1_straight_flush = determine_straight_flush(player1_total_cards)
	player2_straight_flush = determine_straight_flush(player2_total_cards)

	print(f"Player 1's straight flush value is {player1_straight_flush}")
	print(f"Player 2's straight flush value is {player2_straight_flush}")

	if player1_straight_flush > player2_straight_flush:
		return "Player 1", "a straight flush"
	elif player2_straight_flush > player1_straight_flush:
		return "Player 2", "a straight flush"
	elif player1_straight_flush > 0 and player2_straight_flush > 0:
		return "Tie", "the same straight flush"


	player1_four_kind = determine_four_kind(player1_total_cards)
	player2_four_kind = determine_four_kind(player2_total_cards)

	print(f"Player 1's four of a kind value is {player1_four_kind}")
	print(f"Player 2's four of a kind value is {player2_four_kind}")

	if player1_four_kind != [0,0] or player2_four_kind != [0,0]:
		if player1_four_kind > player2_four_kind:
			return "Player 1", "four of a kind"
		elif player2_four_kind > player1_four_kind:
			return "Player 2", "four of a kind"
		else:
			return "Tie", "the same four of a kind"


	player1_full_house = determine_full_house(player1_total_cards)
	player2_full_house = determine_full_house(player2_total_cards)

	print(f"Player 1's full house value is {player1_full_house}")
	print(f"Player 2's full house value is {player2_full_house}")

	if player1_full_house != [0,0] or player2_full_house != [0,0]:
		if player1_full_house > player2_full_house:
			return "Player 1", "a full house"
		elif player2_full_house > player1_full_house:
			return "Player 2", "a full house"
		else:
			return "Tie", "the same full house"
		

	player1_flush = determine_flush(player1_total_cards)
	player2_flush = determine_flush(player2_total_cards)

	print(f"Player 1's flush value is {player1_flush}")
	print(f"Player 2's flush value is {player2_flush}")

	if player1_flush !=[0] or player2_flush != [0]:
		if player1_flush > player2_flush:
			return "Player 1", "a flush"
		elif player2_flush > player1_flush:
			return "Player 2", "a flush"
		else:
			return "Tie", "the same flush"

	player1_straight = determine_straight(player1_total_cards)
	player2_straight = determine_straight(player2_total_cards)

	print(f"Player 1's straight value is {player1_straight}")
	print(f"Player 2's straight value is {player2_straight}")

	if player1_straight > player2_straight:
		return "Player 1", "a straight"
	elif player2_straight > player1_straight:
		return "Player 2", "a straight"
	elif player1_straight > 0 and player2_straight > 0:
		return "Tie", "the same straight"


	player1_three_kind = determine_three_kind(player1_total_cards)
	player2_three_kind = determine_three_kind(player2_total_cards)

	print(f"Player 1's three of a kind value is {player1_three_kind}")
	print(f"Player 2's three of a kind value is {player2_three_kind}")

	if player1_three_kind > player2_three_kind:
		return "Player 1", "three of a kind"
	elif player2_three_kind > player1_three_kind:
		return "Player 2", "three of a kind"
	
	elif player1_three_kind > 0 and player2_three_kind > 0:
		player1_values = sorted_values(player1_total_cards)
		player2_values = sorted_values(player2_total_cards)

		if player1_values > player2_values:
			return "Player 1", "a better three of a kind"
		elif player2_values > player1_values:
			return "Player 2", "a better three of a kind"
		else:
			return "Tie", "same three of a kind"


	player1_two_pair = determine_two_pair(player1_total_cards)
	player2_two_pair = determine_two_pair(player2_total_cards)

	print(f"Player 1's two pair value is {player1_two_pair}")
	print(f"Player 2's two pair value is {player2_two_pair}")

	if player1_two_pair != [0,0,0] or player2_two_pair != [0,0,0]:
		if player1_two_pair > player2_two_pair:
			return "Player 1", "two pair"
		elif player2_two_pair > player1_two_pair:
			return "Player 2", "two pair"
		else:
			return "Tie", "same two pair."

	player1_pair = determine_pair(player1_total_cards)
	player2_pair = determine_pair(player2_total_cards)

	print(f"Player 1's pair value is {player1_pair}")
	print(f"Player 2's pair value is {player2_pair}")

	if player1_pair > player2_pair:
		return "Player 1", "a pair"
	elif player2_pair > player1_pair:
		return "Player 2", "a pair"
	
	elif player1_pair > 0 and player2_pair > 0:
		player1_values = sorted_values(player1_total_cards)
		player2_values = sorted_values(player2_total_cards)

		if player1_values > player2_values:
			return "Player 1", "a better pair"
		elif player2_values > player1_values:
			return "Player 2", "a better pair"
		else:
			return "Tie", "same pair"
	
	else:
		winner = determine_high_card(player1_hand, player2_hand, community_cards)
		return winner, "high card"



def main():
	start_game()
	shuffled_cards = set_up()
	# player1 = player()
	player1_name = "Player 1"
	player1_hand = [shuffled_cards[0], shuffled_cards[2]]
	player1_money = int(input("Player 1 please enter your buy in: "))
	# player2 = player()
	player2_name = "Player 2"
	player2_hand = [shuffled_cards[1], shuffled_cards[3]]
	player2_money = int(input("Player 2 please enter your buy in: "))

	pot = 0

	community_cards = [shuffled_cards[4], shuffled_cards[5], shuffled_cards[6], shuffled_cards[7], shuffled_cards[8]]

	player_showhand(player1_name, player1_hand)
	player_showhand(player2_name, player2_hand)

	print("Pre-flop betting round")

	player1_money, player2_money, pot, game_status = betting(player1_money, player2_money, pot)

	player1_money, player2_money, game_over = game_status_check(game_status, player1_money, player2_money, pot)

	if game_over == True:
		return "Game ended"

	show_flop(shuffled_cards)
	
	player1_money, player2_money, pot, game_status = betting(player1_money, player2_money, pot)

	player1_money, player2_money, game_over = game_status_check(game_status, player1_money, player2_money, pot)

	if game_over == True:
		return "Game ended"
	
	
	show_turn(shuffled_cards)

	player1_money, player2_money, pot, game_status = betting(player1_money, player2_money, pot)

	player1_money, player2_money, game_over = game_status_check(game_status, player1_money, player2_money, pot)

	if game_over == True:
		return "Game ended"
	
	show_river(shuffled_cards)

	player1_money, player2_money, pot, game_status = betting(player1_money, player2_money, pot)

	
	player1_money, player2_money, game_over = game_status_check(game_status, player1_money, player2_money, pot)

	if game_over == True:
		return "Game ended"
	
	winner, winning_hand = determine_winner(player1_hand, player2_hand, community_cards)

	if winner == "Player 1":
		player1_money = player1_money + pot
		print(f"Player 1 wins with {winning_hand} and gets the pot of ${pot}")

	elif winner == "Player 2":
		player2_money = player2_money + pot
		print(f"Player 2 wins with {winning_hand} and gets the pot of ${pot}")

	else:
		player1_money = player1_money + pot / 2
		player2_money = player2_money + pot / 2
		print("It is a tie. The pot is split.")
	
	print(f"Player 1 final money: ${player1_money}")
	print(f"Player 2 final money: ${player2_money}")
	
if __name__=='__main__':
	main()

	


	

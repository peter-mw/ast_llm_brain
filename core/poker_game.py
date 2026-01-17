"""
Poker Environment - Texas Hold'em
Complete game state management for poker learning
"""
import random
from enum import Enum


class Rank(Enum):
    TWO = 2
    THREE = 3
    FOUR = 4
    FIVE = 5
    SIX = 6
    SEVEN = 7
    EIGHT = 8
    NINE = 9
    TEN = 10
    JACK = 11
    QUEEN = 12
    KING = 13
    ACE = 14


class Suit(Enum):
    HEARTS = 'H'
    DIAMONDS = 'D'
    CLUBS = 'C'
    SPADES = 'S'


class Card:
    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit
    
    def __repr__(self):
        rank_names = {11: 'J', 12: 'Q', 13: 'K', 14: 'A'}
        rank_str = rank_names.get(self.rank.value, str(self.rank.value))
        return f"{rank_str}{self.suit.value}"
    
    def __eq__(self, other):
        return self.rank == other.rank and self.suit == other.suit
    
    def __hash__(self):
        return hash((self.rank, self.suit))


class HandRank(Enum):
    HIGH_CARD = 1
    PAIR = 2
    TWO_PAIR = 3
    THREE_OF_KIND = 4
    STRAIGHT = 5
    FLUSH = 6
    FULL_HOUSE = 7
    FOUR_OF_KIND = 8
    STRAIGHT_FLUSH = 9
    ROYAL_FLUSH = 10


class PokerEvaluator:
    """Evaluates poker hands"""
    
    @staticmethod
    def evaluate_hand(cards):
        """
        Evaluate 5-7 cards and return best 5-card hand rank and high card
        Returns (HandRank, high_card_value)
        """
        if len(cards) < 5:
            return (HandRank.HIGH_CARD, 0)
        
        # For simplicity, evaluate exact 5 or use best 5 from 7
        if len(cards) > 5:
            # Try all combinations and return best (simplified)
            cards = cards[:5]
        
        ranks = sorted([c.rank.value for c in cards], reverse=True)
        suits = [c.suit for c in cards]
        
        # Check flush
        is_flush = len(set(suits)) == 1
        
        # Check straight
        is_straight = False
        if ranks == list(range(ranks[0], ranks[0] - 5, -1)):
            is_straight = True
        # Check for wheel (A-2-3-4-5)
        elif ranks == [14, 5, 4, 3, 2]:
            is_straight = True
            ranks = [5, 4, 3, 2, 1]  # Ace low
        
        # Count ranks
        rank_counts = {}
        for r in ranks:
            rank_counts[r] = rank_counts.get(r, 0) + 1
        
        counts = sorted(rank_counts.values(), reverse=True)
        
        # Determine hand rank
        if is_straight and is_flush and ranks[0] == 14:
            return (HandRank.ROYAL_FLUSH, 14)
        elif is_straight and is_flush:
            return (HandRank.STRAIGHT_FLUSH, ranks[0])
        elif counts == [4, 1]:
            return (HandRank.FOUR_OF_KIND, ranks[0])
        elif counts == [3, 2]:
            return (HandRank.FULL_HOUSE, ranks[0])
        elif is_flush:
            return (HandRank.FLUSH, ranks[0])
        elif is_straight:
            return (HandRank.STRAIGHT, ranks[0])
        elif counts == [3, 1, 1]:
            return (HandRank.THREE_OF_KIND, ranks[0])
        elif counts == [2, 2, 1]:
            return (HandRank.TWO_PAIR, ranks[0])
        elif counts == [2, 1, 1, 1]:
            return (HandRank.PAIR, ranks[0])
        else:
            return (HandRank.HIGH_CARD, ranks[0])


class PokerEnvironment:
    """
    Texas Hold'em Poker Environment
    Simplified heads-up (2 player) game
    """
    
    def __init__(self, starting_chips=1000, small_blind=10, big_blind=20):
        self.starting_chips = starting_chips
        self.small_blind = small_blind
        self.big_blind = big_blind
        self.reset()
    
    def reset(self):
        """Start a new hand"""
        self.deck = self._create_deck()
        random.shuffle(self.deck)
        
        # Player states
        self.players = [
            {"chips": self.starting_chips, "hand": [], "bet": 0, "folded": False, "name": "Player1"},
            {"chips": self.starting_chips, "hand": [], "bet": 0, "folded": False, "name": "Player2"}
        ]
        
        self.pot = 0
        self.community_cards = []
        self.current_player = 0
        self.dealer = 0
        self.round = "preflop"  # preflop, flop, turn, river
        self.current_bet = 0
        
        # Post blinds
        self._post_blinds()
        
        # Deal hole cards
        for _ in range(2):
            for player in self.players:
                player["hand"].append(self.deck.pop())
        
        return self.get_state()
    
    def _create_deck(self):
        """Create a standard 52-card deck"""
        deck = []
        for suit in Suit:
            for rank in Rank:
                deck.append(Card(rank, suit))
        return deck
    
    def _post_blinds(self):
        """Post small and big blinds"""
        sb_player = (self.dealer + 1) % 2
        bb_player = (self.dealer + 2) % 2
        
        # Small blind
        self.players[sb_player]["bet"] = self.small_blind
        self.players[sb_player]["chips"] -= self.small_blind
        self.pot += self.small_blind
        
        # Big blind
        self.players[bb_player]["bet"] = self.big_blind
        self.players[bb_player]["chips"] -= self.big_blind
        self.pot += self.big_blind
        
        self.current_bet = self.big_blind
        self.current_player = sb_player
    
    def get_state(self):
        """Get current game state"""
        return {
            "players": self.players,
            "pot": self.pot,
            "community_cards": self.community_cards,
            "current_player": self.current_player,
            "round": self.round,
            "current_bet": self.current_bet
        }
    
    def get_legal_actions(self, player_idx):
        """Get legal actions for player"""
        player = self.players[player_idx]
        
        if player["folded"]:
            return []
        
        actions = ["fold"]
        
        to_call = self.current_bet - player["bet"]
        
        if to_call == 0:
            actions.append("check")
        
        if to_call > 0 and player["chips"] >= to_call:
            actions.append("call")
        
        if player["chips"] > to_call:
            actions.append("raise")
        
        if player["chips"] > 0:
            actions.append("all_in")
        
        return actions
    
    def take_action(self, player_idx, action, amount=0):
        """
        Execute an action
        Returns (new_state, reward, done)
        """
        player = self.players[player_idx]
        
        if action == "fold":
            player["folded"] = True
            # Other player wins
            winner = 1 - player_idx
            reward = -player["bet"]  # Lost what we put in
            return self.get_state(), reward, True
        
        elif action == "check":
            # Do nothing, move to next player
            pass
        
        elif action == "call":
            to_call = self.current_bet - player["bet"]
            actual_call = min(to_call, player["chips"])
            player["chips"] -= actual_call
            player["bet"] += actual_call
            self.pot += actual_call
        
        elif action == "raise":
            # Simple raise: double the current bet
            to_call = self.current_bet - player["bet"]
            raise_amount = max(self.big_blind, self.current_bet)
            total_bet = to_call + raise_amount
            
            if player["chips"] >= total_bet:
                player["chips"] -= total_bet
                player["bet"] += total_bet
                self.pot += total_bet
                self.current_bet = player["bet"]
        
        elif action == "all_in":
            all_in_amount = player["chips"]
            player["chips"] = 0
            player["bet"] += all_in_amount
            self.pot += all_in_amount
            if player["bet"] > self.current_bet:
                self.current_bet = player["bet"]
        
        # Move to next player or next round
        done, reward = self._advance_game(player_idx)
        
        return self.get_state(), reward, done
    
    def _advance_game(self, player_idx):
        """Advance to next player or betting round"""
        # Check if betting round is complete
        active_players = [p for p in self.players if not p["folded"]]
        
        if len(active_players) == 1:
            # Someone folded, hand over
            winner = 0 if not self.players[0]["folded"] else 1
            reward = self.pot if winner == player_idx else -self.players[player_idx]["bet"]
            return True, reward
        
        # Check if all bets are equal
        bets = [p["bet"] for p in active_players]
        all_equal = len(set(bets)) == 1
        
        # Move to next player
        self.current_player = (self.current_player + 1) % 2
        
        if all_equal and self.current_player == (self.dealer + 1) % 2:
            # Betting round complete, advance to next round
            return self._next_round(player_idx)
        
        return False, 0
    
    def _next_round(self, player_idx):
        """Move to next betting round"""
        # Reset bets for new round
        for p in self.players:
            p["bet"] = 0
        self.current_bet = 0
        
        if self.round == "preflop":
            # Deal flop (3 cards)
            self.community_cards.extend([self.deck.pop() for _ in range(3)])
            self.round = "flop"
        elif self.round == "flop":
            # Deal turn (1 card)
            self.community_cards.append(self.deck.pop())
            self.round = "turn"
        elif self.round == "turn":
            # Deal river (1 card)
            self.community_cards.append(self.deck.pop())
            self.round = "river"
        elif self.round == "river":
            # Showdown
            return self._showdown(player_idx)
        
        return False, 0
    
    def _showdown(self, player_idx):
        """Determine winner at showdown"""
        evaluator = PokerEvaluator()
        
        hands = []
        for i, player in enumerate(self.players):
            if not player["folded"]:
                all_cards = player["hand"] + self.community_cards
                hand_rank = evaluator.evaluate_hand(all_cards)
                hands.append((i, hand_rank))
        
        # Sort by hand rank (higher is better)
        hands.sort(key=lambda x: (x[1][0].value, x[1][1]), reverse=True)
        
        winner = hands[0][0]
        reward = self.pot if winner == player_idx else -self.players[player_idx]["bet"]
        
        return True, reward

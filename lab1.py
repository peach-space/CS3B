import random

# Card Class
class Card:
    def __init__(self, suit, value):
        self.suit = suit
        self.value = value

    def __str__(self):
        return f"{self.value} of {self.suit}"

    def __repr__(self):
        return f"{self.value} of {self.suit}"

# Deck Class
class Deck:
    def __init__(self):
        self.cards = []
        self.shuffle()

    def shuffle(self):
        suits = ["Hearts", "Diamonds", "Clubs", "Spades"]
        values = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
        self.cards = [Card(suit, value) for suit in suits for value in values]
        random.shuffle(self.cards)

    def deal(self):
        if len(self.cards) == 0:
            raise ValueError("The deck is empty.")
        return self.cards.pop()

    def __len__(self):
        return len(self.cards)

if __name__ == "__main__":
    # student information and the class logistics
    print("Name: Cen Li")
    print("Student ID: 20713344")
    print("Email: liceno1992@gmail.com")
    print("Policy Highlights: Contacting Your Instructor, Enrollment, Late Submission, Regrade.")

    my_deck = Deck()
    print(f"\nNew deck has {len(my_deck)} cards")
    print(f"Dealt: {my_deck.deal()}")
    print(f"Remaining: {len(my_deck)} cards")
    print("Dealing 5 more cards:")
    for i in range(5):
        print(f"{my_deck.deal()}")
    print(f"Remaining: {len(my_deck)} cards")

    my_deck.shuffle()
    print(f"\nAfter shuffle: {len(my_deck)} cards")
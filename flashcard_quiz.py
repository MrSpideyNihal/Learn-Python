"""Simple flashcard quiz."""
import random

def generate_flashcards(card_count):
    """Generate a specified number of flashcards."""
    cards = {}
    for i in range(card_count):
        word = ''.join(random.choice('abcdefghijklmnopqrstuvwxyz') for _ in range(5))
        definition = ' '.join(random.choice(['noun', 'verb', 'adjective', 'adverb']) + random.choice('abcdefghijklmnopqrstuvwxyz') for _ in range(3))
        cards[word] = definition
    return cards

if __name__ == "__main__":
    flashcards = generate_flashcards(10)
    for word, definition in flashcards.items():
        print(f"{word}: {definition}")

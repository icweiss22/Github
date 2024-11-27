import random

# List of French words and their English translations
words = {
    "chien": "dog",
    "chat": "cat",
    "maison": "house",
    "voiture": "car",
    "pomme": "apple",
    "livre": "book",
    "école": "school",
    "amour": "love",
    "soleil": "sun",
    "lune": "moon"
}


def play_game():
    french_word, english_word = random.choice(list(words.items()))
    print(f"Guess the English word for: {french_word}")

    attempts = 3
    while attempts > 0:
        guess = input("Your guess: ").strip().lower()
        if guess == english_word:
            print("Correct! Well done!")
            break
        else:
            attempts -= 1
            print(f"Incorrect. You have {attempts} attempts left.")

    if attempts == 0:
        print(f"Sorry, the correct word was: {english_word}")


if __name__ == "__main__":
    while True:
        play_game()

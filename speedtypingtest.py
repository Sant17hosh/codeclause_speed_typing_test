import random
import time

# List of words for the typing test
word_list = [
    "programming",
    "challenge",
    "python",
    "speed",
    "typing",
    "openai",
    "practice",
    "keyboard",
    "language",
    "development",
]

def run_speed_typing_test():
    input("Press Enter to start the typing test...")
    print("Get ready...")

    time.sleep(2)

    start_time = time.time()

    # Shuffle the word list for randomness
    random.shuffle(word_list)

    correct_words = 0

    for word in word_list:
        print(f"Type the word: {word}")
        user_input = input("Your input: ")

        if user_input == word:
            correct_words += 1

    end_time = time.time()
    total_time = end_time - start_time
    words_per_minute = int((correct_words / total_time) * 60)

    print("\nTyping test completed!")
    print(f"Words per minute: {words_per_minute}")
    print(f"Correct words: {correct_words}/{len(word_list)}")

if __name__ == "__main__":
    print("Welcome to the Speed Typing Test!")
    while True:
        run_speed_typing_test()
        play_again = input("Do you want to play again? (yes/no): ").lower()
        if play_again != "yes":
            break

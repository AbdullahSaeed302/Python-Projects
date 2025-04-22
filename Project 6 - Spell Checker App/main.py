# Step 1 - Loading the required Library's
from spellchecker import SpellChecker
import time
from termcolor import colored # Module used to manage the colours of the output's (text/background)

# Step 2 - Creating the App's class to handle different functions
class SpellCheckerApp:
    def __init__(self):
        self.spell = SpellChecker()
        self.ignore_words = set()  # Set to store words to ignore

    # Step 3 - (Option 1) Function to check each word and provide correctness & suggestions if required
    def correct_text(self, text):
        corrected_text = [] # List to store the corrected text after processing
        original_case = {}  # Dictionary to store original case

        words = text.split()
        for word in words:
            original_case[word] = word # Contains the list of word's original form
            lower_word = word.lower()

            if lower_word in self.ignore_words:
                corrected_text.append(original_case[word])
                continue

            if self.spell.unknown([lower_word]):  # Only check if word is unknown
                corrected_word = self.spell.correction(lower_word)
                suggestions = ', '.join(self.spell.candidates(lower_word))

                if corrected_word:
                    print(f"\nCorrecting '{original_case[word]}' to '{corrected_word}'")
                    print(f"Suggestions: {suggestions}")
                    corrected_text.append(corrected_word)
                else:
                    corrected_text.append(original_case[word])  # No correction found
            else:
                corrected_text.append(original_case[word])

        return ' '.join(corrected_text) # Returns the corrected sentence (if needed)

    # Step 4 - (Option 2) Function to manage ignored words (don't want correctness)
    def manage_ignore_list(self):
        while True:
            action = input("\nType 'add' to add a word to ignore list, 'view' to see ignore list, 'remove' to delete, or 'back' to return: ").lower()
            if action == 'add':
                word = input("Enter a word to ignore: ").strip().lower()
                if word:
                    self.ignore_words.add(word) # Add's the given word to the ignored word's list
                    print(colored(f"'{word}' added to ignore list.", 'yellow'))
            elif action == 'view':
                print(f"Ignore List: {', '.join(self.ignore_words) if self.ignore_words else 'Empty'}") # Preview's ignored words list
            elif action == 'remove':
                word = input("Enter a word to remove from ignore list: ").strip().lower()
                if word in self.ignore_words:
                    self.ignore_words.remove(word) # Removes the ignored word from the list (if present)
                    print(colored(f"'{word}' removed from ignore list.", 'yellow'))
                else:
                    print(colored(f"'{word}' not found in ignore list.", 'red'))
            elif action == 'back':
                break # Returns to the home page

    # Step 5 - Function which will run each time (i.e. Homepage)
    def run(self):
        print(colored("-" * 75, 'green'))
        print(colored(f'>> Welcome to SPELL CHECKER 4.0 - Created by \u2022 Aesthetic Coder \u2022', 'green'))
        time.sleep(1.5)

        while True:
            print("\nOptions: 1) Check Spelling 2) Manage Ignore List 3) Exit")
            choice = input("Select an option (1/2/3): ").strip()
            
            if choice == '1':
                text = input("Enter text to check: ")
                if text.strip():
                    corrected_text = self.correct_text(text) # Processes the text and stores the corrected text
                    print(colored(f"\nCorrected Text: {corrected_text.title()}", 'blue'))
                else:
                    print(colored("Please enter non-empty text.", 'light_red'))
            elif choice == '2':
                self.manage_ignore_list()
            elif choice == '3':
                print(colored("\nClosing the SPELL CHECKER App...", 'yellow'))
                time.sleep(1.5)
                print(colored("-" * 75, 'yellow'))
                break # Terminates the program
            else:
                print(colored("Invalid choice. Please try again.", 'red'))

# Step 6 - Starting the SPELL CHECKER App!
if __name__ == '__main__':
    SpellCheckerApp().run() # Run's the interface (Homepage) of the SPELL CHECKER App
import random

words = [
    {"German": "der", "English": "the"},
    {"German": "die", "English": "the"},
    {"German": "und", "English": "and"},
    {"German": "in", "English": "in"},
    {"German": "den", "English": "the"},
    {"German": "von", "English": "of"},
    {"German": "zu", "English": "to"},
    {"German": "das", "English": "the"},
    {"German": "mit", "English": "with"},
    {"German": "sich", "English": "itself"},
    {"German": "des", "English": "of"},
    {"German": "auf", "English": "on"},
    {"German": "für", "English": "for"},
    {"German": "ist", "English": "is"},
    {"German": "im", "English": "in"},
    {"German": "dem", "English": "the"},
    {"German": "nicht", "English": "not"},
    {"German": "ein", "English": "a"},
    {"German": "Die", "English": "The"},
    {"German": "eine", "English": "a"},
    {"German": "als", "English": "as"},
    {"German": "auch", "English": "also"},
    {"German": "es", "English": "it"},
    {"German": "an", "English": "at"},
    {"German": "werden", "English": "become"},
    {"German": "aus", "English": "out"},
    {"German": "er", "English": "he"},
    {"German": "hat", "English": "has"},
    {"German": "dass", "English": "that"},
    {"German": "sie", "English": "she"},
    {"German": "nach", "English": "after"},
    {"German": "wird", "English": "will"},
    {"German": "bei", "English": "at"},
    {"German": "einer", "English": "a"},
    {"German": "Der", "English": "The"},
    {"German": "um", "English": "around"},
    {"German": "am", "English": "on"},
    {"German": "sind", "English": "are"},
    {"German": "noch", "English": "still"},
    {"German": "wie", "English": "how"},
]


def quiz_user(words):
    random.shuffle(words)
    score = 0
    total = 0
    for word in words:
        print(f"What is the English translation of  '{word['German']}'?")
        user_answer = input("Your answer: ").lower()
        total = total + 1
        if user_answer == word['English'].lower():
            print("Correct!\n")
            score += 1
            choice = input("Enter N to exit: ")
            if choice.lower() == "n" or choice == "N" :
                break
            else:
                continue
        else:
            print("Incorrect!")
            print(f"The correct answer is '{word['English']}'\n")
            choice = input("Enter N to exit: ")
            if choice.lower() == "n" or choice == "N" :
                break
            else:
                continue

    print(f"You got {score} out of "+str(total)+ " correct!")

def main():
    print("Welcome to the language learning App")
    input("Press Enter to start the quiz...")
    quiz_user(words)

if __name__ == "__main__":
    main()
import random

# List of possible words
words = ["python", "programacion", "computadora", "codigo", "desarrollo", 
         "inteligencia"]
# Select a random word
secret_word = random.choice(words)
# Max number of attemps
max_attempts = 10
print ('*'*100)
print("¡Bienvenido al juego de adivinanzas!")
print("Estoy pensando en una palabra. ¿Puedes adivinar cuál es?")
print ('*'*100)
# Select difficulty level
dificultad = input("Seleccione el nivel de dificultad: Fácil (F), Media (M) o Difícil (D)").casefold()

# Validate the selected option
while dificultad != "f" and dificultad != "m" and dificultad != "d":
    print ("La opcion ingresada no está disponible")
    dificultad = input("Seleccione el nivel de dificultad: Fácil (F), Media (M) o Difícil (D)").casefold()
# Complete the word according to the difficulty level
if dificultad == "d":
    # Empty list
    guessed_letters = []
elif dificultad == "m":
    # First and last letter in list
    guessed_letters = [secret_word[0], secret_word[-1]]
elif dificultad == "f":
    # Vowels in list
    guessed_letters = ["a", "e", "i", "o", "u"]
letters = []

# Show the partially guessed word
for letter in secret_word:
    if letter in guessed_letters:
        letters.append(letter)
    else:
        letters.append("_")
word_displayed = "".join(letters)
print(f"Palabra: {word_displayed}")

# Remaining attemps counter. When 0, player loses
remaining_attempts = max_attempts
while remaining_attempts > 0:
    # Player selects a letter
    print ("")
    letter = input("Ingresa una letra: ").lower()
    if letter in guessed_letters:
        print("Ya has intentado con esa letra. Intenta con otra.")
    # Verify that a letter was entered
    elif not letter:
        print ("Por favor, ingrese una letra")
    # Verify that the input was only a letter
    elif len(letter) > 1:
        print ("Por favor, ingrese solo una letra")
    else: 
        # Add letter to guessed letters list
        guessed_letters.append(letter)
        # Verify if guessed letter is in secret word
        if letter in secret_word:
            print("¡Bien hecho! La letra está en la palabra.")
        else:
            print("Lo siento, la letra no está en la palabra.")
            # If incorrecty guessed, reduce remaining attempts
            remaining_attempts -=1
        # Show the partially guessed word
        letters = []
        for letter in secret_word:
            if letter in guessed_letters:
                letters.append(letter)
            else:
                letters.append("_")
    word_displayed = "".join(letters)
    print(f"Palabra: {word_displayed}")
    # If less than 6 attempts remaining, show the remaining attepts and draw hanging body
    if remaining_attempts < 6 and remaining_attempts > 0:
        print(f"Intentos restantes: {remaining_attempts}")
        print("  0")
        if remaining_attempts == 4:
            print("  |")
            print(" ")
        elif remaining_attempts == 3:
            print(" /|")
            print(" ")
        elif remaining_attempts == 2:
            print(" /|\\")
            print(" ")
        elif remaining_attempts == 1:
            print(" /|\\")
            print(" /")

    # Verify if the word was guessed correctly
    if word_displayed == secret_word:
        print('*'*100)
        print(f"¡Felicidades! Has adivinado la palabra secreta: {secret_word}")
        print('*'*100)
        break
else:
    print('*'*100)
    print("  0")
    print(" /|\\")
    print(" / \\")
    print(f"¡Oh no! Has agotado tus {max_attempts} intentos.")
    print(f"La palabra secreta era: {secret_word}")
    print ('*'*100)
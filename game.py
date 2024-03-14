import random

# Lista de palabras posibles
words = ["python", "programación", "computadora", "código", "desarrollo", 
         "inteligencia"]
# Elegir una palabra al azar
secret_word = random.choice(words)
# Número máximo de intentos permitidos
max_attempts = 10

print("¡Bienvenido al juego de adivinanzas!")
print("Estoy pensando en una palabra. ¿Puedes adivinar cuál es?")

#Consultar nivel de dificultad elegido
dificultad = input("Seleccione el nivel de dificultad: Fácil (F), Media (M) o Difícil (D)").lower()
#Verificar si se ingresó una opción válida
while dificultad != "f" and dificultad != "m" and dificultad != "d":
    print ("La opcion ingresada no está disponible")
    dificultad = input("Seleccione el nivel de dificultad: Fácil (F), Media (M) o Difícil (D)").lower()
#Mostrar la palabra según el nivel de dificultad
if dificultad == "d":
    # Lista para almacenar las letras adivinadas. Ninguna letra
    guessed_letters = []
elif dificultad == "m":
    # Lista para almacenar las letras adivinadas. Con primera y ultima letra
    guessed_letters = [secret_word[0], secret_word[len(secret_word)-1]]
elif dificultad == "f":
    # Lista para almacenar las letras adivinadas. Con vocales
    guessed_letters = ["a", "e", "i", "o", "u"]
letters = []

# Mostrarla palabra parcialmente adivinada
for letter in secret_word:
    if letter in guessed_letters:
        letters.append(letter)
    else:
        letters.append("_")
word_displayed = "".join(letters)
print(f"Palabra: {word_displayed}")

#Contador de intentos restantes
remaining_attempts = max_attempts
while remaining_attempts > 0:
    # Pedir al jugador que ingrese una letra
    letter = input("Ingresa una letra: ").lower()
    # Verificar si la letra ya ha sido adivinada
    if letter in guessed_letters:
        print("Ya has intentado con esa letra. Intenta con otra.")
    # Verificar si ingresó una letra
    elif not letter:
        print ("Por favor, ingrese una letra")
    # Verificar si ingresó más de una letra
    elif len(letter) > 1:
        print ("Por favor, ingrese solo una letra")
    else: 
        # Agregar la letra a la lista de letras adivinadas
        guessed_letters.append(letter)
        # Verificar si la letra está en la palabra secreta
        if letter in secret_word:
            print("¡Bien hecho! La letra está en la palabra.")
        else:
            print("Lo siento, la letra no está en la palabra.")
            # Disminuir la cantidad de intentos restantes únicamente en caso de fallos
            remaining_attempts -=1
        # Mostrar la palabra parcialmente adivinada
        letters = []
        for letter in secret_word:
            if letter in guessed_letters:
                letters.append(letter)
            else:
                letters.append("_")
    word_displayed = "".join(letters)
    print(f"Palabra: {word_displayed}")
    # Indicar la cantidad de intentos restantes
    print (f"Intentos restantes: {remaining_attempts}")
    # Verificar si se ha adivinado la palabra completa
    if word_displayed == secret_word:
        print(f"¡Felicidades! Has adivinado la palabra secreta: {secret_word}")
        break
else:
    print(f"¡Oh no! Has agotado tus {max_attempts} intentos.")
    print(f"La palabra secreta era: {secret_word}")
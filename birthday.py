import time
import pygame
from colorama import Fore, Style, init

# Initialize colorama
init()

# Initialize pygame for sound
pygame.mixer.init()
#pygame.mixer.music.load("happy_birthday_song.mp3")  # Replace with the path to your song file

# Birthday Message
def birthday_message():
    print(Fore.MAGENTA + Style.BRIGHT + "\n\n🎉 🎂 Happy Birthday! 🎂 🎉")
    print("Wishing you a day filled with love, laughter, and everything you dream of!\n" + Style.RESET_ALL)
    print("Happy birthday mere babu , mere bchu , mere motu , khotu , pyaru , YOU ARE REALLY SPECIAL")

# Birthday Cake ASCII Art
def cake():
    print(Fore.YELLOW + "         i i i i i i i i i ")
    print(Fore.RED + "        |~~~~~~~~~~~~~~~|")
    print(Fore.YELLOW + "       |  🍰    🍰    🍰   |")
    print(Fore.CYAN + "    ======================")
    print(Fore.MAGENTA + "   ||  H A P P Y  B I R T H D A Y ||")
    print(Fore.CYAN + "    ======================")
    print(Fore.RED + "        |   🎉 🎉 🎉 🎉   |")
    print(Style.RESET_ALL)

# Candle Flicker Effect
def candle_flicker():
    for i in range(5):
        print(Fore.YELLOW + "         i i i i i i i i i " if i % 2 == 0 else "         i i i i i i i i i ", end="\r")
        time.sleep(0.5)

# Light Animation Effect
def light_animation():
    colors = [Fore.RED, Fore.GREEN, Fore.YELLOW, Fore.CYAN, Fore.MAGENTA]
    for i in range(10):
        print(colors[i % len(colors)] + "🎈🎈🎈 🎉 Happy Birthday 🎉 🎈🎈🎈", end="\r")
        time.sleep(0.4)
    print(Style.RESET_ALL)

# Main Function
def celebrate_birthday():
   # pygame.mixer.music.play()  # Play the birthday song
    birthday_message()
    time.sleep(1)
    cake()
    print("\nBlowing candles...\n")
    candle_flicker()  # Candle flickering animation
    print("\nLet’s turn on the lights!\n")
    light_animation()  # Lights animation
    pygame.mixer.music.stop()

# Run the celebration
celebrate_birthday()

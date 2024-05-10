# faça um programa que toque uma musica no terminal

import os
import pygame


# os.system('celluloid ./musica.wav')

"""
pygame.init()
pygame.mixer.music.load('./musica.wav')
pygame.mixer.music.play()
pygame.event.wait()
"""

from pygame import mixer

# Starting the mixer
mixer.init()

# Loading the song
mixer.music.load("musica.wav")

# Setting the volume
mixer.music.set_volume(0.7)

# Start playing the song
mixer.music.play()

# infinite loop
while True:

    print("Press 'p' to pause, 'r' to resume")
    print("Press 'e' to exit the program")
    query = input("  ")

    if query == 'p':

        # Pausing the music
        mixer.music.pause()
    elif query == 'r':

        # Resuming the music
        mixer.music.unpause()
    elif query == 'e':

        # Stop the mixer
        mixer.music.stop()
        break

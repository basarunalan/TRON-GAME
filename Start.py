from turtle import *
from freegames import vector
from PIL import Image
import tkinter as tk
import pygame
def play_space_background_music():
    pygame.mixer.init()
    pygame.mixer.music.load("Documents/Foo Fighters - Everlong (Instrumental).mp3")  
    pygame.mixer.music.play(-1)
def play_desert_background_music():
    pygame.mixer.init()
    pygame.mixer.music.load("Documents/Desert_theme_song.mp3")  
    pygame.mixer.music.play(-1)

def play_forest_background_music():
    pygame.mixer.init()
    pygame.mixer.music.load("Documents/Hill Climb Racing - Theme Song.mp3")  
    pygame.mixer.music.play(-1)

def start_game(_map_choice):
    from Start_race import start_space_race
    from Start_race import start_desert_race
    from Start_race import start_forest_race
    if _map_choice == 1:
     play_space_background_music()
     start_space_race()
    elif _map_choice == 2:
     play_desert_background_music()
     start_desert_race()
    elif _map_choice == 3:
     play_forest_background_music()
     start_forest_race()
       

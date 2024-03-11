## Faça um programa em Python que abra e reproduza o áudio de um arquivo MP3.

import pygame ## importa audios, teclados, controles, mouses e hardwares graficos via OpenGL e Direct3D

pygame.init()
pygame.mixer.music.load('desafio21.mp3')
pygame.mixer.music.play()
pygame.event.wait()

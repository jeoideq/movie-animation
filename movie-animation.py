import pygame
pygame.init()
import time
WIDTH=800
HEIGHT=600


TITLE="STUDIO_GHIBLI"
screen=pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption(TITLE)


run= True
while run:
  mononoke=pygame.image.load("mononoke.jpg")
  mononoke=pygame.transform.scale( mononoke,(800,600))
  screen.blit(mononoke,(0,0))
  font=pygame.font.SysFont("Arial",20)
  message1=font.render("You cannot change fate. However, you can rise to meet it, if you so choose.",True, "white")
  screen.blit(message1,(30,500))
  pygame.display.update()
  time.sleep(5)
  
  spirited=pygame.image.load("spirited.jpg")
  spirited=pygame.transform.scale(spirited,(800,600))
  screen.blit(spirited,(0,0))
  font=pygame.font.SysFont("Arial",20)
  message3=font.render("Nothing that happens is ever forgotten, even if you can't remember it.", True, "white")
  screen.blit(message3,(50,510))
  pygame.display.update()
  time.sleep(5)
  
  
  totoro=pygame.image.load("totoro.jpg")
  totoro=pygame.transform.scale( totoro,(800,600))
  screen.blit(totoro,(0,0))
  font=pygame.font.SysFont("Arial",23)
  message2=font.render("Reality is for people that lack imagination.", True, "white")
  screen.blit(message2,(150,500))
  pygame.display.update()
  time.sleep(5)

  
  pygame.display.update()
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
        run = False
  pygame.display.update()
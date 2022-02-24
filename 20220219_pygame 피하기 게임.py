#pygame) 피하기 게임
import pygame as p
import random as r

p.init() #파이게임 초기화

screen = p.display.set_mode([600,1000]) #해상도 설정

p.display.set_caption("기본판")#게임창 제목

i_bg = p.image.load("bada.jpg")
i_player = p.image.load("bob.png")
i_rock = p.image.load("rock.png")

player_rect = i_player.get_rect(left = 250, top = 850)
rock_rect = i_rock.get_rect(left = 250,top = -100)

playing = True

while playing:
    for event in p.event.get(): #사용자가 뭘 눌렀는지 확인
        if event.type == p.QUIT : #파이게임 x버튼을 눌렀을 때
            p.quit() #파이게임 끄는 명령어
            quit() #shell 창 끄는 명령어
            playing = False
    if event.type == p.KEYDOWN:
        if event.key == p.K_RIGHT:
            if player_rect.left!=500:
                player_rect.left+=1
        if event.key == p.K_LEFT:
            if player_rect.left!=0:
                player_rect.left+=-1
    rock_rect.top +=1
    if rock_rect.top >= 1100:
        rock_rect.left = r.randint(0,500)
        rock_rect.top = -100
    if player_rect.colliderect(rock_rect):
        p.quit()
        quit()
    screen.fill([255,255,255])
    screen.blit(i_bg,[0,0])
    screen.blit(i_player,player_rect)
    screen.blit(i_rock,rock_rect)
    p.display.flip() #화면 업데이트 기능

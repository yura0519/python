#파이게임) 키보드 제어
import pygame as p

p.init() #초기화
size = [700,700] #[x좌표, y좌표]
sc = p.display.set_mode(size) #해상도 설정
p.display.set_caption("Beta") #게임 창 제목 설정
image1 = p.image.load("s.png")

playing = True

while playing:
    for event in p.event.get(): #사용자가 뭘 눌렀는지 확인
        if event.type == p.QUIT : #파이게임 x버튼을 눌렀을 때
            p.quit() #파이게임 끄는 명령어
            quit() #shell 창 끄는 명령어
            playing = False
        if event.type == p.KEYDOWN:#만일 키보드를 눌렀을 때
            if event.key == p.K_UP:#위쪽 방향키를 눌렀을때
                print("up on")
            if event.key == p.K_DOWN:#아래쪽 방향키를 눌렀을 때
                print("down on")
            if event.key == p.K_RIGHT:#오른쪽 방향키를 눌렀을 때
                print("right on")
            if event.key== p.K_LEFT:#왼쪽 방향키를 눌렀을 때
                print("left on")
        if event.type == p.KEYUP:#만일 키보드를 때었을 때
            if event.key == p.K_UP:
                print("up off")
            if event.key == p.K_DOWN:#아래쪽 방향키를 눌렀을 때
                print("down off")
            if event.key == p.K_RIGHT:#오른쪽 방향키를 눌렀을 때
                print("right off")
            if event.key== p.K_LEFT:#왼쪽 방향키를 눌렀을 때
                print("left off")
    sc.fill([255,255,255])
    sc.blit(image1,[300,300])
    p.display.flip() #화면 업데이트 기능

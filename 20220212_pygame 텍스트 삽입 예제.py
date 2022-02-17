#점수 텍스트 삽입
import pygame as p

p.init() #파이게임 초기화

sc = p.display.set_mode([1000,1000]) #해상도 설정

p.display.set_caption("기본판")#게임창 제목
font = p.font.SysFont('malgungothic',20)
amount = 0
playing = True

while playing:
    for event in p.event.get(): #사용자가 뭘 눌렀는지 확인
        if event.type == p.QUIT : #파이게임 x버튼을 눌렀을 때
            p.quit() #파이게임 끄는 명령어
            quit() #shell 창 끄는 명령어
            playing = False
        if event.type == p.KEYDOWN:#만일 키보드를 눌렀을 때
            if event.key == p.K_UP:#위쪽 방향키를 눌렀을때
                amount+=1
            if event.key == p.K_DOWN:#아래쪽 방향키를 눌렀을 때
                amount+=-1
            if event.key == p.K_SPACE:
                amount=0
    sc.fill([255,255,255])
    text = font.render("값 : {}".format(amount),True,[0,0,0])
    sc.blit((text),[450,450])
    p.display.flip() #화면 업데이트 기능

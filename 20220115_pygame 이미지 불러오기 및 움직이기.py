#파이게임) 이미지 불러오기 및 움직이기
import pygame as p
p.init() #초기화
size = [700,700] #[x좌표, y좌표]
sc = p.display.set_mode(size) #해상도 설정
p.display.set_caption("Beta") #게임 창 제목 설정
playing = True
#1.이미지 변수에 저장
image1 = p.image.load("s.png")
image2 = p.image.load("b.png")
image3 = p.image.load("ff.png")
image4 = p.image.load("sm.png")
x=600
y=0
b=-1
c=0
while playing:
    x+= b
    y+=c
    for event in p.event.get(): #사용자가 뭘 누르는지 감지
        if event.type == p.QUIT : # 만일 pygame x버튼을 누르면
            p.quit() #파이게임 끄는 명령어
            quit() #shell 창 끄는 명령어
            playing = False
    sc.fill([255,255,255])#게임배경화면 색 설정 (R,G,B)
    if x==0:
        b=0
        c=1
        if y==600:
            b=1
            c=0
    if x==600:
        b=0
        c=-1
        if y==0:
            b=-1
            c=0   
    sc.blit(image1,[0,0])
    sc.blit(image3,[600,600])
    sc.blit(image4,[0,600])
    sc.blit(image2,[x,y])
    p.display.flip() #화면 업데이트 명령어

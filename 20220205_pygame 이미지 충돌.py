#이미지 충돌 감지
import pygame as p

p.init() #파이게임 초기화

sc = p.display.set_mode([1000,1000]) #해상도 설정

p.display.set_caption("키보드 이미지 제어")#게임창 제목

#그림삽입
im = p.image.load("s.png")
im2 = p.image.load("ff.png")

im_rect = im.get_rect(left = 450, top =450) #left = x좌표 , top = y좌표
print(im_rect.left)
im2_rect = im2.get_rect(left = 450, top =900)
c= -1
playing = True

while playing:
    im2_rect.left+=c
    for event in p.event.get(): #사용자가 뭘 눌렀는지 확인
        if event.type == p.QUIT : #파이게임 x버튼을 눌렀을 때
            p.quit() #파이게임 끄는 명령어
            quit() #shell 창 끄는 명령어
            playing = False
    if event.type == p.KEYDOWN: #키보드를 눌렀을때
        if event.key == p.K_UP: #위쪽 방향키를 눌렀을때
            im_rect.top+=-1
        if event.key == p.K_DOWN: #아래쪽 방향키를 눌렀을때
            im_rect.top+=1
        if event.key == p.K_RIGHT: #오른쪽 방향키를 눌렀을때
            im_rect.left+=1
        if event.key == p.K_LEFT: #왼쪽 방향키를 눌렀을때
            im_rect.left+=-1
    if im2_rect.left==0:
        c=1
    if im2_rect.left==900:
        c=-1
    sc.fill([255,255,255])
    sc.blit(im,im_rect) #이미지 화면 업로드
    sc.blit(im2,im2_rect)
    #이미지 충돌 조건
    if im_rect.colliderect(im2_rect): #이미지 좌표변수.colliderect(충돌할좌표변수):
        p.quit()
        quit()
    p.display.flip() #화면 업데이트 기능

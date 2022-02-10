#369게임에서 박수친 횟수
def sol(end):
      a=0
      for x in range(1,end):
            t=x//10
            o=x%10
            if t==3 or t==6 or t==9:
                  a+=1
            if o==3 or o==6 or o==9:
                  a+=1
      print(a)
sol(40)

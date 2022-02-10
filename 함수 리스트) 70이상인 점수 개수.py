#리스트에서 점수 70점 이상 개수
a = [100,60,80,70,75,36,74,33]
def sol(l):
      b=0
      for x in range(0,len(l)):
            if l[x]>=70:
                  b+=1
      print(b)
print(a)
sol(a)

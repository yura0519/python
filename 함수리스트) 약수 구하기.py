#함수 리스트) 약수 구하기
b = int(input("숫자를 입력하세요:"))
def sol(num):
      a=[]
      for x in range(1,num+1):
            if num%x==0:
                  a.append(x)
      print(a)
sol(b)

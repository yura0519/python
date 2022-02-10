#함수)세 숫자 중 중간값 찾기
#a>b>c / a>c>b / b>a>c / b>c>a / c>a>b / c>b>a
x = int(input("첫번째 숫자를 입력하세요:"))
y =int(input("두번째 숫자를 입력하세요:"))
z =    int(input("세번째 숫자를 입력하세요:"))
def middle(a,b,c):
      if  a>b and b>c or c>b and b>a:
            print(b)
      elif a>c and c>b or b>c and c>a:
            print(c)
      elif b>a and a>c or c>a and a>b:
            print(a)
middle(x,y,z)

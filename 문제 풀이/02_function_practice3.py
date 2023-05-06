# 100 미만의 정수만 입력된다. 정수 n을 입력받아 n x n 크기의 숫자사각형을 출력하는 프로그램을 작성하시오.
#이떄 정수 n을 전달받아 숫자 정사각형을 출력하는 함수를 작성하고, 입력받은 정수 n을 함수로 전달하여 출력한다.

#입력 예
# 4

#출력 예
# 1 2 3 4 
# 5 6 7 8
# 9 10 11 12
# 13 14 15 16

def number_square(n):
    for i in range(n): # 0 1 2 3
        for j in range (1, n+1): # 1 2 3 4 
            print(n*i+j,end='')
        print()

n = int(input())
number_square(n)
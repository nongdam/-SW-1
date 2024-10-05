def add(x,y):
    return x+y

def subtract(x,y):
    return x-y

while True:
    choice = input("| 1.더하기 | 2.빼기 | 0.종료 |")
    
    if choice == 0:
        break    
    
    try:
        num1 = float(input("첫 번째 숫자: "))
        num2 = float(input("두 번째 숫자: ")) 
    except ValueError:
        print("범위를 벗어남. 다시 입력해주세요")
        continue

    if choice == 1:
        print(f"{num1} + {num2} = {add(num1, num2)}")
    
    if choice == 2:
        print(f"{num1} - {num2} = {subtract(num1, num2)}")


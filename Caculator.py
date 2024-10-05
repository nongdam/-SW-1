def add(x,y):
    return x+y

def subtract(x,y):
    return x-y

def multiply(x,y):
    return x*y

def divide(x,y):
    if y == 0:
        return "0으로 나눌 수 없습니다"
    else:
        return x/y

def crash():
    return "충돌"

while True:
    choice = input("| 1.더하기 | 2.빼기 | 3.곱하기 | 4. 나누기 | : ")
    
    try:
        num1 = float(input("첫 번째 숫자: "))
        num2 = float(input("두 번째 숫자: ")) 
        
    except ValueError:
        print("범위를 벗어남. 다시 입력해주세요")
        continue

    match choice:
        case '1':
            print(f"{num1} + {num2} = {add(num1, num2)}")
    
        case '2':
            print(f"{num1} - {num2} = {subtract(num1, num2)}")
            
        case '3':
            print(f"{num1} * {num2} = {multiply(num1, num2)}")
            
        case '4':
            print(f"{num1} / {num2} = {divide(num1, num2)}")
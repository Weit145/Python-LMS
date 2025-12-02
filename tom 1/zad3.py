import random

# 14
def zad1()->tuple:
    temp = tuple(input("Введите кортеж: "))
    return temp[1::2]

# 18
def zad2()->tuple:
    temp = tuple(input("Введите кортеж: "))
    return temp[random.randint(0,len(temp)-1)]

def main():
    print(zad1())
    print(zad2())

if __name__ == "__main__":
    main()
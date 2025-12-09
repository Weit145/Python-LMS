#6
def fibonachi(n:int, a:int =0 , b:int = 1)->int:
    if n == 1:
        return a
    elif n == 2:
        return b
    else:
        return fibonachi(n-1, b, a+b)

def zad1()->int:
    n = int(input("Введите число n: "))
    return fibonachi(n)

#10
def recueain_gcd(val1:int, val2:int, n:int= 0)->int:
    if n==0:
        n =min(val1, val2)
    if val1 % n == 0 and val2 % n == 0:
        return n
    else:
        return recueain_gcd(val1, val2, n-1)

def zad2()->int:
    val1 = int(input("Введите число val1: "))
    val2 = int(input("Введите число val2: "))
    return recueain_gcd(val1, val2)

def main():
    print(zad1())
    print(zad2())

if __name__ == "__main__":
    main()
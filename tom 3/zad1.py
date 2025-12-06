#3
def zad1()->float:
    val1 = float(input("Введите значение val1: "))
    val2 = float(input("Введите значение val2: "))
    return(val1**val2)

#14
def zad2()->float:
    n = float(input("Введите целое число n: "))
    return ((n**2+5)*16)/(25/(3*n))


def main():
    print(zad1())
    print(zad2())

if __name__ == "__main__":
    main()
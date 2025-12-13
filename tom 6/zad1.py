#4
def check_bit(func):
    def check(n):
        x = func(n)
        if (x >> 2) & 1:
            return x + 10
        else:
            return x - 5
    return check

@check_bit
def pow3(n):
    return n**3

def zad1()->int:
    n = int(input("Введите число n: "))
    return pow3(n)

#7
def celsius (func):
    def convert (n):
        x = func(n)
        return (x - 32)* 5/9
    return convert

@celsius
def temperature_fahrenheit(n):
    return n

def zad2()->int:
    fahrenheit = int(input("Введите в Фаренгейтах: "))
    return temperature_fahrenheit(fahrenheit)

def main():
    print(zad1())
    print(zad2())

if __name__ == "__main__":
    main()
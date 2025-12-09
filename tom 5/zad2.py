#4
def closure_sum(a):
    def inner(b):
        return a + b
    return inner

def zad1()->int:
    a = int(input("Введите число a: "))
    b = int (input("Введите число b: "))
    result = closure_sum(a)(b)
    return result

#7
def closure_count_str(char):
    def inner(string):
        return string.count(char)
    return inner

def zad2()->int:
    string = input("Введите строку: ")
    char = input("Введите символ: ")
    result = closure_count_str(char)(string)
    return result

def main():
    print(zad1())
    print(zad2())

if __name__ == "__main__":
    main()
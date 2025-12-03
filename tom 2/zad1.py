# 10
def zad1()->set:
    string = input("Введите строку: ")
    return set(string)

# 13
def zad2()->set:
    set1 = input("Введите множество 1: ")
    set2 = input("Введите множество 2: ")
    return set(set1)|set(set2)

# 14
def zad3()->set:
    set1 = input("Введите множество A: ")
    set2 = input("Введите множество B: ")
    return set(set1)-set(set2)

def main():
    print(zad1())
    print(zad2())
    print(zad3())

if __name__ == "__main__":
    main()
# 14
def zad1()->str:
    string = input("Введите строку: ")
    return string[::2]

# 18
def zad2()->str:
    string = input("Введите строку: ")
    return string[-5::]

def main():
    print(zad1())
    print(zad2())

if __name__ == "__main__":
    main()
# 4
def zad1()->str:
    string = input("Введите строку: ")
    return string.replace("о","*")

# 10
def zad2()->str:
    string = input("Введите строку: ")
    return string[::-1]

def main():
    print(zad1())
    print(zad2())

if __name__ == "__main__":
    main()
#3
def zad1()->bool:
    my_list = list(input("Введите my_list: "))
    if len(my_list)<5:
        return False
    if my_list[0]==my_list[-1]:
        return True
    return False

#14
def zad2()->bool:
    val1 = input("Введите значение val1: ")
    val2 = input("Введите значение val2: ")
    if val1 ==val2:
        return True
    return False


def main():
    print(zad1())
    print(zad2())

if __name__ == "__main__":
    main()
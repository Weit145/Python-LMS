#12
def is_bit_set(val1:int, val2:int)->bool:
    return (val1 & 1<<val2) != 0

def zad1()->bool:
    val1 = int(input("Введите значение val1: "))
    val2 = int(input("Введите значение val2: "))
    return is_bit_set(val1, val2)
#11
def is_anagram(string1:str, string2:str)->bool:
    clean1 = ''.join(string1.lower().split())
    clean2 = ''.join(string2.lower().split())
    if len(clean1) != len(clean2):
        return False
    return sorted(clean1) == sorted(clean2)

def zad2()->bool:
    string1 = input("Введите первую строчку: ")
    string2 = input("Введите вторую строчку: ")
    return is_anagram(string1, string2)


def main():
    print(zad1())
    print(zad2())

if __name__ == "__main__":
    main()
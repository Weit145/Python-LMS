# 6
def zad1()->dict:
    dc = eval(input("Введите словарь: "))
    dc.pop('a',None)
    return dc

# 7
def zad2()->None:
    dc = eval(input("Введите словарь: "))
    for i in range(1,11):
        if dc.get(i):
            print(dc.get(i))
    return 

# 12
def zad3()->bool:
    dc = eval(input("Введите словарь: "))
    if 15 in dc.values():
        return True
    return False

def main():
    print(zad1())
    zad2()
    print(zad3())

if __name__ == "__main__":
    main()
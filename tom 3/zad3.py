# 9
def zad1()->dict:
    string = input("Введите строчку: ")
    result = dict()
    for char in string:
        result[char] = result.get(char,0)+1
    return result

# 16
def zad2()->int:
    z = int(input("Введите целое число z: "))
    numerator = 0
    for n in range(1, z + 1):
        numerator += 16 * (n**2 + 5)
    denominator = 25 / (3 * z) 
    return numerator / denominator

def main():
    print(zad1())
    print(zad2())

if __name__ == "__main__":
    main()
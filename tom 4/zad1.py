#4
def zad1()->list:
    my_list = list(range(-43, 57,14))
    return my_list
#7
def zad2()->list:
    my_list = [1,2,3,4,9,7,4,6,22,3,84,21,45,76]
    return [x for x in my_list if x < 19]

def main():
    print(zad1())
    print(zad2())

if __name__ == "__main__":
    main()
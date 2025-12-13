import inspect

#4
def is_generator(func):
    return inspect.isgeneratorfunction(func)

def generator_func():
    yield 42

def zad1():
    return is_generator(generator_func)

#7
def letters(string):
    for char in string:
        yield char

def zad2():
    string = input("Ведите строку: ")
    for char in letters(string):
        print(char)
    return "\nEnd"

def main():
    print(zad1())
    print(zad2())

if __name__ == "__main__":
    main()
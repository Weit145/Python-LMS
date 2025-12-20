class Student:
    def __init__(self, name: str, grade: float):
        self.name = name
        self.grade = grade
    
    def __lt__(self, other):
        if self.grade == other.grade:
            return self.name < other.name
        return self.grade < other.grade
    
    def __le__(self, other):
        if self.grade == other.grade:
            return self.name <= other.name
        return self.grade <= other.grade
    
    def __eq__(self, other):
        return self.grade == other.grade and self.name == other.name
    
    def __ne__(self, other):
        return not self.__eq__(other)
    
    def __gt__(self, other):
        if self.grade == other.grade:
            return self.name > other.name
        return self.grade > other.grade
    
    def __ge__(self, other):
        if self.grade == other.grade:
            return self.name >= other.name
        return self.grade >= other.grade
    
    def __str__(self):
        return f"{self.name}: {self.grade}"
    
    def __repr__(self):
        return f"Student('{self.name}', {self.grade})"

if __name__ == "__main__":
    students = [
        Student("Анна", 4.5),
        Student("Иван", 4.8),
        Student("Мария", 4.5),
        Student("Петр", 4.2),
        Student("Ольга", 4.8),
        Student("Алексей", 4.2)
    ]
    
    print("Исходный список студентов:")
    for student in students:
        print(student)
    
    students.sort()
    
    print("\nОтсортированный список студентов:")
    for student in students:
        print(student)
    
    print("\nДемонстрация операторов сравнения:")
    s1 = Student("Анна", 4.5)
    s2 = Student("Мария", 4.5)
    s3 = Student("Иван", 4.8)
    
    print(f"s1 (Анна, 4.5) < s2 (Мария, 4.5): {s1 < s2}")
    print(f"s2 (Мария, 4.5) < s1 (Анна, 4.5): {s2 < s1}")
    print(f"s1 (Анна, 4.5) == s2 (Мария, 4.5): {s1 == s2}")
    print(f"s1 (Анна, 4.5) < s3 (Иван, 4.8): {s1 < s3}")
    print(f"s3 (Иван, 4.8) > s1 (Анна, 4.5): {s3 > s1}")
    
    print("\nОтсортированный список в обратном порядке:")
    students.sort(reverse=True)
    for student in students:
        print(student)
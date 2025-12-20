from datetime import datetime

class Email:
    def __init__(self, sender: str, subject: str, date: str, attachments: int = 0):
        
        self.sender = sender
        self.subject = subject
        self.date = datetime.strptime(date, "%Y-%m-%d %H:%M:%S")
        self.attachments = attachments
    
    def __lt__(self, other):
        return self.date < other.date
    
    def __le__(self, other):
        return self.date <= other.date
    
    def __eq__(self, other):
        return self.date == other.date
    
    def __ne__(self, other):
        return self.date != other.date
    
    def __gt__(self, other):
        return self.date > other.date
    
    def __ge__(self, other):
        return self.date >= other.date
    
    def get_attachments_count(self) -> int:
        return self.attachments
    
    def add_attachment(self):
        self.attachments += 1
    
    def remove_attachment(self):
        if self.attachments > 0:
            self.attachments -= 1
    
    def __str__(self):
        return f"{self.sender} - '{self.subject}' ({self.date.strftime('%d.%m.%Y %H:%M')})"

if __name__ == "__main__":
    email1 = Email("alice@mail.com", "Встреча", "2024-03-15 14:30:00", 2)
    email2 = Email("bob@mail.com", "Отчет", "2024-03-16 09:15:00", 1)
    email3 = Email("charlie@mail.com", "Важно", "2024-03-15 14:30:00", 3)
    email4 = Email("diana@mail.com", "Привет", "2024-03-14 18:45:00", 0)
    
    emails = [email1, email2, email3, email4]
    
    print("Исходный список писем:")
    for email in emails:
        print(f"{email} | Вложений: {email.get_attachments_count()}")
    
    emails.sort()
    
    print("\nОтсортированный список писем (по дате):")
    for email in emails:
        print(f"{email} | Вложений: {email.get_attachments_count()}")
    
    print("\nДемонстрация операторов сравнения:")
    print(f"email1 < email2 (раньше): {email1 < email2}")
    print(f"email2 > email4 (позже): {email2 > email4}")
    print(f"email1 == email3 (одновременно): {email1 == email3}")
    print(f"email1 != email2 (разное время): {email1 != email2}")
    
    print("\nРабота с вложениями:")
    print(f"Вложений в email1: {email1.get_attachments_count()}")
    email1.add_attachment()
    print(f"После добавления: {email1.get_attachments_count()}")
    
    print("\nСписок писем от новых к старым:")
    emails.sort(reverse=True)
    for email in emails:
        print(f"{email} | Вложений: {email.get_attachments_count()}")
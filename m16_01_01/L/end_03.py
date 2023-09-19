from dataclasses import dataclass


class Notification:
    def notify(self, message):
        raise NotImplementedError


@dataclass
class Contact:
    name: str
    email: str
    phone: str


class Email(Notification):
    def __init__(self, email):
        self.email = email

    def notify(self, message):
        print(f"Send {message} to email: {self.email}")


class SMS(Notification):
    def __init__(self, phone):
        self.phone = phone

    def notify(self, message):
        print(f"Send {message} sms to phone: {self.phone}")


class NotificationService:
    def __init__(self, notification: Notification):
        self.notification = notification

    def send(self, message):
        self.notification.notify(message)


if __name__ == "__main__":
    person = Contact("Dima", "dima@gmail.com", "+380663332211")
    service_SMS = NotificationService(SMS(person.phone))
    service_email = NotificationService(Email(person.email))
    service_SMS.send("Hello bro!")
    service_email.send("Hello bro!")

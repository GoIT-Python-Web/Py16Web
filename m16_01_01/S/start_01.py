class Person:
    def __init__(self, name: str, phone: str, operator_code: str):
        self.name = name
        self.phone = phone
        self.operator_code = operator_code

    def get_phone_number(self):
        return f"{self.name}: +38({self.operator_code}){self.phone}"


if __name__ == '__main__':

    person = Person("Alexander", "9995544", "050")
    print(person.get_phone_number())
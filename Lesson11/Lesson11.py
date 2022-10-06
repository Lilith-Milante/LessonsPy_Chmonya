class Person:
    def __init__(self, first_name, second_name, last_name, dict_phones: dict):
        self.FIO = [first_name, second_name,last_name]
        self.phones = dict_phones

    def get_phone(self):
        return self.phones.get('private')

    def get_name(self):
        return ''.join(self.FIO)

    def get_work_phone(self):
        return self.phones.get('work')

    def get_sms_text(self):
        return f'Уважаемый {self.FIO[0]} {self.FIO[1]}! Примите!'

class Company:
    def __init__(self, company_name, type_company, phone_number: dict, *args: Person):
        self.worker_list = list(args)
        self.company_name = company_name
        self.type = type_company
        self.phones_company = phone_number

    def get_name(self):
        return self.company_name

    def get_phone(self):
        if not self.phones_company.get('contact') == None:
            return self.phones_company.get('contact')
        else:
            for worker in self.worker_list:
                if not worker.get_work_phone() == None:
                    return worker.get_work_phone()
            return None

    def get_sms_text(self):
        return f'Уважемый {self.company_name}!Примите {self.type}'

def send_sms(*args):
    for el in args:
        if not el.get_phone() == None:
            print(f'Sms send to {el.get_phone()} with {el.get_sms_text()}')
        else:
            print(f'Sms did not send to {el.get_name()}')

person1 = Person("Ivan", "Ivanovich", "Ivanov", {'private': 7543})
person2 = Person("Alex", "Ivanovich", "Borisov", {'private': 73543, 'work': 15678})
company1 = Company("Ozon", 'Marketplace', {'contact':6789}, person1,person2)
company2 = Company("Azon", 'Market', {'private':6789}, person1)

send_sms(person1, person2, company1, company2)
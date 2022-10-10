import numpy

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

person1 = Person('Ivan', 'Ivanovich', 'Ivanov', {'private': 123, 'work': 456})
person2 = Person('Ivan', 'Petrovich', 'Petrov', {'private': 789})
person3 = Person('Ivan', 'Petrovich', 'Sidorov', {'work': 789})
person4 = Person('John', 'Unknown', 'Doe', {})
company1 = Company('Bell', '000', {'Contact': 111}, person3, person4)
company2 = Company('Cell', 'A0', {'non_contact': 222}, person2, person3)
company3 = Company('Dell', 'Ltd', {'non_contact': 333}, person2, person4)

send_sms(person1, person2, person3, company1, company2, company3)

# task 2

class MinStat:

    def __init__(self):
        self.list = []

    def add_number(self, num):
        self.list.append(num)

    def result(self):
        return min(self.list)

class MaxStat:

    def __init__(self):
        self.list = []

    def add_number(self, num):
        self.list.append(num)

    def result(self):
        return max(self.list)

class AverageStat:

    def __init__(self):
        self.list = []

    def add_number(self, num):
        self.list.append(num)

    def result(self):
        return numpy.average(self.list)

values = [1, 2, 3, 4, 5]

mins = MinStat()
maxs = MaxStat()
average = AverageStat()
for i in values:
    mins.add_number(i)
    maxs.add_number(i)
    average.add_number(i)

#print(mins.result(), maxs.result(), '{}'.format(numpy.average.result()))
print(mins.result())
print(maxs.result())
print(average.result())

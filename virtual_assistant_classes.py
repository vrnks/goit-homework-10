from collections import UserDict

class AddressBook(UserDict): 
    def add_record(self, record): # метод add_record додає Record у self.data
        self.data[record.name.value] = record
# додавання/видалення/редагування необов'язкових полів та зберігання обов'язкового поля Name
class Record(): 
    def __init__(self, name, phone=None):
        self.name = name
        self.phones = [phone] if phone else []
    def add_phone(self, phone):
        self.phones.append(phone)
    def delete_phone(self, phone):
        self.phones.remove(phone)
    def modify_phone(self, phone):
        self.phones = phone
        

# логіка, загальна для всіх полів
class Field():
    def __init__(self, value):
        self.value = value
    
# обов'язкове поле з ім'ям
class Name(Field):
    pass

# необов'язкове поле з телефоном
class Phone(Field):
    pass


if __name__ == '__main__':
    name = Name('Bill')
    phone = Phone('1234567890')
    rec = Record(name, phone)
    ab = AddressBook()
    ab.add_record(rec)
    
    assert isinstance(ab['Bill'], Record)
    assert isinstance(ab['Bill'].name, Name)
    assert isinstance(ab['Bill'].phones, list)
    assert isinstance(ab['Bill'].phones[0], Phone)
    assert ab['Bill'].phones[0].value == '1234567890'
    
    print('All Ok)')
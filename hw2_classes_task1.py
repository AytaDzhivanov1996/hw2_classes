class Person:
    def __init__(self, fio, age, passport, weight):
        if self.verify_fio(fio) and self.verify_age(age) and self.verify_ps(passport) and self.verify_weight(weight):
            self.__fio = fio
            self.__age = age
            self.__passport = passport
            self.__weight = weight

    @property
    def fio(self):
        return self.__fio

    @fio.setter
    def fio(self, fio):
        if self.verify_fio(fio):
            self.__fio = fio

    @classmethod
    def verify_fio(cls, string):
        if type(string) is not str:
            raise TypeError('ФИО должно быть строкой')
        elif string.count(' ') != 2:
            raise TypeError('Неверный формат записи ФИО')
        elif [True for i in string.split(' ') if len(i) < 1]:
            raise TypeError('В ФИО должен быть хотя бы один символ')
        elif not string.replace(' ', '').isalpha():
            raise TypeError('В ФИО можно использовать только буквенные символы')
        else:
            return True

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, age):
        if self.verify_age(age):
            self.__age = age

    @classmethod
    def verify_age(cls, num):
        if type(num) is not int:
            raise TypeError('Возраст должен быть целым числом от 14 до 150')
        elif num < 14 or num > 150:
            raise TypeError('Возраст должен быть целым числом от 14 до 150')
        else:
            return True

    @property
    def passport(self):
        return self.__passport

    @passport.setter
    def passport(self, passport):
        if self.verify_ps(passport):
            self.__passport = passport

    @classmethod
    def verify_ps(cls, ps):
        if type(ps) is not str:
            raise TypeError('Паспорт должен быть строкой')
        elif ps.count(' ') != 1 or len(ps.split(' ')[0]) != 4 or len(ps.split(' ')[1]) != 6:
            raise TypeError('Неверный формат паспорта')
        elif not ps.replace(' ', '').isdigit():
            raise TypeError('Серия и номер паспорта должны содержать только числа')
        else:
            return True

    @property
    def weight(self):
        return self.__weight

    @weight.setter
    def weight(self, weight):
        if self.verify_weight(weight):
            self.__weight = weight

    @classmethod
    def verify_weight(cls, weight):
        if type(weight) is not float or weight < 25:
            raise TypeError('Вес должен быть вещественным числом от 25 и выше')
        else:
            return True


u = Person('Иванов Иван Иванович', 50, '0000 000000', 85.0)

import shelve


class PhoneBook:
    def __init__(self, name_book, dic_rec={}):
        self.name_book = name_book
        self.dic_rec = dic_rec

    def load_book(self):
        db = shelve.open(self.name_book)
        self.dic_rec = dict(db.items())
        db.close()

    def save_book(self):
        db = shelve.open(self.name_book)
        for (key, record) in self.dic_rec.items():
            db[key] = record
        db.close()

    def rec_creation(self):
        print(self.name_book)
        label = input('название записи: ')
        phone = input('телефон : ')
        print('ФИО,коммент. - Если нет, просто нажимайте Enter')
        name = input('ФИО: ')
        comment = input('Комментарий: ')
        if len(self.dic_rec) > 0:
            t_list = sorted(self.dic_rec.items(), key=lambda item: item[0])
            key_rec = str(int(t_list[-1][0]) + 1)
        else:
            key_rec = "1"
        record = PhoneRec(key_rec, label, phone, name, comment)
        self.dic_rec[key_rec] = record

    def read_phone_rec(self):
        for key in t1.dic_rec.keys():
            print("{:<3}- {:<25}- {:<20}- {:<30}- {:<30}".format(key, t1.dic_rec[key].label,
                                                                 t1.dic_rec[key].phone,
                                                                 t1.dic_rec[key].familyName,
                                                                 t1.dic_rec[key].comment))


class PhoneRec:
    def __init__(self, key_rec, label, phone, name, comment):
        self.keyRec = key_rec
        self.label = label
        self.phone = phone
        self.familyName = name
        self.comment = comment


if __name__ == '__main__':
    t1 = PhoneBook("Телефоны")
    t1.load_book()
    t1.rec_creation()
    t1.read_phone_rec()

    t1.save_book()

    input('ОКОНЧАНИЕ РАБОТЫ')

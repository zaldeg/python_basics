class Date:
    def __init__(self, date):
        Date.date = date

    @classmethod
    def chislo(cls):
        Date.date = list(list(map(int, Date.date.split("-"))))

    @staticmethod
    def date_validate():
        if 0 < Date.date[0] < 32 and 0 < Date.date[1] < 13:
            print("Date is validated!")
        else:
            print("Date is incorrect!")


a = Date("13-12-2019")
Date.chislo()
print(Date.date)
Date.date_validate()

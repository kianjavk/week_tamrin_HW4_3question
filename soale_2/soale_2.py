import time


class BirthDay:
    def __init__(self, day, month, year, time_of_born):

        self.day = day
        self.month = month
        self.year = year
        self.time_of_born = time_of_born

    def __str__(self):
        return f'{self.day}/{self.month}/{self.year}'

    def age(self):
        time_now = time.localtime()
        return (f'Age now :{time_now.tm_year - self.year},'
                f' Hour now :{time_now.tm_hour}')

    def hours(self):
        hours_now = time.localtime()
        hours=(hours_now.tm_mon - self.month) * 30 * 24
        return f'Hour now :{hours}'




    def time_month(self):
        month_time = time.localtime()

        if self.month > month_time.tm_mon:
            return f'A few months before the birthday :{self.month - month_time.tm_mon} month'

        else:
            return f'A few months before the birthday :{(self.month + 12) - month_time.tm_mon} month'

    def time_day(self):
        days_now = time.localtime()
        day = (30 * (self.month - 1)) + self.day
        if day > days_now.tm_yday:
            return f'A day before the birthday :{day - days_now.tm_yday} days '
        else:
            return f'A day before the birthday :{(day + 365) - days_now.tm_yday} days'





def main():
    while True:
        try:
            the_person = BirthDay(int(input('day:')), int(input('month:')), int(input('year:')),
                                  int(input('time of born:')))
            print(f'======>> {the_person}')
            print('')
            print(the_person.age())
            print(the_person.hours())
            print('')
            print(the_person.time_month())
            print(the_person.time_day())
            print('')



        except ValueError:
            print("thats not an integer number")
            continue


main()

if __name__ == '__main__':
    main()

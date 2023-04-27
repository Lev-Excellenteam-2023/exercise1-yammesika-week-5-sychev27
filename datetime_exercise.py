import datetime


def get_date():
    flag = True
    while flag:
        try:
            year = int(input('Enter a year '))
            month = int(input('Enter a month '))
            day = int(input('Enter a day '))
            date1 = datetime.date(year, month, day)
            flag = False
        except:
            print("Incorrect date")

    return date1


def main():
    today_date = datetime.date.today()

    flag = True
    while flag:
        input_date = get_date()
        if today_date > input_date:
            print("Please enter a future date")
        else:
            flag = False

    delta = input_date - today_date

    print("Difference is " + str(delta.days) + " days")


if __name__ == "__main__":
     main()
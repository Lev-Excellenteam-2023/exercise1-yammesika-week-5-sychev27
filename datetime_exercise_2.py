import datetime_exercise
import radar


def get_two_dates():
    flag = True
    while flag:
        print("Enter a first date")
        date_1 = datetime_exercise.get_date()
        print("Enter a second date that is later than the first")
        date_2 = datetime_exercise.get_date()

        if date_1 > date_2:
            print("First date should be earlier than the second date")
        else:
            flag = False

    return date_1, date_2


def main():
    day_name = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
    date_1, date_2 = get_two_dates()

    random_date = radar.random_date(date_1, date_2)
    day = random_date.weekday()

    print("The random date is: " + str(random_date))
    print("The day of weak is: " + day_name[day])

    if day_name[day] == 'Monday':
        print("אין לי ויניגרט")


if __name__ == "__main__":
     main()
from ppDecorators.GenericValidations import not_empty
from ppEntities.request import PicoPlacaRequest
import datetime as dt

DATE_FORMAT = '%d-%m-%Y'
HOUR_FORMAT = '%H:%M'
DAYS_RESTRICTION = {
    0: [1, 2],
    1: [3, 4],
    2: [5, 6],
    3: [7, 8],
    4: [9, 0]
}
HOURS_RESTRICTION = ['07:00-09:30', '16:00-19:30']


def check_date():
    while True:
        date = input('1) Type The date you need to use your car (day-month-year):\n')
        try:
            date_to_eval = dt.datetime.strptime(date, DATE_FORMAT).date()
            return date_to_eval
        except Exception:
            print('Error: This is not a correct date')


def check_license_plate():
    while True:
        license_plate = input('1) Type your licence plate number (abc-1234):\n')
        lp = str(license_plate).split('-')
        if len(lp) != 2 or not(lp[0].isalpha()) or not(lp[1].isnumeric()):
            print('Error: Incorrect license plate')
        elif len(lp[0]) > 3 or len(lp[1]) > 4:
            print('Error: Incorrect license plate')
        else:
            return license_plate


def check_hour():
    while True:
        hour = input('1) Type the hour for the day entered 24h(hour:minute):\n')
        hr = str(hour).split(':')
        if len(hr) != 2:
            print('Error: Incorrect hour')
        elif 0 > len(hr[0]) < 2 or 0 > len(hr[1]) > 2:
            print('Error: Incorrect hour')
        elif not (hr[0].isnumeric() and hr[1].isnumeric()):
            print('Error: Incorrect hour')
        else:
            return hour


@not_empty
def check_hours_restriction(hour):
    hour_to_eval = dt.datetime.strptime(hour, HOUR_FORMAT)

    for h_rest in HOURS_RESTRICTION:
        hours_restriction = h_rest.split('-')
        h_begin = dt.datetime.strptime(hours_restriction[0], HOUR_FORMAT)
        h_end = dt.datetime.strptime(hours_restriction[1], HOUR_FORMAT)
        if h_begin <= hour_to_eval <= h_end:
            return True
    return False


def check_days_restriction(date, license_plate):
    day = date.weekday()
    if DAYS_RESTRICTION.get(day):
        return int(license_plate[-1]) in DAYS_RESTRICTION.get(day)
    else:
        return False


def check_pico_placa(request):
    if check_days_restriction(request.date, request.license_plate) and check_hours_restriction(request.hour):
        print('[X] You can\'t drive at this date and hour')
    else:
        print('You can drive at this date and hour')


def print_initial_messages():
    print('*' * 60)
    print('*' * 15 + 'Welcome to pico-placa predictor' + '*' * 15)
    print('*' * 60 + '\n' + '-' * 60)
    print('Now we will make a verification of your license plate number \n'
          'to check if there is availability to run on the day you specify')
    print('-' * 60)
    print('Please enter the next information:')


if __name__ == "__main__":
    print_initial_messages()
    again = True
    while again:
        request = PicoPlacaRequest(
            check_license_plate(),
            check_date(),
            check_hour()
        )
        check_pico_placa(request)
        again_str = input('Type \'a\' for check again or any for exit:')
        if again_str == 'a':
            again = False



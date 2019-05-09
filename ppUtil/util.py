from ppDecorators.GenericValidations import not_empty
import datetime as dt

DATE_FORMAT = '%d-%m-%Y'


@not_empty
def check_date(date):
    try:
        date_to_eval = dt.datetime.strptime(date, DATE_FORMAT).date()
        if date_to_eval >= dt.datetime.now().date():
            print('Error: You can only enter future dates')
    except Exception:
        print('Error: This is not a correct date')


@not_empty
def check_license_plate(license_plate):
    lp = str(license_plate).split('-')
    if len(lp) != 2 or not(lp[0].isalpha()) or not(lp[1].isnumeric()):
        print('Error: Incorrect license plate')


@not_empty
def check_hour(hour):
    hr = str(hour).split(':')
    if len(hr) != 2:
        print('Error: Incorrect license plate')
    if not (hr[0].isnumeric() and hr[1].isnumeric()):
        print('Error: Incorrect license plate')


def check_input_data(license_plate, date, hour):
    check_date(date)
    check_hour(hour)
    check_license_plate(license_plate)


def check_pico_placa(license_plate, date, hour):
    date_to_eval = dt.datetime.strptime(date, DATE_FORMAT).date()
    if (str(license_plate)[-1]) :
        print(license_plate)



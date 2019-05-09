from ppUtil import util


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
    license_plate = input('1) Type your licence plate number (abc-1234):\n')
    date = input('1) Type The date you need to use your car (day-month-year):\n')
    hour = input('1) Type the hour for the day entered (hour:minute):\n')
    util.check_input_data(license_plate, date, hour)
    util.check_pico_placa(license_plate, date, hour)



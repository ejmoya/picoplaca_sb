import app
import unittest
import datetime as dt


class TestApp(unittest.TestCase):
    def test_check_hours_restriction(self):
        """
        Test that it can check the hour restrictions
        """
        result1 = app.check_hours_restriction('08:25')
        result2 = app.check_hours_restriction('18:30')
        result3 = app.check_hours_restriction('09:35')
        self.assertEqual(result1, True)
        self.assertEqual(result2, True)
        self.assertEqual(result3, False)

    def test_check_days_restriction(self):
        """
        Test that it check correct days configuration
        """
        license_plate = 'abc-1235'
        data1 = dt.datetime.strptime('08-05-2019', app.DATE_FORMAT).date()
        result1 = app.check_days_restriction(data1, license_plate)
        data2 = dt.datetime.strptime('05-05-2019', app.DATE_FORMAT).date()
        result2 = app.check_days_restriction(data2, license_plate)
        self.assertEqual(result1, True)
        self.assertEqual(result2, False)

    def test_check_date(self):
        """
        Test that it convert the user input to date
        """
        result = app.check_date()
        self.assertIsNotNone(result)

    def test_check_hour(self):
        """
        Test that it return a correct hour
        """
        result = app.check_hour()
        self.assertIsNotNone(result)
        self.assertLess(len(result), 6)

    def test_check_license_plate(self):
        """
        Test that it return a valid license plate
        """
        result = app.check_license_plate()
        self.assertLess(len(result), 9)


if __name__ == '__main__':
    unittest.main()

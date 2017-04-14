import unittest
import datetime
from pycu import Calendar


class TestCase(unittest.TestCase):

    def test_format(self):
        cal = Calendar()
        cal.set_timestamp(datetime.datetime(2017, 1, 1).timestamp())
        self.assertEqual(cal.format('y-MM-dd HH:mm:ss'), '2017-01-01 00:00:00')

    def test_strftime(self):
        selected_date = datetime.datetime(2017, 1, 1)
        cal = Calendar()
        cal.set_timestamp(selected_date.timestamp())

        self.assertEqual(cal.strftime('%Y-%m-%d %H:%M:%S'), selected_date.strftime('%Y-%m-%d %H:%M:%S'))

    def test_datetime(self):
        selected_date = datetime.datetime(2017, 1, 1)
        cal = Calendar()
        cal.set_timestamp(selected_date.timestamp())

        self.assertEqual(cal.get_datetime(), selected_date)
        self.assertEqual(type(cal.get_datetime()), type(selected_date))

    def test_convert_calendar(self):
        # Gregorian To Persian
        cal_gregorian = Calendar(calendar='gregorian')
        cal_gregorian.set_date(2017, 1, 1)

        cal_persian = Calendar(calendar='persian')
        cal_persian.set_timestamp(cal_gregorian.get_timestamp())

        self.assertEqual(cal_persian.get_datetime(), cal_gregorian.get_datetime())

        self.assertEqual(cal_persian.strftime('%Y-%m-%d %H:%M:%S'), '1395-10-12 00:00:00')


if __name__ == '__main__':
    unittest.main()

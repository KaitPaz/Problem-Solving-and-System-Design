# To run these tests:
# python -m unittest test_date_validator.TestValidateDate
import unittest
from date_validator import validate_date

class TestValidateDate(unittest.TestCase):

    def test_valid_date(self):
        self.assertTrue(validate_date("2023-10-27"))

    def test_incorrect_delimiter_forward_slash(self):
        self.assertFalse(validate_date("2023/10/27"))

    def test_incorrect_delimiter_backward_slash(self):
        self.assertFalse(validate_date(r"2023\10\27"))

    def test_incorrect_delimiter_period(self):
        self.assertFalse(validate_date("2023.10.27"))

    def test_short_month_april(self):
        self.assertFalse(validate_date("2023-04-31"))

    def test_short_month_june(self):
        self.assertFalse(validate_date("2023-06-31"))

    def test_short_month_september(self):
        self.assertFalse(validate_date("2023-09-31"))

    def test_short_month_november(self):
        self.assertFalse(validate_date("2023-11-31"))

    def test_30_day_months_valid_30th(self):
        self.assertTrue(validate_date("2023-04-30"))
        self.assertTrue(validate_date("2023-06-30"))
        self.assertTrue(validate_date("2023-09-30"))
        self.assertTrue(validate_date("2023-11-30"))

    def test_31_day_months_valid(self):
        self.assertTrue(validate_date("2023-01-31"))
        self.assertTrue(validate_date("2023-03-31"))
        self.assertTrue(validate_date("2023-05-31"))
        self.assertTrue(validate_date("2023-07-31"))
        self.assertTrue(validate_date("2023-08-31"))
        self.assertTrue(validate_date("2023-10-31"))
        self.assertTrue(validate_date("2023-12-31"))

    def test_feb_non_leap_year(self):
        self.assertTrue(validate_date("2019-02-28"))
        self.assertFalse(validate_date("2019-02-29"))
        self.assertFalse(validate_date("2019-02-30"))
        self.assertFalse(validate_date("2019-02-31"))

    def test_feb_leap_year(self):
        self.assertTrue(validate_date("2024-02-29"))
        self.assertTrue(validate_date("2000-02-29"))

    def test_feb_leap_year_invalid(self):
        self.assertFalse(validate_date("2020-02-30"))
        self.assertFalse(validate_date("2020-02-31"))

    def test_february_century_non_leap_year(self):
        self.assertFalse(validate_date("1900-02-29"))
    
    def test_invalid_month_high(self):
        self.assertFalse(validate_date("2023-13-31"))

    def test_invalid_month_low(self):
        self.assertFalse(validate_date("2023-00-27"))

    def test_invalid_year_high(self):
        self.assertFalse(validate_date("10000-10-31"))

    def test_invalid_year_low(self):
        self.assertFalse(validate_date("0000-10-31"))

    def test_invalid_day_high(self):
        self.assertFalse(validate_date("2023-10-32"))

    def test_invalid_day_low(self):
        self.assertFalse(validate_date("2023-10-00"))
    
    def test_invalid_negative_day(self):
        self.assertFalse(validate_date("2023-10--2"))

    def test_invalid_negative_month(self):
       self.assertFalse(validate_date("2023--3-31"))

    def test_invalid_unumerical_month_Ja(self):
        self.assertFalse(validate_date("2023-Ja-27"))

    def test_invalid_unumerical_month_Fe(self):
        self.assertFalse(validate_date("2023-Fe-27"))

    def test_invalid_unumerical_month_Mr(self):
        self.assertFalse(validate_date("2023-Ma-27"))

    def test_invalid_unumerical_month_Ap(self):
        self.assertFalse(validate_date("2023-Ap-27"))

    def test_invalid_unumerical_month_My(self):
        self.assertFalse(validate_date("2023-My-27"))

    def test_invalid_unumerical_month_Jn(self):
        self.assertFalse(validate_date("2023-Jn-27"))

    def test_invalid_unumerical_month_Jl(self):
        self.assertFalse(validate_date("2023-Jl-27"))

    def test_invalid_unumerical_month_Au(self):
        self.assertFalse(validate_date("2023-Au-27"))

    def test_invalid_unumerical_month_Se(self):
        self.assertFalse(validate_date("2023-Se-27"))

    def test_invalid_unumerical_month_Oc(self):
        self.assertFalse(validate_date("2023-Oc-27"))

    def test_invalid_unumerical_month_No(self):
        self.assertFalse(validate_date("2023-No-27"))

    def test_invalid_unumerical_month_De(self):
        self.assertFalse(validate_date("2023-De-27"))

    def test_gregorian_calendar_anomaly_invalid(self):
        self.assertFalse(validate_date("1582-10-05"))
        self.assertFalse(validate_date("1582-10-10"))
        self.assertFalse(validate_date("1582-10-14"))

    def test_gregorian_calendar_boundary_valid(self):
        self.assertTrue(validate_date("1582-10-04"))   # last valid Julian date
        self.assertTrue(validate_date("1582-10-15"))    # first gregorian date

    def test_whitespace_invalid(self):
        self.assertFalse(validate_date(" 2023-10-27"))
        self.assertFalse(validate_date("2023-10-27 "))
        self.assertFalse(validate_date("2023 -10-27"))

    

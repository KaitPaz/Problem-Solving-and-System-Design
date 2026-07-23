import re

"""
Observations:
  - Cases the Program cannot handle
        - Months with 30 days (April, June, September, November) are counted as valid on the 31st. Need to fix
        - February in a leap year needs 29 days. Need LLM to check for leap year
        - February in a non-leap year only goes to 28 days, right now 29, 30, and 31 are valid. Need to fix
        - Historical anomaly: 10 days (October 5th to October 14th) were removed in 1582 to adopt the gregorian system.
            These are invalid dates. Need to fix
        - LLM made suggestion to handle invalid whitespace, need to fix
  - Cases the Program CAN handle now, but may not in the future when others edit code 
         - The only delimiter the pattern accepts is '-' (cannot accept '/', '.', '\', etc )
         - If the month is too high or low (less than 1 or greater than 12)
            - Negative months too
         - If the day is too high or low (less than 1 or greater than 31)
            - Negative 
         - If the year is too high or low (less than 1 or greater than 9999)
         - If the month is used with its abbreviation rather than its numberical representation

         - 
    

"""

def validate_date(date_string):
    """
    Validates a date string in YYYY-MM-DD format.

    Args:
      date_string: The date string to validate.

    Returns:
      True if the date string is valid according to the basic format, False otherwise.
    """
    pattern = r"^\d{4}-\d{2}-\d{2}$"  # Matches YYYY-MM-DD
    match = re.match(pattern, date_string)

    if not match:
        return False

    year, month, day = map(int, date_string.split('-'))

    if not (1 <= year <= 9999):  # Basic year check
        return False
    if not (1 <= month <= 12):  # Basic month check
        return False
    if not (1 <= day <= 31): # Basic day check
        return False

    # Gregorian calendar adoption anomaly (October 5-14, 1582 do no exist)
    if year == 1582 and month == 10 and 5 <= day <= 14:
        return False

    # Leap year calculation
    def is_leap_year(y: int) -> bool:
        return y % 400 == 0 or (y % 4 == 0 and y % 100 != 0)

    # Different size months handling 
    if month == 2:
        max_day = 29 if is_leap_year(year) else 28
    elif month in {4, 6, 9, 11}:
        max_day = 30
    else:
        max_day = 31

    if day > max_day:
        return False

    return True

from xmlrpc.client import Boolean


def date(day: int, month: int, year: int) -> Boolean:
    """Check the date.

    Args:
        day(int): day of the date
        month(int): month of the date
        year(int): year of the date

    Returns:
        Boolean: if the date exists or not

    """
    if day < 1 or month < 1 or month > 12:
        return False
    months_thirtyone = [1, 3, 5, 7, 8, 10, 12]
    months_thirty = [4, 6, 9, 11]
    if month in months_thirtyone and day > 31 or month in months_thirty and day > 30:
        return False
    elif month == 2:
        if year % 4 == 0 or (year % 100 == 0 and year % 400 == 0):
            if day > 29:
                return False
        elif day > 28:
            return False
    else:
        return True

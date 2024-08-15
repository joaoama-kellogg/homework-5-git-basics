def is_leap_year(integer):
    if integer % 4 == 0 and integer % 100 != 0:
        return True
    elif integer % 100 == 0 and integer % 400 == 0:
        return True
    else:
        return False
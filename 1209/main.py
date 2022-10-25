def func(string: str) -> int:
    """Find the percent of capital letters in the string.

    Args:
        string(str): a string of letters

    Returns:
        int: the percent of capital letters in the string
    """
    sub_arr = string.split()
    # в строке 4 подстроки, из них 3,и 1м =>  len(sub) - up
    upper = 0

    for sub in sub_arr:

        up_simbol = 0
        low_simbol = 0
        for sym in sub:               # буквы
            if sym.isupper() is True:
                up_simbol += 1
            if sym.islower() is True:
                low_simbol += 1

        if up_simbol > low_simbol:    # больше больших
            upper += 1

    return int(upper / len(sub_arr) * 100)


func('NDp Lka nuR vtE')

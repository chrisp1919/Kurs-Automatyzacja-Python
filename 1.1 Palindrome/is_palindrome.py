def is_palindrome(data):

    if not isinstance(data, (str, int, float)):
        raise ValueError("Date is incorrect, you can use only str, int or float")

    data = str(data).replace(' ', '').lower()

    for sign in ',.;!?:':
        data = data.replace(sign, '')

    if data == ''.join(reversed(data)):
        return True
    else:
        return False

test_cases = {
    "": True,
    "R": True,
    "Ada": True,
    12321: True,
    "Kajak.": True,
    1234.4321: True,
    "Anna!?": True,
    "Anxsna": False,
    (1,2,3,4): ValueError,
    tuple({"key": "value"}.items()): ValueError
}

for key, value in test_cases.items():
    try:
        result = is_palindrome(key)
        assert result == value, "For {} should be {} but is {}".format(key, value, result)
        print("Test is correct for {} is {}".format(key, result))
    except ValueError as e:
        # assert isinstance(value, type) and issubclass(value, Exception), "Test nie powiódł się dla {}. Oczekiwano wyjątku {}, otrzymano {}.".format(key,value,e)
        print("Test is correct for {} and have result: {}".format(key, e))
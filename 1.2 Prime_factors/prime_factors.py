def test_prime_factors():
    test_cases = {
        -10: [],    #przypadek szczególny, ujemna
    }

    for number, tab in test_cases.items():
        tab_prime_factors = prime_factors(number)
        assert tab_prime_factors == tab, "For {} should be {} but is {}".format(number, tab, tab_prime_factors)
        print("Test is correct, for {} is {}".format(number, tab_prime_factors))


def prime_factors(number):
    pass


try:
    test_prime_factors()
except AssertionError as e:
    print(e)



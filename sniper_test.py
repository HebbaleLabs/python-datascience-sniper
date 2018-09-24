import sniper


def test_sniper():
    """

    :return:
    """
    my_counter = 0

    _report = sniper.solve((0, 0), (2, 2))
    my_counter += _report["result"]

    _report = sniper.solve((0, 0), (3, 2))
    my_counter += _report["result"]

    _report = sniper.solve((0, 0), (1, 0))
    my_counter += _report["result"]

    _report = sniper.solve((1, 1), (4, 3))
    my_counter += _report["result"]

    assert(my_counter == 10)

    my_num_1 = (1, 1)
    counter = 1
    my_counter = 0

    while counter <= 10:
        my_num_2 = (counter, counter)

        _report = sniper.solve(my_num_1, my_num_2)
        my_counter += _report["result"]
        counter += 1

    assert(my_counter == 72)


if __name__ == "__main__":
    test_sniper()

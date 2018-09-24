

def __report(code, message, result):
    """

    :param code:
    :param message:
    :param result:
    :return:
    """
    return dict(code=code, message=message, result=result)


def solve(origin, dest):
    """

    :param origin:
    :param dest:
    :return:
    """
    return __report(0, "Total number of blocks : ", "Solution missing")


if __name__ == "__main__":

    _report = solve((1, 1), (4, 3))
    print(_report["message"] + " " + str(_report["result"]))

    my_num_1 = (1, 1)
    counter = 1
    my_counter = 0

    while counter <= 10:
        my_num_2 = (counter, counter)

        print(my_num_1)
        print(my_num_2)

        _report = solve(my_num_1, my_num_2)
        my_counter += _report["result"]

        print(_report["result"])

        counter += 1

    print(str(my_counter))



lucas = [2, 1]

def find_nth_lucas(nth):
    """Find the nth Lucas number brute force integer math
       guaranteed accurate, checked against Wolfram Alpha
    """
    if len(lucas) > nth:
        return lucas[nth]
    else:
        # need to extend the lucas list
        last = len(lucas)
        while last <= nth:
            lucas.append(lucas[last - 2] + lucas[last - 1])
            last += 1
        return lucas[nth]


def nth_lucas_phi(nth):
    """Find the nth lucas number using golden ratio formula
       not accurate for large inputs due to floating point precision
       could fix/improve using mpmath (mpmath.org) but not worth the effort
    """
    golden = (1 + 5 ** 0.5) / 2
    return int(pow(golden, nth))


def user_loop():
    while True:
        print("Which lucas number do you want? (or Q to quit)")
        try:
            nth = int(input())
        except ValueError:
            print("GoodBye!")
            break
        if nth < 0:
            print("Negative not allowed, try again")
            continue
        print("The {}th lucas number is: {}".format(nth, find_nth_lucas(nth)))


if __name__ == '__main__':
    user_loop()

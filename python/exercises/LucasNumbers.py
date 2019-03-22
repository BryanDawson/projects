
LUCAS = [2, 1]


def find_nth_lucas(nth):
    if len(LUCAS) > nth:
        return LUCAS[nth]
    else:
        # need to extend the LUCAS list
        last = len(LUCAS)
        while last <= nth:
            LUCAS.append(LUCAS[last - 2] + LUCAS[last - 1])
            last += 1
        return LUCAS[nth]


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

def calculatesum(*args):
    summed = 0
    for arg in args:
        try:
            summed += int(arg)
        except ValueError:
            print("Virheellinen syöte")
    return summed


def multiplyvalues(*args):
    summed = 1
    for arg in args:
        try:
            summed *= int(arg)
        except ValueError:
            print("Virheellinen syöte")
    return summed

def percents(x, y):
    one_percent = x / 100
    result = y / one_percent
    return result

def print_percents(x, y):
    print(str(y) + " is " + str(percents(x, y)) + "% of" + str(x))


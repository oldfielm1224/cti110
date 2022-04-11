def laps_to_miles(miles):
    laps = miles * 0.25
    return laps

if __name__ == '__main__':
    miles = float(input())
    your_value = laps_to_miles(miles)
    print('{:.2f}' .format(your_value))
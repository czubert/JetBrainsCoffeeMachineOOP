def fahrenheit_to_celsius(temps_f):
    temps_c = (temps_f - 32) * 5 / 9
    return round(temps_c, 2)


def celsius_to_fahrenheit(temps_c):
    temps_f = temps_c * 9 / 5 + 32
    return round(temps_f, 2)


def main():
    """Entry point of the program."""
    temperature, unit = input().split()  # read the input
    temperature = float(temperature)
    if unit == 'F':
        conv_temp = fahrenheit_to_celsius(temperature)
        conv_unit = "C"
    else:
        conv_temp = celsius_to_fahrenheit(temperature)
        conv_unit = "F"
    print(conv_temp, conv_unit)

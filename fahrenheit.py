#!/usr/bin/env python3

# Created by: Michael Clermont
# Created on: Mar 2022
# This program prints numbers in columns of 5


def fahrenheit():
    # this function calculates the fahrenheit from celsius

    # input
    celsius_string = input("Enter a temperature(°C): ")

    # process & output
    try:
        celsius_float = float(celsius_string)
        fahrenheit_float = (celsius_float * 1.8) + 32
        print("")
        print("{0}°C is equal to {1}°F".format(celsius_float, fahrenheit_float))
    except Exception:
        print("\nThat is not a decimal number.")
    finally:
        print("\nDone.")


def main():
    # this function just calls other functions

    # call functions
    fahrenheit()


if __name__ == "__main__":
    main()

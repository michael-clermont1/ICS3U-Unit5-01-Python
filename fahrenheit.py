#!/usr/bin/env python3

# Created by: Michael Clermont
# Created on: Mar 2022
# This program prints numbers in columns of 5


def fahrenheit():
    # this function calculates the fahrenheit from celsius

    # input
    celsius = float(input("Enter a temperature(°C): "))

    # process
    fahrenheit_float = (celsius * 1.8) + 32

    # output
    print("")
    print("{0}°C is equal to {1}°F".format(celsius, fahrenheit_float))
    print("\nDone.")

def main():
    # this function just calls other functions

    # call functions
    fahrenheit()


if __name__ == "__main__":
    main()

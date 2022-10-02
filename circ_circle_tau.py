#!/usr/bin/env python3
# Copyright (c) 2022 Ioana Marinescu All rights reserved.
# Created By: Ioana Marinescu
#
# Date: Sept. 29
# calculates circumference using tau


import constants


def main():
    # variables
    radius = float(input("Enter radius: "))

    # calculations
    circumference = constants.TAU * radius

    # displays circumference
    print(f"Circumference: {circumference}cm")


if __name__ == "__main__":
    main()

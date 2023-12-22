#!/usr/bin/env python

import subprocess
import sys

def check_factor(num1, num2, num3):
    if num3 is None:
        product = num1 * num2
    else:
        product = num3

    num = f"{num1}={num2}*{product}"
    print(num)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print('Usage: factors <file>')
        sys.exit(1)

    input_file = sys.argv[1]
    with open(input_file, 'r') as file:
        for line in file:
            number = int(line)
            factor_output = subprocess.check_output(["factor", str(number)]).decode("utf-8").strip()
            factors = list(map(int, factor_output.split(":")[1].split()))
            if len(factors) == 2:
                check_factor(number, factors[0], factors[1])
            else:
                check_factor(number, factors[0], None)

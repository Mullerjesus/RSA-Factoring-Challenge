import sys

def factorize(number):
    for i in range(2, number):
        if number % i == 0:
            return i, number // i
    return None, None

def main():
    if len(sys.argv) != 2:
        print("Usage: factors <file>")
        return

    input_file = sys.argv[1]
    with open(input_file, 'r') as file:
        for line in file:
            number = int(line)
            factor1, factor2 = factorize(number)
            print(f"{number}={factor1}*{factor2}")

if __name__ == "__main__":
    main()


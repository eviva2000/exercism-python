
def is_armstrong_number(number):
    digits = str(number)
    number_of_digits = len(digits)

    total = 0

    for digit in digits:
        total += int(digit) ** number_of_digits

    return total == number

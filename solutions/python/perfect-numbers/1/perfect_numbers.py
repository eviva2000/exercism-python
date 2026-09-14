def classify(number):
    if number <= 0:
        raise ValueError(
            "Classification is only possible for positive integers."
        )

    aliquot_sum = sum(
        divisor
        for divisor in range(1, number)
        if number % divisor == 0
    )

    if aliquot_sum == number:
        return "perfect"
    if aliquot_sum > number:
        return "abundant"

    return "deficient"
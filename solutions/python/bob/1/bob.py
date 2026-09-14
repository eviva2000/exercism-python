def response(hey_bob):
    message = hey_bob.strip()

    if not message:
        return "Fine. Be that way!"

    is_question = message.endswith("?")
    is_yelling = message.isupper()

    if is_question and is_yelling:
        return "Calm down, I know what I'm doing!"

    if is_yelling:
        return "Whoa, chill out!"

    if is_question:
        return "Sure."

    return "Whatever."
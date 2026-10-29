def normalise(text):
    text = text.replace(" ", "")
    text = text.replace("-", "")
    return text.upper()


def is_valid(reg):
    if len(reg) not in (9, 10):
        return False

    if not reg[0:2].isalpha():
        return False

    if not reg[2:4].isdigit():
        return False

    if not reg[4:-4].isalpha():
        return False

    if len(reg[4:-4]) not in (1, 2):
        return False

    if not reg[-4:].isdigit():
        return False

    return True


def format_number(reg):
    if not is_valid(reg):
        return "INVALID"

    return reg[:2] + " " + reg[2:4] + " " + reg[4:-4] + " " + reg[-4:]


numbers = [
    "tn 09 ab 1234",
    "KA-01-M-0007",
    "TN9AB1234",
    "TN 22 1234 AB",
    "KL 07 CD 4567",
    "MH-12-XY-9876"
]

for raw in numbers:
    reg = normalise(raw)

    if is_valid(reg):
        print(raw, "->", reg, "valid")
        print("Receipt:", format_number(reg))
    else:
        print(raw, "->", reg, "INVALID")
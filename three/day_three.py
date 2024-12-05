import re


def multiply(muls: str):
    left, right = re.findall("[0-9]+,[0-9]+", muls)[0].split(",")
    return int(left) * int(right)


def calculate_muls(muls: str):
    muls = re.findall("mul\([0-9]+,[0-9]+\)", muls)
    return sum([multiply(mul) for mul in muls])


def should_go(match):
    return match.group() == "do()"


def main():
    total = 0
    with open("three/input.txt") as file:
        text = "".join(file.readlines())
        go = True
        start_index = 0
        for match in re.finditer("(don't\(\)|do\(\))", text):
            if go:
                total += calculate_muls(text[start_index : match.start()])
            go = should_go(match)
            if go:
                start_index = match.end()
        if go:
            total += calculate_muls(text[start_index:])

    print(f"total : {total}")


if __name__ == "__main__":
    main()

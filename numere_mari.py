
def add_numbers(a, b):
    result = []
    carry = 0

    i = len(a) - 1
    j = len(b) - 1

    while i >= 0 or j >= 0 or carry:
        digit_a = int(a[i]) if i >= 0 else 0
        digit_b = int(b[j]) if j >= 0 else 0

        total = digit_a + digit_b + carry

        result.append(str(total % 10))
        carry = total // 10

        i -= 1
        j -= 1

    return ''.join(reversed(result))


def multiply_numbers(a, b):
    if a == "0" or b == "0":
        return "0"

    result = [0] * (len(a) + len(b))

    for i in range(len(a) - 1, -1, -1):
        for j in range(len(b) - 1, -1, -1):
            product = int(a[i]) * int(b[j])

            total = product + result[i + j + 1]

            result[i + j + 1] = total % 10
            result[i + j] += total // 10

    result = ''.join(str(digit) for digit in result)

    return result.lstrip('0') or "0"


def read_numbers(filename):
    try:
        with open(filename, "r") as file:
            lines = file.readlines()

        if len(lines) != 2:
            raise ValueError("The file must contain exactly two numbers.")

        numbers = []

        for line in lines:
            number = line.strip()

            if not number or not number.isdigit():
                raise ValueError("Invalid input. Use non-negative integers.")

            if len(number) > 200:
                raise ValueError("Each number can have at most 200 digits.")

            number = number.lstrip('0') or "0"
            numbers.append(number)

        return numbers[0], numbers[1]

    except FileNotFoundError:
        print("Error: numere.txt was not found.")
        return None, None

    except ValueError as error:
        print("Error:", error)
        return None, None


def main():
    a, b = read_numbers("numere.txt")

    if a is None:
        return

    total = add_numbers(a, b)
    product = multiply_numbers(a, b)

    print("First number:", a)
    print("Second number:", b)
    print("Sum:", total)
    print("Product:", product)


if __name__ == "__main__":
    main()

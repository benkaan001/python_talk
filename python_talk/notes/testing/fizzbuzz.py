def fizzBuzz(num: int) -> str:
    if num % 5 == 0 and num % 3 == 0:
        return "FizzBuzz"
    elif num % 5 == 0:
        return "Buzz"
    elif num % 3 == 0:
        return "Fizz"
    else:
        return str(num)


expected = "FizzBuzz"
result = fizzBuzz(15)
assert (type(result) == str), f"Expected actual to be of string type, but found {type(result)}"
assert result == expected, f"Expected {expected}, but found {result} "

if __name__ == "__main__":
    fizzBuzz()

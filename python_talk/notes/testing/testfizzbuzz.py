from fizzbuzz import fizzBuzz

def testFizzBuzz(num: int) -> str:
    result = fizzBuzz(num)
    assert type(result) == str, f"Expected actual to be of str, but found {type(result)}"
    assert result == expected, f"Expected {expected}, but found {result}"
    return print(result)

test_numbers = [0, 1, 2, 3, 5, 15]
expectations = ["FizzBuzz", "1", "2", "Fizz", "Buzz", "FizzBuzz"]

for i in range(len(test_numbers)):
    num = test_numbers[i]
    expected = expectations[i]
    testFizzBuzz(num)

"""
FizzBuzz
1
2
Fizz
Buzz
FizzBuzz

"""

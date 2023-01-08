def item_count(input_list: list) -> dict:
    return {item:input_list.count(item) for item in input_list}

empty_list = []
empty_count_result = {}
assert empty_count_result == item_count(empty_list)

breakfast_list = ["scrambled eggs", "eggs benedict", "classic American",
"scrambled eggs", "coffee", "classic American", "coffee", "coffee"]

breakfast_count_result = {"scrambled eggs": 2, "eggs benedict": 1, "classic American": 2,
                        "coffee": 3}

assert item_count(breakfast_list) == breakfast_count_result, \
f"""Expected {breakfast_count_result},but received {item_count(breakfast_list)}"""
print("Test passed!")
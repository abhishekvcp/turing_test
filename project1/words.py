import pandas as pd

print("Module words imported")

list1 = ["god","good","abc","xyz","xxxxyz","pdf","ppdf"]


def solutions (list1):
    output = 0
    string_len = len(list1)
    for str1 in list1:
        for str2 in list1:
            if set(str1) == set(str2):
                print(f"matched {str1} and {str2}")
                output = output + 1
    return int((output - string_len) / 2)

if __name__ == "__main__":
    result = solutions(list1)
    print(result)


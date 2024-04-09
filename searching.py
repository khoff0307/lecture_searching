import os
import json
# get current working directory path
cwd_path = os.getcwd()


def read_data(file_name, field):
    """
    Reads json file and returns sequential data.
    :param file_name: (str), name of json file
    :param field: (str), field of a dict to return
    :return: (list, string),
    """
    file_path = os.path.join(cwd_path, file_name)

    json_filename = file_name
    with open(json_filename, "r") as file_obj:
        data = json.load(file_obj)
    sequence = data[field]
    return sequence

def search_number(sequence, number):
    """
    Search for position of number in sequence
    :param sequence: [list] list of numbers
    :param number: [int] searched number
    :return: [int] position in list
    """
    i = 0
    dict = {}
    positions = []
    count = 0
    while i < len(sequence):
        if sequence[i] == number:
            print(f"Hledané číslo {number} se nachází na pozici {i}.")
            positions.append(i)
            count += 1
            dict["Positions:"] = positions
            dict["Count:"] = count
            i += 1
        else:
            i += 1
            continue
    if count != 0:
        return dict
    return print(f"Hledané číslo {number} není v seznamu.")


def main():
    sequence = read_data("sequential.json", "unordered_numbers")
    print(search_number(sequence, 0))

    pass


if __name__ == '__main__':
    main()
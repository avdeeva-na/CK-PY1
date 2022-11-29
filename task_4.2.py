import json

INPUT_FILE = "input.csv"


def csv_to_list_dict(filename, delimetr, new_line) -> list[dict]:
    with open(filename) as file:
        ls = []
        header = file.readline()
        for value, line in file:
            keys = line.strip(new_line).split(',')
            if value == 0:
                header = keys
                continue
            ls.append({})
            for i in enumerate(header):
                ls[-1][header[i]] = keys[i]
    return ls


print(json.dumps(csv_to_list_dict(INPUT_FILE, ',', '\n'), indent=4))

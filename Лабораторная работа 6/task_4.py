import json
from typing import Dict, Any

INPUT_FILE = "input.csv"


def csv_to_list_dict(filename) -> list[dict]:
    ls = []
    with open(filename) as file:
        j_dict = []
        for line in file:
            j_dict.append(line.split(','))
    for line in range(len(j_dict)-1):
        dict = {}
        for i in range(len(j_dict[0])):
            dict[j_dict[0][i]] = j_dict[1][i]
        ls.append(dict)
    with open('output.json', 'w') as write_file:
        json.dumps(ls, write_file, indent=4)


print(json.dumps)

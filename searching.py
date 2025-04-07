import json
import os

# get current working directory path
cwd_path = os.getcwd()


def read_data(file_name, field):
    """
    Reads json file and returns sequential data.
    :param file_name: (str), name of json file
    :param field: (str), field of a dict to return
    :return: (list, string),
    """
    if field not in {'unordered_numbers', 'ordered_numbers', 'dna_sequence'}:
        return None
    file_path = os.path.join(cwd_path, file_name)

    with open(file_path, 'r') as json_file:
        seq = json.load(json_file)
    return seq[field]

def linear_search(seq,number):
    """

    :param seq:
    :param number:
    :return: (dict):{'positions: <list of indices>, 'count': <total count>}
    """
    indices = []
    count = 0

    idx = 0
    while idx< len(seq):
        if seq[idx] == number:
            indices.append(idx)
            count += 1
        idx += 1
    return {
        'positions':indices,
        'count':count,
    }
def  pattern_search(seq, pattern):
    indices = set()
    pattern_size = len(pattern)

    left_idx = 0
    right_idx = pattern_size
    while right_idx < len(seq):
        for idx in range(pattern_size):
            if pattern[idx] != seq [left_idx + idx]:
                break
        else:
            indices.add(left_idx + pattern_size // 2)
        left_idx+= 1
        right_idx+= 1

def binary_search(seq, number):
    left, right = (0, len(seq) -1)
    middle = (left + right) // 2
    while left <= right:
        if number < seq[middle]:
            right = middle - 1
        elif number > seq[middle]:
            left = middle + 1
        else:
            return middle
    return




def main():
    file_name = 'sequential.json'
    # linear search
    seq = read_data(file_name, field='unordered_numbers')


    results = linear_search(seq, number=0)

    seq = read_data(file_name, field='dna_sequence')
    pattern = 'ATA'

    matches = pattern_search(seq, pattern)

    seq = read_data(file_name, field='ordered_numbers')
    number = 8
    idx = binary_search(seq, number)
    print(idx)

    print(seq,matches, results)

if __name__ == '__main__':
    main()
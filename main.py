import numpy as np
import random
from frequency_predictor import FrequencyPredictor
def die():
    print('Killing process')
    exit(0)

def read_data(filename: str, n_persons: int, contains_days: bool, use_days: bool, use_incomplete: bool):
    data  = []
    valid_count, invalid_count, empty_count = 0, 0, 0

    lines = open(filename, 'r').read().splitlines()

    for i, line in enumerate(lines):
        line_data = line.split(' ')

        if use_days and use_incomplete:
            raise NotImplementedError

        elif use_days and not use_incomplete:
            raise NotImplementedError

        elif not use_days and use_incomplete:
            raise NotImplementedError

        elif not use_days and not use_incomplete:
            if line_data == ['']:
                empty_count += 1
                continue

            line_data = line_data[1:] if contains_days else line_data
            if len(line_data) != n_persons:
                    print(f'Invalid data size at line {i + 1}')
                    invalid_count+=1
                    continue
            else:
                valid_count+=1
            try:
                data.append(list(map(int, line_data)))
            except ValueError as e:
                print(f'[ValueError] Invalid data format at line {i + 1}: {e}')
                invalid_count+=1
                continue

    
    print(f'Read {valid_count} valid lines and skipped {invalid_count} invalid ones')
    return data

def read_labels(filename: str):
    labels = {}
    lines = open(filename, 'r').read().splitlines()

    for line in lines:
        number, name = line.split(' ', 1)
        number = int(number)

        if number in labels:
            print(f'[Error] Label {number} is already used on {labels[number]}!')
            exit(0)

        labels[number] = name
    return labels

labels = read_labels('./labels.txt')
data = read_data('./data.txt', len(labels), True, False, False)

# TODO: handle first prediction better, by taking into account what happened last time
# anyways, for now its just gonna be whos most likely to go next

fp = FrequencyPredictor(labels, data)
fp.predict()

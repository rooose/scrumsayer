from predictor import Predictor
import random

class FrequencyPredictor(Predictor):
    def __init__(self, labels, data):
        Predictor.__init__(self, labels, data)


    def to_index(self, array):
        # example input is [0, 1, 3, 11, 1] or [0, 1, 3, 1, 11]
        return '|'.join([str(elem) for elem in array])

    def from_index(self, index):
        # example input is 0|1|3|11|1 or 0|1|3|1|11
        return [int(elem) for elem in index.split('|')]


    def predict_nth_person(self, n):
        # for this one, check the probability of the next one being
        # first
        counts = {}
        sequences = [ scrum[:n] for scrum in self._data ]
        unique_sequences = [list(item) for item in set(tuple(row) for row in sequences)]

        for unique_sequence in unique_sequences:
            index = self.to_index(unique_sequence)
            counts[index] = sequences.count(unique_sequence)

        counts = {k: v for k, v in sorted(counts.items(), key=lambda item: item[1])}

        if list(counts.values())[len(counts) - 1] == 0:
            # just predict a random person
            result = random.randint(0, len(self._labels) - 1)

        else:
            total = sum(counts.values())
            rnd = random.randint(1, total)
            curr_total = 0
            for key, value in counts.items():
                curr_total += value
                if curr_total >= rnd:
                    result = self.from_index(key)[-1]
                    break
        
        return result



    def predict(self):

        for n in range(len(self._labels)):
            result = self.predict_nth_person(n + 1)
            print(f'NTH PERSON IS {self._labels[result]}')
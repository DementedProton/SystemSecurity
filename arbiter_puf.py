import random
import numpy as np
import math


class ArbiterPuf:

    def __init__(self, number_of_bits):
        self.number_of_bits = number_of_bits
        self.delay_vector = [random.uniform(-1, 1) for i in range(number_of_bits)]  # uniform is in range [a,b]

    def calculate_responses(self, number_of_challenges):
        list_of_responses = []
        for x in range(number_of_challenges):
            challenge = [random.randint(0, 1) for i in range(self.number_of_bits)]  # generate a random bit vector
            list_of_responses.append(self.calculate_one_response(challenge))
        return list_of_responses

    def calculate_one_response(self, challenge):
        response = challenge.copy()
        phi_vector = [self._calculate_phi(challenge[i:]) for i in range(len(challenge))]
        delay = np.dot(np.transpose(self.delay_vector), phi_vector)  # dot multiply phi vector with delay vector
        response.append(0 if delay < 0 else 1)
        return response

    @staticmethod
    def _calculate_phi(challenge_seq):
        return np.prod([math.pow(-1, i) for i in challenge_seq])


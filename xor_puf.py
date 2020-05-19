from arbiter_puf import ArbiterPuf
import random


class XorPUF:

    def __init__(self, number_of_bits, number_of_pufs):
        self.number_of_bits = number_of_bits
        self.list_of_pufs = [ArbiterPuf(number_of_bits) for x in range(number_of_pufs)]

    def calculate_responses(self, number_of_challenges):
        list_of_responses = []
        for i in range(number_of_challenges):
            challenge = [random.randint(0, 1) for j in range(self.number_of_bits)]  # generate a random bit vector
            list_of_responses.append(self.calculate_single_response(challenge))
        return list_of_responses

    def calculate_single_response(self, challenge):
        final_response = challenge.copy()
        list_of_responses_of_pufs = []
        for puf in self.list_of_pufs:
            response = puf.calculate_one_response(challenge).pop()
            list_of_responses_of_pufs.append(response)
        result = 0
        for response in list_of_responses_of_pufs:
            result ^= response
        final_response.append(result)  # each response is a list of challenge bits, and one response bit
        return final_response


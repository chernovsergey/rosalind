__author__ = 'Sergey'
#from __future__ import division
import sys
import unittest


class Test(unittest.TestCase):
    SAMPLE_DATASET = (2, 2, 2)
    SAMPLE_OUTPUT = 0.78333

    def test_definition_sample(self):
        self.assertAlmostEqual(
            self.SAMPLE_OUTPUT,
            probability(*self.SAMPLE_DATASET),
            places=5
        )


def probability(k, m, n):
    """Find the probability that two randomly selected mating organisms will
    produce an individual with a dominant allele."""

    pops = {'k': k, 'm': m, 'n': n}

    def _total_pop(populations):
        return sum(v for k, v in populations.items())

    def _event_probablity(subpop, populations):
        return populations[subpop] / _total_pop(populations)

    def _pick(p1, p2, populations):
        _pop = dict(populations)

        first_event_probability = _event_probablity(p1, _pop)
        _pop[p1] -= 1
        second_event_probability = _event_probablity(p2, _pop)

        if 'k' in (p1, p2):
            multiplier = 1.0
        elif p1 == p2 and p1 == 'm':
            multiplier = 0.75
        elif 'm' in (p1, p2) and 'n' in (p1, p2):
            multiplier = 0.5
        elif 'n' == p1 and 'n' == p2:
            multiplier = 0.0

        return first_event_probability * second_event_probability * multiplier

    return sum(_pick(subpop1, subpop2, pops)
        for subpop2 in pops.keys()
        for subpop1 in pops.keys())

def main():
    with open("mendel_first_law.txt") as f:
        k, m, n = tuple(int(pop, 10)
            for pop in f.read().replace('\n', '').split(' '))
        print(probability(k, m, n))


if __name__ == '__main__':
    main()
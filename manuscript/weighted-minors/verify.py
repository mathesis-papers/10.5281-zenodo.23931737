import itertools
import json
import math
from fractions import Fraction


def dot(first, second):
    return sum(left * right for left, right in zip(first, second))


def reflect(vector, normal):
    multiplier = 2 * dot(vector, normal) / dot(normal, normal)
    return [entry - multiplier * axis for entry, axis in zip(vector, normal)]


def frame(dimension, seed):
    columns = [[Fraction(int(row == column)) for row in range(dimension)] for column in range(3)]
    if seed:
        for turn in range(2):
            normal = [Fraction(((index + 1) * (seed + turn + 1)) % 7 - 3) for index in range(dimension)]
            columns = [reflect(column, normal) for column in columns]
    for first in range(3):
        for second in range(3):
            assert dot(columns[first], columns[second]) == int(first == second)
    return columns


def pair_minor(first, second, pair):
    left, right = pair
    return first[left] * second[right] - first[right] * second[left]


def triple_minor(first, second, third, triple):
    left, middle, right = triple
    return (third[left] * pair_minor(first, second, (middle, right))
            - third[middle] * pair_minor(first, second, (left, right))
            + third[right] * pair_minor(first, second, (left, middle)))


def integer_masses(pair_masses, triple_masses):
    denominator = math.lcm(*(entry.denominator for entry in pair_masses + triple_masses))
    return ([int(entry * denominator) for entry in pair_masses],
            [int(entry * denominator) for entry in triple_masses])


def check_pairs():
    family_checks = 0
    weighted_checks = 0
    energy_checks = 0
    frame_checks = 0
    dimensions = list(range(3, 7))
    for dimension in dimensions:
        pairs = list(itertools.combinations(range(dimension), 2))
        triples = list(itertools.combinations(range(dimension), 3))
        pair_index = {pair: index for index, pair in enumerate(pairs)}
        triple_edges = [[pair_index[pair] for pair in itertools.combinations(triple, 2)] for triple in triples]
        triple_masks = [sum(1 << edge for edge in edges) for edges in triple_edges]
        for seed in range(4):
            original_first, original_second, third = frame(dimension, seed)
            for variant in range(2):
                if variant:
                    first = [2 * left + right for left, right in zip(original_first, original_second)]
                    second = [left - 3 * right for left, right in zip(original_first, original_second)]
                else:
                    first, second = original_first, original_second
                assert dot(third, first) == dot(third, second) == 0
                pair_values = [pair_minor(first, second, pair) for pair in pairs]
                triple_values = [triple_minor(first, second, third, triple) for triple in triples]
                pair_masses = [value ** 2 for value in pair_values]
                triple_masses = [value ** 2 for value in triple_values]
                gram = dot(first, first) * dot(second, second) - dot(first, second) ** 2
                assert sum(pair_masses) == sum(triple_masses) == gram
                for pair, value in zip(pairs, pair_values):
                    left, right = pair
                    recovered = sum(third[index] * triple_minor(first, second, third, (index, left, right))
                                    for index in range(dimension))
                    assert recovered == value
                pair_integer, triple_integer = integer_masses(pair_masses, triple_masses)
                totals = [0] * (1 << len(pairs))
                for mask in range(1, len(totals)):
                    lowest = mask & -mask
                    totals[mask] = totals[mask ^ lowest] + pair_integer[lowest.bit_length() - 1]
                for mask, left_mass in enumerate(totals):
                    right_mass = sum(mass for mass, neighborhood in zip(triple_integer, triple_masks)
                                     if mask & neighborhood)
                    assert left_mass <= right_mass, (dimension, seed, variant, mask)
                    family_checks += 1
                for pattern in range(100):
                    if pattern == 0:
                        weights = [-3] * len(pairs)
                    elif pattern == 1:
                        weights = [0] * len(pairs)
                    elif pattern == 2:
                        weights = [1] * len(pairs)
                    else:
                        weights = [((edge + 1) * (pattern + 2) + seed) % 17 - 8 for edge in range(len(pairs))]
                    maximums = [max(weights[edge] for edge in edges) for edges in triple_edges]
                    left_value = sum(weight * mass for weight, mass in zip(weights, pair_integer))
                    right_value = sum(weight * mass for weight, mass in zip(maximums, triple_integer))
                    assert left_value <= right_value
                    if pattern < 3:
                        assert left_value == right_value
                    minimum = min(weights)
                    levels = sorted(set([0] + [weight - minimum for weight in weights]))
                    threshold_difference = 0
                    for previous, level in zip(levels, levels[1:]):
                        left_mass = sum(mass for weight, mass in zip(weights, pair_integer) if weight - minimum >= level)
                        right_mass = sum(mass for weight, mass in zip(maximums, triple_integer) if weight - minimum >= level)
                        assert left_mass <= right_mass
                        threshold_difference += (level - previous) * (right_mass - left_mass)
                    assert threshold_difference == right_value - left_value
                    weighted_checks += 1
                arbitrary = {pair: Fraction((index + 1) * (seed + 1) % 11 - 5)
                             for index, pair in enumerate(pairs)}

                def alternating(left, right):
                    if left == right:
                        return Fraction(0)
                    return arbitrary[(left, right)] if left < right else -arbitrary[(right, left)]

                contraction = [sum(third[index] * alternating(index, right) for index in range(dimension))
                               for right in range(dimension)]
                lifted = [third[left] * alternating(middle, right)
                          - third[middle] * alternating(left, right)
                          + third[right] * alternating(left, middle)
                          for left, middle, right in triples]
                assert sum(value ** 2 for value in lifted) + sum(value ** 2 for value in contraction) == sum(value ** 2 for value in arbitrary.values())
                energy_checks += 1
                frame_checks += 1
    return {
        'arithmetic': 'exact rational and integer',
        'dimensions': dimensions,
        'rational_frames_and_variants': frame_checks,
        'pair_family_inequalities': family_checks,
        'weighted_inequalities': weighted_checks,
        'exterior_energy_identities': energy_checks,
        'weight_cases': 'constant negative, zero, constant positive, and deterministic signed patterns',
        'scope': 'finite real-coordinate checks; universal statements have written proofs in note.pdf',
        'status': 'pass',
    }


class Gaussian:
    __slots__ = ('real', 'imaginary')

    def __init__(self, real=0, imaginary=0):
        self.real = Fraction(real)
        self.imaginary = Fraction(imaginary)

    def __add__(self, other):
        other = other if isinstance(other, Gaussian) else Gaussian(other)
        return Gaussian(self.real + other.real, self.imaginary + other.imaginary)

    __radd__ = __add__

    def __neg__(self):
        return Gaussian(-self.real, -self.imaginary)

    def __sub__(self, other):
        return self + (-other)

    def __mul__(self, other):
        other = other if isinstance(other, Gaussian) else Gaussian(other)
        return Gaussian(self.real * other.real - self.imaginary * other.imaginary,
                        self.real * other.imaginary + self.imaginary * other.real)

    __rmul__ = __mul__

    def __eq__(self, other):
        other = other if isinstance(other, Gaussian) else Gaussian(other)
        return self.real == other.real and self.imaginary == other.imaginary

    def conjugate(self):
        return Gaussian(self.real, -self.imaginary)

    def squared_norm(self):
        return self.real ** 2 + self.imaginary ** 2


def wedge(first, second):
    result = {}
    for first_indices, first_value in first.items():
        for second_indices, second_value in second.items():
            if set(first_indices).intersection(second_indices):
                continue
            indices = tuple(sorted(first_indices + second_indices))
            inversions = sum(left > right for left in first_indices for right in second_indices)
            result[indices] = result.get(indices, Gaussian()) + (-1) ** inversions * first_value * second_value
    return result


def contract_form(vector, form):
    result = {}
    for indices, value in form.items():
        for position, coordinate in enumerate(indices):
            remaining = indices[:position] + indices[position + 1:]
            result[remaining] = (result.get(remaining, Gaussian())
                                 + (-1) ** position * vector[coordinate].conjugate() * value)
    return result


def full_frame(dimension, seed):
    columns = [[Fraction(int(row == column)) for row in range(dimension)]
               for column in range(dimension)]
    if seed:
        for turn in range(2):
            normal = [Fraction(((index + 1) * (seed + turn + 1)) % 7 - 3)
                      for index in range(dimension)]
            columns = [reflect(column, normal) for column in columns]
    return columns


def form_norm_squared(form):
    return sum(value.squared_norm() for value in form.values())


def check_exterior_degrees():
    configurations = [(4, 1, 1), (5, 2, 1), (6, 2, 2), (6, 3, 1), (6, 3, 2), (6, 1, 3)]
    phases = [Gaussian(1), Gaussian(0, 1), Gaussian(Fraction(3, 5), Fraction(4, 5)),
              Gaussian(Fraction(-5, 13), Fraction(12, 13)),
              Gaussian(Fraction(8, 17), Fraction(-15, 17)), Gaussian(0, -1)]
    family_checks = 0
    weighted_checks = 0
    cases = 0
    complex_cases = 0
    nondecomposable_cases = 0
    exhaustive_family_cases = 0
    for dimension, degree, lifts in configurations:
        subsets = list(itertools.combinations(range(dimension), degree))
        supersets = list(itertools.combinations(range(dimension), degree + lifts))
        neighbors = [[index for index, subset in enumerate(subsets) if set(subset).issubset(superset)]
                     for superset in supersets]
        neighborhood_masks = [sum(1 << index for index in indices) for indices in neighbors]
        for seed in range(3):
            columns = full_frame(dimension, seed)
            for complex_coordinates in [False, True]:
                coordinate_phases = phases[:dimension] if complex_coordinates else [Gaussian(1)] * dimension
                vectors = [[phase * value for phase, value in zip(coordinate_phases, column)]
                           for column in columns]
                for first in range(dimension):
                    for second in range(dimension):
                        assert sum(left.conjugate() * right for left, right in zip(vectors[first], vectors[second])) == int(first == second)
                horizontal = {}
                for index, selected_columns in enumerate(itertools.combinations(range(lifts, dimension), degree)):
                    term = {(): Gaussian(1)}
                    for column in selected_columns:
                        term = wedge(term, {(coordinate,): value for coordinate, value in enumerate(vectors[column])})
                    coefficient = Gaussian(Fraction((index + 1) * (seed + 2) % 11 - 5),
                                           Fraction((index + seed) % 7 - 3, 5) if complex_coordinates else 0)
                    for indices, value in term.items():
                        horizontal[indices] = horizontal.get(indices, Gaussian()) + coefficient * value
                for vector in vectors[:lifts]:
                    assert form_norm_squared(contract_form(vector, horizontal)) == 0
                lifted = horizontal
                for vector in vectors[:lifts]:
                    lifted = wedge({(coordinate,): value for coordinate, value in enumerate(vector)}, lifted)
                recovered = lifted
                for vector in reversed(vectors[:lifts]):
                    recovered = contract_form(vector, recovered)
                assert all(recovered.get(indices, Gaussian()) == horizontal.get(indices, Gaussian())
                           for indices in subsets)
                original_masses = [horizontal.get(indices, Gaussian()).squared_norm() for indices in subsets]
                lifted_masses = [lifted.get(indices, Gaussian()).squared_norm() for indices in supersets]
                assert sum(original_masses) == sum(lifted_masses) > 0
                if degree == 2 and form_norm_squared(wedge(horizontal, horizontal)) > 0:
                    nondecomposable_cases += 1
                original_integer, lifted_integer = integer_masses(original_masses, lifted_masses)
                if len(subsets) <= 10:
                    family_masks = range(1 << len(subsets))
                    exhaustive_family_cases += 1
                else:
                    modulus = 1 << len(subsets)
                    family_masks = sorted({0, modulus - 1}
                                          | {1 << index for index in range(len(subsets))}
                                          | {((index + 1) * 2654435761 + seed * 101) % modulus
                                             for index in range(256)})
                for mask in family_masks:
                    original_mass = sum(mass for index, mass in enumerate(original_integer) if mask & (1 << index))
                    lifted_mass = sum(mass for mass, neighborhood in zip(lifted_integer, neighborhood_masks)
                                      if mask & neighborhood)
                    assert original_mass <= lifted_mass
                    family_checks += 1
                for pattern in range(64):
                    if pattern < 3:
                        weights = [(-3, 0, 2)[pattern]] * len(subsets)
                    else:
                        weights = [((index + 1) * (pattern + 2) + seed) % 19 - 9
                                   for index in range(len(subsets))]
                    minimums = [min(weights[index] for index in indices) for indices in neighbors]
                    maximums = [max(weights[index] for index in indices) for indices in neighbors]
                    lower = sum(weight * mass for weight, mass in zip(minimums, lifted_integer))
                    middle = sum(weight * mass for weight, mass in zip(weights, original_integer))
                    upper = sum(weight * mass for weight, mass in zip(maximums, lifted_integer))
                    assert lower <= middle <= upper
                    if pattern < 3:
                        assert lower == middle == upper
                    weighted_checks += 1
                cases += 1
                complex_cases += int(complex_coordinates)
    assert nondecomposable_cases > 0
    return {
        'arithmetic': 'exact Gaussian rational, rational, and integer',
        'configurations_n_k_r': configurations,
        'cases': cases,
        'nonreal_coordinate_cases': complex_cases,
        'certified_nondecomposable_two_form_cases': nondecomposable_cases,
        'cases_with_exhaustive_subset_families': exhaustive_family_cases,
        'subset_family_inequalities': family_checks,
        'two_sided_weighted_inequalities': weighted_checks,
        'identities': 'Hermitian orthonormality, horizontal contraction, recovery, equal mass, constant-weight equality',
        'scope': 'finite examples of Corollaries 4 and 5; universal statements have written proofs in note.pdf',
        'status': 'pass',
    }


def main():
    first = [Fraction(4, 5), Fraction(3, 5)]
    second = [Fraction(4, 5), Fraction(-3, 5)]
    third = [Fraction(1), Fraction(0)]
    long_side = pair_minor(first, second, (0, 1)) ** 2
    short_sides = pair_minor(first, third, (0, 1)) ** 2 + pair_minor(third, second, (0, 1)) ** 2
    assert long_side == Fraction(576, 625) > short_sides == Fraction(18, 25)
    print(json.dumps({'pair_minors': check_pairs(), 'exterior_degrees': check_exterior_degrees(),
                      'distance_exponent_control': {'exponent': 1, 'dimension': 2,
                                                    'long_side': str(long_side),
                                                    'sum_of_short_sides': str(short_sides),
                                                    'triangle_inequality': False,
                                                    'scope': 'one exact instance of Corollary 7'},
                      'status': 'pass'}, indent=2))


if __name__ == '__main__':
    main()

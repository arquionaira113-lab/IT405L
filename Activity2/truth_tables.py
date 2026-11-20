# Activity 2 -- truth_tables.py

from itertools import product
from logic_ops import evaluate
import importlib


# My E1 and E2
E1_TUPLE = ('implies', ('and', 'r', 'p'), 'q')
E2_TUPLE = ('and', ('implies', 'r', 'q'), ('implies', 'p', 'q'))


# STEP 1
def assignments(variables):
    return [
        dict(zip(variables, combo))
        for combo in product([False, True], repeat=len(variables))
    ]


# STEP 3
def fill(expr, s):
    if isinstance(expr, str):
        return s[expr]

    if isinstance(expr, bool):
        return expr

    return tuple([expr[0]] + [fill(x, s) for x in expr[1:]])


def truth_table(expr, variables):
    print(' ' + ' '.join('%-5s' % v for v in variables) + ' | value')

    for s in assignments(variables):
        print(
            ' ' +
            ' '.join('%-5s' % s[v] for v in variables) +
            ' | %s' % evaluate(fill(expr, s))
        )


# STEP 5
def equivalent(expr1, expr2, variables):
    return all(
        evaluate(fill(expr1, s)) == evaluate(fill(expr2, s))
        for s in assignments(variables)
    )


# CLASSIFICATION
def classify(expr, variables):
    values = [
        evaluate(fill(expr, s))
        for s in assignments(variables)
    ]

    if all(values):
        return 'tautology'

    if not any(values):
        return 'contradiction'

    return 'contingency'


# STEP 8
def witness(expr1, expr2, variables):
    for s in assignments(variables):
        if evaluate(fill(expr1, s)) != evaluate(fill(expr2, s)):
            return ','.join(
                '%s=%s' % (v, s[v])
                for v in sorted(variables)
            )

    return 'none'


# STEP 9 FIX
def variables_of(expr):
    if isinstance(expr, str):
        return {expr}

    if isinstance(expr, bool):
        return set()

    return set().union(
        *(variables_of(x) for x in expr[1:])
    )


def equivalent_complete(expr1, expr2):
    names = sorted(
        variables_of(expr1) |
        variables_of(expr2)
    )

    return equivalent(expr1, expr2, names)


if __name__ == '__main__':

    # STEP 2
    print('STEP 2 -- the count is 2 to the power n')

    for n in (1, 2, 3, 4):
        names = ['v%d' % i for i in range(n)]

        print(
            ' n = %d: %d rows (2^%d = %d)'
            % (n, len(assignments(names)), n, 2 ** n)
        )

    print()

    # STEP 4
    print('STEP 4 -- p or not p')

    truth_table(
        ('or', 'p', ('not', 'p')),
        ['p']
    )

    print(
        ' ->',
        classify(
            ('or', 'p', ('not', 'p')),
            ['p']
        ),
        '(true on every row)'
    )

    print('STEP 4 -- p and not p')

    truth_table(
        ('and', 'p', ('not', 'p')),
        ['p']
    )

    print(
        ' ->',
        classify(
            ('and', 'p', ('not', 'p')),
            ['p']
        ),
        '(false on every row)'
    )

    print()

    # STEP 6
    dm1 = ('not', ('and', 'p', 'q'))
    dm2 = ('or', ('not', 'p'), ('not', 'q'))

    print('STEP 6 -- De Morgan: not (p and q)')
    truth_table(dm1, ['p', 'q'])

    print('STEP 6 -- (not p) or (not q)')
    truth_table(dm2, ['p', 'q'])

    print(
        ' equivalent:',
        equivalent(dm1, dm2, ['p', 'q'])
    )

    print()

    # STEP 7
    im1 = ('implies', 'p', 'q')
    im2 = ('or', ('not', 'p'), 'q')

    print('STEP 7 -- p implies q')
    truth_table(im1, ['p', 'q'])

    print('STEP 7 -- not p or q')
    truth_table(im2, ['p', 'q'])

    print(
        ' equivalent:',
        equivalent(im1, im2, ['p', 'q'])
    )

    print()

    # STEP 8
    P = importlib.import_module(
        'IT405_A02_2310213-2'
    )

    names = sorted(
        variables_of(E1_TUPLE) |
        variables_of(E2_TUPLE)
    )

    print(
        'STEP 8 -- my own E1 = %s and E2 = %s over %s'
        % (P.E1, P.E2, names)
    )

    print('E1:')
    truth_table(E1_TUPLE, names)

    print('E2:')
    truth_table(E2_TUPLE, names)

    print(
        ' equivalent:',
        equivalent(E1_TUPLE, E2_TUPLE, names),
        '| differing row:',
        witness(E1_TUPLE, E2_TUPLE, names)
    )

    print()

    # STEP 9
    a = ('or', 'p', 'q')
    b = ('or', 'p', ('or', 'q', 'r'))

    print(
        'STEP 9 -- equivalent(a, b, [p, q])'
    )

    try:
        print(
            ' ->',
            equivalent(a, b, ['p', 'q'])
        )

    except KeyError as e:
        print(
            ' -> KeyError:',
            e,
            '(r was never given a value)'
        )

    print(
        ' with the fix, over every variable of both (p, q, r):',
        equivalent_complete(a, b),
        '| differing row:',
        witness(
            a,
            b,
            sorted(
                variables_of(a) |
                variables_of(b)
            )
        )
    )
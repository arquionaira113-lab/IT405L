# Activity 1 -- logic_ops.py
# IT 405L -- Logical Operators and an Expression Evaluator
# Student: Arquion, Aira Mae L.
# Student No.: 2310213-2
# Section B -- Group B01 -- Slip B01-2

import sys
import traceback


# ============================================================
# STEP 2 -- Logical Operators
# ============================================================

def my_and(a, b):
    """True only when both are True."""
    return (a, b) == (True, True)


def my_or(a, b):
    """False only when both are False."""
    return (a, b) != (False, False)


def my_not(a):
    """The opposite truth value."""
    return a == False


# ============================================================
# STEP 3 -- Implies
# ============================================================

def my_implies(a, b):
    """
    'a implies b' is False only when a is True
    and b is False.

    Truth table:
    T T -> True
    T F -> False
    F T -> True
    F F -> True
    """
    return (a, b) != (True, False)


# ============================================================
# STEP 5 -- Expression Evaluator
# ============================================================

def evaluate(expr):
    """
    Evaluate a nested logical expression.

    A boolean value returns itself.

    Supported operators:
        and
        or
        not
        implies
    """

    # If the expression is already True or False
    if isinstance(expr, bool):
        return expr

    # First item is the operator
    op = expr[0]

    # NOT has only one operand
    if op == 'not':
        return my_not(evaluate(expr[1]))

    # AND, OR, and IMPLIES have two operands
    left = evaluate(expr[1])
    right = evaluate(expr[2])

    if op == 'and':
        return my_and(left, right)

    if op == 'or':
        return my_or(left, right)

    if op == 'implies':
        return my_implies(left, right)

    # Unknown operator
    raise ValueError('unknown operator: %r' % (op,))


# ============================================================
# MAIN PROGRAM
# ============================================================

if __name__ == '__main__':

    import importlib

    # Load the student's own parameter file.
    # The filename contains a hyphen, so importlib is used.
    P = importlib.import_module('IT405_A01_2310213-2')

    # Get the expression from the student's own file.
    # DO NOT manually retype EXPR here.
    EXPR = P.EXPR
    EXPR_TEXT = P.EXPR_TEXT


    # ========================================================
    # STEP 1 -- Python Version
    # ========================================================

    print(
        'STEP 1 -- Python version on this computer:',
        sys.version.split()[0]
    )

    print()


    # ========================================================
    # STEP 4 -- Test every logical function
    # ========================================================

    print(
        'STEP 4 -- every function on every combination '
        '(compare with the paper table)'
    )

    # Test NOT
    for a in (True, False):
        print(
            ' my_not(%-5s) = %s' %
            (a, my_not(a))
        )

    # Test AND, OR, and IMPLIES
    for name, f in (
        ('my_and', my_and),
        ('my_or', my_or),
        ('my_implies', my_implies)
    ):

        for a in (True, False):

            for b in (True, False):

                print(
                    ' %s(%-5s, %-5s) = %s' %
                    (name, a, b, f(a, b))
                )


    print()


    # ========================================================
    # STEP 6 -- Test six expressions
    # ========================================================

    print(
        'STEP 6 -- evaluate on six expressions '
        '(the last one is EXPR from my own file)'
    )

    tests = [

        # Test 1
        (
            ('and', True, ('not', False)),
            True
        ),

        # Test 2
        (
            ('or', False, False),
            False
        ),

        # Test 3
        (
            ('implies', True, False),
            False
        ),

        # Test 4
        (
            ('implies', False, False),
            True
        ),

        # Test 5
        (
            ('not', ('and', True, ('or', False, True))),
            False
        ),

        # Test 6 -- student's own EXPR
        (
            EXPR,
            True
        )
    ]


    # Run all six tests
    for expr, by_hand in tests:

        got = evaluate(expr)

        print(
            ' evaluate(%s) = %s    (by hand: %s) %s' %
            (
                expr,
                got,
                by_hand,
                'OK' if got == by_hand else 'DIFFERENT'
            )
        )


    # Print the student's expression in normal text form
    print(
        ' EXPR written out:',
        EXPR_TEXT
    )


    print()


    # ========================================================
    # STEP 7 -- Expected Error
    # ========================================================

    print(
        'STEP 7 -- ("or", True, ("and", 1/0, False))'
    )

    try:

        # This is EXPECTED to cause ZeroDivisionError.
        expr = (
            'or',
            True,
            ('and', 1 / 0, False)
        )

        print(
            ' evaluate ->',
            evaluate(expr)
        )

    except ZeroDivisionError:

        print(
            ' The error exactly as Python reports it:'
        )

        print(
            ' ' +
            traceback.format_exc()
            .strip()
            .replace('\n', '\n ')
        )
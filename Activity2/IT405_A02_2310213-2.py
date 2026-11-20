# -*- coding: utf-8 -*-

import hashlib

STUDENT_NO = '2310213-2'

E1 = '((r and p) implies q)'
E2 = '((r implies q) and (p implies q))'
VARIABLES = ['p', 'q', 'r']


def stamp(student_no, activity, *values):
    payload = '|'.join(
        [str(student_no).strip(), str(activity)]
        + [repr(v) for v in values]
    )
    return hashlib.sha256(
        payload.encode('utf-8')
    ).hexdigest()[:10].upper()


if __name__ == '__main__':
    verdict = False
    witness = 'p=False,q=False,r=True'

    print(stamp(STUDENT_NO, 2, E1, E2, verdict, witness))
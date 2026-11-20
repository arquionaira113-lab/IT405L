# -*- coding: utf-8 -*-

import hashlib

STUDENT_NO = '2310213-2'

FACTS = [
    ('olen', 'kira'),
    ('kira', 'carl'),
    ('kira', 'jom'),
    ('jom', 'hugo'),
    ('jom', 'elle'),
    ('carl', 'rey'),
    ('carl', 'mara'),
    ('kira', 'gina'),
]

STEP8 = ('kira', 'kira')


def stamp(student_no, activity, *values):
    payload = '|'.join(
        [str(student_no).strip(), str(activity)]
        + [repr(v) for v in values]
    )
    return hashlib.sha256(
        payload.encode('utf-8')
    ).hexdigest()[:10].upper()


if __name__ == '__main__':
    grandparents = (
        ('kira', 'elle'),
        ('kira', 'hugo'),
        ('kira', 'mara'),
        ('kira', 'rey'),
        ('olen', 'carl'),
        ('olen', 'gina'),
        ('olen', 'jom')
    )
    print(stamp(STUDENT_NO, 3, tuple(tuple(f) for f in FACTS), grandparents))
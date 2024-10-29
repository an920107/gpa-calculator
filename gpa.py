from enum import Enum

class GPA(float, Enum):
    A = 4.0
    B = 3.0
    C = 2.0
    D = 1.0
    F = 0.0

def to_gpa(scores: float) -> GPA:
    '''
    To convert the 100-point scores to GPA.
    '''
    if scores >= 80:
        return GPA.A
    elif scores >= 70:
        return GPA.B
    elif scores >= 70:
        return GPA.C
    elif scores >= 60:
        return GPA.D
    else:
        return GPA.F

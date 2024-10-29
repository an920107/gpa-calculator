import os
from gpa import to_gpa
from table import print_table

def create(name: str) -> None:
    '''
    To create a new semester with the given name.
    '''

    path = os.path.join('data', name)

    if os.path.exists(path):
        print('The semester has already been created.')
        return

    os.makedirs(path)


def list_all() -> None:
    '''
    To list all the semesters.
    '''

    semesters = os.listdir('data')

    if len(semesters) == 0:
        print('No semester has been created.')
        return
    
    semesters.sort()

    rows = []
    credit_sum = scores_sum = point_sum = 0
    for semester in semesters:
        subjects = os.listdir(os.path.join('data', semester))
        subjects.sort()
        for subject in subjects:
            with open(os.path.join('data', semester, subject)) as file:
                credit = int(file.readline())
                scores = float(file.readline())
                rank = to_gpa(scores)
                rows.append([semester, subject, credit, scores, rank.name, rank.value])
                credit_sum += credit
                scores_sum += scores * credit
                point_sum += rank.value * credit

    if len(rows) == 0:
        print('No subject has been added.')
        return

    print_table(['Semester', 'Subject', 'Credit', 'Scores', 'GPA', 'Point'], rows)
    print(f'Total credit: {credit_sum}')
    print(f'Weighted scores: {scores_sum / credit_sum:.2f}')
    print(f'GPA: {point_sum / credit_sum:.2f}')


def print_semester(name: str) -> None:
    '''
    To print the semester and its subjects.
    '''

    path = os.path.join('data', name)

    if not os.path.exists(path):
        print('The semester does not exist.')
        return

    subjects = os.listdir(path)

    if len(subjects) == 0:
        print('No subject has been added.')
        return
    
    subjects.sort()

    rows = []
    credit_sum = scores_sum = point_sum = 0
    for subject in subjects:
        with open(os.path.join(path, subject)) as file:
            credit = int(file.readline())
            scores = float(file.readline())
            rank = to_gpa(scores)
            rows.append([subject, credit, scores, rank.name, rank.value])
            credit_sum += credit
            scores_sum += scores * credit
            point_sum += rank.value * credit
    print_table(['Subject', 'Credit', 'Scores', 'GPA', 'Point'], rows)
    print(f'Total credit: {credit_sum}')
    print(f'Weighted scores: {scores_sum / credit_sum:.2f}')
    print(f'GPA: {point_sum / credit_sum:.2f}')


def rename(original: str, new: str) -> None:
    '''
    To rename the semester.
    '''

    path = os.path.join('data', original)

    if not os.path.exists(path):
        print('The semester does not exist.')
        return

    new_path = os.path.join('data', new)

    if os.path.exists(new_path):
        print('The semester has already been created.')
        return

    os.rename(path, new_path)


def delete(name: str) -> None:
    '''
    To delete the semester.
    '''

    path = os.path.join('data', name)

    if not os.path.exists(path):
        print('The semester does not exist.')
        return

    os.rmdir(path)

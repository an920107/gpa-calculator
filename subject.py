import os
from gpa import to_gpa
from table import print_table

def create(semester_name: str, name: str, credit: int, scores: float) -> None:
    '''
    To create a subject with the given name, credit, and scores.
    '''

    path = os.path.join('data', semester_name)

    if not os.path.exists(path):
        print('The semester does not exist.')
        return
    
    path = os.path.join(path, name)

    if os.path.exists(path):
        print('The subject has already been created.')
        return

    with open(path, 'w') as file:
        file.writelines([str(credit) + "\n", str(scores)])


def print_subject(semester_name: str, name: str) -> None:
    '''
    To print the subject with the given name.
    '''

    path = os.path.join('data', semester_name)

    if not os.path.exists(path):
        print('The semester does not exist.')
        return
    
    path = os.path.join(path, name)

    if not os.path.exists(path):
        print('The subject does not exist.')
        return
    
    with open(path) as file:
        lines = file.readlines()
        credit = int(lines[0])
        scores = float(lines[1])
    gpa = to_gpa(scores)
    print_table(
        ['Subject', 'Credit', 'Scores', 'GPA', 'Point'],
        [[name, str(credit), str(scores), gpa.name, str(gpa.value)]]
    )


def edit(semester_name: str, name: str, credit: int, scores: float) -> None:
    '''
    To edit the subject with the given name, credit, and scores.
    '''

    path = os.path.join('data', semester_name)

    if not os.path.exists(path):
        print('The semester does not exist.')
        return
    
    path = os.path.join(path, name)

    if not os.path.exists(path):
        print('The subject does not exist.')
        return

    with open(path, 'w') as file:
        file.writelines([str(credit) + "\n", str(scores)])


def rename(semester_name: str, original: str, new: str) -> None:
    '''
    To rename the subject with the given name.
    '''

    path = os.path.join('data', semester_name)

    if not os.path.exists(path):
        print('The semester does not exist.')
        return
    
    original_path = os.path.join(path, original)

    if not os.path.exists(original_path):
        print('The subject does not exist.')
        return

    new_path = os.path.join(path, new)

    if os.path.exists(new_path):
        print('The subject has already been created.')
        return

    os.rename(original_path, new_path)


def move(original_semester_name: str, name: str, new_semester_name: str) -> None:
    '''
    To move the subject with the given name to the new semester.
    '''

    original_path = os.path.join('data', original_semester_name)

    if not os.path.exists(original_path):
        print('The semester does not exist.')
        return
    
    path = os.path.join(original_path, name)

    if not os.path.exists(path):
        print('The subject does not exist.')
        return

    new_path = os.path.join('data', new_semester_name)

    if not os.path.exists(new_path):
        print('The semester does not exist.')
        return
    
    new_path = os.path.join(new_path, name)

    if os.path.exists(new_path):
        print('The subject has already been created.')
        return

    os.rename(path, new_path)


def delete(semester_name: str, name: str) -> None:
    '''
    To delete the subject with the given name.
    '''

    path = os.path.join('data', semester_name)

    if not os.path.exists(path):
        print('The semester does not exist.')
        return
    
    path = os.path.join(path, name)

    if not os.path.exists(path):
        print('The subject does not exist.')
        return

    os.remove(path)

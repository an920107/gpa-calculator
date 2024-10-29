import os

def command() -> tuple[str]:
    '''
    To get the command from the user.
    '''

    print('\n>>> ', end='')
    line = input().strip()
    return tuple(line.split())

def main() -> None:
    '''
    The entry point of this tool.
    '''

    os.makedirs('data', exist_ok=True)
    handle_empty()
    while True:
        cmd = command()
        if len(cmd) == 0:
            handle_empty()
        elif cmd[0] == 'sm':
            handle_semester(*cmd[1:])
        elif cmd[0] == 'sj':
            handle_subject(*cmd[1:])
        elif cmd[0] == 'p':
            handle_print(*cmd[1:])
        elif cmd[0] == 'q' and len(cmd) == 1:
            handel_quit()
        elif cmd[0] == '?' and len(cmd) == 1:
            handle_help()
        else:
            handle_unknown()

        
def handle_empty() -> None:
    '''
    To handle the empty command.
    '''

    print('Enter "?" for help')


def handle_unknown() -> None:
    '''
    To handle the unknown command.
    '''

    print('Unknown command')
    handle_empty()


def handel_quit() -> None:
    '''
    To quit this tool.
    '''

    exit(0)


def handle_help() -> None:
    '''
    To print the help message.
    '''

    print('===== Semester =====')
    print('sm c <name>: create a new semester with the given name')
    print('sm p: list all the semesters')
    print('sm p <name>: print the semester and its subjects')
    print('sm r <original name> <new name>: rename the semester')
    print('sm d <name>: delete a semester with the given name')
    print()

    print('===== Subject =====')
    print('sj c <semester name> <subject name> <credit> <scores>: create and add a subject to a semester')
    print('sj p <semester name> <subject name>: print the subject with the given name')
    print('sj e <semester name> <subject name> <credit> <scores>: modify scores of the subject')
    print('sj r <semester name> <original name> <new name>: rename the subject')
    print('sj m <original semester name> <subject name> <new semester name>: move the subject to another semester')
    print('sj d <semester name> <subject name>: delete a subject with the given name')
    print()

    print('===== General =====')
    print('p: alias for "sm l"')
    print('p <semester name>: alias for "sm p"')
    print('p <semester name> <subject name>: alias for "sj p"')
    print('q: quit this tool')
    print('?: print this help message')


def handle_semester(*cmd) -> None:
    '''
    To handle the semester command.
    '''

    import semester
    if len(cmd) == 0:
        handle_unknown()
    elif cmd[0] == 'c' and len(cmd) == 2:
        semester.create(cmd[1])
    elif cmd[0] == 'p' and len(cmd) == 1:
        semester.list_all()
    elif cmd[0] == 'p' and len(cmd) == 2:
        semester.print_semester(cmd[1])
    elif cmd[0] == 'r' and len(cmd) == 3:
        semester.rename(cmd[1], cmd[2])
    elif cmd[0] == 'd' and len(cmd) == 2:
        semester.delete(cmd[1])
    else:
        handle_unknown()


def handle_subject(*cmd) -> None:
    '''
    To handle the subject command.
    '''

    import subject
    if len(cmd) == 0:
        handle_unknown()
    elif cmd[0] == 'c' and len(cmd) == 5:
        if not cmd[3].isdecimal():
            print('The credit must be an integer')
            return
        try:
            float(cmd[4])
        except ValueError:
            print('The scores must be a number')
            return
        subject.create(cmd[1], cmd[2], int(cmd[3]), float(cmd[4]))
    elif cmd[0] == 'p' and len(cmd) == 3:
        subject.print_subject(cmd[1], cmd[2])
    elif cmd[0] == 'e' and len(cmd) == 5:
        if not cmd[3].isdecimal():
            print('The credit must be an integer')
            return
        try:
            float(cmd[4])
        except ValueError:
            print('The scores must be a number')
            return
        subject.edit(cmd[1], cmd[2], int(cmd[3]), float(cmd[4]))
    elif cmd[0] == 'r' and len(cmd) == 4:
        subject.rename(cmd[1], cmd[2], cmd[3])
    elif cmd[0] == 'm' and len(cmd) == 4:
        subject.move(cmd[1], cmd[2], cmd[3])
    elif cmd[0] == 'd' and len(cmd) == 3:
        subject.delete(cmd[1], cmd[2])
    else:
        handle_unknown()


def handle_print(*cmd) -> None:
    '''
    To handle the print command.
    '''

    import semester, subject
    if len(cmd) == 0:
        semester.list_all()
    elif len(cmd) == 1:
        semester.print_semester(cmd[0])
    elif len(cmd) == 2:
        subject.print_subject(*cmd)


if __name__ == '__main__':
    print('Welcome to GPA Calculator')
    try:
        main()

    # Catch Ctrl+C and Ctrl+D
    except KeyboardInterrupt:
        pass
    except EOFError:
        pass

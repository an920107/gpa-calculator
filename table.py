def print_table(title: list[str], rows: list[list[str]]) -> None:
    '''
    To print a table with the given title and rows.
    '''

    max_length = [max(len(str(cell)) for cell in col) for col in zip(*[title, *rows])]

    print('┌' + '┬'.join('-' * length for length in max_length) + '┐')
    print('|' + '|'.join([f'{cell:<{max_length[i]}}' for i, cell in enumerate(title)]) + '|')
    print('├' + '┼'.join('-' * length for length in max_length) + '┤')
    for row in rows:
        print('|' + '|'.join([f'{cell:<{max_length[i]}}' for i, cell in enumerate(row)]) + '|')
    print('└' + '┴'.join('-' * length for length in max_length) + '┘')

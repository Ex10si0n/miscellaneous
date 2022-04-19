import csv

filename = 'example.csv'

def print_board(data):
    for i in range(9):
        for j in range(9):
            if data[i][j] == '':
                print('.', end = ' ')
            else:
                print(data[i][j], end = ' ')
        print()


def check_region(data, i, j):
    if data[i][j] == '':
        return False
    for cor in range(9):
        if data[i][cor] == data[i][j] and cor != j:
            return False
        if data[cor][j] == data[i][j] and cor != i:
            return False
    i_start = i // 3 * 3
    j_start = j // 3 * 3
    i_end = i_start + 2
    j_end = j_start + 2
    for i_cor in range(i_start, i_end + 1):
        for j_cor in range(j_start, j_end + 1):
            if data[i_cor][j_cor] == data[i][j] and (i_cor != i or j_cor != j):
                return False
    return True

def dfs(data, i, j):
    if i == 9:
        return True
    if j == 9:
        return dfs(data, i + 1, 0)
    if data[i][j] != '':
        return dfs(data, i, j + 1)
    for num in range(1, 10):
        data[i][j] = str(num)
        if check_region(data, i, j):
            if dfs(data, i, j + 1):
                return True
    data[i][j] = ''
    return False

    


if __name__ == '__main__':
    with open(filename, 'r') as f:
        reader = csv.reader(f)
        data = list(reader)
        data[0][0] = ''
        print_board(data)
        dfs(data, 0, 0)
        print()
        print_board(data)




import os
from git import Repo  # pip install gitpython
from os import listdir

git_url = "https://github.com/meddlin/tiktok-recipes.git"
repo_dir = "./test-repo"


def get_next_letter(curr_idx):
    alpha = 'abcdefghijklmnopqrstuvwxyz'
    return list(alpha)[curr_idx]

def blank_shapes(row, col):
    blocking_rows = [4, 5, 6, 7]
    blocking_cols = [7, 8, 9, 10]
    if (row in blocking_rows) and (col in blocking_cols):
        return True
    else:
        return False


def matrix_print():
    for a in range(40):     # rows
        for b in range(80): # cols
            if ((a in [3, 4, 5, 6]) and (b in [4, 5, 6, 7])) or ((a in [3, 4, 5, 6]) and (b in [12, 13, 14, 15])):
                print(f' ', end=" ")
            else:
                print(f'x', end=" ")
        print(f'', end="\n")

def clone_repo(git_url, repo_dir):
    Repo.clone_from(git_url, repo_dir)

def print_a_file():
    files = []
    files = os.listdir('./test-repo')
    print(files)

    # printing a file
    with open('./test-repo/config.js') as f:
        s = f.read()
        squashed_text = "".join(s.split())
        print(squashed_text)
        print('Contents have been printed...')
        print('...')
        print('...')
        print('Now printing squashed text as a list')
        print( list(squashed_text) )

def main():
    # matrix_print()
    # clone_repo(git_url, repo_dir)
    print_a_file()
        

if (__name__ == "__main__"):
    main()
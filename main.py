import os
from git import Repo  # pip install gitpython

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

def main():    
    matrix_print()
        

if (__name__ == "__main__"):
    main()

# clone repo
# Repo.clone_from(git_url, repo_dir)
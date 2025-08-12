import readchar
import os
import math
from pathlib import Path

folder_path = Path('./.poshthemes')
filenames = [f.name for f in folder_path.iterdir() if f.is_file()]

COLOR_ITER = '\033[96m'
COLOR_TEXT = '\033[95m'
RESET = '\033[0m'

def theme_list(file_names: list[str], page: int = 0, page_size: int = 50) -> None:
    names = []
    for fn in file_names:
        p = fn.find(".omp.")
        if p != -1:
            names.append(fn[:p].capitalize())
        else:
            names.append(fn.capitalize())

    max_len = max(len(name) for name in names) + 15

    start = page * page_size
    end = start + page_size
    page_names = names[start:end]

    for i in range(0, len(page_names), 2):
        left = f"{COLOR_ITER}({start + i + 1}){RESET} {COLOR_TEXT}{page_names[i]}{RESET}".ljust(max_len + 8)
        right = ""
        if i + 1 < len(page_names):
            right = f"{COLOR_ITER}({start + i + 2}){RESET} {COLOR_TEXT}{page_names[i + 1]}{RESET}"
        print(left + right)

def main():
    page = 0
    while True:
        os.system('clear')
        theme_list(filenames, page)
        print("\nChoose your theme ('m' for more & 'q' for quit): ", end="")

        user_input = ""
        while True:
            ch = readchar.readkey()
            if ch == '\r' or ch == '\n':  # Enter pressed
                break
            elif ch == '\x7f' or ch == '\b':  # Backspace pressed
                if len(user_input) > 0:
                    user_input = user_input[:-1]
                    # Move cursor back, erase char, move cursor back again
                    print('\b \b', end='', flush=True)
            elif ch in ['m', 'q'] and len(user_input) == 0:
                user_input = ch
                print(ch)
                break
            elif ch.isdigit():
                user_input += ch
                print(ch, end='', flush=True)
            # Ignore other keys

        if user_input == 'm':
            max_page = math.ceil(len(filenames) / 50) - 1
            if page < max_page:
                page += 1
            else:
                print("\nNo more pages. Press Enter to continue...")
                input()
        elif user_input == 'q':
            print("\nExiting.")
            break
        elif user_input.isdigit():
            choice = int(user_input)
            if 1 <= choice <= len(filenames):
                print(f"\nYou chose theme number {choice}: {filenames[choice-1]}")
                break
            else:
                print("\nInvalid choice number. Press Enter to continue...")
                input()
        else:
            print(f"\nInvalid input: {user_input}. Press Enter to continue...")
            input()

main()

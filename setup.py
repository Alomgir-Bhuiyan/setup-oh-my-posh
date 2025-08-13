import readchar
import os
import math
from pathlib import Path
import shutil
import subprocess

folder_path = Path('./.poshthemes')
filenames = [f.name for f in folder_path.iterdir() if f.is_file()]

COLOR_ITER = '\033[96m'
COLOR_TEXT = '\033[95m'
RESET = '\033[0m'
COLOR_SUCCESS = '\033[92m'
COLOR_ERROR = '\033[91m'
COLOR_RESET = '\033[0m'

def logo():
    RESET = "\033[0m"
    CYAN = "\033[96m"
    PURPLE = "\033[95m"
    YELLOW = "\033[93m"
    print(f"{YELLOW}------===------===------===------===------{RESET}\n")
    print(f"{CYAN}"
          "  ____  _____ _____ _____   _   _ \n"
          " / ___|| ____|_   _| ____| | \\ | |\n"
          " \\___ \\|  _|   | | |  _|   |  \\| |\n"
          "  ___) | |___  | | | |___  | |\\  |\n"
          " |____/|_____| |_| |_____| |_| \\_|\n"
          f"{RESET}")
    print(f"\n{YELLOW}------===------===------===------===------{RESET}\n")
    author_line = "Author: Alomgir Bhuiyan"
    github_line = "GitHub: https://github.com/Alomgir-Bhuiyan"
    contact_line = "Contact: alomgirbhuiyan16@gmail.com"
    width = 50
    print(f"{PURPLE}{author_line.center(width)}{RESET}")
    print(f"{PURPLE}{github_line.center(width)}{RESET}")
    print(f"{PURPLE}{contact_line.center(width)}{RESET}\n")

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

def ensure_file_and_dir(path: str) -> None:
    path_obj = Path(path).expanduser()
    if not path_obj.parent.exists():
        path_obj.parent.mkdir(parents=True, exist_ok=True)
    if not path_obj.exists():
        path_obj.touch()

def setup_theme(theme_file: str) -> None:
    g_zshrc = f"""eval "$(oh-my-posh init zsh --config ~/.poshthemes/{theme_file})"
    """
    g_fish_conf = f"""
    oh-my-posh init fish --config ~/.poshthemes/{theme_file} | source
    if status is-interactive
    end
    """
    zshrc_path = os.path.expanduser("~/.zshrc")
    fish_conf_path = os.path.expanduser("~/.config/fish/config.fish")
    ensure_file_and_dir(zshrc_path)
    ensure_file_and_dir(fish_conf_path)
    with open(zshrc_path, 'w') as f:
        f.write(g_zshrc)
        print(f"\n{COLOR_SUCCESS}[SUCCESS]{COLOR_RESET} New .zshrc file added")
    with open(fish_conf_path, 'w') as f:
        f.write(g_fish_conf)
        print(f"{COLOR_SUCCESS}[SUCCESS]{COLOR_RESET} New fish config file added")
    print(f"\n{COLOR_SUCCESS}[SUCCESS]{COLOR_RESET} Theme file linked")

def add_theme():

    commands_with_msgs = [
        ("rm -rf $HOME/.poshthemes", "Removed old .poshthemes directory from home."),
        ("cp -rf .poshthemes $HOME/", "Copied new .poshthemes directory to home."),
        
    ]
    def run_cmd(cmd, msg):
        if os.getuid() != 0:
            cmd = "sudo " + cmd
        result = os.system(cmd)
        if result == 0:
            print(f"{COLOR_SUCCESS}[SUCCESS]{COLOR_RESET} {msg}")
        else:
            print(f"{COLOR_ERROR}[ERROR]{COLOR_RESET} Failed to execute: {cmd}")
    for cmd, msg in commands_with_msgs:
        run_cmd(cmd, msg)

def change_shell_to_fish():
    fish_path = shutil.which("fish")
    if not fish_path:
        print(f"{COLOR_ERROR}[ERROR]{COLOR_RESET} Fish shell not found. Please install fish first.")
        return
    if "com.termux" in os.environ.get("PREFIX", ""):
        rc_paths = [os.path.expanduser("~/.bashrc"), os.path.expanduser("~/.zshrc")]
        for rc in rc_paths:
            if os.path.exists(rc):
                with open(rc, "a") as f:
                    f.write(f"\nexec fish\n")
        print(f"{COLOR_SUCCESS}[SUCCESS]{COLOR_RESET} Termux detected. Added 'exec fish' to shell rc files.")
    else:
        try:
            os.system(f"chsh -s /bin/fish")
            print(f"{COLOR_SUCCESS}[SUCCESS]{COLOR_RESET} Shell changed to fish successfully.")
        except subprocess.CalledProcessError:
            print(f"{COLOR_ERROR}[ERROR]{COLOR_RESET} Could not change shell automatically. Please run: chsh -s /bin/fish")

        print(f"{COLOR_ERROR}Killing Shell Processes{COLOR_RESET}")
        os.system(f"killall -15 bash zsh fish")


def main():
    page = 0
    while True:
        os.system('clear')
        logo()
        theme_list(filenames, page)
        print("\nChoose your theme ('m' for more & 'q' for quit): ", end="")
        user_input = ""
        while True:
            ch = readchar.readkey()
            if ch == '\r' or ch == '\n':
                break
            elif ch == '\x7f' or ch == '\b':
                if len(user_input) > 0:
                    user_input = user_input[:-1]
                    print('\b \b', end='', flush=True)
            elif ch in ['m', 'q'] and len(user_input) == 0:
                user_input = ch
                print(ch)
                break
            elif ch.isdigit():
                user_input += ch
                print(ch, end='', flush=True)
        if user_input == 'm':
            max_page = math.ceil(len(filenames) / 50) - 1
            if page < max_page:
                page += 1
            else:
                page = 0
        elif user_input == 'q':
            print("\nExiting.")
            break
        elif user_input.isdigit():
            choice = int(user_input)
            if 1 <= choice <= len(filenames):
                setup_theme(filenames[choice-1])
                add_theme()
                change_shell_to_fish()
                break
            else:
                print("\nInvalid choice number. Press Enter to continue...")
                input()
        else:
            print(f"\nInvalid input: {user_input}. Press Enter to continue...")
            input()

main()

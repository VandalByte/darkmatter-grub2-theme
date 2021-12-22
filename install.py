#!/usr/bin/env python3

#   ,_   _   ,_  ,  ,    , , _  ___,___,_,,_       _,  ,_  ,  ,  __     ___, ,  _, , ,  _,
#   | \,'|\  |_) |_/    |\/|'|\' | ' | /_,|_)     / _  |_) |  | '|_)   ' | |_|,/_,|\/| /_,
#  _|_/  |-\'| \'| \    | `| |-\ |   |'\_'| \    '\_|`'| \'\__| _|_)     |'| |'\_ | `|'\_
# '      '  `'  `'  `   '  ` '  `'   '   `'  `     _|  '  `   `'         ' ' `   `'  `   `
#                                                 '
# Version: 1.3
#
# Written by Vandal (vandalsoul)
#
# Contributors:
#  - Janek (xeruf)
#  - LinuxHeki
#
# Github: https://github.com/vandalsoul/darkmatter-grub2-theme/


import subprocess
import os
import shutil
import re


def check_root() -> None:
    id = int(subprocess.check_output("id -u", shell=True).decode("utf-8"))
    if id != 0:
        print("(!) Run the script with 'sudo' privileges or as root user !!\n")
        exit()


def change_grub_theme(grub_theme_path: str) -> None:

    output = str(subprocess.check_output("cat /etc/*-release", shell=True).decode("utf-8"))
    id = re.search(".*[a-zA-Z]+=[a-zA-Z]+", output).group(0)
    distro = id.replace("ID=","").lower().strip()

    with open("/etc/default/grub", "r") as grub_file:
        data = grub_file.readlines()
        flag = False
        for i, line in enumerate(data):
            # fedora fix
            if (distro in ["fedora","redhat"]) and (line.startswith("GRUB_TERMINAL_OUTPUT")):
                data.pop(i)
                data.insert(i, f'#{line}\n')

            elif line.startswith("GRUB_THEME"):
                flag = True
                data.pop(i)
                data.insert(i, f'GRUB_THEME="{grub_theme_path}"\n')  # adding new line
				
        if not flag:
            data.append(f'GRUB_THEME="{grub_theme_path}"\n')

    with open("/etc/default/grub", "w") as grub_file:
        grub_file.writelines(data)

def prompt(choices) -> str:
    options = list(choices)
    while True:
        print(f"(#) Choose an option [{options[0]}-{options[-1]}] : ", end="")
        choice = input()
        if choice not in options:
            print(f"\nSelect one of the available options !!\n")
            continue
        return choice


def main():
    print(
        r"""
     ,_   _   ,_  ,  ,    , , _  ___,___,_,,_       _,  ,_  ,  ,  __     ___, ,  _, , ,  _,
     | \,'|\  |_) |_/    |\/|'|\' | ' | /_,|_)     / _  |_) |  | '|_)   ' | |_|,/_,|\/| /_,
    _|_/  |-\'| \'| \    | `| |-\ |   |'\_'| \    '\_|`'| \'\__| _|_)     |'| |'\_ | `|'\_
   '      '  `'  `'  `   '  ` '  `'   '   `'  `     _|  '  `   `'         ' ' `   `'  `   `
                                                   '
    Written by Vandal (vandalsoul)
    Github: https://github.com/vandalsoul/darkmatter-grub2-theme/                                                                 
    """
    )

    print("\n( DARK MATTER GRUB-THEME INSTALLER )\n")
    check_root()

    THEME = "dark-matter/"


    if os.path.exists("/boot/grub/"):

        GRUB_THEMES_DIR = "/boot/grub/themes/"
        GRUB_UPDATE_CMD = "grub-mkconfig -o /boot/grub/grub.cfg"

        if not os.path.exists(GRUB_THEMES_DIR):
            os.mkdir(GRUB_THEMES_DIR)

    elif os.path.exists("/boot/grub2/"):

        GRUB_THEMES_DIR = "/boot/grub2/themes/"
        GRUB_UPDATE_CMD = "grub2-mkconfig -o /boot/grub2/grub.cfg"

        if not os.path.exists(GRUB_THEMES_DIR):
            os.mkdir(GRUB_THEMES_DIR)

    else:
        print("\n(!) Couldn't find the GRUB directory. Exiting the script ...")
        exit()

    # theme styles
    styles = {
        "1": "Linux",
        "2": "Debian",
        "3": "Ubuntu",
        "4": "Manjaro",
        "5": "Arch",
        "6": "Windows-11",
        "7": "Linux-Mint",
        "8": "Void-Linux",
        "9": "Fedora",
        "10": "MX-Linux",
        "11": "Pop-OS",
        "12": "ArchStrike",
        "13": "BlackArch",
        "14": "EndeavourOS",
        "15": "Gentoo",
        "16": "Pentoo",
        "17": "Zorin-OS",
        "18": "Red-Hat",
        "19": "Kali-Linux",
        "20": "Parrot-OS",
    }

    print("(#) Choose your Theme-Style :\n")

    style_sheet_menu = f"""
        (1)  Linux           (10)  MX Linux        (19)  Kali Linux
        (2)  Debian          (11)  PopOS           (20)  Parrot OS
        (3)  Ubuntu          (12)  ArchStrike
        (4)  Manjaro         (13)  BlackArch
        (5)  Arch Linux      (14)  EndeavourOS
        (6)  Windows 11      (15)  Gentoo Linux
        (7)  Linux Mint      (16)  Pentoo Linux
        (8)  Void Linux      (17)  Zorin OS
        (9)  Fedora          (18)  Red Hat

    """
    print(style_sheet_menu)
    choice = prompt(styles.keys())

    THEME_DIR = f"{GRUB_THEMES_DIR}{THEME}"

    if os.path.exists(THEME_DIR):
        print("\n")
        ask = input("(?) Another version of this theme is already installed,\n    Do you wish to remove it and add the new one (y/n)? [default = n] : ")
        if ask.lower() != "y":
            print("\n(!) No changes were made. Exiting the script ...\n")
            exit()
        else:
            shutil.rmtree(THEME_DIR)
            print("\n($) Removed the previous version ...")

    print("\n($) Copying the theme directory ...")
    shutil.copytree(THEME, THEME_DIR)

    ICON_THEME = "color"
    ICONS_PATH = f"assets/icons/{ICON_THEME}/"
    shutil.copytree(ICONS_PATH, f"{THEME_DIR}/{ICON_THEME}")
    os.rename(f"{THEME_DIR}{ICON_THEME}/", f"{THEME_DIR}icons/")

    BACKGROUND_PATH = f"assets/backgrounds/{styles.get(choice).lower()}.png"
    shutil.copy(BACKGROUND_PATH, f"{THEME_DIR}")
    os.rename(f"{THEME_DIR}{styles.get(choice).lower()}.png", f"{THEME_DIR}background.png")

    PROGRESSBAR_PATH = f"assets/progressbar/{styles.get(choice).lower()}_pb.png"
    shutil.copy(PROGRESSBAR_PATH, f"{THEME_DIR}")
    os.rename(f"{THEME_DIR}{styles.get(choice).lower()}_pb.png", f"{THEME_DIR}progress_highlight_c.png")

    print("\n($) Editing the GRUB file ...")
    THEME_PATH = f"{THEME_DIR}theme.txt"
    change_grub_theme(THEME_PATH)

    print("\n($) Updating GRUB ...\n")
    subprocess.run(GRUB_UPDATE_CMD, shell=True)

    print("\n($) Dark Matter GRUB theme was successfully installed !!\n")
    exit()


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print("\n(!) An unexpected error occured while running the script. Installation was unsuccessful ...\n")
        print(f"(!) ERROR: {e}")
        exit()

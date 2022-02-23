#!/usr/bin/env python3

#   ,_   _   ,_  ,  ,    , , _  ___,___,_,,_       _,  ,_  ,  ,  __     ___, ,  _, , ,  _,
#   | \,'|\  |_) |_/    |\/|'|\' | ' | /_,|_)     / _  |_) |  | '|_)   ' | |_|,/_,|\/| /_,
#  _|_/  |-\'| \'| \    | `| |-\ |   |'\_'| \    '\_|`'| \'\__| _|_)     |'| |'\_ | `|'\_
# '      '  `'  `'  `   '  ` '  `'   '   `'  `     _|  '  `   `'         ' ' `   `'  `   `
#                                                 '
# Version: 1.5
#
# Written by Vandal (vandalsoul)
# Github: https://github.com/vandalsoul/darkmatter-grub2-theme/
#
# Contributors:
#  - Janek (xeruf)
#  - LinuxHeki
#  - Giannis Lagodimos (Giann1s)

# imports
import subprocess
import os
import shutil
import re
import sys

def check_root() -> None:
    id = int(subprocess.check_output("id -u", shell=True).decode("utf-8"))
    if id != 0:
        print("(!) Run the script with 'sudo' privileges or as root user !!\n")
        exit()


def check_distro():
    cwd_cont = os.listdir("/etc")
    release_file_path = '/etc/os-release' if 'os-release' in cwd_cont else ''
    if not release_file_path:
        for i in cwd_cont:
            if i.endswith("-release") and os.path.isfile(f"/etc/{i}"):
                release_file_path = f"/etc/{i}"
                break
    
    if not release_file_path:
        raise Exception("Release file not found")

    output = open(release_file_path, 'r').read()
    id = re.search(r"(\w*_ID=\w*)|(\w*ID=\w*)", output).group(0)
    distro = id.split("=")[-1].lower().strip()
    return distro


def change_grub_theme(grub_theme_path):
    distro = check_distro()

    with open("/etc/default/grub", "r") as grub_file:
        data = grub_file.readlines()
        flag = False
        for i, line in enumerate(data):

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

def invalid_arguments(arg_list, style_list):

    if len(arg_list) > 3:       # more than 3 arguments
        return True

    elif len(arg_list) == 3:    # 3 arguments
        if "-y" in arg_list:
            pass
        else:
            return True
        for style in style_list:
            if style in arg_list:
                return False
        else:
            return True
    
    elif len(arg_list) == 2:    # 2 arguments
        if "-y" in arg_list:
            return False
        else:
            for style in style_list:
                if style in arg_list:
                    return False
            else:
                return True

    else:                       # 1 argument (only filename)
        return False

def main():
    print(
        r"""
     ,_   _   ,_  ,  ,    , , _  ___,___,_,,_       _,  ,_  ,  ,  __     ___, ,  _, , ,  _,
     | \,'|\  |_) |_/    |\/|'|\' | ' | /_,|_)     / _  |_) |  | '|_)   ' | |_|,/_,|\/| /_,
    _|_/  |-\'| \'| \    | `| |-\ |   |'\_'| \    '\_|`'| \'\__| _|_)     |'| |'\_ | `|'\_
   '      '  `'  `'  `   '  ` '  `'   '   `'  `     _|  '  `   `'         ' ' `   `'  `   `
                                                   '
    Written by Vandal (vandalsoul)                                                            
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
        "21": "Garuda",
        "22": "Ubuntu-mate",
        "23": "Elementary",
        "24": "openSUSE",
        "25": "Deepin",
        "26": "FreeBSD",
        "27": "CentOS",
        "28": "KDE-neon",
        "29": "Solus",
	"30": "Kubuntu",
	"31": "Devuan",
	"32": "Linux-Lite",
        "33": "Lubuntu",
	"34": "Slackware",
	"35": "Sparky",
    }

    arg_list = []
    for arg in sys.argv:
        arg_list.append(arg.lower())

    style_list = list(styles.values())
    for i in range(len(style_list)):
        style_list.append(style_list[0].lower())
        style_list.pop(0)

    if invalid_arguments(arg_list, style_list):
        raise Exception("Invalid Arguments!")

    for style_number in range(1, len(styles) + 1):
        if styles[str(style_number)].lower() in arg_list:
            choice = str(style_number)
            break
    else:
        print("(#) Choose your Theme-Style :\n")
        tab_count = 3
        for id,key in enumerate(styles,1):
            if tab_count==0:
                print(end="\n")
                tab_count = 3
            if len(key) == 1:
                print(f"({id})   {styles[key]:<13}",end="")
                tab_count-=1
            else:
                print(f"({id})  {styles[key]:<13}",end="")
                tab_count-=1
        print()

        choice = prompt(styles.keys())

    THEME_DIR = f"{GRUB_THEMES_DIR}{THEME}"

    if os.path.exists(THEME_DIR):  # added due to shutil.copytree fail
        if "-y" in sys.argv:
            shutil.rmtree(THEME_DIR)
            print("\n($) Removed the previous version ...")
        else:
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

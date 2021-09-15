![logo](/media/logo.png)

![GitHub](https://img.shields.io/github/license/vandalsoul/dedsec-grub2-theme?style=for-the-badge)

This theme was created, inspired by the fictional hacker group **DedSec** from **Watch Dogs** video game developed by **Ubisoft**.

## 📙 Table of Contents
- [Installation](https://github.com/vandalsoul/darkmatter-grub2-theme#%EF%B8%8F-installation)
- [Donate](https://github.com/vandalsoul/darkmatter-grub2-theme#-donate)
- [Preview](https://github.com/vandalsoul/darkmatter-grub2-theme#-preview)
- [Fix-it Tips](https://github.com/vandalsoul/darkmatter-grub2-theme#-fix-it-tips)
- [License](https://github.com/vandalsoul/darkmatter-grub2-theme#-license)

## ⚙️ Installation

### ✅ Using Installation Script

#### 1️⃣ First clone the repository, then navigate into it.
```shell
git clone https://github.com/vandalsoul/darkmatter-grub2-theme.git
cd ddarkmatter-grub2-theme
```

#### 2️⃣ Run the `install.py`
```shell
sudo python3 install.py
```

### ✅ Manual Installation

#### 1️⃣ Download your favourite version of the theme from Pling

Extract it and navigate into the directory ( *Here I'm using debian version of my theme as an example* )
```sh
extract command here
navigate command
```
*The rest of the commands are the same for all versions of the theme*

#### 2️⃣ Copy the theme directory.
```shell
sudo cp -r dark-matter /boot/grub/themes/
```
#### 3️⃣ Make changes to the GRUB config file.

```shell
sudo nano /etc/default/grub
```
Find the line `GRUB_THEME=` then change it to `GRUB_THEME="/boot/grub/themes/dark-matter/theme.txt"`

Then save the file.

#### 4️⃣ Finally, update the grub.

- **Debian | Ubuntu | Arch**
```shell
sudo grub-mkconfig -o /boot/grub/grub.cfg
```
- **Fedora | Redhat**
```shell
sudo grub2-mkconfig -o /etc/grub2.cfg
```
Now the theme should be successfully installed, enjoy !!

## 💰 Donate
Alright COOL people 😎 visiting this page, if you like my work please consider donating 😄, it would really help me a lot guys, thanks 😇

<a href="https://www.buymeacoffee.com/vandalsoul" target="_blank"><img src="https://cdn.buymeacoffee.com/buttons/v2/default-yellow.png" alt="Buy Me A Coffee" style="height: 60px !important;width: 217px !important;" ></a>

## 📸 Preview
 
|  |  |
| :---: | :---: |
| <img src="https://raw.githubusercontent.com/AdisonCavani/distro-grub-themes/master/preview/Debian.png"/> | <img src="https://raw.githubusercontent.com/AdisonCavani/distro-grub-themes/master/preview/CentOS.png"/> |
| <img src="https://raw.githubusercontent.com/AdisonCavani/distro-grub-themes/master/preview/Linux%20Mint.png"/> | <img src="https://raw.githubusercontent.com/AdisonCavani/distro-grub-themes/master/preview/Artix%20Linux.png"/> |

## 💡 Fix-it Tips
*Click to view...*

<details>
  <summary><b>( Q ] GRUB theme doesn't show up after installing the theme?</b></summary>
  <br>
  
 *It is mainly because of your grub config file ( **located at /etc/default/grub** ).*
  
 *Default grub config will be different for every linux distro. So inorder for this to work you will have to make some tweaks in your grub config file.*

 *This is the [GRUB config](/media/mx-linux-grub-config-file.txt) file for MX Linux 19.4*

 **[ WARNING ] : This is only for referance and not for copy-pasting since it is a Debian-based distro, yours might be different and can mess up the boot if copy-pasted.**
  
</details>

## 📝 License
Made with 💖 and it's released under the **MIT** license.


![logo](/media/logo.png)

<p align="center">
  <b>Dark Matter is a dark polished GRUB theme collection for variety of Linux distributions.</b>
</p>

<p align="center">
  <a href="https://raw.githubusercontent.com/vandalsoul/darkmatter-grub2-theme/main/LICENSE"><img alt="undefined" src="https://img.shields.io/badge/License-GPL--3.0-blue?style=for-the-badge&logo=github">
  <a href="https://www.gnome-look.org/p/1603282"><img alt="undefined" src="https://img.shields.io/badge/Download-Here-green?style=for-the-badge&logo=github"></a>
</p>

#### 📢 What's Next?
**( Pentesting OS Edition ):** Kali Linux, Parrot OS, BlackArch etc...

## 📙 Table of Contents
- **[Installation](https://github.com/vandalsoul/darkmatter-grub2-theme#%EF%B8%8F-installation)**
- **[Donate](https://github.com/vandalsoul/darkmatter-grub2-theme#-donate)**
- **[Preview](https://github.com/vandalsoul/darkmatter-grub2-theme#-preview)**

## ⚙️ Installation

### ✅ Using Installation Script

#### 1️⃣ First clone the repository, then navigate into it.
```shell
git clone https://github.com/vandalsoul/darkmatter-grub2-theme.git
cd darkmatter-grub2-theme
```

#### 2️⃣ Run the `install.py`
```shell
sudo python3 install.py
```

### ✅ Manual Installation
*Click to view...*
<details>
 <summary><b>Debian 💢 Ubuntu 💢 Arch</b></summary>
 
  #### 1️⃣ Download your favourite version of the theme from [**Pling**](https://www.pling.com/p/1603282/).

  Now extract your downloaded .zip file.

  Either manually extract it or use the command below. ( *Here I'm using debian version of my theme as an example* )
  ```shell
  unzip dark-matter-debian.zip
  ```
  *The rest of the commands are the same for all theme styles.*

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
  ```shell
  sudo grub-mkconfig -o /boot/grub/grub.cfg
  ```
  Now the theme should be installed successfully, enjoy !!
</details>

<details>
 <summary><b>Fedora 💢 Redhat</b></summary>
 
  #### 1️⃣ Download your favourite version of the theme from [**Pling**](https://www.pling.com/p/1603282/).

  Now extract your downloaded .zip file.

  Either manually extract it or use the command below. ( *Here I'm using debian version of my theme as an example* )
  ```shell
  unzip dark-matter-debian.zip
  ```
  *The rest of the commands are the same for all theme styles.*

  #### 2️⃣ Copy the theme directory.
  ```shell
  sudo cp -r dark-matter /boot/grub2/themes/
  ```
  #### 3️⃣ Make changes to the GRUB config file.

  ```shell
  sudo nano /etc/default/grub
  ```
  Find the line `GRUB_THEME=` then change it to `GRUB_THEME="/boot/grub2/themes/dark-matter/theme.txt"`
 
  Change the line `GRUB_TERMINAL_OUTPUT=console` to this *(comment it out)* `#GRUB_TERMINAL_OUTPUT=console`

  Then save the file.

  #### 4️⃣ Finally, update the grub.
  ```shell
  sudo grub2-mkconfig -o /boot/grub2/grub.cfg
  ```
  Now restart your computer the grub theme should be installed successfully, enjoy !!
</details>

> **( NOTE )** *To request the theme for any specific linux distro of your liking open an issue with `feature request` label and let me know !!*

## 💰 Donate
**Hey guys 🙋‍♂️ If you like my projects feel free to buy me a coffee ☕ anytime to show your loving 💗 support !!**

<a href="https://www.buymeacoffee.com/vandalsoul" target="_blank"><img src="https://cdn.buymeacoffee.com/buttons/v2/default-yellow.png" alt="Buy Me A Coffee" style="height: 60px !important;width: 217px !important;" ></a>

## 📸 Preview
 
|  |  |
| :---: | :---: |
| ![Linux](/media/previews/preview-linux.png) | ![Debian](/media/previews/preview-debian.png) |
| ![Arch](/media/previews/preview-arch.png) | ![Ubuntu](/media/previews/preview-ubuntu.png) |
| ![Manjaro](/media/previews/preview-manjaro.png) | ![Windows-11](/media/previews/preview-windows-11.png) |
| ![Arch](/media/previews/preview-mx.png) | ![Ubuntu](/media/previews/preview-mint.png) |
| ![Arch](/media/previews/preview-fedora.png) | ![Ubuntu](/media/previews/preview-void.png) |
| ![Arch](/media/previews/preview-popos.png) |  |

## 📝 License
Made with 💖 and it's released under the [**GNU General Public License v3.0**](/LICENSE).


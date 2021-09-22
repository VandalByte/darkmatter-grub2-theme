![logo](/media/logo.png)

![GitHub](https://img.shields.io/github/license/vandalsoul/dedsec-grub2-theme?style=for-the-badge)

Dark Matter is a dark polished GRUB theme collection for variety of Linux distributions.

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
cd darkmatter-grub2-theme
```

#### 2️⃣ Run the `install.py`
```shell
sudo python3 install.py
```

### ✅ Manual Installation

#### 1️⃣ Download your favourite version of the theme from Pling.

Now extract your downloaded .zip file.

Either manually extract it or use the command below. ( *Here I'm using debian version of my theme as an example* )
```shell
unzip dark-matter-debian.zip
```
*The rest of the commands are the same for all versions of the theme.*

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

- **Debian ◻️ Ubuntu ◻️ Arch**
```shell
sudo grub-mkconfig -o /boot/grub/grub.cfg
```
- **Fedora ◻️ Redhat**
```shell
sudo grub2-mkconfig -o /etc/grub2.cfg
```
Now the theme should be installed successfully, enjoy !!

> **( NOTE )** *To request the theme for any specific linux distro of your liking open an issue with `feature request` label and let me know guys 😉*

## 💰 Donate
**Hey guys 🙋‍♂️ Feel free to buy me a coffee ☕ anytime to show your loving 💗 support !!**

<a href="https://www.buymeacoffee.com/vandalsoul" target="_blank"><img src="https://cdn.buymeacoffee.com/buttons/v2/default-yellow.png" alt="Buy Me A Coffee" style="height: 60px !important;width: 217px !important;" ></a>

## 📸 Preview
 
|  |  |
| :---: | :---: |
| ![Linux](/media/previews/preview-linux.png) | ![Debian](/media/previews/preview-debian.png) |
| ![Arch](/media/previews/preview-arch.png) | ![Ubuntu](/media/previews/preview-ubuntu.png) |
| ![Manjaro](/media/previews/preview-manjaro.png) | ![Windows](/media/previews/preview-windows.png) |

## 💡 Fix-it Tips
*Click to view...*

<details>
  <summary><b>(❔) GRUB theme doesn't show up after installing the theme?</b></summary>
  <br>
  
 *It is mainly because of your grub config file ( **located at /etc/default/grub** ).*
  
 *Default grub config will be different for every linux distro. So inorder for this to work you will have to make some tweaks in your grub config file.*

 *This is the [GRUB config](/media/mx-linux-grub-config-file.txt) file for MX Linux 19.4*

 **[ WARNING ❌ ] : This is only for referance and not for copy-pasting since it is a Debian-based distro, yours might be different and can mess up the boot.**
  
</details>

## 📝 License
Made with 💖 and it's released under the [**MIT** License](/LICENSE).


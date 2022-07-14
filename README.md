<p align="center">
  <img width=90% src="https://raw.githubusercontent.com/VandalByte/darkmatter-grub2-theme/update-2.0/media/banner.png" alt="banner" />
</p>

<p align="center">
  <a href="https://raw.githubusercontent.com/VandalByte/darkmatter-grub2-theme/main/LICENSE">
    <img src="https://img.shields.io/badge/License%20GPL--3.0-008a8a?style=for-the-badge&logo=github&logoColor=000000" alt="license" />
  </a>
  <a href="https://www.pling.com/p/1603282">
    <img src="https://img.shields.io/badge/Download-green?style=for-the-badge&logo=github&logoColor=000000" alt="license" />
  </a>
  <a href="https://www.pling.com/p/1603282">
    <img src="https://img.shields.io/badge/Version--2.0-ff173f?style=for-the-badge&logo=github&logoColor=000000" alt="version" />
  </a>
</p>

### ✔️ Installation

```shell
git clone --depth 1 https://github.com/VandalByte/darkmatter-grub2-theme.git && cd darkmatter-grub2-theme
sudo python3 darkmatter-theme.py --install
```

### ✔️ Manual Installation
*Click to view...*
<details>
 <summary><b>Debian ✨ Ubuntu ✨ Arch</b></summary>
 
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
 <summary><b>Fedora ✨ Redhat</b></summary>
 
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

> **To request a theme for a specific Linux distro, open an issue with the `feature request` label and let me know**

### ❌ Uninstallation
```shell
sudo python3 darkmatter-theme.py --uninstall
```
**With a little effort the theme's text colours, progress bar colours, progress bar text, and so on can all be customised in `theme.txt` to your liking 💕**
<p align="center">
  <b>Please consider 🤗 giving this project a star ⭐ if you liked it</b>
</p>

<p align="center">
  <b>Follow me on 💬 <a href="https://github.com/VandalByte">Github</a> or 💬 <a href="https://twitter.com/VandalByte">Twitter</a>  to stay up to date on all future updates ...</b>
</p>

  
## 📸 Preview

<p align="center">
  <img width="48%" src="https://raw.githubusercontent.com/VandalByte/darkmatter-grub2-theme/main/media/previews/preview-artix.png" />
  <img width="48%" src="https://raw.githubusercontent.com/VandalByte/darkmatter-grub2-theme/main/media/previews/preview-lubuntu.png" />
  <img width="48%" src="https://raw.githubusercontent.com/VandalByte/darkmatter-grub2-theme/main/media/previews/preview-sparky.png" />
  <img width="48%" src="https://raw.githubusercontent.com/VandalByte/darkmatter-grub2-theme/main/media/previews/preview-linuxlite.png" />
  <img width="48%" src="https://raw.githubusercontent.com/VandalByte/darkmatter-grub2-theme/main/media/previews/preview-slackware.png" />
  <img width="48%" src="https://raw.githubusercontent.com/VandalByte/darkmatter-grub2-theme/main/media/previews/preview-kubuntu.png" />
  <img width="48%" src="https://raw.githubusercontent.com/VandalByte/darkmatter-grub2-theme/main/media/previews/preview-devuan.png" />
  <img width="48%" src="https://raw.githubusercontent.com/VandalByte/darkmatter-grub2-theme/main/media/previews/preview-elementary.png" />
  <img width="48%" src="https://raw.githubusercontent.com/VandalByte/darkmatter-grub2-theme/main/media/previews/preview-openbsd.png" />
  <img width="48%" src="https://raw.githubusercontent.com/VandalByte/darkmatter-grub2-theme/main/media/previews/preview-deepin.png" />
  <img width="48%" src="https://raw.githubusercontent.com/VandalByte/darkmatter-grub2-theme/main/media/previews/preview-opensuse.png" />
  <img width="48%" src="https://raw.githubusercontent.com/VandalByte/darkmatter-grub2-theme/main/media/previews/preview-kdeneon.png" />
  <img width="48%" src="https://raw.githubusercontent.com/VandalByte/darkmatter-grub2-theme/main/media/previews/preview-garuda.png" />
  <img width="48%" src="https://raw.githubusercontent.com/VandalByte/darkmatter-grub2-theme/main/media/previews/preview-ubuntumate.png" />
  <img width="48%" src="https://raw.githubusercontent.com/VandalByte/darkmatter-grub2-theme/main/media/previews/preview-centos.png" />
  <img width="48%" src="https://raw.githubusercontent.com/VandalByte/darkmatter-grub2-theme/main/media/previews/preview-solus.png" />
  <img width="48%" src="https://raw.githubusercontent.com/VandalByte/darkmatter-grub2-theme/main/media/previews/preview-endeavour.png" />
  <img width="48%" src="https://raw.githubusercontent.com/VandalByte/darkmatter-grub2-theme/main/media/previews/preview-zorin.png" />
  <img width="48%" src="https://raw.githubusercontent.com/VandalByte/darkmatter-grub2-theme/main/media/previews/preview-archstrike.png" />
  <img width="48%" src="https://raw.githubusercontent.com/VandalByte/darkmatter-grub2-theme/main/media/previews/preview-kali.png" />
  <img width="48%" src="https://raw.githubusercontent.com/VandalByte/darkmatter-grub2-theme/main/media/previews/preview-parrot.png" />
  <img width="48%" src="https://raw.githubusercontent.com/VandalByte/darkmatter-grub2-theme/main/media/previews/preview-redhat.png" />
  <img width="48%" src="https://raw.githubusercontent.com/VandalByte/darkmatter-grub2-theme/main/media/previews/preview-blackarch.png" />
  <img width="48%" src="https://raw.githubusercontent.com/VandalByte/darkmatter-grub2-theme/main/media/previews/preview-gentoo.png" />
  <img width="48%" src="https://raw.githubusercontent.com/VandalByte/darkmatter-grub2-theme/main/media/previews/preview-pentoo.png" />
  <img width="48%" src="https://raw.githubusercontent.com/VandalByte/darkmatter-grub2-theme/main/media/previews/preview-linux.png" />
  <img width="48%" src="https://raw.githubusercontent.com/VandalByte/darkmatter-grub2-theme/main/media/previews/preview-debian.png" />
  <img width="48%" src="https://raw.githubusercontent.com/VandalByte/darkmatter-grub2-theme/main/media/previews/preview-arch.png" />
  <img width="48%" src="https://raw.githubusercontent.com/VandalByte/darkmatter-grub2-theme/main/media/previews/preview-ubuntu.png" />
  <img width="48%" src="https://raw.githubusercontent.com/VandalByte/darkmatter-grub2-theme/main/media/previews/preview-manjaro.png" />
  <img width="48%" src="https://raw.githubusercontent.com/VandalByte/darkmatter-grub2-theme/main/media/previews/preview-windows-11.png" />
  <img width="48%" src="https://raw.githubusercontent.com/VandalByte/darkmatter-grub2-theme/main/media/previews/preview-mx.png" />
  <img width="48%" src="https://raw.githubusercontent.com/VandalByte/darkmatter-grub2-theme/main/media/previews/preview-mint.png" />
  <img width="48%" src="https://raw.githubusercontent.com/VandalByte/darkmatter-grub2-theme/main/media/previews/preview-void.png" />
  <img width="48%" src="https://raw.githubusercontent.com/VandalByte/darkmatter-grub2-theme/main/media/previews/preview-fedora.png" />
  <img width="48%" src="https://raw.githubusercontent.com/VandalByte/darkmatter-grub2-theme/main/media/previews/preview-popos.png" />
</p>

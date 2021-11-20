![logo](/media/logo.png)

<p align="center">
  <a href="https://raw.githubusercontent.com/vandalsoul/darkmatter-grub2-theme/main/LICENSE">
    <img src="https://img.shields.io/badge/License-GPL--3.0-blue?style=for-the-badge&logo=github&logoColor=white" alt="license" />
  </a>
  <a href="https://www.pling.com/p/1603282">
    <img src="https://img.shields.io/badge/Download-here-green?style=for-the-badge&logo=github&logoColor=white" alt="license" />
  </a>
  <a href="https://www.buymeacoffee.com/vandalsoul">
    <img src="https://img.shields.io/badge/Donate-Buy%20Me%20A%20Coffee-d4b700?style=for-the-badge&logo=buymeacoffee&logoColor=d4b700" alt="license" />
  </a>
</p>

#### 📢 What's Next?
**( Pentesting OS Edition ):** Kali Linux, Parrot OS, BlackArch etc...

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

> **( NOTE )** *To request the theme for any specific linux distro of your liking open an issue with `feature request` label and let me know !!*

<p align="center">
  <b>Also, if you liked 💕 my project please give it a star ⭐ this will inspire me lot and show me that you guys actually like and support my work...</b>
  <b>So... ummm that's all 😅 have a awesome day 🤗</b>
</p>

## ❤️ Support

<p align="center">
  <a href="https://teamseas.org/">
    <img width="25%" src="https://assets01.teamassets.net/assets/images/teamseas-tm-logo.png" alt="teamseas" />
  </a>
  <br>
  <br>
  <b>Hey guys if you can, please support <a href="https://teamseas.org/">#TEAMSEAS<a></b> 
  <br>
  <b>😉 Let's be a part of saving our beautiful Oceans 🌊 and it's Wildlife 🐢🐬🐙 shall we...</b>
  <br><br>
  <b><i>“Alone we can do so little, together we can do so much.” - Helen Keller</i></b>
</p>

## 📸 Preview

<p align="center">
  <img width="48%" src="https://raw.githubusercontent.com/vandalsoul/darkmatter-grub2-theme/main/media/previews/preview-linux.png" />
  <img width="48%" src="https://raw.githubusercontent.com/vandalsoul/darkmatter-grub2-theme/main/media/previews/preview-debian.png" />
  <img width="48%" src="https://raw.githubusercontent.com/vandalsoul/darkmatter-grub2-theme/main/media/previews/preview-arch.png" />
  <img width="48%" src="https://raw.githubusercontent.com/vandalsoul/darkmatter-grub2-theme/main/media/previews/preview-ubuntu.png" />
  <img width="48%" src="https://raw.githubusercontent.com/vandalsoul/darkmatter-grub2-theme/main/media/previews/preview-manjaro.png" />
  <img width="48%" src="https://raw.githubusercontent.com/vandalsoul/darkmatter-grub2-theme/main/media/previews/preview-windows-11.png" />
  <img width="48%" src="https://raw.githubusercontent.com/vandalsoul/darkmatter-grub2-theme/main/media/previews/preview-mx.png" />
  <img width="48%" src="https://raw.githubusercontent.com/vandalsoul/darkmatter-grub2-theme/main/media/previews/preview-mint.png" />
  <img width="48%" src="https://raw.githubusercontent.com/vandalsoul/darkmatter-grub2-theme/main/media/previews/preview-void.png" />
  <img width="48%" src="https://raw.githubusercontent.com/vandalsoul/darkmatter-grub2-theme/main/media/previews/preview-fedora.png" />
  <img width="48%" src="https://raw.githubusercontent.com/vandalsoul/darkmatter-grub2-theme/main/media/previews/preview-popos.png" />
</p>

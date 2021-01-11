#!/bin/bash

declare -a programs=(

# terminal utils
  "rsync"
  "openssh"
  "nfs-utils"
  "usbutils"
  "cronie"
  "curl"
  "wget"
  "bash-completion"
  "vim"
  "nano"
  "git"
  "speedtest-cli"
  "nmap"
  "ettercap"
  "man-db"
  "ethtool"
  "htop"
  "tldr"
  "zsh"


# development utils
  "python"
  "python-pip"
  "python-pyaudio"
  "espeak"
  "pycharm-community-edition"
  "wireshark-qt"
  "gparted"
  "arduino"
  "arduino-avr-core"

# desktop utils
  "spectacle"
  "kate"
  "gwenview"
  "kinfocenter"
  "keepassxc"
  "vlc"
  "filelight"

# system utils
  "tlp"
  
# requirements for ventoy
  "exfat-utils"
)

for i in "${programs[@]}"
do
  pacman -S "$i" --noconfirm --needed
done

# configure newly installed services
usermod -aG wireshark jogi
usermod -aG uucp jogi
usermod -aG lock jogi
systemctl enable tlp

# python import for arduino
pip install pyserial

reboot

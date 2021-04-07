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
  "ethtool"
  "htop"
  "tldr"
  "zsh"
  "autofs"
  "stress"
  "ansible"

# development utils
  "python"
  "python-pip"
  "python-pyaudio"
  "espeak"
  "scapy"
  "pycharm-community-edition"
  "wireshark-qt"
  "gparted"
  "arduino"
  "arduino-avr-core"
  "kdevelop"
  "virtualbox"
  "openscad"

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
usermod -aG vboxusers jogi
systemctl enable tlp
systemctl enable autofs

# python import for arduino
pip install pyserial

# download firefox webdriver (geckodriver) for webscraping with selenium and python and install it in /usr/local/bin
wget "https://github.com/mozilla/geckodriver/releases/download/v0.29.0/geckodriver-v0.29.0-linux64.tar.gz" -P /usr/local/bin

reboot

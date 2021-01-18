#!/bin/bash

# yay installation
cd /opt
sudo git clone https://aur.archlinux.org/yay.git
cd /opt/yay
makepkg -si

declare -a programs=(

  "spotify"
)

for i in "${programs[@]}"
do
  yay -S "$i" --noconfirm --needed
done

reboot

#!/bin/bash

# update mirrorlist
sudo cp /etc/pacman.d/mirrorlist /etc/pacman.d/mirrorlist.bak
sudo pacman -S reflector --noconfirm --needed
sudo reflector --verbose --latest 10 --sort rate --save /etc/pacman.d/mirrorlist

# update system
sudo pacman -Syu
yay -Syu
omz update

# clean cached pacman and AUR files
sudo pacman -S pacman-contrib --noconfirm --needed
sudo paccache -r
sudo pacman -Rns $(pacman -Qtdq)
yay -Yc

# clean chached files and logs
sudo rm -rf .cache/*
sudo journalctl --vacuum-time=2weeks

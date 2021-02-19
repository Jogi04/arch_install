#!/bin/bash


declare -a programs=(

  "spotify"
  "android-studio"
  "downgrade"
)

for i in "${programs[@]}"
do
  sudo mkdir /opt/"$i"
  sudo chown jogi:jogi /opt/"$i"
  git clone https://aur.archlinux.org/"$i".git
  cd /opt/"$i"
  makepkg -si
done

echo y | pacman -S snapd
systemctl status snapd
snap install --devmode --beta anbox

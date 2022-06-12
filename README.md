# Dotfiles

These are my personal config files I use for my linux setup.

I documented most of what I've done for the future me and possibly other people which wants take a look! :)

I generally try to take a more general approach which works with different setups so if see something I could improve on I'd appreciate you to open a Issue or make a short merge request!

Running `setup.sh` will link the config files to the right places for programs to recognize them.
(does not override if the directories already exist)

![Desktop](./pictures/setup_background.png)
![Terminal](./pictures/terminal.png)
![dashboard](./pictures/dashboard.png)
Wallpaper source: 
https://wall.alphacoders.com/big.php?i=487879


dependencies to get the same setup:
- [bspwm](https://github.com/baskerville/bspwm)
- [sxhkd](https://github.com/baskerville/sxhkd)
- [feh](https://feh.finalrewind.org/)
- [eww](https://github.com/elkowar/eww)
- [python (3)](https://www.python.org/)
- [Fira Code Font](https://github.com/tonsky/FiraCode)

on arch linux you can install these programs with:

`pacman -S bspwm sxhkd feh python ttf-fira-code`

for eww check the according [installation guide](https://elkowar.github.io/eww/)

For any specific dependencies of a program check the according readme
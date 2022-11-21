# Dotfiles
These are the config files I use for my Linux setup.

I documented most of what I've done for the future me and possibly other people who want to take a look! :)

I generally try to take a more general approach that works with different setups so if see something I could improve on I'd appreciate you to open an issue or make a short merge request!

Running `place_configs.sh` will link the config files to the right places for programs to recognize them.
(does not override if the directories already exist)

![Action](./pictures/screenshot_action.jpg)
![Standard](./pictures/screenshot_standard.png)
<!-- ![dashboard](./pictures/dashboard.png) -->

Wallpaper credit: 
https://twitter.com/sh1m4da

dependencies to get the same setup:
- [bspwm](https://github.com/baskerville/bspwm)
- [sxhkd](https://github.com/baskerville/sxhkd)
- [feh](https://feh.finalrewind.org/)
- [eww](https://github.com/elkowar/eww)
- [python (3)](https://www.python.org/)
- [Fira Code Font](https://github.com/tonsky/FiraCode)
- playerctl
- fortune-mod
- libpulse
- wmctrl

on Arch Linux you can install these programs:

`pacman -S bspwm sxhkd feh python ttf-fira-code playerctl fortune-mod libpulse wmctrl`

For eww you can check out the according to [installation guide](https://elkowar.github.io/eww/)](https://elkowar.github.io/eww/)

For any specific dependencies of a program check the according readme 
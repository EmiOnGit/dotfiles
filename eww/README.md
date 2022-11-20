# eww: 

If you just copy my [eww](https://github.com/elkowar/eww) setup don't forget to run: 
- `scripts/helper/launch_bar` when you want the top bar 
- `scripts/helper/toggle_dashboard` whenever you want to toggle the dashboard (automatically used by the top bar) 

You need eww in your `PATH` to be able to use the scripts
I start my top bar with my window manager (as most likely you want too)
For an example of how to achieve that you might want to look in my [bspwm/bspwmrc](bspwm/bspwmrc).

## icons used:
from [papirus-icon-theme](https://github.com/PapirusDevelopmentTeam/papirus-icon-theme)
[luffy head](https://cipherpolfiles.tumblr.com/image/175211535566)

## Mails:
if you want the number of unread emails shown in your topbar you need to 
create a file in your [eww](https://github.com/elkowar/eww) folder.
dotfiles/eww/mail.json with content

`{"mail": "Your@mail.com", "password": "YourPassword", "server" : "YourServer ( 'imap.gmx.net' for gmx)" }`

Don't forget to activate external access to your emails in your settings!
I am aware that it isn't secure to store your credentials in a text file and so should you. 
If someone implements a more secure version, feel free to make a pr!


## System dependencies:
You need [eww](https://github.com/elkowar/eww) in your `PATH`

- playerctl 
- fortune
- libpulse
- wmctrl

for arch:
`pacman -S playerctl fortune-mod libpulse wmctrl`

## python packages: 
- imaplib
- glob2
- pathlib (part of std >= 3.4)
- python_weather
# eww: 
if you just copy my [eww](https://github.com/elkowar/eww) setup don't forget to run: 
- `scripts/helper/launch_bar` when you want the top bar 
- `scripts/helper/toggle_dashboard` whenever you want to toggle the dashboard (automatically used by the top bar) 
I start my bar with my window manager (as most likely you want to)
for an example how to do that you might want to look in my `bspwm/bspwmrc`.

## icons used:
from [papirus-icon-theme](https://github.com/PapirusDevelopmentTeam/papirus-icon-theme)
[luffy head](https://cipherpolfiles.tumblr.com/image/175211535566)

## mails:

if you the the amount of unread emails shown in your topbar you need to 
create a file in your `eww` folder.
dotfiles/eww/mail.json with content

`{"mail": "Your@mail.com", "password": "YourPassw","server" : "YourServer ( 'imap.gmx.net' for gmx)" }`

don't forget to activate external access to your emails in your settings!

## dependencies:
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
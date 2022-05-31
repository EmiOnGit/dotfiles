#!/bin/bash

SCRIPTPATH="$( cd -- "$(dirname "$0")" >/dev/null 2>&1 ; pwd -P )"
function to_config {
   ln -sf $SCRIPTPATH/$1 ~/.config/
}
function to_home {
   ln -sf $SCRIPTPATH/$1 ~/
}
to_config "sxhkd"
to_config "bspwm"
to_config "kitty"
to_home ".xinitrc"
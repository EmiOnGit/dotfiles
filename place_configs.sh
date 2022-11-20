#!/bin/bash
echo "This scripts tries to place the configs in the right folders"
echo "It doesn't override your existing config in case it already exists."
read -r -p "Are you sure you want to execute this script? [y/N] " response
response=${response,,}    # to lower case
if [[ ! "$response" =~ ^(yes|y)$ ]]
then 
   echo "exit script"
   exit
fi

SCRIPTPATH="$( cd -- "$(dirname "$0")" >/dev/null 2>&1 ; pwd -P )"

# assumes the input to be a directory
function to_config {
   if [ -d "$HOME/.config/$1" ]; then
      echo "Config for $1 already found. Skipping"
   else
      echo "Create config for $1"
      ln -sf $SCRIPTPATH/$1 ~/.config/
   fi
}
# assumes the input to be a file
function to_home {
   if [ -h "$HOME/$1" ]; then
      echo "Config file $1 already exists in home directory. Skipping"
   else 
      echo "Place file $1 in home directory"
      ln -sf $SCRIPTPATH/$1 ~/$1
   fi
}
to_config "sxhkd"
to_config "bspwm"
to_config "kitty"
to_config "eww"
to_config "picom"
to_config "nushell"
to_config "mangal"
to_home ".xinitrc"

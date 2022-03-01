#!/bin/sh
feh --bg-fill --randomize ~/Pictures/Backgrounds &
xrandr --output eDP-1 --mode 1600x900 &
xrandr --output HDMI-2 --auto --right-of eDP-1 &
picom -b --experimental-backends &

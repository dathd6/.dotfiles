#!/bin/sh
#source ~/.fehbg &
#xrandr --output eDP-1 --mode 1600x900 &
xrandr --output HDMI-2 --auto --right-of eDP-1 &
picom -b --experimental-backends &
xss-lock --transfer-sleep-lock -- i3lock --nofork &
#betterlockscreen -w dim &
feh --bg-fill --randomize ~/Pictures/wallpaper &

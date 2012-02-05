#!/bin/bash
resolutions=('1600x1200' '1440x900')
rm ~/.wallpaper/*.png
for resolution in ${resolutions[@]}; do
    xplanetFX --geometry $resolution
    xplanetFX --render-single ~/.wallpaper/$resolution.png
feh --bg-scale ~/.wallpaper/*

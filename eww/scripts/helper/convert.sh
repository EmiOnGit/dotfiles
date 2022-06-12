#!/bin/bash
# this scripts is just for my own purposes and very bad written
# it converts the svg's I use to png's I can use.
# (svg support in eww isn't great at times of writing this)

#### !TODO make it better :o
for filename in ../icons/svg/*.svg; do
    inkscape -w 128 -h 128 $filename -o ../icons/png_base/$(basename "$filename" .svg).png
done
sleep 2
for filename in ../icons/png_base/*.png; do
    echo $filename
    magick "$filename" -fuzz 35% -fill "#$1" -opaque black "../icons/$(basename "$filename" )"
done

# ----
for filename in ../icons/folder/svg/*.svg; do
    inkscape -w 128 -h 128 $filename -o ../icons/folder/$(basename "$filename" .svg).png
done
eww reload
#!/bin/bash

#### !TODO
for filename in ../icons/svg/*.svg; do
    inkscape -w 128 -h 128 $filename -o ../icons/png_base/$(basename "$filename" .svg).png
done
sleep 4
for filename in ../icons/png_base/*.png; do
    echo $filename
    magick "$filename" -fuzz 35% -fill "#$1" -opaque black "../icons/$(basename "$filename" )"
done

# ----
for filename in ../icons/folder/svg/*.svg; do
    inkscape -w 128 -h 128 $filename -o ../icons/folder/$(basename "$filename" .svg).png
done
eww reload
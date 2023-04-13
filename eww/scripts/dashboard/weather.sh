#!/usr/bin/bash
curl wttr.in/Marburg_tqp0.png > raw_weather.png
convert raw_weather.png -geometry +50+50 -composite weather.jpg


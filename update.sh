#!/bin/bash
echo "# Gallery" >README.md
echo "| Wallpaper | Filename |" >>README.md
echo "| :---: | :--- |" >>README.md

for f in *.{png,jpg,jpeg,webp}; do
  # Encode spaces for markdown
  encoded_f="${f// /%20}"
  echo "| <img src=\"$encoded_f\" width=\"200\"> | $f |" >>README.md
done

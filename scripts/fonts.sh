#!/bin/sh

if [ ! -d "~/.fonts" ]; then
    mkdir ~/.fonts
fi

# Install powerline-fonts
if [ -d "~/.fonts/powerline-fonts" ]; then
    rm -rf ~/.fonts/powerline-fonts
fi

git clone https://github.com/Lokaltog/powerline-fonts.git ~/.fonts

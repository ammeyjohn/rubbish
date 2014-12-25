#!/bin/sh

# Install vim vundle

## Remove the bundle folde if exsits
if [ -d "~/.vim/bundle" ]; then
    rm -rf "~/.vim/bundle"
fi

## clone git
git clone https://github.com/gmarik/Vundle.vim.git ~/.vim/bundle/Vundle.vim

## Install all vim plugins
vim +PluginInstall +qall

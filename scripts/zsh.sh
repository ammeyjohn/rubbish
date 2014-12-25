#!/bin/sh

# Install zsh
brew install zsh

# Use zsh as the default temrinal
chsh -s /bin/zsh

# Install oh-my-zsh
wget --no-check-certificate http://install.ohmyz.sh -O - | sh

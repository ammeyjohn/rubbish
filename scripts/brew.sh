#!/bin/sh

# Install brew
ruby -e "$(curl -fsSL https://raw.github.com/Homebrew/homebrew/go/install)"

## Check whether brew install successful
brew doctor

# Install brew tap homebrew-cask

brew tap phinze/cask
brew install brew-cask

## Check whether homebrew-cask install successful
brew cask

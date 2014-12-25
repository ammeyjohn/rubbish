#!/bin/sh

# Download get-pip.py
wget https://bootstrap.pypa.io/get-pip.py -o ~/Downloads/get-pip.py

# Install pip
sudo python ~/Downloads/get-pip.py

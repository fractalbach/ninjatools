#!/bin/bash

# Some variables that are likely to change often.
VERSION=1.10.1
OS=linux
ARCH=amd64

# Download the archived Go.
sudo curl https://dl.google.com/go/go$VERSION.$OS-$ARCH.tar.gz -o go$VERSION.$OS-$ARCH.tar.gz

# Unpack the Archive, placing it in /usr/local.
sudo tar -C /usr/local -xzf go$VERSION.$OS-$ARCH.tar.gz

# Add go to the path.
cat <<EOT >> ~/.profile
export PATH=$PATH:/usr/local/go/bin
EOT
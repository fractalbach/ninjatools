#!/bin/bash

# Some variables that are likely to change often.
VERSION=1.10.1
OS=linux
ARCH=amd64


# Check current version of Go, because it might already be installed.
# If the version is currently working correctly, don't bother downloading.
if [[ "$(go version)" = "go version go$VERSION $OS/$ARCH" ]]; then
    echo "You already have version $VERSION installed."
else
    DownloadAndUnpack
fi
AppendToPath



# FUNCTION DownloadAndUnpack will do the following actions:
# 1. Change directory to user's home.
# 2. Download the archived Go.
# 3. Unpack the Archive, placing it in /usr/local.
# 4. Remove the archive that was previously downloaded.
function DownloadAndUnpack {
    cd ~
    sudo curl https://dl.google.com/go/go$VERSION.$OS-$ARCH.tar.gz -o go$VERSION.$OS-$ARCH.tar.gz
    sudo tar -C /usr/local -xzf go$VERSION.$OS-$ARCH.tar.gz
    sudo rm go$VERSION.$OS-$ARCH.tar.gz
}



# FUNCTION AppendToPath will...
# 1. Append the GOPATH and the GOROOT to the user's bash PATH.
function AppendToPath {
    cat <<EOT >> ~/.profile
    export PATH=$PATH:/usr/local/go/bin:$HOME/go/bin
    EOT
}
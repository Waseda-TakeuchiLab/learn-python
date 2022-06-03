#! /bin/bash
set -e
apt update
apt install -y chromium fonts-ipafont fonts-ipaexfont
pip install -U pip
if [ -f "requirements.txt" ]; then
    pip install -r requirements.txt
fi

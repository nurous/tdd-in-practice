#!/bin/bash
set -e
set -u
DIR="$( cd "$( dirname "$0" )" && pwd )"
cd $DIR

if [ `which python` ]; then echo "`python --version 2>&1` installed"; else brew install -v2.7.2 python; fi
if [ `which pip` ]; then  echo $(echo `pip --version` | sed 's/\(.*\) from \(.*\)/\1 installed/g'); else easy_install pip; fi
if [ `which virtualenv` ]; then echo "virtualenv `virtualenv --version` installed"; else pip install virtualenv; fi
if [ ! -d 've' ]; then virtualenv ve; fi

set +u
source ve/bin/activate
pip install -r requirements.pip

if [ ! -f ve/bin/chromedriver ]; then
  echo 'Installing Chrome WebDriver'
  curl -O http://chromium.googlecode.com/files/chromedriver_mac_16.0.902.0.zip
  unzip chromedriver_mac_16.0.902.0.zip
  mv chromedriver ve/bin/
  rm chromedriver_mac_16.0.902.0.zip
fi
#!/bin/bash
if [ -z `which pip` ]
then
	echo "pip missing. Install pip for python packages."
fi

echo "installing dependencies"
sudo pip install docopt sh
echo "You are good to go!"
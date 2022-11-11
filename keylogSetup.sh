#! /bin/bash

echo -e "Process Starting\n"
apt-get install python3 -y &> /dev/null &
echo -e "Python3 installed."
apt-get install pip -y &> /dev/null &
echo -e "pip installed."
pip install pynput &> /dev/null &
echo -e "pynput installed."
pip install argparse &> /dev/null &
echo -e "argparse module installed."
pip install time &> /dev/null &
echo -e "time module installed.\n\nProcess Finished\n"

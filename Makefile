.PHONY: all run test docs install uninstall clean
#NOTE: PROJECT_DIR doesn't work w/ spaces in the path and MAKEFILE_LIST is a GNU specific variable
#PROJECT_DIR:=$(shell dirname $(realpath $(firstword $(MAKEFILE_LIST))))
#
#x = ${PROJECT_DIR}/binary_watch.service
#$(info [${x}])

#/lib/systemd/system/binary_watch.service:

#all: install docs test run
all: install docs run

install:
	sudo apt-get update
	sudo apt install git
	sudo apt install python3
	sudo apt install python3-pip
	sudo apt install pip
	sudo apt install sense-hat
	sudo apt install pandoc

docs:
	sudo mkdir -p /usr/local/share/man/man1
	sudo pandoc --standalone --to man binary_clock.md -o /usr/local/share/man/man1/binary_clock.1
	sudo mandb

run: binary_watch.py
	python binary_watch.py

#test: 

uninstall:
	sudo rm /lib/systemd/system/binary_watch.service

clean:
	sudo systemctl disable binary_watch.service
	sudo systemctl daemon-reload

#!/usr/bin/env python

import os, sys

if os.getuid() != 0:
	print ''
	sys.exit("[ERROR] Please run as 'ROOT' user")

conf = raw_input("Your are about to install 'sfinder', are you sure? [Yn] ")
cwd = os.getcwd()

if conf in ('Y', 'y', 'yes', 'Yes', ''):
	os.system('chown -R root:root {0}/sfinder/'.format(cwd))
	os.system('chmod 0755 {0}/sfinder/; chmod 0755 {0}/sfinder/src/'.format(cwd))
	os.system('chmod 0644 {0}/sfinder/src/data.py'.format(cwd))
	os.system('chmod 0644 {0}/sfinder/src/process.py'.format(cwd))
	os.system('chmod 0644 {0}/sfinder/src/progressbar.py'.format(cwd))
	os.system('chmod 0644 {0}/sfinder/src/data.py'.format(cwd))
	os.system('chmod 0655 {0}/sfinder/sfinder.py'.format(cwd))
	os.system('chmod 0644 {0}/sfinder/sfinder.1.gz'.format(cwd))
	os.system('cp {0}/sfinder/sfinder.1.gz /usr/share/man/man1/'.format(cwd))
	os.system('cp -r sfinder/ /opt/')
	os.system('ln -s /opt/sfinder/src/sfinder.py /usr/local/bin/sfinder')
	os.system('chmod 0655 /usr/local/bin/sfinder')
	os.system('rm -r {0}/sfinder/'.format(cwd))
	os.system('rm /opt/sfinder/sfinder.1.gz'.format(cwd))
		
	print "\n[INFO] Source located at: /opt/sfinder"
	print "[INFO] 'sfinder' manual page installed."
	print "[INFO] ==> You may now run and execute 'sfinder'"
else:
	sys.exit("'sfinder' installation cancelled.")

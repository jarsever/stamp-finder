#!/usr/bin/env python

import os, sys

if os.getuid() != 0:
	print ''
	sys.exit("[ERROR] Please run as 'ROOT' user")

conf = raw_input("Your are about to install 'sfinder', are you sure? [Yn] ")
cwd = os.getcwd()

if conf in ('Y', 'y', 'yes', 'Yes', ''):
	os.system('chown -R root:root {0}/sfinder/'.format(cwd))
	os.chmod('{0}/sfinder/'.format(cwd), 0755)
	os.chmod('{0}/sfinder/src/'.format(cwd), 0755)
	os.chmod('{0}/sfinder/src/data.py'.format(cwd), 0644)
	os.chmod('{0}/sfinder/src/process.py'.format(cwd), 0644)
	os.chmod('{0}/sfinder/src/progressbar.py'.format(cwd), 0644)
	os.chmod('{0}/sfinder/src/data.py'.format(cwd), 0644)
	os.chmod('{0}/sfinder/sfinder.py'.format(cwd), 0655)
	os.chmod('{0}/sfinder/sfinder.1.gz'.format(cwd), 0644)
	os.system('cp {0}/sfinder/sfinder.1.gz /usr/share/man/man1/'.format(cwd))
	os.system('cp -r sfinder/ /opt/')
	os.symlink('/opt/sfinder/sfinder.py', '/usr/local/bin/sfinder')
	os.rmdir('{0}/sfinder/'.format(cwd))
	os.remove('/opt/sfinder/sfinder.1.gz'.format(cwd))
		
	print "\n[INFO] Source located at: /opt/sfinder"
	print "[INFO] 'sfinder' manual page installed."
	print "[INFO] ==> You may now run and execute 'sfinder'"
else:
	sys.exit("'sfinder' installation cancelled.")

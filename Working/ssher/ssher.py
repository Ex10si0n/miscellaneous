import os

usr = input('Remote user name: ')
ip = input('Remote IP: ')
os.system('ssh %s@%s' % (usr, ip))

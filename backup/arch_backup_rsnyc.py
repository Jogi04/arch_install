#!/bin/python

import os
import time
import datetime
import configparser
from termcolor import cprint
from WoL import WoL


class ArchBackupRsync:
    def __init__(self, base_command, include_list, exclude_list, source, destination, username, server):
        self.base_command = base_command
        self.include_list = include_list
        self.exclude_list = exclude_list
        self.source = source
        self.destination = destination
        self.username = username
        self.server = server
        if not self.remote_host_up():
            # wake remote server and wait for 2 minutes while server is booting
            WoL()
            time.sleep(120)
        self.start_time = datetime.datetime.now()
        self.backup()
        self.print_runtime()
        self.shutdown_remote_server()

    def backup(self):
        """
        main function to backup specified directories, uses base_cmd string and appends the include/exclude options to
        the string
        """

        full_command = self.base_command
        for include in self.include_list:
            full_command += " " + "--include='" + str(include + "'")
        for exclude in self.exclude_list:
            full_command += " " + "--exclude='" + str(exclude) + "'"
        full_command += ' ' + str(self.source) + ' ' + self.username + '@' + self.server + ':' + str(self.destination)
        cprint(full_command, 'green')
        os.system(full_command)

    def remote_host_up(self):
        """
        verify that remote host is up
        """

        if os.system('ping -c 3 ' + self.server) is 0:
            return True
        else:
            return False

    def print_runtime(self):
        """
        prints how long the backup took
        """

        end_time = datetime.datetime.now()
        runtime = end_time - self.start_time
        cprint('Backup took ' + str(runtime), 'green')

    def shutdown_remote_server(self):
        os.system(f'ssh {self.username}@{self.server} "poweroff"')


# load personal information from config file, named config_rsync.ini
config = configparser.ConfigParser()
config.read('/home/jogi/programming/python/fun_projects/config_rsync.ini')
base_cmd = 'rsync -av --delete --stats'
excl_lst = config['options']['exclude_list'].split(' ')
incl_lst = config['options']['include_list'].split(' ')
backup_source = config['paths']['backup_source']
backup_destination = config['paths']['backup_destination']
rsync_server = config['paths']['nfs_server']
ssh_username = config['paths']['username']

if __name__ == '__main__':
    backup = ArchBackupRsync(base_cmd, incl_lst, excl_lst, backup_source, backup_destination, ssh_username, rsync_server)

import os
import datetime

import configparser


class Arch_Backup:
    def __init__(self, base_command, include_list, exclude_list, source, destination):
        self.base_command = base_command
        self.include_list = include_list
        self.exclude_list = exclude_list
        self.source = source
        self.destination = destination
        self.start_time = datetime.datetime.now()
        self.backup()
        self.print_runtime()

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
        full_command += ' ' + str(self.source) + ' ' + str(self.destination)
        print(full_command)
        os.system(full_command)

    def print_runtime(self):
        """
        prints how long the backup took
        """

        end_time = datetime.datetime.now()
        runtime = end_time - self.start_time
        print('Backup took ' + str(runtime))


# load personal information from config file, named config_nfs.ini
config = configparser.ConfigParser()
config.read('config_nfs.ini')
base_cmd = 'rsync -av --delete --stats'
excl_lst = config['options']['exclude_list'].split(' ')
incl_lst = config['options']['include_list'].split(' ')
backup_source = config['paths']['backup_source']
backup_destination = config['paths']['backup_destination']


if __name__ == '__main__':
    backup = Arch_Backup(base_cmd, incl_lst, excl_lst, backup_source, backup_destination)

import os
import termcolor
import configparser


class ArchRestore:
    def __init__(self, remote_user, remote_host, backup_directory, restore_destination_directory):
        self.remote_user = remote_user
        self.remote_host = remote_host
        self.backup_directory = backup_directory
        self.restore_destination_directory = restore_destination_directory
        self.restore()

    def restore(self):
        """
        main restore function which performs the restore process
        """
        command = f'rsync -av --stats {self.remote_user}@{self.remote_host}:{self.backup_directory} {self.restore_destination_directory}'
        termcolor.cprint(command, 'green')
        os.system(command)


if __name__ == '__main__':
    # load personal information from config file, named config_rsync_restore.ini
    config = configparser.ConfigParser()
    config.read('/home/jogi/programming/python/fun_projects/config_rsync_restore.ini')
    ssh_username = config['paths']['username']
    rsync_server = config['paths']['rsync_server']
    backup_dir = config['paths']['backup_dir']
    restore_destination = config['paths']['restore_destination']

    test = ArchRestore(remote_user=ssh_username, remote_host=rsync_server, backup_directory=backup_dir,
                       restore_destination_directory=restore_destination)

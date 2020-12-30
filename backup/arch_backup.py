import os
import subprocess
import datetime


class Arch_Backup:
    def __init__(self, base_command, include, exclude, source, destination, disk, mount_directory):
        self.base_command = base_command
        self.include = include
        self.exclude = exclude
        self.source = source
        self.destination = destination
        self.disk = disk
        self.mount_directory = mount_directory
        self.mount_backup_destination()
        self.start_time = datetime.datetime.now()
        self.backup()
        self.print_runtime()
        self.umount_backup_destination()

    def backup(self):
        full_command = self.base_command
        for include_option in self.include:
            full_command.append("--include='" + include_option)
        for exclude_option in self.exclude:
            full_command.append(" --exclude='" + exclude_option)
        full_command.append(self.source)
        full_command.append(self.destination)
        full_command_string = self.list_to_string(full_command)
        os.system(full_command_string)

    def list_to_string(self, lst):
        str1 = ' '
        return str1.join(lst)

    def mount_backup_destination(self):
        subprocess.run(['sudo', '-S', 'mount', str(self.disk), str(self.mount_directory)])
        print('Drive successfully mounted')

    def umount_backup_destination(self):
        subprocess.run(['sudo', '-S', 'umount', str(self.mount_directory)])
        print('Drive successfully unmounted')

    def print_runtime(self):
        end_time = datetime.datetime.now()
        runtime = end_time - self.start_time
        print('Backup took ' + str(runtime))


base_cmd = ['rsync', '-av', '--delete', '--stats']
include_list = [".bashrc'", ".config'", ".ssh'", ".kde4'", ".local'"]
exclude_list = ["/.*'", "Downloads'", "Android'", "Arduino'", "VMs'"]
backup_source = '/home/jogi/'
backup_destination = '/mnt/USB_backup/backup/'
destination_disk = '/dev/sda'
mount_dir = '/mnt/USB_backup/'


if __name__ == '__main__':
    backup = Arch_Backup(base_cmd, include_list, exclude_list, backup_source, backup_destination, destination_disk,
                         mount_dir)

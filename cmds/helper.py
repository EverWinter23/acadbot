'''
16th april 2018 monday
helper
'''
from tabulate import tabulate

class Helper:
    # def __init__(self, args):
    #     self.args = args
    
    def help_command(self):
        t = (['Configure', 'acadbot config --user [username]\nacadbot config --passwd'],
            ['Fetch', 'acadbot fetch time-table\nacadbot fetch attendance'],
            ['Help', 'acadbot --help [option]'],
            ['Version', 'acadbot --version'])
        print(tabulate(t))
        print('')

    def help_config(self):
        t = (['Usage:', 'acadbot config [--user <username>]'],
            ['Usage:', 'acadbot config [--passwd <return>]'])
        print(tabulate(t)) 
        print('')
        
    def help_username(self):
        t = (['Usage:', 'acadbot config [--user <username>]'],
            ['Username:', 'Numeric Roll Number'])
        print(tabulate(t))
        print('')
    
    def help_password(self):
        t = ([['Usage:', 'acadbot config [--passwd <return>]']])
        print(tabulate(t))
        print('')

    def help_fetch(self):
        t = (['Usage:', 'acadbot fetch [attendance]'],
            ['Usage:', 'acadbot fetch [time-table]'])
        print(tabulate(t))
        print('')

    def help_lists(self):
        #print('calling')
        t = (['[all]', 'Display command list'],
            ['[config]','Configure acadbot'],
            ['[fetch]', 'Fetch information from server'],
            ['[version]', 'Acadbot version'])
        print(tabulate(t))
        print('')

    def help_version(self):
        t = ([['Usage:', 'acadbot --version']])
        print(tabulate(t))

    def help_helper(self):
        t = ([['Usage:', 'acadbot --help [option]']])
        print(tabulate(t))

    def help_time_table(self):
        t = ([['Usage:', 'acadbot fetch time-table [batch] [day <optional>]']])
        print(tabulate(t))
        print('')

    def help_attendance(self):
        t = ([['Usage:', 'acadbot fetch attendance']])
        print(tabulate(t))
        print('')

    def help_cgpa(self):
        t = ([['Usage:', 'acadbot fetch cgpa']])
        print(tabulate(t))
        print('')
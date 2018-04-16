'''
acadbot v0.3
16th april 2018 monday
'''

import sys
from cmds.cmd_version import cmd_version
from cmds.cmd_username import cmd_username
from cmds.cmd_passwd import cmd_passwd
from custom_parser import ArgParser
from cmds.helper import Helper

# commands
CONFIG, FETCH, VERSION, HELP = 'config', 'fetch', '--version', '--help'
USERNAME, PASSWORD = '--user', '--passwd'
ATTENDANCE, TIME_TABLE = 'attendance', 'time-table'
ALL = 'all'
COMMANDS = [CONFIG, FETCH, VERSION, HELP]
CONFIG_ARGS = [USERNAME, PASSWORD]
FETCH_ARGS = [ATTENDANCE, TIME_TABLE]

# print help when required
helper = Helper()

def validate_arg(arg):
    if arg not in COMMANDS:
        print("acadbot: '" + arg + "' Command not found... ")
        print('acadbot: Please run from the following command list...')
        Helper().help_command()
        print('acadbot: Exiting...')
        exit()

def validate_config_arg(arg):
    if arg not in CONFIG_ARGS: 
        print("acadbot: '" + str(arg) +"' option not found...")
        Helper().help_config()
        print('acadbot: Exiting...')
        # error
        exit()

def validate_fetch_arg(arg):
    if arg not in FETCH_ARGS:
        print("acadbot: '" + str(arg) +"' option not found...")
        Helper().help_fetch()
        print('acadbot: Exiting...')
        exit()

def main(args):
    parser = ArgParser(args)

    validate_arg(parser.cur_arg)
    if parser.cur_arg == CONFIG:
        # config can have the following two args only
        #   1. --user 
        #   2. --passwd
        parser.get_next_arg()

        # if no argument print usage help
        validate_config_arg(parser.cur_arg)
        
        # usage: acadbot config --user '151301'
        if parser.cur_arg == USERNAME:
            parser.get_next_arg()
            if parser.cur_arg  is not None and parser.cur_arg.isnumeric():
                cmd_username(parser.cur_arg)
            else:
                print("acadbot: '" + str(parser.cur_arg) +"' is an invalid username...")
                helper.help_username()
                print('acadbot: Exiting...')
                exit()
        
        # usage: acadbot config --passwd<enter>    
        elif parser.cur_arg == PASSWORD:
            parser.get_next_arg()
            if parser.cur_arg is None:                
                cmd_passwd()
            else:
                print("acadbot: 'Do not enter password as an argument'")
                helper.help_password()
                print('acadbot: Exiting...')
                # error
                exit()
 
    # usage: acadbot fetch [attendance | time-table] 
    elif parser.cur_arg == FETCH:
        # fetch can have the following two args only
        #   1. attendance
        #   2. time-table
        parser.get_next_arg()
        # if no argument print usage help
        validate_fetch_arg(parser.cur_arg)

        # usage: acadbot fetch time_table batch [day]
        if parser.cur_arg == TIME_TABLE:
            parser.get_next_arg()
            batch = parser.cur_arg
            if batch is not None and batch and len(batch) == 2 and batch[0].isaplha() and batch[0].isnumeric():
                # if day has been passed as an arg
                parser.get_next_arg()
                if parser.cur_arg is not None and parser.cur_arg in days:
                    # TODO here
                    cmd_time_table(batch, parser.cur_arg)

                elif parser.cur_arg is None:
                    # TODO here
                    cmd_time_table(batch)
                else:
                    # usage
                    exit()                
            else:
                print("acadbot: '" + str(parser.cur_arg) +"' is an invalid option...")
                # TODO here
                helper.help_time_table()
                print('acadbot: Exiting...')
                exit()
        
        # usage: acadbot fetch attendance
        elif parser.cur_arg == ATTENDANCE:
            parser.get_next_arg()
            # TODO here
            cmd_attendance()        

    # usage: acadbot --version
    elif parser.cur_arg == VERSION:
        cmd_version()
    
    # usage: acadbot --help
    elif parser.cur_arg == HELP:
        parser.get_next_arg()
        if parser.cur_arg == CONFIG:
            helper.help_config()

        elif parser.cur_arg == FETCH:
            helper.help_fetch()

        elif parser.cur_arg == HELP:
            helper.help_helper()
            helper.help_lists()

        elif parser.cur_arg == ALL:
            helper.help_command()

        elif parser.cur_arg == VERSION:
            helper.help_version()

        else:
            helper.help_helper()
            helper.help_lists()
          


if __name__ == "__main__":
    user_args = sys.argv[1:]
    if len(user_args) == 0:
        helper.help_helper()
        helper.help_lists()
        exit()

    main(user_args)

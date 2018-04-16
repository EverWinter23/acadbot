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

def validate_arg(arg):
    if arg not in COMMANDS:
        print("acadbot: '" + arg + "' Command not found... ")
        print('acadbot: Please run from the following command list...')
        Helper().help_command()
        print('acadbot: Exiting...')
        exit()

def validate_config_arg(arg):
    if arg not in CONFIG_ARGS: 
        print("acadbot: config: '" + str(arg) +"' option not found...")
        Helper().help_config()
        print('acadbot: Exiting...')
        # error
        exit()

def main(args):
    parser = ArgParser(args)

    validate_arg(parser.cur_arg)
    # usage: acadbot config --user '151301'
    # usage: acadbot config --passwd<enter>
    if parser.cur_arg == CONFIG:
        # config can have the following two params only
        #   1. --user 
        #   2. --passwd
        parser.get_next_arg()
        validate_config_arg(parser.cur_arg)
        
        if parser.cur_arg == USERNAME:
            parser.get_next_arg()
            if parser.cur_arg  is not None and parser.cur_arg.isnumeric():
                cmd_username(parser.cur_arg)
            else:
                print("acadbot: config: user: '" + str(parser.cur_arg) +"' is an invalid username...")
                Helper().help_username()
                print('acadbot: Exiting...')
                exit()
                   
        elif parser.cur_arg == PASSWORD:
            parser.get_next_arg()
            if parser.cur_arg is None:                
                cmd_passwd()
            else:
                print("acadbot: config: passwd: 'Do not enter password as an argument'")
                Helper().help_password()
                print('acadbot: Exiting...')
                # error
                exit()
        else:
            # raise error
            exit()

    # usage: acadbot fetch [attendace | time-table] 
    elif parser.cur_arg == FETCH:
        raise NotImplementedError

    # usage: acadbot --version
    elif parser.cur_arg == VERSION:
        cmd_version()
    
    # usage: acadbot --help
    elif parser.cur_arg == HELP:
        parser.get_next_arg()
        if parser.cur_arg == CONFIG:
            Helper().help_config()
        elif parser.cur_arg == FETCH:
            Helper().help_fetch()
        elif parser.cur_arg == HELP:
            Helper().help_helper()
            Helper().help_lists()
        elif parser.cur_arg == ALL:
            Helper().help_command()
        elif parser.cur_arg == 'version':
            Helper().help_version()
        else:
            Helper().help_helper()
            Helper().help_lists()
          


if __name__ == "__main__":
    user_args = sys.argv[1:]
    if len(user_args) == 0:
        #cmd_version()
        #help_usage()
        # also print usage message
        exit()

    main(user_args)

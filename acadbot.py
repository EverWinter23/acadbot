'''
acadbot v0.3
16th april 2018 monday
'''

import sys
from cmds.cmd_version import cmd_version
from cmds.cmd_username import cmd_username
from cmds.cmd_passwd import cmd_passwd
from parser import ArgParser
VER = 'v0.3'
ACADBOT = "acadbot"

# commands
CONFIG, FETCH, VERSION, HELP = 'config', 'fetch', '--version', '--help'
USERNAME, PASSWORD = '--user', '--passwd'
ATTENDANCE, TIME_TABLE = 'attendance', 'time-table'
COMMANDS = [CONFIG, FETCH, VERSION, HELP]
CONFIG_ARGS = [USERNAME, PASSWORD]
FETCH_ARGS = [ATTENDANCE, TIME_TABLE]

def validate_arg(arg):
    if arg not in COMMANDS:
        # help_usage()
        exit()

def validate_config_arg(arg):
    if arg not in CONFIG_ARGS:
        # help config usage
        exit()

def main(args):
    parser = ArgParser(args)

    validate_arg(parser.cur_arg)
    # usage: acadbot config --user '151301'
    # usage: acadbot config --passwd<enter>
    if parser.cur_arg == CONFIG:
        # config can have the following two pars only
        #   1. user.rollnum
        #   2. user.password
        parser.get_next_arg()
        validate_config_arg(parser.cur_arg)
        
        if parser.cur_arg == USERNAME:
            parser.get_next_arg()
            if parser.cur_arg  is not None and parser.cur_arg.isnumeric():
                cmd_username(parser.cur_arg)
            else:
                # usage error
                exit()
                   
        elif parser.cur_arg == PASSWORD:
            parser.get_next_arg()
            if parser.cur_arg is None:                
                cmd_passwd()
            else:
                # usage error
                exit()
            # set passwd
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
        raise NotImplementedError   


if __name__ == "__main__":
    user_args = sys.argv[1:]
    if len(user_args) == 0:
        #cmd_version()
        #help_usage()
        # also print usage message
        exit()

    main(user_args)

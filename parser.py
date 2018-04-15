'''
16th april 2018 monday
argument parser
'''

class ArgParser:
    def __init__(self, args):
        self.args = args
        self.head = 0
        self.cur_arg = args[self.head]
        self.argc = len(args)
    
    def get_next_arg(self):
        self.head += 1
        self.cur_arg = None
        if self.head < len(self.args):
            self.cur_arg = self.args[self.head]

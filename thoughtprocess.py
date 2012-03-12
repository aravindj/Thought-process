#!/usr/bin/python

import sys, json, hashlib
from optparse import OptionParser, OptionGroup

class MaxCharsExceeded(Exception):
    pass

class MandatoryArgMissing(Exception):
    pass
class Thoughts:
    def __init__(self, category=None, filename=None, username=''):
        self.category = category or ''
        self.filename = filename or "thought.process"
        self.username = username or ''
        self.thoughts = []

    def add_thought(self, thought):
        try:
            if len(thought) > 140:
                raise MaxCharsExceeded("Not more than 140 characters are allowed! Yours contain %s chars"%(len(thought)))
            thought_dict = {'text' : thought, 'category' : self.category,
                            'username' : self.username, 'id' : hash_value(thought)}
            self.thoughts.append(thought_dict)
        except MaxCharsExceeded, e:
            print e.message
    def get_thoughts(self):
        thoughts = []
        try:
            with open(self.filename, 'r') as file:
                for each_thought in file:
                    thought = json.loads(each_thought)
                    if (self.category == '' or thought['category'] == self.category) and \
                        (self.username ==  '' or thought['username'] == self.username):
                        thoughts.append(thought)
        except IOError:
            pass
        return thoughts
    
    def save_thought(self):
        file = open(self.filename, 'a')
        for each_thought in self.thoughts:
            file.write(json.dumps(each_thought))
            file.write("\n")
        self.thoughts = []
        file.close()

def hash_value(text):
    return hashlib.md5(text).hexdigest()
def pretty_print_thoughts(thoughts):
    for thought in thoughts:
        tid = thought['id']
        txt = thought['text']
        uname = '' if thought['username'] is '' else '@%s' %(thought['username'])
        category = '' if thought['category'] is '' else '(c)%s' %(thought['category'])
        print "%s %s %s (id)%s\n"%(tid, txt, uname, category)
def command_line_args():
    usage = "%prog [-f FILE] [-c CATEGORY] [-u USERNAME] [-l] [TEXT]"
    parser = OptionParser(usage = usage)
    parser.add_option("-c", "--category", dest="category",
                    help="Cateogry of the thought")
    parser.add_option("-u", "--user", dest="username",
                    help="Username. See to that it contains no space")
    parser.add_option("-f", "--file", dest="filename", default = 'thought.process',
                    help="Target filename.")
    parser.add_option("-l", "--list", dest="list", default = False,
                    action = "store_true",
                    help="List the thoughts. If used with -c, -f or -u then appropriate thoughts alone are listed.")
    return parser
if __name__ == '__main__':
    parser = command_line_args()
    (options, args) = parser.parse_args()
    arg = ' '.join(args).strip()
    arguments = {
                'category' : options.category,
                'filename' : options.filename,
                'username' : options.username
    }
    thoughts = Thoughts(**arguments)
    if arg:
        thoughts.add_thought(arg)
        thoughts.save_thought()
    elif options.list:
        pretty_print_thoughts(thoughts.get_thoughts())
        
    else:
        print "Usage : %s [-f FILE] [-c CATEGORY] [-u USERNAME] [-l] [TEXT]"% (sys.argv[0])

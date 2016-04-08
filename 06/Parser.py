"""
Parser Module
"""

"""
Later on, move file open part to main.py ??

input: .asm file, output 'mnemonics  ...for translation with Code.py"
"""

import re
def initialize(asm_filename):
    return open(asm_filename, 'r')

def hasMoreCommands(numLines, currentLine):
    return currentLine < numLines

def advance(asm_file):
    return asm_file.readline()

def commandType(command):

    if re.match('\s*@', command, flags=0):
        return 'A_COMMAND'

    elif re.match('\s*[ADM]+\=|\s*[AMD01];', command, flags=0):
        return 'C_COMMAND'

    elif re.match('^\(', command, flags=0):
        return 'L_COMMAND'

    else:
        return

def symbol(command):
    #write symbol or decimal Xxx of the current command @Xxx or (Xxx)
    m = re.search('(?<=@)([a-zA-Z0-9_\.\$\:]+)', command)
    if m != None:
        return m.group(1)
    else:
        l = re.search('(?<=\()(.+)(?=\))', command)
        return l.group(1)

def comp(command):
    
    m = re.search('(?<=\=)([01ADM\!\+\-&\|]+)|([01AMD]{1}(?=\;))', command)
    
    if m.group(1) != None:
	return m.group(1)

    else:
	return m.group(2)
  
   
def dest(command):
    m = re.search('([AMD]+)(?=\=)', command)
    if m != None:
	return m.group(1)
    else:
	return 'nodest'

def jump(command):
    m = re.search('(?<=;)([JGTQLNMPE]{3})', command)
    if m != None:
        return m.group(1)
    else:
	return 'nojump'
    

   




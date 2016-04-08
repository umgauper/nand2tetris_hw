from sys import argv 

script, asm_filename = argv

import re
import Code
import Parser
import SymbolTable

asm_file = Parser.initialize(asm_filename)
m =  re.search('([a-z]+)(?=\.)(?i)', asm_filename)
out_filename = "%s.hack" % m.group(1)
output = open(out_filename, 'w')

numLines = 0
for l in asm_file:
    numLines += 1

currentLine = 0

asm_file = Parser.initialize(asm_filename)

print "Translating %s and writing to %s" % (asm_filename, out_filename)

# First pass:

ROMaddr = 0

while Parser.hasMoreCommands(numLines, currentLine):
    command = Parser.advance(asm_file)
    print command
    commandType = Parser.commandType(command)
    print commandType 
    if commandType == 'A_COMMAND' or commandType == 'C_COMMAND':
        ROMaddr += 1
        print ROMaddr
    elif commandType == 'L_COMMAND':
        label = Parser.symbol(command)
        SymbolTable.addEntry(label, ROMaddr)
    else:
        pass
    currentLine += 1


# Second pass
print "second pass"
currentLine = 0
asm_file = Parser.initialize(asm_filename)
decOfNewSymbol = 16

while Parser.hasMoreCommands(numLines, currentLine):

    command = Parser.advance(asm_file)
    commandType = Parser.commandType(command)
    
    if commandType == 'C_COMMAND':
        print command
	destmnemonic = Parser.dest(command)
	print destmnemonic
        destbin = Code.dest(destmnemonic)
	compmnemonic = Parser.comp(command) 
	print compmnemonic
	compbin = Code.comp(compmnemonic)
        jumpmnemonic = Parser.jump(command)
        jumpbin = Code.jump(jumpmnemonic)
        output.write("111%s%s%s\n" % (compbin, destbin, jumpbin))
    elif commandType == 'A_COMMAND':
#	print 'A_command, %s' % command
        # if @number ... output binary of that, else output binary of the corresponding value in the symbolTable
        symbol = Parser.symbol(command)
#	print 'Symbol %r' % symbol
#	print 'R0\r' == symbol
        if re.match('^([0-9]+)', symbol) != None:
#	    print 'found a number'
            binStr = format(int(symbol), 'b')
            
        else:
            if SymbolTable.contains(symbol):
#	        print "this is a symbol"
	        dec = SymbolTable.getAddress(symbol)
#		print dec
            else:
#		print "adding %s to table" % symbol
		SymbolTable.addEntry(symbol, decOfNewSymbol)
                dec = decOfNewSymbol
		decOfNewSymbol += 1

	    binStr = format(dec, 'b')

        output.write("%s\n" % binStr.zfill(16))

    else:
       pass

    currentLine += 1

print "Done"
output.close()    
asm_file.close()

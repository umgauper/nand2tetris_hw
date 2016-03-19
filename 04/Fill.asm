(LISTEN)
//**reset the variables**/
@16384  //A=16384
D=A		//D=16384
@j      //A=j
M=D    //Memory[j]=16384

@8191  //A=8191
D=A    //D=8191
@i     //A=i
M=D    //Memory[i]=8191
@i2    //A=i2
M=D    //Memory[i2]=8191

@24576 //A=24576
D=M    //
@WHITE
D;JEQ
@BLACK
D;JNE  


(BLACK)
@32767
D=A
@j
A=M      //A=Memory[j] = 16384
M=D      //Memory[16384] = 32767
D=D+1
@j
A=M  //A = Memory[j] = 16384
M=M+D //Memory[16384] = Memory[16384] + -32768 = -1

@j
M=M+1
@i
D=M-1
@LISTEN
D;JLE
@i
M=M-1
@BLACK
0;JMP

(WHITE)
@32767
D=A
@j
A=M  //A = Memory[j] = 16384
M=0  //Memory[16384] = 0

@j
M=M+1
@i2
D=M-1
@LISTEN
D;JLE
@i2
M=M-1
@WHITE
0;JMP

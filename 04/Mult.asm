@10
D=A
@w
M=D
@5
D=A
@y
M=D
@product
M=0

(LOOP)
@y
D=M
@END
D;JLE
@w
D=M
@product
M=M+D
@y
M=M-1
@LOOP
0;JMP

(END)
@END
0;JMP

//try to make it work with my own numbers w=10, y=5, store in product, y--
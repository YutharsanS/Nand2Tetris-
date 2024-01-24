// This file is part of www.nand2tetris.org
// and the book "The Elements of Computing Systems"
// by Nisan and Schocken, MIT Press.
// File name: projects/04/Mult.asm

@0  // RAM[2] = 0
D=A
@R2
M=D

@i // i = 0
M=D

(LOOP)
    @i
    D=M
    @R0
    D=M-D
    @END
    D;JEQ // If RAM[0] - i == 0; jump to the END

    @R1
    D=M
    @R2
    M=M+D // Adding the R1 to R2

    @i
    M=M+1 // i++

    @LOOP
    0;JMP

(END)
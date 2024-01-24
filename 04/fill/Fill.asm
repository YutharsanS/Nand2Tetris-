// This file is part of www.nand2tetris.org
// and the book "The Elements of Computing Systems"
// by Nisan and Schocken, MIT Press.
// File name: projects/04/Fill.asm

(START)
    @KBD
    D=M
    @BSCREEN
    D;JNE
    @WSCREEN
    D;JEQ

(BSCREEN)
    @R1
    M=-1
    @MAIN
    0; JMP

(WSCREEN)
    @R1
    M=0
    @MAIN
    0; JMP

(MAIN)
    @SCREEN
    D=A
    @8191
    D=A+D
    @i
    M=D

    (LOOP)
        @i
        D=M
        @SCREEN
        D=D-A

        @START
        D;JLT // Jump to BSCREEN if D <= 0 (i >= 8192)

        @R1
        D=M // Set pixel to color

        @i
        A=M
        M=D

        @i
        M=M-1 // i--


        @LOOP
        0;JMP

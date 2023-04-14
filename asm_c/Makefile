all: main

mult.o: mult.asm
	nasm -f elf32 -o mult.o mult.asm

main: main.c mult.o
	gcc -g -m32 -o main main.c mult.o

clean:
	rm -f main mult.o
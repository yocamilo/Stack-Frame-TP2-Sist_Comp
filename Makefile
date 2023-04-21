CC=gcc
ASM=nasm
CFLAGS= -g -m32 -o
AFLAGS= -g -f elf32 -o

all: mylib

mult.o: mult.asm
	$(ASM) $(AFLAGS) mult.o mult.asm

mylib: my_lib.c mult.o
	$(CC) $(CFLAGS) mylib my_lib.c mult.o

clean:
	rm mylib mult.o
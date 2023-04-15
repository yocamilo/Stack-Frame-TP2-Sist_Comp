CC=gcc
PY=python3
CFLAGS= -shared -o


all: mylib.so py_request.py

mylib.so: my_lib.c
	$(CC) $(CFLAGS) mylib.so my_lib.c

py_request.py:
	$(PY) py_request.py

clean:
	rm mylib.so
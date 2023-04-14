all: mylib.so py_request.py

mylib.so: my_lib.c
	gcc -shared -o mylib.so my_lib.c

py_request.py:
	python3 py_request.py

clean:
	rm mylib.so
# Stack Frame 

## TP2 Sistema de Computacion

### Instalacion y ejecucion programa

Primero se debe clonar el repositorio, abrir la terminal en la carpeta en donde esta el repositorio. Luego en la terminal ejecutar 

```bash
    make
    python3 py_request.py
```
A partir de aqui se ejecutara el programa, y se debe seguir las instrucciones para ingresar las inputs

En caso de obtener "fatal error: bits/libc-header-start.h: No such file or directory" se debe instalar los headers y librerias de 32 bits mediante

```
sudo apt install gcc-multilib
```
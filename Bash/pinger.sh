#!/bin/bash

if [ $# -eq 0 ]; then
echo "Añade la red/24 como argumento"
echo "Ejemplo de uso: ./pinger.sh 10.10.10.0"

else
argumento=$1
red=${argumento:0:-2}
for ip in `seq 1 254`; do
ping -c 1 $red.$ip | grep "64 bytes" | cut -d " " -f4 | tr -d ":" &
done
fi
#!/bin/bash

case "$#" in
    1)
        python3 genrated_ia.py "$1"
        ;;
    2)
        python3 genrated_ia.py "$1" --modo "$2"
        ;;
    *)
        echo "Error: Cada vez que se ejecute este script, debe proporcionar una o dos cadenas de texto."
        ;;
esac

# Divide el argumento en pregunta y modo
#IFS=';' read -r pregunta modo <<< "$1"
#!/bin/bash

function sgd(){

    current_dir = $(pwd)
    if [ "$#" -eq 0 ]; then
        python3 ./generated_comm.py "$current_dir"        return 1
    fi

    comentario=$1
    git add .
    git commit -m "$comentario"

    if [[ "$2" == "-p" ]]; then
        git push -u origin main
        echo "Push realizado"
    fi

}


#!/bin/bash

read -p "Enter the number of files to generate: " num_files

if ! [[ $num_files =~ ^[0-9]+$ ]]; then
    echo "Invalid input. Please enter a valid number."
    exit 1
fi

for ((i=1; i<=$num_files; i++)); do
    filename="section_$i.tex"
    touch "$filename"
    echo "File $filename created."
done

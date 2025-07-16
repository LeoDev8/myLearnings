#!/bin/bash

if [ -z "$1" ]; then
  echo "Error: Please input the commit message!"
  exit 1
fi

git add .;

echo "Commit Message: $1 . "

git commit -m "$1";

git push -u origin main;

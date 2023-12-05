#!/bin/sh

ans=$(zote $1.zote)


aoc submit $2 -d $1 -y 2015 $ans

echo "submitted $ans\n"

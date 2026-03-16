#!/bin/bash

for i in linux git jenkins docker kubernets terraform
do
	mkdir $i
	touch $i/Notes.md
done

#!/usr/bin/env bash

if [ ! -f commits.txt ]; then
    git log --oneline master | awk '{print $1}' | tail -r > commits.txt
fi

current=`git log --oneline | head -n1 | awk '{print $1}'`
next=`grep $current -A1 -B0 commits.txt | grep -v $current`

git checkout $next

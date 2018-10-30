#!/bin/bash
deductions=0
for ((i=0;i<=9;i++))
do
    echo "Test $i:"
    python3 preprocess.py < inTP$i > outTP$i
    diff -wB ansTP$i outTP$i
    if [ $? != 0 ]
    then
        deductions=$((deductions + 3))
    else
        echo "Correct"
    fi
done
echo "Final Score: $((30 - $deductions))/30"

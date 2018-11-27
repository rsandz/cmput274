#!/bin/bash
deductions=0
echo "Test 0:"
python3 preprocess.py keep-digits < inCLA0 > outCLA0
diff -wB ansCLA0 outCLA0
if [ $? != 0 ]
then
    deductions=$((deductions + 3))
else
    echo "Correct"
fi

echo "Test 1:"
python3 preprocess.py keep-stops < inCLA1 > outCLA1
diff -wB ansCLA1 outCLA1
if [ $? != 0 ]
then
    deductions=$((deductions + 3))
else
    echo "Correct"
fi

echo "Test 2:"
python3 preprocess.py keep-symbols < inCLA2 > outCLA2
diff -wB ansCLA2 outCLA2
if [ $? != 0 ]
then
    deductions=$((deductions + 3))
else
    echo "Correct"
fi

echo "Test 3:"
python3 preprocess.py keep-digits < inCLA3 > outCLA3
diff -wB ansCLA3 outCLA3
if [ $? != 0 ]
then
    deductions=$((deductions + 3))
else
    echo "Correct"
fi

echo "Test 4:"
python3 preprocess.py keep-stops < inCLA4 > outCLA4
diff -wB ansCLA4 outCLA4
if [ $? != 0 ]
then
    deductions=$((deductions + 3))
else
    echo "Correct"
fi

echo "Test 5:"
python3 preprocess.py keep-symbols < inCLA5 > outCLA5
diff -wB ansCLA5 outCLA5
if [ $? != 0 ]
then
    deductions=$((deductions + 3))
else
    echo "Correct"
fi

echo "Test 6:"
python3 preprocess.py keep-digits keep-stops < inCLA6 > outCLA6
diff -wB ansCLA6 outCLA6 >> /dev/null
if [ $? == 0 ]
then
    deductions=$((deductions + 3))
    echo "Failed: Should have caused an error"
else
    echo "Correct"
fi

echo "Test 7:"
python3 preprocess.py keep-digits keep-digits < inCLA7 > outCLA7
diff -wB ansCLA7 outCLA7 >> /dev/null
if [ $? == 0 ]
then
    deductions=$((deductions + 3))
    echo "Failed: Should have caused an error"
else
    echo "Correct"
fi

echo "Test 8:"
python3 preprocess.py not-a-real-argument < inCLA8 > outCLA8
diff -wB ansCLA8 outCLA8 >> /dev/null
if [ $? == 0 ]
then
    deductions=$((deductions + 3))
    echo "Failed: Should have caused an error"
else
    echo "Correct"
fi

echo "Test 9:"
python3 preprocess.py keep-symbols < inCLA9 > outCLA9
diff -wB ansCLA9 outCLA9
if [ $? != 0 ]
then
    deductions=$((deductions + 3))
else
    echo "Correct"
fi

echo "Final Score: $((30 - $deductions))/30"

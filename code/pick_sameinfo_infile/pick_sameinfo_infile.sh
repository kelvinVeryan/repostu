#!/bin/bash

file=$1
if [ ! -f $1 ];then
	echo "usage $0 filename"
	exit -1
fi

#log filename eq $1+.log
log_file=`pwd`/$1.log

#cat $file | while read line  # effect : block will setfree after command 'cat' run over.
#for line in `cat $file` # effect : { line1a line1b line2a line2b line2c line3}
#do
#	echo $line
#done

declare -a block
block=()
echo ${block[*]}
block_num=0

if [ -f $log_file ];then
	echo > $log_file
fi

# read file 
while read line
do
        block[num]=$line
#	echo $num
#       echo ${block[num]}
#       echo ${block[*]}
        let num++
done < $file

block_num=${#block[@]}
echo $block_num >> $log_file
echo "block_num: $block_num"

# rewrite info
#echo ${block[1]}
line=""
for ((i=0; i<block_num; i++))
do
        block_A=`echo ${block[i]} |awk '{print $1}'`
	echo $block_A
	let "j=i+1"
	echo "i= $i ; j= $j"
	for ((j; j<block_num; j++))
	do
		#echo "i= $i ; j= $j"
		block_B=`echo ${block[j]} |awk '{print $1}'`
		if [ ${block_A} == ${block_B} ];then
			echo "block[i]: ${block[i]}"
			echo "block[j]: ${block[j]}"
			echo
			echo "i = $i || ${block[i]}" >> $log_file
			echo "j = $j || ${block[j]}" >> $log_file
		fi
	done
done

#check result
for ((i=0; i<block_num; i++))
do
	info=""
	info=`grep " $i ||" $log_file`
	if [ -z "$info" ];then
		echo "$i not found in $log_file"
	fi
done

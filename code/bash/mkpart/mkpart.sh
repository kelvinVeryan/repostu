#!/bin/bash
# Author: 
# 
# Test Report: base DISTRIB_DESCRIPTION="Ubuntu 16.04.2 LTS" test ok.
# Note: use sudo; need input operate device id.

# savepart, system deviceinfo , prevent mishanding.
savepart=('/dev/sda' '/dev/sdb' '/dev/sdc')
shellusr=`whoami`

if [ "$shellusr" != "root" ];then
	echo "please use sudo run scripts "
	exit -1
fi

if [ -z "$1" ];then
	echo "please input device id. "
	exit -1
fi

opdevid="$1"

fdisk -l | grep "$opdevid" 2>&1 >/dev/null
if [ "$?" != "0" ];then
	echo "Not found device $opdevid. will exit."
	exit -1
else
	echo " handle device $opdevid"
fi
for dev in ${savepart[@]}
do
	echo "$dev"
	if [ "$dev" == "$opdevid" ];then
		echo "Device $opdevid can't fdisk. please input another device."
		exit -2
	fi
done

fdisk $opdevid << EOF
n
p
1


t
83
p
w
EOF

mkfs -t ext4 -c "$opdevid"1 
mkdir /www
mount "$opdevid"1 /www
df 

cat /etc/fstab | grep "$opdevid"1
if [ $? == 0 ];then
	echo "$opdevid"1 in /etc/fstab , please check file.
else
	echo "${opdevid}1	/www	ext4	defaults	1	2" >> /etc/fstab

fi

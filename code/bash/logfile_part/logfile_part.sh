#!/bin/bash
# run command and record log 
# logfile size lessthan maxsize 

DTIME=`date +%Y%m%d%H%M`
maxsize=$((1024*1024*16))
logfile=command_log_${DTIME}.log
touch ${logfile}
while (true)
do
	sleep 3
	echo ""
	echo `date +%Y%m%d%H%M%S`" : ==========================================" >> ${logfile}
	# run command 
	top -Hn1 >> ${logfile}
	logfile_size=`ls -l ${logfile}| awk '{print $5}'`
	echo "${logfile_size} ${maxsize}" 
	if [ ${logfile_size} -gt ${maxsize} ];then
		echo "${logfile_size} > $maxsize" >> ${logfile}
		DTIME=`date +%Y%m%d%H%M`
		logfile=command_log_${DTIME}.log
	else 
		echo "${logfile_size} < $maxsize" >> ${logfile}
	fi
done

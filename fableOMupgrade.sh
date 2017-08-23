#!/bin/bash

curdir=`pwd`
CMDEND="/"

find . -name "*.sql" -exec dos2unix {} \;
find . -name "*.txt" -exec dos2unix {} \;
find . -name "*.sh" -exec chmod +x {} \;
find . -name "d2u*" -exec rm -rf {} \;

run_mysql_script()
{
	unset LC_ALL
	unset LANG
	chmod 644 /Fablesoft/InsightView/third/mysql/my.cnf
	
	echo "请输入数据库IP："
	mysqlIp=$enable__databaseIp
	echo $mysqlIp
	
	if [ ! $SERVER ]; 
	then
           echo "数据库服务名为空！默认使用itsm" 
           SERVER=itsm
	fi
	
	echo "删除已经存在${SERVER}数据库，并创建一个空的${SERVER}数据库"
	echo $MYSQL_HOME/bin/mysql
	
	#$MYSQL_HOME/bin/mysql -u$USERNAME -p$PASSWORD -S$MYSQL_HOME/mysql.sock --default-character-set=utf8 --character-sets-dir=$MYSQL_HOME/share/mysql/charsets/ -e"
	echo "$MYSQL_HOME/bin/mysql -u$USERNAME -p$PASSWORD -h$mysqlIp --default-character-set=utf8 --character-sets-dir=$MYSQL_HOME/share/mysql/charsets/ -e"
	$MYSQL_HOME/bin/mysql -u$USERNAME -p$PASSWORD -h$mysqlIp --default-character-set=utf8 --character-sets-dir=$MYSQL_HOME/share/mysql/charsets/ -e"
	drop database if exists ${SERVER};
	CREATE SCHEMA ${SERVER} DEFAULT CHARACTER SET utf8 ;
	"
	echo "创建数据表及初始化数据表"
	for dir in $dirlist
	do
          for file in `cat ${curdir}/$dir/sql_file_sequence.txt`
          do
                echo "run ${curdir}/$dir/$file"
		echo "run ${curdir}/$dir/$file" >> init.log
                #$MYSQL_HOME/bin/mysql $SERVER -u$USERNAME -p$PASSWORD -S$MYSQL_HOME/mysql.sock --default-character-set=utf8 --character-sets-dir=$MYSQL_HOME/share/mysql/charsets/ < ${curdir}/$dir/$file >> $curdir/init.log
				$MYSQL_HOME/bin/mysql $SERVER -u$USERNAME -p$PASSWORD -h$mysqlIp --default-character-set=utf8 --character-sets-dir=$MYSQL_HOME/share/mysql/charsets/ < ${curdir}/$dir/$file >> $curdir/init.log

          done
	done
	echo "完成创建数据表及初始化数据表"
}

run_upgrade_mysql_script()
{
	unset LC_ALL
	unset LANG
	echo "请输入数据库IP："
	read mysqlIp
	echo "增量初始化数据"
	
          for file in `cat ${curdir}/sql_file_sequence.txt`
          do
                echo "run ${curdir}/$file"
	        echo "run ${curdir}/$file" >> init.log
		#$MYSQL_HOME/bin/mysql $SERVER -u$USERNAME -p$PASSWORD -S$MYSQL_HOME/mysql.sock --default-character-set=utf8 --character-sets-dir=$MYSQL_HOME/share/mysql/charsets/ < ${curdir}/$file >> $curdir/init.log
		$MYSQL_HOME/bin/mysql $SERVER -u$USERNAME -p$PASSWORD -h$mysqlIp --default-character-set=utf8 --character-sets-dir=$MYSQL_HOME/share/mysql/charsets/ < ${curdir}/$file >> $curdir/init.log

          done	
	echo "完成增量初始化数据"
}


run_oracle_script()
{
     for dir in $dirlist
     do	
	for file in `cat ${curdir}/$dir/sql_file_sequence.txt`
	do
		newfile=${curdir}/$dir/${file}ora
		echo "set define off" >$newfile
		echo "set echo off" >>$newfile
		echo "set feedback on" >>$newfile
		cat ${curdir}/$dir/$file >>$newfile
		echo "exit" >>$newfile
		echo "/" >>$newfile
		echo "run $file" | tee -a init.log
		sqlplus $USERNAME/$PASSWORD@$SERVER @$newfile >> init.log
		rm $newfile
	done
    done
}

source ./commonConf.ini
#echo "在下面的操作中你需要输入数据库用户名、用户口令和数据库服务名并选择数据库类型."
#
#echo "\n当前支持的数据库类型:\n"
#echo "******************************\n"
#echo "    1 - MySQL Version\n"
#echo "    2 - Oracle Version\n"
#echo "    0 - Quit\n"
#echo "******************************\n"
#echo "    Please choose[0-2]:\c"

#read ch
echo "******************************\n"
echo "数据库安装开始\n"

DBTYPE="mysql"
echo "请输入数据库用户名:\c"
USERNAME=$enable__databaseUsername
echo $USERNAME
echo "请输入用户口令:\c"
PASSWORD=$enable__databasePassword
echo $PASSWORD
echo "请输入数据库服务名:\c"
SERVER=$enable__databaseSchema
echo $SERVER

if [ -r init.log ]
then
	cp init.log init.log.orig
fi

cat /dev/null > init.log

dirlist="SCCP_BASE_ONE
	     SCCP_BASE_SECOND
         SCCP_BASE_THIRD"	
if [ $DBTYPE = "mysql" ]
then
	run_mysql_script $dirlist
        #run_upgrade_mysql_script
elif [ $DBTYPE = "oracle" ]
then
	run_oracle_script $dirlist
fi

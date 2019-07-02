#!/bin/sh

if test -z $1; then
	echo "Usage: ./judge.sh ./World_of_Warcraftx/"
	exit 0
fi

PROJECT_DIR=$1

cd $PROJECT_DIR
python3 ./main.py > data/my_output.txt
cd ./data
diff my_output.txt std_output.txt

echo "Done!"

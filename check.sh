EXE=$1
TEST=$2
ANS=$3

# make up some reasonable filename for the output
OUTPUT="out/$(basename $EXE).$(basename $TEST).output"

if ! timeout 1s $EXE < $TEST > $OUTPUT
then
	echo "ERR"
	exit
fi

if ! diff $ANS $OUTPUT > /dev/null
then
	echo "WA"
	exit
fi

echo "AC"

if [[ -z $1 ]]; then
    echo "Enter a task number"
    exit
fi

CURRENT_DATE="$(date +%F)"
CURRENT_DATE_FOLDER="./$CURRENT_DATE"

printf -v INPUT "%02d" $1

TASK_FILE="$CURRENT_DATE_FOLDER/task-$INPUT.py"

if [[ -f $TASK_FILE ]]; then
    echo "Task already exists"
    exit
fi

mkdir $CURRENT_DATE_FOLDER -p
echo "#!python\n" > $TASK_FILE
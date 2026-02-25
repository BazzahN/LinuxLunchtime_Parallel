#!/bin/bash

#Sets processes to default if no argument supplied
PROCESSES=${1:-5}

#Log Current Time
start=`date +%s.%N`

echo -e "Running in Parallel\n"
for (( i = 1; i <= $PROCESSES; i++ )) 
do
    echo "Running n=2000 m = 50 s = $i"
    
    # Line runs our python script with the arguments. The & is the most important part. & makes the code run asynchronously.
    python matrix.exp.py -n 2000 -m 50 --seed ${i} --name test > logs/log.${i}.out &

done

# wait doesn't return to command line until all processes are complete.
wait

end=`date +%s.%N`


runtime=$( echo "$end - $start" | bc -l )

echo "Total runtime: $runtime";

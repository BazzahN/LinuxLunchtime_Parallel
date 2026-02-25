#!/bin/bash

PROCESSES=${1:-5}

source ./run_serial.sh $PROCESSES
source ./run_parallel.sh $PROCESSES

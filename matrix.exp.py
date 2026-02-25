import numpy as np
import argparse
import os
from datetime import datetime
from utils import matexp
pid = os.getpid()
print(f"\npid is : {pid}")
now = datetime.now()
print("start time : ",now)

#Handle commandline arguments with argparse library
parser = argparse.ArgumentParser()
parser.add_argument("-n",type=int,required=True,help="The size of the randomly generated X matrix")
parser.add_argument("-m",type=int,required=True,help="Number of terms in the approximation")

parser.add_argument("--seed",type=int,required=False,help="RNG seed. If none supplied then seed=12345 by default")
parser.add_argument("--name",required=False,help="Stem name of the files to be exported")

#Import command line arguments and assign to the correct variables
args = parser.parse_args()
n = args.n
m = args.m

#Assign variables if no argument has been given
seed = args.seed
if seed is None:
	seed = 12345

##Uses default name for output files if none supplied
stem = args.name
if stem is None:
	stem = ""
      

np.random.seed(seed)
# Randommly generate X
X = np.random.rand(n,n)

#Run 
Y = matexp(X,m)

#Save output to numpy files
##Save the randomlly generated X matrix 
folder = "data/"

np.save(f"{folder}/{stem}.X.n={n}.m={m}.s={seed}",X)
np.save(f"{folder}/{stem}.X.n={n}.m={m}.s={seed}",Y)

#Print End time of parralel process
now = datetime.now()
print(f"end time :{now}\n") 

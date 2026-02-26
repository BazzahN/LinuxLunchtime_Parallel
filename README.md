# Introduction
In this Linux Lunchtime we will be dealing with a script to calculate the matrix exponential:

$$
\exp{X} = \sum_{m=0}^{\infty} \frac{1}{m!} X^m
$$

---
We want to set up our python environment here we can use `python_setup`. First make `python_setup` executable and then run it using the code below:
```
chmod +x python_setup
source ./python_setup
```
This should setup everything you need in this project folder. 

Our function `matrix.exp` takes as an argument 
- $m$, which is the number of terms for the approximation
- $n$, which is the size of the randomly generated matrix.
- $seed$, which is the seed for random number generation.

The shell script `run_serial.sh` lets you run this code in series, and `run_parallel.sh` in parallel. The script `run_together.sh` runs both for comparison.
These scripts have already been made executable in `python_setup`, the only thing you need to do is
```
./run<name>.sh
```

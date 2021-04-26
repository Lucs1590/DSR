# Audio convolution
# How it works?
In this project it is possible to learn and see how to convolve audios with themself or with each other. So, with examples, in this README, we will see a manual example, and running the code, we will see practical examples using sounds.
# How to run?

## Prerequisites
First you need to install the prerequisites and to do that, you need to have **Python3** or higher and **pip**.
After having the two prerequisites mentioned, just run:
```bash
pip install requirements.txt --user
```

## Running the project
After install the prerequisites, run the following command at terminal on ST1 folder:
```bash
python src/main.py
```

# Examples
### Making two discrete-time signals and convolving them
a[·] = [2, 4]

b[·] = [1, 2, 4, 8]

y[·] = a[·] * b[·]

y[·] = [2, 8, 16, 32, 32]

### Convolving y by y
z[·] = y[·] * y[·]

                          64 -  256 -  512 - 1024 - 1024
                    64 - 256 -  512 - 1024 - 1024
              32 - 128 - 256 -  512 -  512
         16 - 64 - 128 - 256 -  256
     4 - 16 - 32 -  64 -  64
    ----------------------------------------------------
    4 - 32 -128 - 384 - 896 - 1536 - 2048 - 2048 - 1024

z[·] = [4, 32, 128, 384, 896, 1536, 2048, 2048, 1024]

### General equation to calculate the length

n = (n1 + n2) - 1
 - n = size of result
 - n1 = size of signal 1
 - n2 = size of signal 2

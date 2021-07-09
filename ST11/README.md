# Correlation and AMDF

# How it works?
This project has a script that does a correlation using AMDF auto and shows F0. For this, we apply a correlation to find the minimum value of the signal and then try to define the interval between waves, as well as a determination of F0 through these intervals and the value of samples per second.

# How to run?

## Prerequisites
First you need to install the prerequisites and to do that, you need to have **Python3** or higher and **pip**.
After having the two prerequisites mentioned, just run:
```bash
pip install -r  requirements.txt --user
```

## Running the project
After install the prerequisites, run the following command at terminal on ST11 folder:
```bash
python src/main.py
```
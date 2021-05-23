# Normalization

# How it works?
Normalization happens so that the entire scale of the filter or signal in question is close, modifying the curve, but allowing for a better visualization and similar behavior.

# How to run?

## Prerequisites
First you need to install the prerequisites and to do that, you need to have **Python3** or higher and **pip**.
After having the two prerequisites mentioned, just run:
```bash
pip install -r  requirements.txt --user
```

## Running the project
After install the prerequisites, run the following command at terminal on ST6 folder:
```bash
python src/main.py
```

------
## Difference Equation

To get the difference equation between the signal and the filter, we need to multiply a piece of the signal with the filter coefficients.
About the exercise, the formula to have difference equation is:

y[z] = - 0.190 * x[n] - 0.002 * x[n-1] + 1.386 * x[n-2] - 0.002 * x[n-3] - 0.190 * x[n-4]

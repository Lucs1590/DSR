# Define Signal and Window

# How it works?
The filter can be set when the fluctuations are present, as well as the transition band value. In addition, it is worth mentioning that the filter must be windowed in such a way that it attenuates the relevant values and reduces the fluctuation for the others. This window can vary according to the need.

# How to run?

## Prerequisites
First you need to install the prerequisites and to do that, you need to have **Python3** or higher and **pip**.
After having the two prerequisites mentioned, just run:
```bash
pip install -r  requirements.txt --user
```

## Running the project
After install the prerequisites, run the following command at terminal on ST7 folder:
```bash
python src/main.py
```

------
## Difference Equation

To get the difference equation between the signal and the filter, we need to multiply a piece of the signal with the filter coefficients.
About the exercise, the formula to have difference equation is:

y[z] =  0.004 * x[n-1] + 0.012 * x[n-2] + 0.006 * x[n-3] - 0.020 * x[n-4] - 0.051 * x[n-5] - 0.045 * x[n-6] + 0.037 * x[n-7] + 0.195 * x[n-8] + 0.374 * x[n-9] + 0.485 * x[n-10]

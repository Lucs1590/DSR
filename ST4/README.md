# High pass filter
Through high pass filters, we limit that only high frequencies are accepted. Here are some practical and theoretical examples of this learning.
# How it works?
We calculate the low-pass filter and, from there, mirror the behavior of the curve, just applying a signal transformation alternately.

# How to run?

## Prerequisites
First you need to install the prerequisites and to do that, you need to have **Python3** or higher and **pip**.
After having the two prerequisites mentioned, just run:
```bash
pip install requirements.txt --user
```

## Running the project
After install the prerequisites, run the following command at terminal on ST4 folder:
```bash
python src/main.py
```

# Z-Transform
From the **Z-Transform** we can have the frequency domain, which in turn, can calculate the transfer function of the system using the euler function as well.

## Frequency domain
To transform a filter (or signal) to the frequency domain, we need only of the coefficients and the index of coefficients.

g[n] = [0.07073739905582861, 0.17644333177153582, 0.624387301951779, -0.624387301951779, -0.17644333177153582, -0.07073739905582861]

**G[z] = 0.070 + (0.176 * z<sup>-1</sup>) + (0.624 * z<sup>-2</sup>) - (-0.624 * z<sup>-3</sup>) - (0.176 * z<sup>-4</sup>) - (0.070 * z<sup>-5</sup>)**

## System transfer function
Having the frequency domain, we can now use the Euler transfer function and to obtain the system transfer function.

G[z] = 0.070 + (0.176 * z<sup>-1</sup>) + (0.624 * z<sup>-2</sup>) - (-0.624 * z<sup>-3</sup>) - (0.176 * z<sup>-4</sup>) - (0.070 * z<sup>-5</sup>)

G(j&omega;) = 0.070 + 0.176 e<sup>-j&omega;</sup> + 0.624 e<sup>-2j&omega;</sup> - 0.624 e<sup>-3j&omega;</sup> - 0.176 e<sup>-4j&omega;</sup> - 0.070 e<sup>-5j&omega;</sup>

**G(j&omega;) = 0.070 + 0.176(cos(&omega;) - j sin(&omega;)) + 0.624(cos(2&omega;) - j sin(2&omega;)) - 0.624(cos(3&omega;) - j sin(3&omega;)) - 0.176(cos(4&omega;) - j sin(4&omega;)) - 0.070(cos(5&omega;) - j sin(5&omega;))**
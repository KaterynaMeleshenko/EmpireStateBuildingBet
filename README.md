# Empire State Building Bet

This code simulates results for **Empire State Building Bet** that is:

To walk up the stairs of the Empire State Building and roll a regular 6-sided die 100 times and move up or down the stairs based on the numbers rolled, as follows:

If it's 1 or 2, we'll go one step down.

If it's 3, 4, or 5, we'll go one step up.

If it's 6, we'll throw the die again and will walk up the resulting number of steps.

We can not go lower than step number 0. We admit that we're a bit clumsy and have a chance of 0.1% falling down the stairs when we make a move. Falling means that we have to start again from step 0.

With all of this in mind, we bet that we'll reach 60 steps high.

The task is to evaluate our chances of winning and decide if we actually want to bet.

## How to Use the Code
To run the code, follow these steps:

1. Install the required dependencies: **numpy**, **matplotlib** and **IPython**. You can install them using **pip**:
```
pip install numpy matplotlib ipython
```

2. Clone or download the code to your local machine.

3. Run the **esb_bet.py** file using a Python interpreter:
```
python esb_bet.py
```
The code will run 100 simulations of the final steps of 1000 walks and visualize the distribution of results on the animated histogram.

## File Structure
The project includes one file:

**esb_bet.py**: contains the Python code to simulate the Empire State Building walks and generate an animated histogram.

## Contributing
Contributions to the code are welcome. If you find a bug or have a feature request, please open an issue on the GitHub repository. If you want to contribute code, please fork the repository and submit a pull request.

## License
This code is released under the EPL-2.0 license. See LICENSE for more information.

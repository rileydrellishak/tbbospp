"""
The Birthday Paradox, also called the Birthday Problem, is the 
surprisingly high probability that two people will have the same
birthday even in a small group of people. In a group of 70 people, 
there’s a 99.9 percent chance of two people having a matching birthday.
But even in a group as small as 23 people, there’s a 50 percent chance 
of a matching birthday. This program performs several probability 
experiments to determine the percentages for groups of different sizes.
We call these types of experiments, in which we conduct multiple random
trials to understand the likely outcomes, Monte Carlo experiments.
"""

# Simulate a group of people and check how often at least two share the same birthday.
# Prompt the user for the group size (number of people).
# Assign each person a random birthday (1–365).
# Check if any two birthdays match.
# Repeat simulation many times (e.g., 10,000 trials) to estimate probability.
# Print percentage of trials where a shared birthday occurs.
# Concepts covered: lists, loops, random number generation, probability estimation.
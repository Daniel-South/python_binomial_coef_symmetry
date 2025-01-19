"""
FILE:	python_binomial_coefficient_symmetry.py
AUTHOR:	Daniel R. South
DATE:	2025-01-19
TITLE:	Demonstrate the Symmetry of the Binomial Coefficient
	i.e. n select k should be equal to n select (n-k)

DESCRIPTION:

Ms. Manager wants to form two committees from her team of five people,
a Taco Tuesday Committee with two members and a Pizza Friday Committee with three members.

Committee membership will be mutually exclusive. No one will serve on both committies.
Employees not selected for one committee will be automatically assigned to the other committee.

The Binomial Coefficient gives the number of combinations of k members from a set of n (n select k)
without replacement.

The Symmetry of the Binomial Coefficient suggests that there are as many ways to select n-k from n
as there are ways to select k from n.

This suggests that the number of ways to select 2 people from a group of 5 to form the Taco Tuesday Committee
is the same number of ways to select 3, or (5-2), people to form the Pizza Friday Committee.

We'll show this with a naive algorithm that will choose team members for one committee
and assign the remaining team members to the other committee.

We'll do this with each committee to demonstrate that the number of selections is the same and
that it will match what is predicted by the Binomial Coefficient.
"""

from math import factorial

team = ["Ann", "Bradley", "Clarice", "David", "Edna"]

n_param = 5
print(f"n_param = {n_param}")

k_param = 2
print(f"k_param = {k_param}")

n_minus_k = n_param - k_param

print(f"Select {k_param} members from {n_param} to form the Taco Tuesday Committee")

combo_counter = 0
for i in range(n_param):
    for j in range(i+1, n_param):
        taco_com = [team[i], team[j]]
        pizza_com = sorted(list(set(team) - set(taco_com)))
        combo_counter += 1
        print("Taco:", taco_com, " --->  Pizza:", pizza_com)
print(f"There are {combo_counter} ways to select {k_param} members from a set of {n_param}")


print("")
print(f"n_param = {n_param}")
print(f"n_minus_k = {n_minus_k}")

print(f"Select {n_minus_k} members from {n_param} to form the Pizza Friday Committee")

combo_counter = 0
for i in range(n_param):
    for j in range(i+1, n_param):
        for k in range(j+1, n_param):
            pizza_com = [team[i], team[j], team[k]]
            taco_com = sorted(list(set(team) - set(pizza_com)))
            combo_counter += 1
            print("Pizza:", pizza_com, " --->  Taco:", taco_com)
print(f"There are {combo_counter} ways to select {n_minus_k} members from a set of {n_param}")


print("")

result = factorial(n_param) / (factorial(k_param) * factorial(n_minus_k))
print(f"The Binomial Coefficient for n select k is {result}")


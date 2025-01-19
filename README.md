# python_binomial_coef_symmetry
  
Demonstrate the Symmetry of the Binomial Coefficient. 
i.e. n select k should be equal to n select (n-k)  
  
Author: Daniel R. South 2025-01-19  
  
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
  
  
PROGRAM OUTPUT:  
  
n_param = 5  
k_param = 2  
Select 2 members from 5 to form the Taco Tuesday Committee  
Taco: ['Ann', 'Bradley']  --->  Pizza: ['Clarice', 'David', 'Edna']  
Taco: ['Ann', 'Clarice']  --->  Pizza: ['Bradley', 'David', 'Edna']  
Taco: ['Ann', 'David']  --->  Pizza: ['Bradley', 'Clarice', 'Edna']  
Taco: ['Ann', 'Edna']  --->  Pizza: ['Bradley', 'Clarice', 'David']  
Taco: ['Bradley', 'Clarice']  --->  Pizza: ['Ann', 'David', 'Edna']  
Taco: ['Bradley', 'David']  --->  Pizza: ['Ann', 'Clarice', 'Edna']  
Taco: ['Bradley', 'Edna']  --->  Pizza: ['Ann', 'Clarice', 'David']  
Taco: ['Clarice', 'David']  --->  Pizza: ['Ann', 'Bradley', 'Edna']  
Taco: ['Clarice', 'Edna']  --->  Pizza: ['Ann', 'Bradley', 'David']  
Taco: ['David', 'Edna']  --->  Pizza: ['Ann', 'Bradley', 'Clarice']  
There are 10 ways to select 2 members from a set of 5  
  
n_param = 5  
n_minus_k = 3  
Select 3 members from 5 to form the Pizza Friday Committee  
Pizza: ['Ann', 'Bradley', 'Clarice']  --->  Taco: ['David', 'Edna']  
Pizza: ['Ann', 'Bradley', 'David']  --->  Taco: ['Clarice', 'Edna']  
Pizza: ['Ann', 'Bradley', 'Edna']  --->  Taco: ['Clarice', 'David']  
Pizza: ['Ann', 'Clarice', 'David']  --->  Taco: ['Bradley', 'Edna']  
Pizza: ['Ann', 'Clarice', 'Edna']  --->  Taco: ['Bradley', 'David']  
Pizza: ['Ann', 'David', 'Edna']  --->  Taco: ['Bradley', 'Clarice']  
Pizza: ['Bradley', 'Clarice', 'David']  --->  Taco: ['Ann', 'Edna']  
Pizza: ['Bradley', 'Clarice', 'Edna']  --->  Taco: ['Ann', 'David']  
Pizza: ['Bradley', 'David', 'Edna']  --->  Taco: ['Ann', 'Clarice']  
Pizza: ['Clarice', 'David', 'Edna']  --->  Taco: ['Ann', 'Bradley']  
There are 10 ways to select 3 members from a set of 5  
  
The Binomial Coefficient for n select k is 10.0  

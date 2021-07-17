## DIRECTIONS
> Hello there, please complete all of the questions. For each, solve the problem. 
> In these, you might have to write the output of the code or write some code to solve a problem. Or, fix the bug in a segment of code.
> You can either write your solutions on a piece of paper or make a copy of this directory and write it on this file.
> *Good luck!*

## TOPICS
* loops
* if and then statements
* lists
* indexing
* importing libraries

## QUESTIONS

### Question 1: *which loop?*
> Explain the difference between these two loops:
```python
for i in range(100):
    print('loop')

while True:
    print('loop')
```

### Question 2: *elif if if if*
> What is the output of this code?
```python
var = 1
if False and var == 1:
    print('Here!')
elif False or var == 1:
    print('No, here!')
elif var == 1:
    print('HERE!')
else:
    print('here?')
```

### Question 3: *loopy loops*
> Write a loop that will print the following:
```
0
1
2
3
4
5
6
7
8
9
10
```

### Question 4: *loopy loopy loops*
> Write a loop that will print the following:
```
1 
1 2 
1 2 3 
1 2 3 4 
1 2 3 4 5
```

### Question 5: *list recap*
> What is the output of this code?
```python
my_list = [3, 1, 5, 3, 9]
print(my_list[3])
```

### Question 6: *my list, your list*
> What are the values inside `your_list` after this program is complete?
```python
my_list = ['foo', 'bar', 'foobar', 'barfoo', 'foofoo', 'barbar']
your_list = []
for i in range(len(my_list)):
    if i % 2 == 0:
        your_list.append(my_list[i])
```

### Question 7: *my list, your list, our list*
> What are the values inside `our_list` after this program is complete?
```python
my_list = ['foo', 'bar', 'foobar', 'barfoo', 'foofoo', 'barbar']
your_list = ['bar', 'barfoo', 'foofoo', 'barfoo', 'foo', 'barbar']
our_list = []
for i in range(len(my_list)):
    for j in range(len(your_list)):
        if my_list[i] == your_list[j] and i == j:
            our_list.append(my_list[j])
```

### Question 8: *concept check!*
> What is a "library" or "module" in Python, and why do we import them?
```python
# ex:
import boyer, reporty
```

### Question 9: *de-bug my program, than my grammar*
> Find the 3 errors in this program, then correct them.
> *BONUS:* also find the grammatical error
```python
from random imprt randint:

number = randint(1, 3)

if number == '1':
print("The random number is won!")
```

### Question 10: *de-burger*
> Why won't this program EVER print `you win a burger!`?
```python
import random

if random.randint(1, 3) == 2.5:
    print("you win a burger!")
```

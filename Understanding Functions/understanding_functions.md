# Understanding Functions
> A function is a subprogram that acts on data and often return a value, It is a reusable block of programming statements designed to perform a certain task.

## Why should we use functions?
1. Reusability of code.
1. Makes program handling easier.
1. Makes program more readable and understandable.

## Types of function in python

### Built-in functions.
> Pre defined functions that are available for use. For example:
```python
len(),type(), id(), input(), print()
```

### Functions defined in modules
> Pre defined functions in particular modules and can be used for importing. For example:
```python
#1
import math
from math import sqrt()
#2
import discord
from discord import app_commands
```

### User Defined Functions
> Functions defined by the programmer. For example:
```python
def sum(x, y):
    s=x+y
    return s
```

### Function Components
> Function Header: The first line of function definition that begins with keyword **def** and ends with **:**, specifies name of the function and its parameters.
> Parameters : Variables that are listed within the parenthesis.
> Function Body: The block of indented/ statements beneath function header.
> Return Statement: The statement that returns a value from the function. For example:
```python
def <function name>([parameters]):
    """..."""
    <statement>
    [<statement>]
    [return [value]]
```
#### Top level Statement & Function callings
> Top level statement is the statement that is not within a function. For example:
> Syntax for calling function: [variable]=<Functionname>([arguments])

```python
def sum(x, y):
    s=x+y
    return s
#Outside the function    
a=int(input("Enter a number: ")) # Top level statement
b=int(input("Enter another number: ")) # Top level statement
c=sum(a,b) # Top level statement and function call  
```
#### Function Arguments
> Function arguments are the values that are passed to the function when it is called. For example:
```python
def sum(x, y):
    s=x+y
    return s
#Outside the function
a=int(input("Enter a number: ")) # Top level statement
b=int(input("Enter another number: ")) # Top level statement
c=sum(a,b) # Top level statement and function call
```
#### Function Parameters
> Function parameters are the variables that are defined within the function header. For example:
```python
def sum(x, y):
    s=x+y
    return s
#Outside the function
a=int(input("Enter a number: ")) # Top level statement
b=int(input("Enter another number: ")) # Top level statement
c=sum(a,b) # Top level statement and function call
```
#### Types of parameters
> Positional Arguments (Required arguments), Default Arguments and Keyword (or named) Arguments.

1. Positional Arguments:
> Positional arguments are the arguments that are passed to the function in the order in which they are defined. For example:
```python
def func(x,y):
    print(x,y)
    n1=int()
    n2=int()
    n3=int()
func(n1,n2)
func(n1) #error
func(n1,n2,n3) #error
```
2. Default Arguments:
> Default arguments are the arguments that are passed to the function when it is called. For example:
```python
def func(x,y=0):
    print(x,y)
    n1=int()
    n2=int()
    n3=int()
func(n1,n2)
func(n1) #error
func(n1,n2,n3) #error
```
3. Keyword Arguments:
> Keyword arguments are the arguments that are passed to the function when it is called. For example:
```python
def func(x,y=0):
    print(x,y)
    n1=int()
    n2=int()
    n3=int()
func(n1,n2)
func(n1) #error
func(n1,n2,n3) #error
```
#### Rules for combining all three types of arguments
1. Positional Arguments must be passed in the order in which they are defined.
2. Default Arguments must be passed after the positional arguments.
3. Keyword Arguments must be passed after the default arguments.
4. An argument list must first contain positional arguments followed by any keyword argument
5. Keyword arguments should be taken from the required arguments preferably
6. You cannot specify a value for an argument more than once.

#### Two type of functions on the basis of return value:
1. Non-Void Functions / Fruitful Functions: Functions returning some value.
The value returned can be:
Literal eg: return 2
Variable eg: return sol
Expression eg: return sol*2

2. Void Functions / Empty Functions: Functions that do not return any value.

### Scope of Variables
> Scope of variables is the region of code in which the variable is accessible.
> Local variables: Variables defined within a function.
> Global variables: Variables defined outside a function.
> Built-in variables: Variables defined in the Python interpreter.
> Class variables: Variables defined in the class.
> Instance variables: Variables defined in the instance.

```python
#this function uses global variables
def abc():
    print d
    return
#global variable
d="..."
abc()
```

#### Lifetime of variables
> Lifetime of variables is the period of time in which the variable is accessible.
1. Global variable has a lifetime of entire program run.
2. For local variable lifetime is function’s run i.e as long as their function is being executed.

####  Name resolution
> Name resolution is the process of finding the value of a variable.
> Name resolution starts from the most local scope and works its way up to the global scope.
> Name resolution is done by searching the local scope and then the enclosing scopes.
Priority order of name resolution is:
1. Local scope
2. Enclosing scopes
3. Global scope
4. Built-in scope
-> LEGB Rule

### Nested Functions
> Nested functions are functions defined within another function.
> Nested functions are useful when you want to reuse the same function in multiple places.
> for example:
```python
def outer():
    print("outer function")
    def inner():
        print("inner function")
    inner()
outer()
```

"""Collection of the core mathematical operators used throughout the code base."""

import math

# ## Task 0.1
from typing import Callable, Iterable

#
# Implementation of a prelude of elementary functions.

# Mathematical functions:
# - mul
def mul(a:any, b:any):
    return a * b
# - id
def id(a:any):
    return a
# - add
def add(a:any, b:any):
    return a + b
# - neg
def neg(a:any):
    return -a
# - lt
def lt(a:any, b:any):
    return a < b
# - eq
def eq(a:any, b:any):
    return a == b
# - max
def max(a:any, b:any):
    return a if a >= b else b
# - is_close
def is_close(a:any, b:any):
    return abs(a - b) < 1e-2
# - sigmoid
def sigmoid(a:any):
    return 1 / (1 + math.exp(-a)) if a >=0 else math.exp(a)/(1.0 + math.exp(a))
# - relu
def relu(a:any):
    return a if a >= 0 else 0
# - log
def log(a:any):
    return math.log(a)
# - exp
def exp(a:any):
    return math.exp(a)
# - log_back
def log_back(a:any, b:any):
    return b / a
# - inv
def inv(a:any):
    return 1 / a
# - inv_back
def inv_back(a:any, b:any):
    return - b / (a * a)
# - relu_back
def relu_back(a:any, b:any):
    return b if a > 0 else 0
#
# For sigmoid calculate as:
# $f(x) =  \frac{1.0}{(1.0 + e^{-x})}$ if x >=0 else $\frac{e^x}{(1.0 + e^{x})}$
# For is_close:
# $f(x) = |x - y| < 1e-2$


# TODO: Implement for Task 0.1.


# ## Task 0.3

# Small practice library of elementary higher-order functions.

# Implement the following core functions
# - map
def map(f: Callable, ls: Iterable):
    return [f(x) for x in ls]
# - zipWith
def zipWith(f:Callable, a:Iterable, b:Iterable):
    return [f(x, y) for x, y in zip(a, b)]
# - reduce
def reduce(f:Callable, ls:Iterable, st:any):
    res = st
    for el in ls:
        res = f(res, el)
    return res
# Use these to implement
# - negList : negate a list
def negList(ls: Iterable):
    return map(neg, ls)
# - addLists : add two lists together
def addLists(a:Iterable, b:Iterable):
    return zipWith(add, a, b)
# - sum: sum lists
def sum(ls :Iterable):
    return reduce(add, ls, 0)
# - prod: take the product of lists
def prod(ls:Iterable):
    return reduce(mul, ls, 1)

# TODO: Implement for Task 0.3.

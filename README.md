# Understanding Memory Management in Programming

When compiling an application, machine-level binary code is generated and loaded into the computer's memory.

## Memory Segments

### 1. Stack

- Stack memory is a special region in RAM (Random Access Memory).
- It stores local variables and manages method calls.
- It helps the programming language keep track of where to return after finishing the execution of a given method.
- Small in memory but very fast.

### 2. Heap

- Heap memory is a special region in RAM where dynamic memory allocation takes place.
- In C programming, the `malloc()` function is used for dynamic memory allocation.
- Larger in size than stack memory.
- Objects and references are stored on the heap.
- Garbage collector in languages like Java removes unused objects from heap memory.

### 3. Machine Code

- Machine code, generated during compilation, is loaded into memory.

## Example:

```python
class House:
    windows = 5
    doors = 10

house_ref = House()

```
# `house_ref` is the object stored in the stack memory,
# and references to windows and doors are stored in the heap memory.
When the house_ref reference variable is no longer pointing to the object, it becomes eligible for garbage collection, and the garbage collector will remove it from the heap.

FAQ
Q. What happens to an object with no active references from the stack memory?
A. If there are no active references to an object on the heap, it becomes eligible for garbage collection, and the garbage collector will remove it from the heap.

Recursion Problem Statement:
Problem:
Calculate the sum of the first N integers.

Solution (Python):
```python
def calculate_sum(N):
    if N == 1:
        return 1
    else:
        return N + calculate_sum(N - 1)
```

<pre>
  ┌─────────────────┐
  ├     1+sum(0)    ┤
  ├─────────────────┤
  ├     2+sum(1)    ┤
  ├─────────────────┤
  │     3+sum(2)    │
  ├─────────────────┤
  │     4+sum(3)    │
  └─────────────────┘
  </pre>

## Type of recursion
1. Head Recursion
```python
def tail(n):
    #base case
    if n == 0:
        return 
    #operation
    print(n)
    #make the recursive function call
    tail(n-1)
tail(5)
```
2. Tail Recursion
```python
def head(n):
    #base case
    if n == 0:
        return 
    #make the recursive function call
    head(n-1)
    #operation
    print(n)
head(5)
```
- Recursion is twice slower then iteration becasue of fold and unfold of function

Problem 2: Calculate the multiplication of the first N integers.
```python
def calculate_sum(N):
    if N == 1:
        return 1
    else:
        return N + calculate_sum(N - 1)
```
Problem 3: Calculate the Factorial of the first N integers.
```python
def factorial(n, acc):
    #base case
    if n == 0:
        return acc
    return factorial(n-1, n*acc)
factorial(n, acc)
```

```python
#head Recursion
def factorial(n):
    #base case
    if n == 1:
        return 1
    return n+factorial(n-1)
factorial(5)
```
## Fibonacci number using iterative method
```python
def fibonacci_iterative(n):
    a, b = 0,1
    while n > 0:
        n = n-1
        a, b = b, a+b
    return a

print(fibonacci_iterative(7))
```
## Fibonacci Number problem with head recursion
- some value are calculate twice
- will use dynamic programming to make it efficient
```python
def febo(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    return febo(n-1)+febo(n-2)

print(febo(7))
```

## Fibonacci Number stack Memory Visualization
### Head Recursion
```python
def fiboncci(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    
    fibo1 = fibonacci(n-1)
    fibo2 = fibonacci(n-2)
    result = fibo1+fibo2
    return result
```
### Tail Recursion 
```python
def fibonacci_tail(n, a=0, b=1):
    if n==0: return a
    if n==1: return b
    return fibonacci_tail(n-1, b, a+b)

print(fibonacci_tail(6))
```
## Towers of Hanoi
- still in progress

## What is the Euclidean Algorithm
- Euclidean Algorithm is an efficient method for computing the greatest common
divisor(GCD) of two integers
- GCD - the largest number that divides them both without a remainder

```
GCD(a,b)
for two given number a and b such that a>=b
-> if b/a then GCD(a,b) = b
-> otherwise GCD(a,b) = GCD(b, a mod b)
```
- 3 is Greatest Common Divisor for (24,9)
```
GCD(24,9) --> GCD(9, 6) --> GCD(6, 3) --> return 3
```
- Implement Euclidean Algorithm using Recursion method
```python
def GCD(a,b):
    #base case: if b/a(without a remainder) then b is gcd
    if a%b==0:
        return b
    
    return GCD(b, a%b)

print(GCD(24,9))
```

- Implement Euclidean Algorithm using Iterative method
```python
def gcd_iter(a,b):
    while a%b != 0:
        a,b = b, a%b
    return b
print(gcd_iter(24,9))
```

## What is Linear Search
- linear search(sequential search) is a mothod for finding an item in an unsorted list.
- the algorithm makes N comparsions in worst-case, hense time complexity is o(N)
- Not good practice we can use binary search which take O(logN) or hash-function which will take O(1) time complexity.

- Implement Linear search using Iterative method
```python
def linear_search(container, item):
    for i in range(len(container)):
        if container[i] == item:
            return i
    return -1
print(linear_search([5,7,4,8,9,5,4,8], 5))
```
- Implement Linear Search using Recursion
```python
def linear_search(container, item, index=0):
    if index >= len(container): #base case 1:
        return -1
    if container[index] == item: #base case 2: When we found item
        return index
    
    return linear_search(container, item, index+1)

print(linear_search([4,5,8,2,1,4,7], 2))
```
## What is binary Search?
- method fo finding an item in an sorted list
- the algorithm make logN comparision in worst-case, hence the running time complexity is o(logN).
- discard half of the dataset in every iteration.

### Implement Binary search using iterative method
```python
def binarySearch(lst, key):
    mid = 0
    left, right = 0, len(lst)-1
    while left <= right:
        mid = (left+right)//2
        if lst[mid] == key:
            return mid
        elif key > lst[mid]:
            left = mid+1
        elif key < lst[mid]:
            right = mid-1
    return -1
            
print(binarySearch([1,2,3,4,5,6,7,8,9], 10))
```
### Implement Binary search using recursion method
```python
def binary_search(lst, key, left, right):
    #base case 1: if start index greater the end index
    if left > right:
        return -1
    
    #base case 2: if element found return index
    mid = (left+right)//2
    if lst[mid] == key:
        return mid
    
    if key > lst[mid]:
        return binary_search(lst, key, mid+1, right)
    elif key < lst[mid]:
        return binary_search(lst, key, left, mid-1)

    
lst = [1,2,3,4,5,6,7,8,9]
key = 3
ans = binary_search(lst, key, 0, len(lst)-1)
print(ans)
    
```








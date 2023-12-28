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
```
def calculate_sum(N):
    if N == 1:
        return 1
    else:
        return N + calculate_sum(N - 1)
```
Memory Management
    when we compile the application then the machine level binary code is generated.
    This generated machine level code is loaded into the Memory
    
*The RAM is a memory region that is used to run program. it has 3 segment
    1. Heap
    2. Stack
    3. Machine Code

Stack 
    - Stack Memory is a special region in the RAM(Random Access Memory)
    - it is used to stores local variables and method calls.
    - this is how the programming language knows where to return after finish Execution of a given method
    - Small in memory but very fast

Head
    - Heap memory is a special region in the RAM where dynamic memory allocation takes place.
    - in c programming, we use malloc() function to allocate the memory dynamically
    - the size of the head is way larger then the size of the stack memory.
    - Object and reference are stored on the heap memory
    - it is large in size but slow to access.
    - in java programming, garbage collector remove the unused object form the head memeory.

class House:
    windows = 5
    doors = 10

house_ref = House()
** here house_ref is the object and store into the stack memeory and the refernce of windows and doors are stored into the heap memeory.
- when house_ref reference varible is no longer pointing to the object it can be removed.

Q. What happens to an object that has no active references from the stack memory?
A. if there are no active reference to an object on the heap then it is eligible for garbage collection- the garbage collector will remove it from the heap.

Recursion Problem statment:
1. Calculate the sum of first N integers.


'''
Chapter 3 - Recursion

Exercises:
3.1 - Suppose I show you a call stack like this.
        ________________________
       /______________________/
       |____GREET2____________|
       |_NAME:_|__MAGGIE______|
       |____GREET_____________|
       |_NAME:_|__MAGGIE______|
What information can you give me, just base on this call stack?

The greet function called greet2 and both are from the same person

3.2 - Supose you accidentally write a recursive funciton that runs forever. As you saw, your computer allocates memory on the stack for each function call. What happens to the stack when your recursive function runs forever?

The stack keep growing and growing until there's no more memory or you hit a memory limit and then it crahses
'''

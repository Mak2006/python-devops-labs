1. Basic python language revision notes
2. Running files
      1. Either as a main 
      `if __name__ == '__main__':`
           `print("something")`
      2. Use __init__.py to make the directory in a module, then you can import the file. 
      3. Use starter hash like to run it as a script. 
      		`#!/usr/bin/env python`

2. Help links
      1. [https://www.w3schools.com/python/python_strings.asp](https://www.w3schools.com/python/python_strings.asp)
3. Packages
      1. NLTK - natural language processing
      2. NUMPY - ML
      3. networkx - graph package 
      4. itertools - multiple interesting functions related to permutations and combinations. 
4. Vairous IDE's
      1. Pycharm, eclipse, pythonportable, jupyter, pycharm, 
      2. [https://www.onlinegdb.com/online_python_interpreter](https://www.onlinegdb.com/online_python_interpreter)
5. Prints, I/O - print ("x")
      1. print() by default puts a newline
      3. use this print to do without newline - print(str, end = '')
      4. No semicolon to end line, \n is the separator. print(msg)
      5. use the format to print variables like print("The count is {}".format(count))
      1. Aslo the **\*\*locals** can be used. Check here[https://stackoverflow.com/questions/4128144/replace-string-within-file-contents]. 
      1. Flush the prints then and there -         print(file, flush=True)
6. Variables -
      1. Every variable is an object, type does not require to be defined.
      2. v = "a"
      3. variable scope modifiers – global and nonlocal
      4. more [here](https://www.w3schools.com/python/python_scope.asp)  
      5. x = None; # means x is set to null. To check if a variable is None we can us `is` or `--` operators, like `if x is None` or `if x == None` 
      6.  Var can be 0, -1, 1.0, None, "xyz", 'xy', False, True. Types are int, float, NoneType, str, tuple, list, dict
7. Strings operations
      1. earlier we had ascii in python 2, python 3 uses unicode, so we have all languages and even unicode. 
      2. String Concatation operator is +
      3.  String can be multiplied !, operation you can do on a list can be done on a string.  So thats why you can use the in operator ex. `for "alpha" in x: ` or `print("alpha" in x)` returns true. 
      4. Different ways are - ''' is for multiline string, ' or ''
      5. All operators exists
      6. str.format(a, b, c) replaces {} within str with a, b,c - a nice function. This operator also removes the need of `str(x)` during concatenation as we can use format to take care of type during concatenation. There are three steps in this. First is define the variables, and then create the string with the place holders `s = {} is the address of {}` and thirdly use format to get the final string `s.format(v1, v2)` this will correctly format the string. We can then use the `s` string.  
      7. w = "alphabeta"; print(w[a:b]) prints starting with a, till before b; -1 goes in reverse   
      8. 0 is the first index.
      9. print(w[:]) prints the full wor   
      10. string.len() gives the length. #Note this is not for array size. 
      11. To get words from string use **split** say `x = " aaa bb ccc";` then `x.split(" ")[1]` gives bb.
8. General, History
      1. Comments is ''' or /* or #
      2. Started in 1994, Guido is the creator, now works for Dropbox.
      3. After 2002, python 2, 3.
9. Indentation
      1. Relies heavily on indentation.
      2. Indentation is brackets
      3. There should be no indentation on the first line or parent sequence.
      4. Use two spaces for indentation
      5. Two empty lines after a function
      5. "Python uses a different principle. Python programs get structured through indentation, i.e. code blocks are defined by their indentation. Okay that's what we expect from any program code, isn't it? Yes, but in the case of Python it's a language requirement not a matter of style. This principle makes it easier to read and understand other people's Python code." - [source](https://www.pythoncourse.eu/python3_blocks.php)
10. List , tuples dictionary
     1. It is some sequence of data.
       2. Is separate by comma x = [a, b, “c”]
       3. Add to the list using `x.append("more element")`;
       4. Operator var in list returns true if var is in list list
       5. Id(var) returns the index or pointer to the list . ??
       Arrays
       6. X[-1] = the last item.
       7. Index starts at `0`. Lenght is obtained by `x.len()`
       8. **Basic operations on list** - len(x), min(x), max(x)
       9. **list [] / tuple () / dic {}**= list is [], you u can change it, tuple is () you cant change it, dictionary is map and created by
   {x:y}, note x can be interger float as well.
       1. dict k = {'x':'p', 3.29:'r'} so print (k[3.29]) gives mean 'r', I can set k[3.29] = 3.44 , i.e. reassign  the value. 
           1. Iteration, `for name in x:` iterates over keys. you can access the values by `x[name]`
           2. `for name in x.values():` iterates over the values of x. 
       2. printing list is easy just say print x # it gives all element in the list
       3. various good ways of creating a list - this is List Comprehension. 
       4. K= [x**2 for x in range(1,10)]
       5. L= [fun(x) for x in [ or ( 1,2,3,'x' ) or ])
       6. T= [x for x in K if x%2 ==0] # this is damn good chain
       7. Creating list with range e.g. various list = range (0,15) or {a, b, c}
       `times_tables() == [i*j for i in range(1, 10) for j in range(1, 10)]`
`print(list(times_tables()))`
       9. 
   11. Function definition
       1. How do we know it is end of function? - two blank lines. 
       2. Must be defined before we use it. 
       3. functions are dynamically typed, the return type can be different and depends upon execution. 
```
def f(a, b):
    if a == 1:
        return 2;
    else:
        return "3";

print(type(f(1,"this returns int")));
print(type(f(2,"this returns string")))
```
   6.  function defintion  eg.
   `def my_function():`
   `print("Hello from a function");`
   
       4. Note function definition ends in `:`
       5. Function range(x) - starts from 0 and till x.  Defined as `range_(start, stop, step)`
       6. calling a function f(with args if there)
       7. variable args and variable key value pairs *args and **kargs
              1. very good explanation [here](https://www.saltycrane.com/blog/2008/01/how-to-use-args-andkwargs- in-python/),  
       8. functions with __constructor__
             1. function can be defined inside functions
             2. they cannot be assigned to variables.
       9. `def add (x, y=None):` Here `None` is a null variable.  Here add can be called with one or two vars. If add is called with one var the other is set to None. So this type of function defition also serves to set a default value to variables in function.  If var is supplied then the var is use or None is used !. 
       10. **type** function -  this is a funciton which can take variables and functions names even and returns what is the type of the argument. 
12. Operators - Maths, operators remain the same, + - / * , modulus operator is %, power operator **,
       1. Floor operator - // ignore the decimals
       2. x = 1,   y = 2
       3. MULTIPLE ASSIGNMENT  is possible  x,y = y,y // good feature
       4. OPERATOR precedence [here](https://www.mathcs.emory.edu/~valerie/courses/fall10/155/resources/op_preceden ce.html)-
       5. n += 4 // n = n + 4
       6. Comparision ==, <>, >=, <=, note there is no !=, it is <>
       7. Division operators % and // 
`a=13; print(a%3) ; print(a//3) # gives 1 and 4`
       9. 
15. Loop
       1. Types -  if else, while, for,
       2. `if` Loop
```
if
  print() # indentation by two spaces
  xy; xz; #note no braces, # indentation helps.
elif (): #optional
  statements
else : 
  statemetnes
  

```
9. For loop
     `for a in list:`
          `stmt`
      
12.  General Errors
        1. python c:\asda ada\p1.py results is in file not found, put quotes.
        2. Typecast error, you cannot add a string and a number.
        3. Indentation error
        4. Print always requries braces
        5. Function to be used has to be defined b4
   16. I/O -
       1. Take input from user = rawInput(), gives a string, so you have to convert b4 using.
   17. Conversion
       1.  X = int(str)
       2. Str = str(24)
   18. Variable naming
       1. Reserved words ignore
       2. Char set [a-zA-Z_][a-zA-Z_]*
       3. No . Or reserved with
    1. The value of `_` in python
		   1. Ignoring the variable like `for _ in range(2)` -`_` here signifies a private variable.
		   2. Signifying private use - `def __init__`
		   3.  [more here](https://hackernoon.com/understanding-the-underscore-of-python-309d1a029edc)
   19. Class
       1. key word is class; class Text:
       2. indentation marks the end of the class as below
       3. variables do not need to be defined before use. 
       4. there are no protected and private scopes. 
       5. lambdas can be used. 
  

     class Test:
       def method1(self):
       return 'howdy python'
       def method2(self, methodToRun):
       result = methodToRun()
       return result
       def method3(self):
       return sel   5.method2(sel   5.method1)
       test = Test()
       print test.method3()
      
  16.  Map function
       1. the first is a fucntion and rest are arguments.
       2. if arguments are passed to the function. 
       3. if argument is a list , map iterates over the items of the list. 
       4. the function may be defined as a lambda
       5. Map has lazy intitalization and this saves tons of memory. 
  17. lamda 
        1. inline function 
        2. lambda bouded variables1, 2, ..,n : experession
        3. can be assigned within print as print(f(args) == lambda x:x+1)
  18. Built in majic commands
	  1. Line magic and cell magic. 
	  2. Line magic defitions are created with % and invoked with %.
	  3. `%alias  newcommand old_comm inputs` example `%alias e echo %s`  `%e 'this is a msg'` for calling we use `%` and for arguments we use `%l` for whole line and `%s` for single arguments. 
	  `%alias bbb echo "<%l>" `
	  `%bbb 'this is msg'`
  or 
    `%alias bbb echo "%s" som thing "%s"`
	  `%bbb 'this is msg' `
	  5. Note both %s and %l cannot be used together.
	  6. 
	  7. Cell commands are %% abd invoked with %% 
	  8. %%timeit -n 100 # do the statement in the shell for 100 times and tell the time. 
  20. 

<!--stackedit_data:
eyJoaXN0b3J5IjpbMTcwMTIyOTA4LC0xMTM4ODMzODk3LC0xMj
E1NzU0NTU5LDEyNzk5NjU4MjZdfQ==
-->

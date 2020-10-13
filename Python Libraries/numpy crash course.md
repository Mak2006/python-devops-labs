## Numpy tips
Maintained in the Numpy Bootcamp.ipynb file 
**To be removed**
1. Array library, faster than built in python lists. Primarily because of Locality of reference, that is continuous memory locations. Written in Python, C and C++;
	1. Why it is fast - two reasons, one is the data is held directly in memory. Losing a pointer helps faster lookups. Losing data size and precision speeds up computation. 
2. `pip install numpy` and `Import numpy as np`
3. **Array creation  basics-** 
	1.  arr = np.array(python list or tuple or any array);
	2.  indexing starts from 0. 
	3.  arrays can be multi dimenstional viz 
	4. `np.array([1,2,3,4])`
	5. `np.array([  [], []  ])`
	6. `np.array([   [ [],  []  ] ])`
	7.  	8. access arr[a, b , c , d ]  - take the $a^{th}$ element within that take the $b^{th}$ element within that take the $c^{th}$ element and within that take the $d^{th}$. and so on. This would be possible from a 4D array.
	8. Negative indexing is there, 0 is the first element so -1 is the last element and so on.  
4. **Array Creation** 
	1.  **Arange** - `n = np.arange(0, 20, 2)` creates a 1 D from 0 to 20 with step 2.  Note 20 is not included.
	2. **linspace** - `numpy.linspace(start, stop, num=50, endpoint=True, retstep=False, dtype=None)` - creates an array from `start` to `stop` (included if `endpoint` =True, else not) containing `num` items in total.
	3. `n = ones((4, 3)) , zeros((4,3)), eye(4), diag(5), vstack([	a, 2*a]), hstack([a, 2*a]) `
	4. We can write `np.zeros(2,3,4,5,6)` it will give us a appropriate n dim matrix.  In the above case `ndim` will be 5. How to visualize this ndim array? 	It is hard to visualize, however, here is the way to represent it textually. An array containing 2 arrays each element of which is a 3 element array, each element of which is 4 element array and so on. 
	5. arrange - `numpy.arange([start, ]stop, [step, ], dtype=None) -> numpy.ndarray` 
	6.  
	7. How is arrange different from linspace. Linspace may or may not include the `end` while Arange never includes. Next Arange can take one argument `stop, start defaults to 0 and step defaults to 1` or two arguments `start and stop, step defaults to 1` 
	8. `logspace` values are spaced logarithemically. 
	9. `geomspace` values are spaced geometrically. 
	10.  Random number generation -  **random** library - example  `p = np.random.randint(10, 100, 9)`
	11.  Create from a string using - `a = np.fromstring('20 30 40 90', dtype=np.int, sep=' ')` cre
	12. Another ways is to use the fill method - ``numpy.``full`(_shape_, _fill_value_, _dtype=None_, _order='C'_)`

5. **Array attributes** - `a.size, shape, ndim, itemsize, dtype, nbytes` ndim 
6. **Array slicing -** 
	1. `newarr = oldarr[start : end : step]` THe defaults are 0 for start, arr.length() for end and 1 for step. Both the start index is included and **the end index is excluded**.  example `print(a[1:5:2])`
	2.  negative indexing exists. 
	3.  Slicing 2d arrays - `newarr = old[arraySelection, itemSelection]` e.g. `newarr = arr[0:1, 2]` for all the elements 0 to 1, tget the $2^{th}$ element. 
7. **Reshape , Resize , Arange**
	6. Reshape  creates a new array. Resize changes to original. Linspace
	7. `np.reshape(array, commands)`
	8. `n = n.reshape(rows, cols)` 
	9. `n = resize(row, cols)`
	10.**swap axes ** this si transpose. `a.swapaxes(0,1)` 
8. Mathematical Operations 
	1. `a.min(), a.max(), a.mean(), a.std()`
	2. `a.var() # variance`
	3. `print(g.argmin())      # index of min element`
	4. `print(g.argmax())      # index of max element`
	5. `print(g.argsort())     # returns array of indices that would put the array in sorted order`
	6. find where the min max occurs `a.argmax(), a.argmin()` 
	7. `resize` and `reshape` helps in sizing. 
	8. variables point to original array. `r.copy()` creates a new matrix. 
	9. `r.reshape(4)` creates a 4x4 array. 
	10. conditional assignment - `a[a>20] = 20` sets all items > 20 to 20. 
	11.**Column operations** -   
9. NaN -  this is not a number. 
	1. Methods `np.isnan(var) = True` if it is a NaN
	2. `np.nan == None` returns false
	3. `np.nan == np.nan` returns false.
	4. 
10. Optimization - 
	1. default data types are int32 and int64. these consume lots of memory. instead consider lower types if required `d = np.arange(0,100, dtype='int8')`
11.  I/O
	1. `f = np.loadtxt('filedata.txt', skiprows=1, delimiter=',', dtype=np.int32)`
	2. saving `np.savetxt('data2.txt', f, delimiter=';', fmt='%d', header='a;b;c;d;e;f;g;h;i;j', comments='')`
12.  **Distributions in numpy**
	1. Binomial distributions 
	2. 
14. 
<!--stackedit_data:
eyJoaXN0b3J5IjpbNTA3NDk4NjkwLDUwNTg0NzA0LDIwNzg4OD
c5MTIsNTA4ODIxNywtMzU1MjgzNTI1LDQwMTYwMDM2LC0xNzE1
MDQ2MjgzLDk3NTA2MDMyMCwtMTY5MTQ0MDUzNywtMzE4MDMyMC
wxMzY2MjE0NDAxXX0=
-->
# Pandas
1. Essentially 3 data structures, series, dataframe, panels
	1. Series is 1d, like a column, 
	3. Datapframe is like 2d, worksheet
	4. Panel is 3d, like a excel file, multiple worksheets.
2. importing - `import pandas as pd`
3. 
## Series

1. take help `pd.Series?`
2. This is a list, it can either Stirings or numebrs  or both. It has index and a label. Index is integer sequence and starts with 0, while label is another set of strings making this a key value pair. 
3. Define - 
	1. `animals = ["tiger", "bear", "moose"]` 
	2. make it mixed `animals = ["tiger", "bear", 1, None]` 
	3. Note for both cases when it is string and it is mixed, the underlying type is `dtype: object`
	4. Printing `pd.Series(animals)`or `s.head()`
	5.  Creating using labels `animals = ["tiger", "bear", "moose"]` 
	6.  Defining a series with existing list or tuple or  dictionary. 
```
# Defining using dic
L = ['a', 'b', 'c']
t = ('a', 'b', 'c')
d = {'Kite': 'paper',
          'Chair': 'wood',
          'Notebook': 'paper',
          'Mirror': 'glass'}
s = pd.Series(L or t or d) # all works
s #print it. 
``` 
  7. - Continued 
     7. creating from random.  `s = pd.series(np.random.randint(0, 1000, 10000))`
     9. 
   	  

4.  Defining index in series. 
	1. Index is a list so would be defined by `[]` and can contain only strings. 
	2. If List or tuple is being used index would have to contain exact number of arguments. 
	3. If dict is being used index is already defined as the keys of ht edict and those are used. This is like a query and not a creation. 
5.  Query - either by index or index label.  There are two attributes to do this `iloc` and `loc` MNote these are not methods. They are attributes so usages are `s.iloc[3] or s.loc['Notebook']`
	 1. `s.iloc['2']` is error as we require int here as these are index. 
	 2. `s.['3']` can work on dictionary having key `'3'` else it will throw error.
	 3. There is confusion if we are trying to index or we are referrind to keys, hence it isbetter to use loc and iloc. 
	 4. 
6. Working witht he series
	1.  Do not iterate, use Vector methods
	2.  use numpy for the methods and pass them the series `import numpy as np`  `total = np.sum(s)` gives us summ of all numbers of s. Similarly `mean, min, max, std`
	3. `s+=2` increases all elements by 2, similary `-=, *= /=`
	4. `len(s)` gives the length of s

## Assorted points

1. `res=census_df[['SUMLEV', 'STNAME', 'CENSUS2010POP']]` this gives a view of the nesseary things, is very handy. 
2. `res = res[['SUMLEV' =50]]` WHERE CLAUSE
 

3. 
 
<!--stackedit_data:
eyJoaXN0b3J5IjpbMTE5Mjg2MzE4MiwtMTEzMTE5ODY1NSwtOD
YwNDQxMDk2LDU1ODcyMjQ5Nyw5MDM3MTk3NDAsLTE2NjcyMzAx
MTQsLTgxNjU3Mzc4NywtMjU0Mjg3NDIzLC00Nzk1MzI3OTgsNT
Y3MDgyNzQ3XX0=
-->
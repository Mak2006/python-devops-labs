1. Input output to terminals. 
	    1. This is done by print and input() and is the basic way from stdin. 
2.  To and from CSV files
    1.  `import csv`
    2.  Open the file -  `csvfile = open('file.csv')`
    3.  Create the list data structure  `csvvar = list(csv.DictReader(file));`
    5. Gernaer operations
         1.   csvvar[0].keys() gives the list of keys. 
         2. `len(csvvar)` gives the length
     3. Row operations - `for row in csv:` This row is a dictioary.
     4.  Column operation - iterate over the rows and pic the correct column using row['col_name'] `for row in csvvar:     k += float(row['col_name']);` 
         1.  easier - `sum(float(d['cty']) for d in mpg) / len(mpg)` 
     6. 
3.  To and from XML files
4.  To images
5.  General file operations = read and write
	1. `file = open('name.txt')`
	2. `print(file.readline())` # read a line
	3. `print(file.read())` # read till the end
	4. `line.strip()` removes the new line fromt heend.
	5. `file.close()` closes th file pointer and **to flush the buffer.**
	6.  open modes - r, w, a, r+  - read, write, append, read & write. `open('file', 'r+')`
	7. writing files = `file.write(str)`
	8. [Official doc](https://docs.python.org/3/library/functions.html#open)
	9.  Example code
```
new_guests = ["Sam", "Danielle", "Jacob"]

with open("guests.txt", 'a') as guests:
    for i in new_guests:
        guests.write(i + "\n")

guests.close()	
```

7.
	10. Renaming and permissions. 
	11. `import os`
	12. `os.remove('file')`
	13. `os.rename('oldname', 'newname')` 
	14.  `os.path.isfile('filename')` retuns true if file exists.
	15.  size  - `os.path.getsize('filename')` gives the size. Note the arg is not a file var.
	16.  timestamp since jan 1970 - `timestamp = os.path.getmtime('file')` 
	17. `import datetime`
	`datetime.datetime.fromtimestamp(timestamp)`
	19. 
17. Directory manipulation 
		1. `print(os.getcwd())` pwd equivalent, current wd.
		2. `os.mkdir('newdir')` #mkdir
		3. `os.chdir('dir')`  #cd 
		4. `os.rmdir('newdir')`  #empty deletion
		5. `os.listdir('newdir')`  #ls
		6.  for the slash problem  use `os.path.join('file')`
		7. 
18.  Example to create a dire and file 
The new_directory function creates a new directory inside the current working directory, then creates a new empty file inside the new directory, and returns the list of files in that directory. Fill in the gaps to create a file "script.py" in the directory "PythonPrograms".
```
import os

def new_directory(directory, filename):
  # Before creating a new directory, check to see if it already exists
  if os.path.isdir(directory) == False:
     os.mkdir(directory)
    
  #cd 
  #os.chdir(directory)

  # Create the new file inside of the new directory
  os.chdir(directory)
  with open ("script.py", 'w') as file:
    pass
  file.close()

  # come out
  
  # Return the list of files in the new directory
  return os.listdir('.')

print(new_directory("PythonPrograms", "script.py"))
```
20.  Example 
The file_date function creates a new file in the current working directory, checks the date that the file was modified, and returns just the date portion of the timestamp in the format of yyyy-mm-dd. Fill in the gaps to create a file called "newfile.txt" and check the date that it was modified.

```
import os
import datetime

def file_date(filename):
  # Create the file in the current directory
  with open(filename, "w") as fva:
    #fva.write(comments)
    #filesize = os.stat(filename).st_size
    fva.close()
    
  timestamp = os.path.getmtime(filename)
  # Convert the timestamp into a readable format, then into a string
  timestamp = datetime.datetime.fromtimestamp(timestamp)
  print(timestamp)
  k = str(timestamp )
  # Return just the date portion 
  # Hint: how many characters are in “yyyy-mm-dd”? 
  return k.split(' ')[0] # ("{___}".format(___))

print(file_date("newfile.txt")) 
# Should be today's date in the format of yyyy-mm-dd
```

### CSV file manipulations 
23. `import csv` 
24. `f = open('file')`
25. `csvf = csv.reader(f)` # use the csv reader
26. Reading rows
```
for row in csvf:
	col1, col2, col3 = row # exact num of cols req. 
	print("Col1 {}, Col2 {}, Col3 {}".format(col1,col2,col3))
	#row
```
27.  Generate - have a 2d array data = [[], []] ... 
	`writerow` or `writerows` example
```
with open('x.csv', 'w') as file_csv:
	writer = csv.writer(file_csv)
	writer.writerows(data)

```
28.  Use the `DictReader` and `DictWriter`
29. Example 
We're working with a list of flowers and some information about each one. The create_file function writes this information to a CSV file. The contents_of_file function reads this file into records and returns the information in a nicely formatted block. Fill in the gaps of the contents_of_file function to turn the data in the CSV file into a dictionary using DictReader.

```
import os
import csv

# Create a file with data in it
def create_file(filename):
  with open(filename, "w") as file:
    file.write("name,color,type\n")
    file.write("carnation,pink,annual\n")
    file.write("daffodil,yellow,perennial\n")
    file.write("iris,blue,perennial\n")
    file.write("poinsettia,red,perennial\n")
    file.write("sunflower,yellow,annual\n")
  file.close()


# Read the file contents and format the information about each row
def contents_of_file(filename):
  return_string = ""

  # Call the function to create the file 
  create_file(filename)

  # Open the file
  with open(filename, "r") as file:
    # Read the rows of the file into a dictionary
    reader = csv.DictReader(file)
    # Process each item of the dictionary
    for row in reader:
      return_string += "a {} {} is {}\n".format(row["color"], row["name"], row["type"])
  return return_string

#Call the function
print(contents_of_file("flowers.csv"))
```
31. 
<!--stackedit_data:
eyJoaXN0b3J5IjpbLTEzNzMxNzY3ODUsLTM3NzIxMDA2LDIwMD
QxMzg3MzgsMTA1OTAyNTk0MiwtMTk0NjgxMTM1NSwxMzU0OTg0
MDU2LDQyMDM0NTAxOSw1Mzg2NzczMDUsLTM3ODA0NTQ3OSwtMT
MzMjAzMTM0NywyMTI3NzczMDE0LDMyOTU3OTE1MV19
-->
# Vi commands
1. **Good resources**
		1. [Atmos](http://www.atmos.albany.edu/daes/atmclasses/atm350/vi_cheat_sheet.pdf)
		2. [CCSF](https://www.ccsf.edu/Pub/Fac/vi.html)
2. **Abbreviations** - 
	2. esc - em = escape mode, col - cursor on line.  ct - ctrl, i - im = insert mode
3.  **Env set up**
		1. .cshrc, .vimrc, .bashrc - save the commands
		2. em :setnu/
4. **Small navigation within the file** - 
		1. em H/M/L - go to upper left, middle, lower right
		2. em h/j/k/l - move left, down, up, right
		3. em ^/$ - beginning or end of line
		4. em w/b - one word forward or backword
5. **Large navigations within a file**
		1.  ct d/u/ scroll down/up half a screen
		2.  em G/nG/:n go to last/nth/nth line
6. **Start to write**
		1. em i/a - write before/after cursor
		2. em o/O - write above/below the line at cursore

7. **copy and paste.**  
	1. from external - depending on shell, ctrl v ctrl c works, however shift insert and ctrl insert also works. 
	2. **internal** - this is yanking - 
	3. em - xyy - p/P - x number of lines, p is paste before theline and P is after the line. 
	4. **copying a partial line **em -yfc - p : where you are copying from cursor to the char 'c'
8. **Deletion** - 
	1. em - d0 - delete from cursor to begining
	2. em - d$ will delete from current position to end of line.
	3. dw deletes current to end of current word (including trailing space) 
9. **Indentation**
	3. escape mode, col, 2>> indents to lines to right
	4. em, col, 2<< - shift two lines to left
10. Undo - em u - undo last change
11. **Nerd**
		4. em :r file - insert file at cursor 
12.  **save**
	1. em - :wq - write and quit
14. 
Commands for vi and nano and sublime


<!--stackedit_data:
eyJoaXN0b3J5IjpbLTE3NTMzMzQ1MjgsMTA2NDc1NTgwOF19
-->
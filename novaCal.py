import sys
import tkinter
import calendar

year = int(sys.argv[1])

root = tkinter.Tk()
root.title("Calendars")

def jan():
	print(calendar.TextCalendar(firstweekday=6).formatmonth(year,1,0,0))

def feb():
	print(calendar.TextCalendar(firstweekday=6).formatmonth(year,2,0,0))

def mar():
	print(calendar.TextCalendar(firstweekday=6).formatmonth(year,3,0,0))

def apr():
	print(calendar.TextCalendar(firstweekday=6).formatmonth(year,4,0,0))

def may():
	print(calendar.TextCalendar(firstweekday=6).formatmonth(year,5,0,0))

def jun():
	print(calendar.TextCalendar(firstweekday=6).formatmonth(year,6,0,0))

def jul():
	print(calendar.TextCalendar(firstweekday=6).formatmonth(year,7,0,0))

def aug():
	print(calendar.TextCalendar(firstweekday=6).formatmonth(year,8,0,0))

def sep():
	print(calendar.TextCalendar(firstweekday=6).formatmonth(year,9,0,0))

def oct():
	print(calendar.TextCalendar(firstweekday=6).formatmonth(year,10,0,0))

def nov():
	print(calendar.TextCalendar(firstweekday=6).formatmonth(year,11,0,0))

def dec():
	print(calendar.TextCalendar(firstweekday=6).formatmonth(year,12,0,0))

january = tkinter.Button(root,text="January "+str(year),command=jan)
february = tkinter.Button(root,text="February "+str(year),command=feb)
march = tkinter.Button(root,text="March "+str(year),command=mar)
april = tkinter.Button(root,text="April "+str(year),command=apr)
may = tkinter.Button(root,text="May "+str(year),command=may)
june = tkinter.Button(root,text="June "+str(year),command=jun)
july = tkinter.Button(root,text="July "+str(year),command=jul)
august = tkinter.Button(root,text="August "+str(year),command=aug)
september = tkinter.Button(root,text="September "+str(year),command=sep)
october = tkinter.Button(root,text="October "+str(year),command=oct)
november = tkinter.Button(root,text="November "+str(year),command=nov)
december = tkinter.Button(root,text="December "+str(year),command=dec)

january.pack()
february.pack()
march.pack()
april.pack()
may.pack()
june.pack()
july.pack()
august.pack()
september.pack()
october.pack()
november.pack()
december.pack()

root.mainloop()

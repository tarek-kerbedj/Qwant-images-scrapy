from tkinter import *
import subprocess
from tkinter import messagebox
from subprocess import *
from tkinter import ttk
from threading import Thread




root = Tk()
root.title('Qwant scraper')
textv = StringVar()
root.geometry('600x600')
my_label_frame=LabelFrame(root,text="Type your query")
my_label_frame.pack(pady=20)
      
entry = Entry(my_label_frame,width=80,textvariable=textv)
entry.pack()
def clear():
    text.delete(0,END)
   
button_frame=Frame(root)
button_frame.pack(pady=10)
search_button = Button(button_frame,text = 'Search',command=lambda :Thread(target=threaded_function()).start())
# clear the text in the search entry
clear_button = Button(button_frame,text = 'Clear',command=clear)

search_button.grid(row=0,column=0)
clear_button.grid(row=0,column=1)
text_frame=LabelFrame(root,text="Instructions")
text_frame.pack(pady=20)
text=Text(text_frame,width=120)
text.pack()
text.insert('1.0', 
'Step 1):Insert your search keywords seperated by commas eg:Kanye west,Sia\n\n\
Step 2):Press the search button and voilà\n\n\
All the query results will be saved in the same directory')
text.config(state=DISABLED)

        
        


  
def threaded_function():
        messagebox.showwarning("warning",'Warning: the program may appear to freeze during the crawling')
  
        process = subprocess.Popen(f"scrapy crawl images",stdin=PIPE)
        ls=bytes(textv.get(),'utf-8')      
        
        print(ls)
        process.communicate(ls)

        messagebox.showinfo("info", "Finished")
       
           

    

    




root.mainloop()



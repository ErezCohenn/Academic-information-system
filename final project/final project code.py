import pandas as pd
from tkinter import *
from tkinter import ttk
import numpy as np
import matplotlib.pyplot as plt
import tkinter.filedialog as FD
from PIL import ImageTk,Image
import matplotlib.patches as mpatches
from mpl_toolkits.mplot3d import Axes3D

window = Tk()
window.title('Analysis Students Program')
window.minsize(1000,450)

df = pd.read_csv("data.csv", index_col= 0)
rows, cols = df.shape
df['Annual average'] = ((df['Average A'])+(df['Average B']))/2

def submit3():
    if combo3_value.get() == "":
        pass
    else:
        window3 = Toplevel()
        Label(window3,text = combo3_value.get(), font = ('BN cloud',70)).pack()
        window3.mainloop()

def submit2():
    if combo2_value.get() == "":
        pass
    else:
        window3 = Toplevel()
        Label(window3,text = combo2_value.get(), font = ('BN cloud',70)).pack()
        window3.mainloop()

def submit():
    if combo1_value.get() == "הנדסת תעשייה וניהול":
        window2 = Toplevel()
        window2.minsize(1200,630)
        frame = Frame(window2)
        frame.place(relx=0.5, rely=0.1, relwidth=0.75, relheight=0.1, anchor='n')

        img1 = Image.open('open.jpg')
        img1 = img1.resize((20, 20), Image.ANTIALIAS)
        img1 = ImageTk.PhotoImage(img1)
        img2 = Image.open('save as.jpg')
        img2 = img2.resize((20, 20), Image.ANTIALIAS)
        img2 = ImageTk.PhotoImage(img2)
        img3 = Image.open('graph.jpg')
        img3 = img3.resize((20, 20), Image.ANTIALIAS)
        img3 = ImageTk.PhotoImage(img3)
        img4 = Image.open('calculator.jpg')
        img4 = img4.resize((20, 20), Image.ANTIALIAS)
        img4 = ImageTk.PhotoImage(img4)
        img5 = Image.open('Register.png')
        img5 = img5.resize((20, 20), Image.ANTIALIAS)
        img5 = ImageTk.PhotoImage(img5)

        def setMenu(win):
            menubar = Menu(win)

            Filemenu = Menu(menubar, bg = 'white')
            Filemenu.add_command(label="Open", command=OpenFile,image = img1,compound="left",accelerator="Ctrl+O")
            Filemenu.add_command(label="Save as", command=save_file,image = img2,compound="left",accelerator="Ctrl+S")
            Filemenu.add_separator()
            Filemenu.add_command(label="Exit", command=window2.destroy)
            menubar.add_cascade(label="File", menu= Filemenu)

            Candidatesmenu = Menu(menubar, bg = 'white')
            Candidatesmenu.add_command(label="Summarize grade Calculator", command=calculator,image = img4,compound="left")
            Candidatesmenu.add_command(label="Student Registration", command=register,image = img5,compound="left")
            menubar.add_cascade(label="Candidates Students", menu=Candidatesmenu)

            Amenu = Menu(menubar, bg = 'white')
            Amenu.add_command(label="Search Student", command=student, image = img2,compound="left")
            Amenu.add_separator()
            Amenu.add_command(label="1. Excellent students 2015-2020", command=graph1, compound="left", image=img3)
            Amenu.add_command(label="2. Final Average grades 2015-2020", command=graph2, compound="left", image=img3)
            Amenu.add_command(label="3. Physics grades 2015-2020", command=graph3,compound="left",image = img3)
            Amenu.add_command(label="4. Hedva grades 2015-2020", command=graph4, compound="left", image=img3)
            Amenu.add_command(label="5. Potentially failing students", command=graph5, compound="left", image=img3)
            Amenu.add_command(label="6. Summarized vs Annual average grade", command=graph6,compound="left",image = img3)
            Amenu.add_command(label="7. Evening studies vs Morning studies", command=graph7, compound="left",image=img3)
            Amenu.add_command(label="8. The effect of an English course on the annual average", command=graph8,compound="left",image = img3)
            Amenu.add_command(label="9. Hedva vs matriculation units in math", command=graph9,compound="left",image = img3)
            Amenu.add_command(label="10. Physics vs matriculation units in Physics", command=graph10,compound="left",image = img3)
            Amenu.add_command(label="11. Students who failed in core courses", command=graph11,compound="left",image = img3)
            Amenu.add_command(label="12. Number of students 2015-2020", command=graph12,compound="left",image = img3)
            Amenu.add_command(label="13. Histogram of annual grades", command=graph13,compound="left",image = img3)
            Amenu.add_command(label="14. 3D annual grades semester A/B", command=graph14,compound="left",image = img3)
            menubar.add_cascade(label="Year A", menu=Amenu)

            Bmenu = Menu(menubar, bg = 'white')
            Bmenu.add_command(label="Search Student", command=donothing, image = img2,compound="left")
            Bmenu.add_separator()
            Bmenu.add_command(label="1. Excellent students 2015-2020", command=donothing, compound="left", image=img3)
            Bmenu.add_command(label="2. Final Average grades 2015-2020", command=donothing, compound="left", image=img3)
            Bmenu.add_command(label="3. Physics grades 2015-2020", command=donothing,compound="left",image = img3)
            Bmenu.add_command(label="4. Hedva grades 2015-2020e", command=donothing, compound="left", image=img3)
            Bmenu.add_command(label="5. Potentially failing students", command=donothing, compound="left", image=img3)
            Bmenu.add_command(label="6. Summarized vs Annual Average Grade", command=donothing,compound="left",image = img3)
            Bmenu.add_command(label="7. Evening studies vs Morning studies", command=donothing, compound="left",image=img3)
            Bmenu.add_command(label="8. The effect of an English course on the annual average", command=donothing,compound="left",image = img3)
            Bmenu.add_command(label="9. Hedva vs matriculation units in math", command=donothing,compound="left",image = img3)
            Bmenu.add_command(label="10. Physics vs matriculation units in Physics", command=donothing,compound="left",image = img3)
            Bmenu.add_command(label="11. Students who failed in core courses", command=donothing,compound="left",image = img3)
            Bmenu.add_command(label="12. Number of students 2015-2020", command=donothing,compound="left",image = img3)
            Bmenu.add_command(label="13. Histogram of annual grades", command=donothing,compound="left",image = img3)
            Bmenu.add_command(label="14. 3D annual grades semester A/B", command=donothing,compound="left",image = img3)
            menubar.add_cascade(label="Year B", menu=Bmenu)

            Cmenu = Menu(menubar, bg = 'white')
            Cmenu.add_command(label="Search Student", command=donothing, image = img2,compound="left")
            Cmenu.add_separator()
            Cmenu.add_command(label="1. Excellent students 2015-2020", command=donothing, compound="left", image=img3)
            Cmenu.add_command(label="2. Final Average grades 2015-2020", command=donothing, compound="left", image=img3)
            Cmenu.add_command(label="3. Physics grades 2015-2020", command=donothing,compound="left",image = img3)
            Cmenu.add_command(label="4. Hedva grades 2015-2020", command=donothing, compound="left", image=img3)
            Cmenu.add_command(label="5. Potentially failing students", command=donothing, compound="left", image=img3)
            Cmenu.add_command(label="6. Summarized vs Annual Average Grade", command=donothing,compound="left",image = img3)
            Cmenu.add_command(label="7. Evening studies vs Morning studies", command=donothing, compound="left",image=img3)
            Cmenu.add_command(label="8. The effect of an English course on the annual average", command=donothing,compound="left",image = img3)
            Cmenu.add_command(label="9. Hedva vs matriculation units in math", command=donothing,compound="left",image = img3)
            Cmenu.add_command(label="10. Physics vs matriculation units in Physics", command=donothing,compound="left",image = img3)
            Cmenu.add_command(label="11. Students who failed in core courses", command=donothing,compound="left",image = img3)
            Cmenu.add_command(label="12. Number of students each year", command=donothing,compound="left",image = img3)
            Cmenu.add_command(label="13. Histogram of annual grades", command=donothing,compound="left",image = img3)
            Cmenu.add_command(label="14. 3D annual grades semester A/B", command=donothing,compound="left",image = img3)
            menubar.add_cascade(label="Year C", menu=Cmenu)

            Dmenu = Menu(menubar, bg = 'white')
            Dmenu.add_command(label="Search Student", command=donothing, image = img2,compound="left")
            Dmenu.add_separator()
            Dmenu.add_command(label="1. Excellent students 2015-2020", command=donothing, compound="left", image=img3)
            Dmenu.add_command(label="2. Final Average grades 2015-2020", command=donothing, compound="left", image=img3)
            Dmenu.add_command(label="3. Physics grades 2015-2020", command=donothing,compound="left",image = img3)
            Dmenu.add_command(label="4. Hedva grades 2015-2020", command=donothing, compound="left", image=img3)
            Dmenu.add_command(label="5. Potentially failing students", command=donothing, compound="left", image=img3)
            Dmenu.add_command(label="6. Summarized vs Annual Average Grade", command=donothing,compound="left",image = img3)
            Dmenu.add_command(label="7. Evening studies vs Morning studies", command=donothing, compound="left",image=img3)
            Dmenu.add_command(label="8. The effect of an English course on the annual average", command=donothing,compound="left",image = img3)
            Dmenu.add_command(label="9. Hedva vs matriculation units in math", command=donothing,compound="left",image = img3)
            Dmenu.add_command(label="10. Physics vs matriculation units in Physics", command=donothing,compound="left",image = img3)
            Dmenu.add_command(label="11. Students who failed in core courses", command=donothing,compound="left",image = img3)
            Dmenu.add_command(label="12. Number of students 2015-2020", command=donothing,compound="left",image = img3)
            Dmenu.add_command(label="13. Histogram of annual grades", command=donothing,compound="left",image = img3)
            Dmenu.add_command(label="14. 3D annual grades semester A/B", command=donothing,compound="left",image = img3)
            menubar.add_cascade(label="Year D", menu=Dmenu)

            win.config(menu=menubar)
            window2.bind("<Control-s>", save_file)
            window2.bind("<Control-o>", OpenFile)

        def donothing():
          return

        def register():
            def save_info():
                try:
                    with open('New_Student.txt', 'a') as f:
                        f.write('\n')
                        f.write('Student ID: ' + str(ID_entry.get()) + '\n')
                        f.write('Year: ' + str(Year_entry.get()) + '\n')
                        f.write('Faculty: ' + str(fac_entry.get()) + '\n')
                        f.write('Class: ' + str(class_entry.get()) + '\n')
                        f.write('Matriculation units in Math: ' + str(Math_entry.get()) + '\n')
                        f.write('Matriculation units in Pyhsics: ' + str(Physic_entry.get()) + '\n')
                        f.write('English level (0-5): ' + str(eng_entry.get()) + '\n')
                        f.write('Summarize grade: ' + str(Summarize_entry.get()) + '\n')

                except IOError as e:
                    print(e)
                    lbl = Label(screen, text='Registration failed', bg='red', width="30", height="1", font = ('GISHA bold',9))
                    lbl.place(x=122, y=520)
                else:
                    lbl = Label(screen, text='Registration completed', bg='green', width="30", height="1", font = ('GISHA bold',9))
                    lbl.place(x=122, y=520)

            screen = Tk()
            screen.geometry("500x550")
            screen.title("Registration Form")
            heading = Label(screen,text="Form", bg="cornflowerblue", fg="black", width="500", height="3")
            heading.pack()

            ID_text = Label(screen,text="Student ID: ", )
            Year_text = Label(screen,text="Year: ", )
            fac_text = Label(screen,text="Faculty: ", )
            class_text = Label(screen,text='Class: ')
            Math_text = Label(screen,text='Matriculation units in Math: ')
            Pyhsic_text = Label(screen,text='Matriculation units in Pyhsics: ')
            eng_text = Label(screen,text='English level (0-5): ')
            Summarize_text = Label(screen,text='Summarize grade: ')

            ID_text.place(x=15, y=70)
            Year_text.place(x=260, y=70)
            fac_text.place(x=15, y=180)
            class_text.place(x=260, y=180)
            Math_text.place(x=15, y=290)
            Pyhsic_text.place(x=260, y=290)
            eng_text.place(x=15, y=400)
            Summarize_text.place(x=260, y=400)

            ID_entry = Entry(screen,width="30")
            Year_entry = Entry(screen,width="30")
            fac_entry = Entry(screen,width="30")
            class_entry = Entry(screen,width="30")
            Math_entry = Entry(screen,width="30")
            Physic_entry = Entry(screen,width="30")
            eng_entry = Entry(screen,width="30")
            Summarize_entry = Entry(screen,width="30")

            ID_entry.place(x=15, y=100)
            Year_entry.place(x=260, y=100)
            fac_entry.place(x=15, y=210)
            class_entry.place(x=260, y=210)
            Math_entry.place(x=15, y=320)
            Physic_entry.place(x=260, y=320)
            eng_entry.place(x=15, y=430)
            Summarize_entry.place(x=260, y=430)

            register = Button(screen, text="Register", width="30", height="2", command=save_info, bg="cornflowerblue")
            register.place(x=120, y=470)
            screen.mainloop()

        def calculator():
            def calcu():
                x = (int(txt.get())*0.7)/10+(int(txt2.get())*0.3)
                if x >= 70:
                    Label(window6,bg = 'green', text='The summary grade is: ' + str(x),font = (16)).grid(column=0, row=3, columnspan=2)
                else:
                    Label(window6, bg='red', text='The summary grade is: ' + str(x), font=(16)).grid(column=0, row=3, columnspan=2)
            window6 = Tk()
            window6.geometry("450x130")
            Label(window6, text='Psychometric score: ',font = (18)).grid(column=0, row=0)
            txt = Entry(window6,font = (18))
            txt.grid(column=1, row=0)
            Label(window6, text='Average matriculation: ',font = (18)).grid(column=0, row=1)
            txt2 = Entry(window6,font = (18))
            txt2.grid(column=1, row=1)
            Button(window6,text = 'Calculate',command = calcu,bg = 'cornflowerblue',font = (18)).grid(column = 0, row = 2, columnspan = 2)
            window6.mainloop()

        def student():
            rows, cols = df.shape
            def search1():
                for i in range(rows):
                    if int(txt.get()) != df.loc[i,'Students ID']:
                        Label(window6,text = 'Student does not exsit', bg = 'red',font = (15)).grid(column=0, row=1,columnspan = 3)
                    else:
                        x = df.loc[:, 'Year':][df['Students ID'] == int(txt.get())]
                        y = x.index.values.astype(int)[0]
                        lst = []
                        for i in x:
                            z = x.loc[y, i]
                            lst.append(z)
                        print(lst)
                        fig ,(ax1,ax2,ax3) = plt.subplots(nrows =3, ncols= 1,figsize = (15,5))
                        fig.suptitle('Student ID : '+txt.get()+'\n'+'Year: '+str(lst[0]))
                        ax1.scatter(x=df.columns[2:6],y=lst[1:5])
                        ax2.plot(df.columns[6:14],lst[5:13])
                        ax3.plot(df.columns[14:], lst[13:])
                        ax2.set_ylabel('Data')
                        ax3.set_xlabel('Category')
                        plt.show()
            window6 = Tk()
            Label(window6, text = 'Student ID: ',font = (20)).grid(column = 0,row = 0)
            txt = Entry(window6,font = (20))
            txt.grid(column=1, row=0)
            Button(window6, text='Search',command = search1, bg = 'cornflowerblue',font = (20)).grid(column=2, row=0)
            lbly = Label(window6, text='').grid(column=0, row=1)
            window6.mainloop()

        def save_file(event=None):
            file_name = FD.asksaveasfilename()
            if file_name:
                print(file_name)

        def OpenFile(event=None):
            file = FD.askopenfilename(initialdir="/",
                                      filetypes=(("CSV files", "*.csv"), ('Python Files','*.py'),("All Files", "*.*")),
                                      title="Choose a file")
            try:
                with open(file, 'r') as f:
                    print(f.read())
            except:
                print("Failed to open File")

        def autolabel(ax, rects):
            first = True
            for rect in rects:
                height = rect.get_height()
                if first:
                    xy = (rect.get_x() + rect.get_width()) / 2, height
                    first = False
                else:
                    xy = rect.get_x() + rect.get_width(), height
                ax.annotate(height, xy=xy,
                            xytext=(0, 3), textcoords="offset points", ha='center', va='bottom')
                
        def graph1():  
        
            total2015 = (df['Annual average'][df['Year']==2015]) >= 85
            num_Excellent_2015= total2015.value_counts().tolist()[1]

            total2015 = (df['Annual average'][df['Year']==2016]) >= 85
            num_Excellent_2016= total2015.value_counts().tolist()[1]

            total2015 = (df['Annual average'][df['Year']==2017]) >= 85
            num_Excellent_2017= total2015.value_counts().tolist()[1]

            total2015 = (df['Annual average'][df['Year']==2018]) >= 85
            num_Excellent_2018= total2015.value_counts().tolist()[1]

            total2015 = (df['Annual average'][df['Year']==2019]) >= 85
            num_Excellent_2019= total2015.value_counts().tolist()[1]

            total2015 = (df['Annual average'][df['Year']==2020]) >= 85
            num_Excellent_2020= total2015.value_counts().tolist()[1]



            labels = ['2015', '2016', '2017', '2018', '2019','2020']
            Average_A = [num_Excellent_2015, num_Excellent_2016, num_Excellent_2017, num_Excellent_2018, num_Excellent_2019, num_Excellent_2020]

            x = np.arange(len(labels)) 
            width = 0.2  

            fig, ax = plt.subplots(figsize=(10,5), dpi= 70)
            rects1 = ax.bar(x, Average_A, width, color='orange', linewidth=1, alpha=0.7, label='Excellent students')

            ax.set_ylabel('Number of excellent students', fontdict={'size':15})
            ax.set_title('Number of excellent students during 2015-2020', fontdict={'size':15})
            ax.set_xticks(x)
            ax.set_xticklabels(labels,  fontdict={'horizontalalignment': 'right'})
            ax.legend()
            plt.show()
    
        def graph2():
                
            Average_A_2015 = (df['Average A'][df['Year']==2015]).mean()
            Average_A_2016 = (df['Average A'][df['Year']==2016]).mean()
            Average_A_2017 = (df['Average A'][df['Year']==2017]).mean()
            Average_A_2018 = (df['Average A'][df['Year']==2018]).mean()
            Average_A_2019 = (df['Average A'][df['Year']==2019]).mean()
            Average_A_2020 = (df['Average A'][df['Year']==2020]).mean()

            Average_B_2015 = (df['Average B'][df['Year']==2015]).mean()
            Average_B_2016 = (df['Average B'][df['Year']==2016]).mean()
            Average_B_2017 = (df['Average B'][df['Year']==2017]).mean()
            Average_B_2018 = (df['Average B'][df['Year']==2018]).mean()
            Average_B_2019 = (df['Average B'][df['Year']==2019]).mean()
            Average_B_2020 = (df['Average B'][df['Year']==2020]).mean()


            labels = ['2015', '2016', '2017', '2018', '2019','2020']
            Average_A = [Average_A_2015, Average_A_2016, Average_A_2017-5, Average_A_2018, Average_A_2019, Average_A_2020+10]
            Average_B = [Average_B_2015+5, Average_B_2016+10, Average_B_2017+5, Average_B_2018+10, Average_B_2019+5, Average_B_2020-5]

            x = np.arange(len(labels)) 
            width = 0.2  

            fig, ax = plt.subplots(figsize=(10,5), dpi= 70)
            rects1 = ax.bar(x - width, Average_A, width, label='Average A')
            rects2 = ax.bar(x + width, Average_B, width, label='Average B')

            ax.set_ylabel('Averages', fontdict={'size':15})
            ax.set_title('Final Average grades between 2015-2020 during the first year', fontdict={'size':15})
            ax.set_xticks(x)
            ax.set_xticklabels(labels)
            ax.legend()

            plt.show()
                
        def graph3():
               
            Physics0_2015 = (df['Physics0'][df['Year']==2015]).mean()
            Physics0_2016 = (df['Physics0'][df['Year']==2016]).mean()
            Physics0_2017 = (df['Physics0'][df['Year']==2017]).mean()
            Physics0_2018 = (df['Physics0'][df['Year']==2018]).mean()
            Physics0_2019 = (df['Physics0'][df['Year']==2019]).mean()
            Physics0_2020 = (df['Physics0'][df['Year']==2020]).mean()

            Physics1_2015 = (df['Physics1-B'][df['Year']==2015]).mean()
            Physics1_2016 = (df['Physics1-B'][df['Year']==2016]).mean()
            Physics1_2017 = (df['Physics1-B'][df['Year']==2017]).mean()
            Physics1_2018 = (df['Physics1-B'][df['Year']==2018]).mean()
            Physics1_2019 = (df['Physics1-B'][df['Year']==2019]).mean()
            Physics1_2020 = (df['Physics1-B'][df['Year']==2019]).mean()

            Physics2_2015 = (df['Physics2-B'][df['Year']==2015]).mean()
            Physics2_2016 = (df['Physics2-B'][df['Year']==2016]).mean()
            Physics2_2017 = (df['Physics2-B'][df['Year']==2017]).mean()
            Physics2_2018 = (df['Physics2-B'][df['Year']==2018]).mean()
            Physics2_2019 = (df['Physics2-B'][df['Year']==2019]).mean()
            Physics2_2020 = (df['Physics2-B'][df['Year']==2019]).mean()


            labels = ['2015', '2016', '2017', '2018', '2019','2020']
            Physics0 = [Physics0_2015, Physics0_2016, Physics0_2017, Physics0_2018, Physics0_2019, Physics0_2020]
            Physics1 = [Physics1_2015, Physics1_2016, Physics1_2017, Physics1_2018, Physics1_2019, Physics1_2020]
            Physics2 = [Physics2_2015, Physics2_2016, Physics2_2017, Physics2_2018, Physics2_2019, Physics2_2020]

            x = np.arange(len(labels)) 
            width = 0.2  

            fig, ax = plt.subplots(figsize=(10,5), dpi= 70)
            rects1 = ax.bar(x - width, Physics0, width, label='Grade in Physics0')
            rects2 = ax.bar(x + width, Physics1, width, label='Grade in Physics1')
            rects3 = ax.bar(x, Physics2, width, label='Grade in Physics2')

            ax.set_ylabel('Grades')
            ax.set_title('Grades in Physics in the last five years and the difference', fontdict={'size':15})
            ax.set_xticks(x)
            ax.set_xticklabels(labels)
            ax.legend(bbox_to_anchor = (0.55,0.2))

            plt.show()
        
        def graph4():

            Hedva0_2015 = (df['Hedva0'][df['Year']==2015]).mean()
            Hedva0_2016 = (df['Hedva0'][df['Year']==2016]).mean()
            Hedva0_2017 = (df['Hedva0'][df['Year']==2017]).mean()
            Hedva0_2018 = (df['Hedva0'][df['Year']==2018]).mean()
            Hedva0_2019 = (df['Hedva0'][df['Year']==2019]).mean()
            Hedva0_2020 = (df['Hedva0'][df['Year']==2020]).mean()

            Hedva1_2015 = (df['Hedva1-B'][df['Year']==2015]).mean()
            Hedva1_2016 = (df['Hedva1-B'][df['Year']==2016]).mean()
            Hedva1_2017 = (df['Hedva1-B'][df['Year']==2017]).mean()
            Hedva1_2018 = (df['Hedva1-B'][df['Year']==2018]).mean()
            Hedva1_2019 = (df['Hedva1-B'][df['Year']==2019]).mean()
            Hedva1_2020 = (df['Hedva1-B'][df['Year']==2019]).mean()

            Hedva2_2015 = (df['Hedva2-B'][df['Year']==2015]).mean()
            Hedva2_2016 = (df['Hedva2-B'][df['Year']==2016]).mean()
            Hedva2_2017 = (df['Hedva2-B'][df['Year']==2017]).mean()
            Hedva2_2018 = (df['Hedva2-B'][df['Year']==2018]).mean()
            Hedva2_2019 = (df['Hedva2-B'][df['Year']==2019]).mean()
            Hedva2_2020 = (df['Hedva2-B'][df['Year']==2019]).mean()


            labels = ['2015', '2016', '2017', '2018', '2019','2020']
            Hedva0 = [Hedva0_2015, Hedva0_2016, Hedva0_2017, Hedva0_2018, Hedva0_2019, Hedva0_2020]
            Hedva1 = [Hedva1_2015, Hedva1_2016, Hedva1_2017, Hedva1_2018, Hedva1_2019, Hedva1_2020]
            Hedva2 = [Hedva2_2015, Hedva2_2016, Hedva2_2017, Hedva2_2018, Hedva2_2019, Hedva2_2020]

            x = np.arange(len(labels)) 
            width = 0.2  

            fig, ax = plt.subplots(figsize=(10,5), dpi= 70)
            rects1 = ax.bar(x - width, Hedva0, width, label='Grade in Hedva0')
            rects2 = ax.bar(x + width, Hedva1, width, label='Grade in Hedva1')
            rects3 = ax.bar(x, Hedva2, width, label='Grade in Hedva2')

            ax.set_ylabel('Grades')
            ax.set_title('Grades in Hedva in the last 6 years and the difference', fontdict={'size':15})
            ax.set_xticks(x)
            ax.set_xticklabels(labels)
            ax.legend(bbox_to_anchor = (0.55,0.2))

            plt.show()

        def graph5():
            
            potentially_failing_students = df.loc[:][df['Annual average']<60]

            year_to_overall_average = {}
            for row in potentially_failing_students.iterrows():
                # Row is tuple of index to Series
                series = row[1]
                year = series['Year']
                if year not in year_to_overall_average:
                    year_to_overall_average[year] = 1
                else:
                    year_to_overall_average[year] += 1

            width = 0.2
            labels = list(range(2015, 2021))
            # Index used to shift bars along the X-axis
            index = 0
            fig, ax = plt.subplots(figsize=(12.5, 5))
            rects = []
            for label in labels:
                r1 = ax.bar(index, year_to_overall_average[label], width, label=label)
                rects += r1
                index += 1

            autolabel(ax, rects)
            # Add empty string to skip label on 0,0
            ax.set_xticklabels([""] + labels)
            ax.set_ylabel("Amount of Students")
            ax.set_xlabel("Year")
            ax.set_title("Potentially failing students by Year") 
            
            plt.show()

        def graph6():
            
            year_to_summarized_grade = {}
            year_to_average_grade = {}
            years = list(range(2015, 2021))
            for year in years:
                year_to_summarized_grade[year] = int(df["Summarize grade"][df["Year"] == year].mean())
                year_to_average_grade[year] = int(df["Annual average"][df["Year"] == year].mean())

            width = 0.2
            labels = years
            index = 0
            fig, ax = plt.subplots(figsize=(12.5, 5))
            rects = []
            for label in labels:
                r1 = ax.bar(index, year_to_summarized_grade[label], width, color="Blue")
                r2 = ax.bar(index + width, year_to_average_grade[label], width, color="Red")
                rects += r1
                rects += r2
                index += 1

            autolabel(ax, rects)
            ax.set_xticklabels([""] + labels)
            ax.set_ylabel("Grade")
            ax.set_xlabel("Year")
            ax.set_title("Summarized vs Overall Average Grade")
            red_patch = mpatches.Patch(color='red', label='Average Grade')
            blue_patch = mpatches.Patch(color='blue', label='Summarized Grade')
            plt.legend(handles=[red_patch, blue_patch], bbox_to_anchor=(1, 1), bbox_transform=plt.gcf().transFigure)
            
            plt.show()

        def graph7():
            
            y11 = int(df['Hedva1-A'][df['Path (M-0,E-1)'] == 0].mean())
            y12 = int(df['Hedva1-A'][df['Path (M-0,E-1)'] == 1].mean())
            y21 = int(df['Hedva2-A'][df['Path (M-0,E-1)'] == 0].mean())
            y22 = int(df['Hedva2-A'][df['Path (M-0,E-1)'] == 1].mean())
            y31 = int(df['Physics1-A'][df['Path (M-0,E-1)'] == 0].mean())
            y32 = int(df['Physics1-A'][df['Path (M-0,E-1)'] == 1].mean())
            y41 = int(df['Physics2-A'][df['Path (M-0,E-1)'] == 0].mean())
            y42 = int(df['Physics2-A'][df['Path (M-0,E-1)'] == 1].mean())
            y51 = int(df['Average A'][df['Path (M-0,E-1)'] == 0].mean())
            y52 = int(df['Average A'][df['Path (M-0,E-1)'] == 1].mean())
            y61 = int(df['Average B'][df['Path (M-0,E-1)'] == 0].mean())
            y62 = int(df['Average B'][df['Path (M-0,E-1)'] == 1].mean())
            y71 = int(df['Python-A'][df['Path (M-0,E-1)'] == 0].mean())
            y72 = int(df['Python-A'][df['Path (M-0,E-1)'] == 1].mean())

            width = 0.20
            labels = ['Hedva1', 'Hedva2', 'Physics1', 'Physics2','Python', 'Average 1st semster', 'Average 2nd semster']
            boker = [y11, y21, y31, y41, y71, y51, y61]
            erev = [y12, y22, y32, y42, y72, y52, y62]
            x = np.arange(len(labels))
            fig, ax = plt.subplots(figsize=(12.5, 5))
            rects1 = ax.bar(x - width / 2, boker, width, label='Morning')
            rects2 = ax.bar(x + width / 2, erev, width, label='Evening')

            def autolabel(rects):
                for rect in rects:
                    height = rect.get_height()
                    ax.annotate('{}'.format(height),
                                xy=(rect.get_x() + rect.get_width() / 2, height),
                                xytext=(0, 3),
                                textcoords="offset points",
                                ha='center', va='bottom')

            ax.set_ylabel('Average Grades')
            ax.set_title('Morning route vs Evening route grades')
            autolabel(rects1)
            autolabel(rects2)
            fig.tight_layout()
            ax.set_xticks(x)
            ax.set_xticklabels(labels)
            ax.legend(bbox_to_anchor=(-0.03, 1))
            plt.subplots_adjust(left=0.12)
           
            plt.show()

        def graph8():
            
            y11 = df['Annual average'][(df['English course (no-0,E-1)'] == 0) & (df['Year'] == 2020)].mean()
            y12 = df['Annual average'][(df['English course (no-0,E-1)'] == 1) & (df['Year'] == 2020)].mean()
            y21 = df['Annual average'][(df['English course (no-0,E-1)'] == 0) & (df['Year'] == 2019)].mean()
            y22 = df['Annual average'][(df['English course (no-0,E-1)'] == 1) & (df['Year'] == 2019)].mean()
            y31 = df['Annual average'][(df['English course (no-0,E-1)'] == 0) & (df['Year'] == 2018)].mean()
            y32 = df['Annual average'][(df['English course (no-0,E-1)'] == 1) & (df['Year'] == 2018)].mean()
            y41 = df['Annual average'][(df['English course (no-0,E-1)'] == 0) & (df['Year'] == 2017)].mean()
            y42 = df['Annual average'][(df['English course (no-0,E-1)'] == 1) & (df['Year'] == 2017)].mean()
            y51 = df['Annual average'][(df['English course (no-0,E-1)'] == 0) & (df['Year'] == 2016)].mean()
            y52 = df['Annual average'][(df['English course (no-0,E-1)'] == 1) & (df['Year'] == 2016)].mean()
            y61 = df['Annual average'][(df['English course (no-0,E-1)'] == 0) & (df['Year'] == 2015)].mean()
            y62 = df['Annual average'][(df['English course (no-0,E-1)'] == 1) & (df['Year'] == 2015)].mean()
            x = ['2015', '2016', '2017', '2018', '2019', '2020']
            eng1 = [y61, y51, y41, y31, y21, y11]
            eng2 = [y62, y52, y42, y32, y22, y12]
            plt.figure(figsize=(10, 5))
            plt.plot(x, eng1, '-.', c='teal', linewidth=2)
            plt.plot(x, eng2, '-.', c='olive', linewidth=2)
            plt.title('Annual average grades')
            plt.ylabel('Average grades')
            plt.legend({'Without English course', 'Includes an English course'})
            plt.show()

        def graph9():
            
            y11 = int(df['Hedva1-B'][(df['Bagrot math'] == 3) & (df['Year'] == 2015)].mean())
            y12 = int(df['Hedva1-B'][(df['Bagrot math'] == 4) & (df['Year'] == 2015)].mean())
            y13 = int(df['Hedva1-B'][(df['Bagrot math'] == 5) & (df['Year'] == 2015)].mean())
            y21 = int(df['Hedva1-B'][(df['Bagrot math'] == 3) & (df['Year'] == 2016)].mean())
            y22 = int(df['Hedva1-B'][(df['Bagrot math'] == 4) & (df['Year'] == 2016)].mean())
            y23 = int(df['Hedva1-B'][(df['Bagrot math'] == 5) & (df['Year'] == 2016)].mean())
            y31 = int(df['Hedva1-B'][(df['Bagrot math'] == 3) & (df['Year'] == 2017)].mean())
            y32 = int(df['Hedva1-B'][(df['Bagrot math'] == 4) & (df['Year'] == 2017)].mean())
            y33 = int(df['Hedva1-B'][(df['Bagrot math'] == 5) & (df['Year'] == 2017)].mean())
            y41 = int(df['Hedva1-B'][(df['Bagrot math'] == 3) & (df['Year'] == 2018)].mean())
            y42 = int(df['Hedva1-B'][(df['Bagrot math'] == 4) & (df['Year'] == 2018)].mean())
            y43 = int(df['Hedva1-B'][(df['Bagrot math'] == 5) & (df['Year'] == 2018)].mean())
            y51 = int(df['Hedva1-B'][(df['Bagrot math'] == 3) & (df['Year'] == 2019)].mean())
            y52 = int(df['Hedva1-B'][(df['Bagrot math'] == 4) & (df['Year'] == 2019)].mean())
            y53 = int(df['Hedva1-B'][(df['Bagrot math'] == 5) & (df['Year'] == 2019)].mean())
            y61 = int(df['Hedva1-B'][(df['Bagrot math'] == 3) & (df['Year'] == 2020)].mean())
            y62 = int(df['Hedva1-B'][(df['Bagrot math'] == 4) & (df['Year'] == 2020)].mean())
            y63 = int(df['Hedva1-B'][(df['Bagrot math'] == 5) & (df['Year'] == 2020)].mean())

            z11 = int(df['Hedva2-B'][(df['Bagrot math'] == 3) & (df['Year'] == 2015)].mean())
            z12 = int(df['Hedva2-B'][(df['Bagrot math'] == 4) & (df['Year'] == 2015)].mean())
            z13 = int(df['Hedva2-B'][(df['Bagrot math'] == 5) & (df['Year'] == 2015)].mean())
            z21 = int(df['Hedva2-B'][(df['Bagrot math'] == 3) & (df['Year'] == 2016)].mean())
            z22 = int(df['Hedva2-B'][(df['Bagrot math'] == 4) & (df['Year'] == 2016)].mean())
            z23 = int(df['Hedva2-B'][(df['Bagrot math'] == 5) & (df['Year'] == 2016)].mean())
            z31 = int(df['Hedva2-B'][(df['Bagrot math'] == 3) & (df['Year'] == 2017)].mean())
            z32 = int(df['Hedva2-B'][(df['Bagrot math'] == 4) & (df['Year'] == 2017)].mean())
            z33 = int(df['Hedva2-B'][(df['Bagrot math'] == 5) & (df['Year'] == 2017)].mean())
            z41 = int(df['Hedva2-B'][(df['Bagrot math'] == 3) & (df['Year'] == 2018)].mean())
            z42 = int(df['Hedva2-B'][(df['Bagrot math'] == 4) & (df['Year'] == 2018)].mean())
            z43 = int(df['Hedva2-B'][(df['Bagrot math'] == 5) & (df['Year'] == 2018)].mean())
            z51 = int(df['Hedva2-B'][(df['Bagrot math'] == 3) & (df['Year'] == 2019)].mean())
            z52 = int(df['Hedva2-B'][(df['Bagrot math'] == 4) & (df['Year'] == 2019)].mean())
            z53 = int(df['Hedva2-B'][(df['Bagrot math'] == 5) & (df['Year'] == 2019)].mean())
            z61 = int(df['Hedva2-B'][(df['Bagrot math'] == 3) & (df['Year'] == 2020)].mean())
            z62 = int(df['Hedva2-B'][(df['Bagrot math'] == 4) & (df['Year'] == 2020)].mean())
            z63 = int(df['Hedva2-B'][(df['Bagrot math'] == 5) & (df['Year'] == 2020)].mean())

            width = 0.20
            labels = ['2015', '2016', '2017', '2018', '2019', '2020']
            units31 = [y11, y21, y31, y41, y51, y61]
            units41 = [y12, y22, y32, y42, y52, y62]
            units51 = [y13, y23, y33, y43, y53, y63]
            units32 = [z11, z21, z31, z41, z51, z61]
            units42 = [z12, z22, z32, z42, z52, z62]
            units52 = [z13, z23, z33, z43, z53, z63]
            x = np.arange(len(labels))
            fig, (ax1, ax2) = plt.subplots(nrows=1, ncols=2, figsize=(12.5, 5))
            r1 = np.arange(len(units31))
            r2 = [x + width for x in r1]
            r3 = [x + width for x in r2]
            rects11 = ax1.bar(r1, units31, width, label='3 Unites')
            rects12 = ax1.bar(r2, units41, width, label='4 Unites')
            rects13 = ax1.bar(r3, units51, width, label='5 Unites')
            rects21 = ax2.bar(r1, units32, width, label='3 Unites')
            rects22 = ax2.bar(r2, units42, width, label='4 Unites')
            rects23 = ax2.bar(r3, units52, width, label='5 Unites')

            ax1.set_ylabel('Average Grades')
            fig.suptitle('Average grade in Hedva versus matriculation units in math')
            ax1.set_title('Hedva1')
            ax2.set_title('Hedva2')

            fig.tight_layout()
            ax1.set_xticks(x)
            ax1.set_xticklabels(labels)
            ax2.set_xticks(x)
            ax2.set_xticklabels(labels)
            ax1.legend(bbox_to_anchor=(-0.05, 1))
            plt.subplots_adjust(left=0.12, bottom=0.07, top=0.87, wspace=0.14)
            plt.show()

        def graph10():
            
            y11 = int(df['Physics2-B'][(df['Bagrot physics'] == 3) & (df['Year'] == 2015)].mean())
            y12 = int(df['Physics2-B'][(df['Bagrot physics'] == 4) & (df['Year'] == 2015)].mean())
            y13 = int(df['Physics2-B'][(df['Bagrot physics'] == 5) & (df['Year'] == 2015)].mean())
            y21 = int(df['Physics2-B'][(df['Bagrot physics'] == 3) & (df['Year'] == 2016)].mean())
            y22 = int(df['Physics2-B'][(df['Bagrot physics'] == 4) & (df['Year'] == 2016)].mean())
            y23 = int(df['Physics2-B'][(df['Bagrot physics'] == 5) & (df['Year'] == 2016)].mean())
            y31 = int(df['Physics2-B'][(df['Bagrot physics'] == 3) & (df['Year'] == 2017)].mean())
            y32 = int(df['Physics2-B'][(df['Bagrot physics'] == 4) & (df['Year'] == 2017)].mean())
            y33 = int(df['Physics2-B'][(df['Bagrot physics'] == 5) & (df['Year'] == 2017)].mean())
            y41 = int(df['Physics2-B'][(df['Bagrot physics'] == 3) & (df['Year'] == 2018)].mean())
            y42 = int(df['Physics2-B'][(df['Bagrot physics'] == 4) & (df['Year'] == 2018)].mean())
            y43 = int(df['Physics2-B'][(df['Bagrot physics'] == 5) & (df['Year'] == 2018)].mean())
            y51 = int(df['Physics2-B'][(df['Bagrot physics'] == 3) & (df['Year'] == 2019)].mean())
            y52 = int(df['Physics2-B'][(df['Bagrot physics'] == 4) & (df['Year'] == 2019)].mean())
            y53 = int(df['Physics2-B'][(df['Bagrot physics'] == 5) & (df['Year'] == 2019)].mean())
            y61 = int(df['Physics2-B'][(df['Bagrot physics'] == 3) & (df['Year'] == 2020)].mean())
            y62 = int(df['Physics2-B'][(df['Bagrot physics'] == 4) & (df['Year'] == 2020)].mean())
            y63 = int(df['Physics2-B'][(df['Bagrot physics'] == 5) & (df['Year'] == 2020)].mean())

            z11 = int(df['Physics1-B'][(df['Bagrot physics'] == 3) & (df['Year'] == 2015)].mean())
            z12 = int(df['Physics1-B'][(df['Bagrot physics'] == 4) & (df['Year'] == 2015)].mean())
            z13 = int(df['Physics1-B'][(df['Bagrot physics'] == 5) & (df['Year'] == 2015)].mean())
            z21 = int(df['Physics1-B'][(df['Bagrot physics'] == 3) & (df['Year'] == 2016)].mean())
            z22 = int(df['Physics1-B'][(df['Bagrot physics'] == 4) & (df['Year'] == 2016)].mean())
            z23 = int(df['Physics1-B'][(df['Bagrot physics'] == 5) & (df['Year'] == 2016)].mean())
            z31 = int(df['Physics1-B'][(df['Bagrot physics'] == 3) & (df['Year'] == 2017)].mean())
            z32 = int(df['Physics1-B'][(df['Bagrot physics'] == 4) & (df['Year'] == 2017)].mean())
            z33 = int(df['Physics1-B'][(df['Bagrot physics'] == 5) & (df['Year'] == 2017)].mean())
            z41 = int(df['Physics1-B'][(df['Bagrot physics'] == 3) & (df['Year'] == 2018)].mean())
            z42 = int(df['Physics1-B'][(df['Bagrot physics'] == 4) & (df['Year'] == 2018)].mean())
            z43 = int(df['Physics1-B'][(df['Bagrot physics'] == 5) & (df['Year'] == 2018)].mean())
            z51 = int(df['Physics1-B'][(df['Bagrot physics'] == 3) & (df['Year'] == 2019)].mean())
            z52 = int(df['Physics1-B'][(df['Bagrot physics'] == 4) & (df['Year'] == 2019)].mean())
            z53 = int(df['Physics1-B'][(df['Bagrot physics'] == 5) & (df['Year'] == 2019)].mean())
            z61 = int(df['Physics1-B'][(df['Bagrot physics'] == 3) & (df['Year'] == 2020)].mean())
            z62 = int(df['Physics1-B'][(df['Bagrot physics'] == 4) & (df['Year'] == 2020)].mean())
            z63 = int(df['Physics1-B'][(df['Bagrot physics'] == 5) & (df['Year'] == 2020)].mean())

            width = 0.20
            labels = ['2015', '2016', '2017', '2018', '2019', '2020']
            units31 = [y11, y21, y31, y41, y51, y61]
            units41 = [y12, y22, y32, y42, y52, y62]
            units51 = [y13, y23, y33, y43, y53, y63]
            units32 = [z11, z21, z31, z41, z51, z61]
            units42 = [z12, z22, z32, z42, z52, z62]
            units52 = [z13, z23, z33, z43, z53, z63]
            x = np.arange(len(labels))
            fig, (ax1, ax2) = plt.subplots(nrows=1, ncols=2, figsize=(12.5, 5))
            r1 = np.arange(len(units31))
            r2 = [x + width for x in r1]
            r3 = [x + width for x in r2]
            rects11 = ax1.bar(r1, units31, width, label='3 Unites')
            rects12 = ax1.bar(r2, units41, width, label='4 Unites')
            rects13 = ax1.bar(r3, units51, width, label='5 Unites')
            rects21 = ax2.bar(r1, units32, width, label='3 Unites')
            rects22 = ax2.bar(r2, units42, width, label='4 Unites')
            rects23 = ax2.bar(r3, units52, width, label='5 Unites')

            ax1.set_ylabel('Average Grades')
            fig.suptitle('Grade average in Physics versus matriculation units in Physics')
            ax1.set_title('Physics 1')
            ax2.set_title('Physics 2')

            fig.tight_layout()
            ax1.set_xticks(x)
            ax1.set_xticklabels(labels)
            ax2.set_xticks(x)
            ax2.set_xticklabels(labels)
            ax1.legend(bbox_to_anchor=(-0.05, 1))
            plt.subplots_adjust(left=0.12, bottom=0.07, top=0.87, wspace=0.14)
            plt.show()

        def graph11():
            
            lst = []
            for j in range(2015, 2021):
                count1 = 0
                for i in range(rows):
                    if df.loc[i, 'Hedva1-A'][df.loc[i, 'Year'] == j] < 60 and df.loc[i, 'Hedva1-B'][
                        df.loc[i, 'Year'] == j] < 60:
                        count1 += 1
                perc1 = (count1 / rows) * 100
                perc1 = "{:.2f}".format(perc1)
                lst.append(perc1)

            lst1 = []
            for j in range(2015, 2021):
                count1 = 0
                for i in range(rows):
                    if df.loc[i, 'Hedva2-A'][df.loc[i, 'Year'] == j] < 60 and df.loc[i, 'Hedva2-B'][
                        df.loc[i, 'Year'] == j] < 60:
                        count1 += 1
                perc1 = (count1 / rows) * 100
                perc1 = "{:.2f}".format(perc1)
                lst1.append(perc1)

            lst2 = []
            for j in range(2015, 2021):
                count1 = 0
                for i in range(rows):
                    if df.loc[i, 'Physics1-A'][df.loc[i, 'Year'] == j] < 60 and df.loc[i, 'Physics1-B'][
                        df.loc[i, 'Year'] == j] < 60:
                        count1 += 1
                perc1 = (count1 / rows) * 100
                perc1 = "{:.2f}".format(perc1)
                lst2.append(perc1)

            lst3 = []
            for j in range(2015, 2021):
                count1 = 0
                for i in range(rows):
                    if df.loc[i, 'Physics2-A'][df.loc[i, 'Year'] == j] < 60 and df.loc[i, 'Physics2-B'][
                        df.loc[i, 'Year'] == j] < 60:
                        count1 += 1
                perc1 = (count1 / rows) * 100
                perc1 = "{:.2f}".format(perc1)
                lst3.append(perc1)

            lst4 = []
            for j in range(2015, 2021):
                count1 = 0
                for i in range(rows):
                    if df.loc[i, 'Python-A'][df.loc[i, 'Year'] == j] < 60 and df.loc[i, 'Python-B'][
                        df.loc[i, 'Year'] == j] < 60:
                        count1 += 1
                perc1 = (count1 / rows) * 100
                perc1 = "{:.2f}".format(perc1)
                lst4.append(perc1)

            data = np.array([lst, lst1, lst2, lst3, lst4])
            data = np.asfarray(data, float)
            years = ['2015', '2016', '2017', '2018', '2019', '2020']
            courses = ['Hedva1', 'Hedva2', 'Physics1', 'Physics2', 'Python']

            fig, ax = plt.subplots(figsize = (9,5))
            im = ax.imshow(data, 'YlGn')

            cbar = ax.figure.colorbar(im, ax=ax)
            cbar.ax.set_ylabel('Percentage', rotation=-90, va="bottom")
            ax.set_xticks(np.arange(len(years)))
            ax.set_yticks(np.arange(len(courses)))
            ax.set_xticklabels(years)
            ax.set_yticklabels(courses)

            plt.setp(ax.get_xticklabels(), rotation=45, ha="right", rotation_mode="anchor")

            for i in range(len(courses)):
                for j in range(len(years)):
                    x = data[i,j]
                    y = str(x)+'%'
                    text = ax.text(j, i, y,
                                   ha="center", va="center", color="black")
            ax.set_title("Percentage of students who failed in core courses")
            fig.tight_layout()
            plt.subplots_adjust(top=0.92)
            plt.show()

        def graph12():
            
            def func(pct, allvals):
                absolute = int(pct / 100 * np.sum(allvals))
                return "{:d}".format(absolute)
            l1 = df['Year'].value_counts()
            values = list(l1)
            years = ['2019', '2017', '2015', '2020', '2016', '2018']
            fig, ax = plt.subplots()
            ax.pie(values, labels=years, colors=['teal', 'firebrick', 'darkorange', 'goldenrod', 'khaki', 'yellowgreen']
                   , autopct=lambda pct: func(pct, values), explode=(0.2, 0, 0, 0, 0, 0), shadow=True, startangle=90)
            ax.axis('equal')
            plt.tight_layout()
            ax.set_title('Number of students each year', fontsize=20)
            plt.subplots_adjust(top=0.85)
            plt.show()

        def graph13():
            df['Annual average'].hist()
            plt.ylabel('Frequency')
            plt.xlabel('Average')
            plt.title('Histogram')
            plt.show()

        def graph14():
            fig = plt.figure()
            ax = fig.add_subplot(111, projection='3d')
            ax.set_xlabel('Average B')
            ax.set_ylabel('Average A')
            ax.set_zlabel('Annual average')
            ax.scatter(df['Average B'], df['Average A'], df['Annual average'] ,  c='r', marker='^')
            plt.show()

        setMenu(window2)
        bg = PhotoImage(file='logo2.png')
        background_label = Label(window2, image=bg)
        background_label.place(relwidth=1, relheight=1)
        window2.mainloop()

    elif combo1_value.get() == "":
        pass
    else:
        window2 = Toplevel()
        Label(window2, text=combo1_value.get(), font=('BN cloud', 70)).pack()
        window2.mainloop()

image = ImageTk.PhotoImage(Image.open('logo6.jpg'))
lblImage = Label(window,image = image)
lblImage.place(relwidth=1, relheight=1)

combo1_value=StringVar()
combo2_value=StringVar()
combo3_value=StringVar()

lbl = Label(window,text = 'כלי לניתוח נתונים אקדמיים',relief = SOLID,padx = 50 , pady = 20, font = ('BN cloud',26),bg = 'whitesmoke', bd = 5, fg = 'firebrick').grid(column = 0 , row = 1, columnspan = 3,sticky = N)

lbl1 = Label(window,text = 'הפקולטה לעיצוב',bg = 'yellowgreen', fg = 'white', padx = 30, pady = 20,font = ('BN cloud',10),relief = RIDGE).grid(column = 0 , row = 2)
lbl2 = Label(window,text = 'הפקולטה להנדסה',bg = 'deepskyblue4', fg = 'white', padx = 30, pady = 20,font = ('BN cloud',10),relief = RIDGE).grid(column = 1 , row = 2)
lbl3 = Label(window,text = 'הפקולטה לאומנות',bg = 'chocolate1', fg = 'white', padx = 30, pady = 20,font = ('BN cloud',10),relief = RIDGE).grid(column = 2 , row = 2)
lbl4 = Label(window,text = ':בחר מחלקה מתוך הרשימה',relief = GROOVE, bg = 'white',font = ('BN cloud',8)).grid(column = 0, row = 3)
lbl5 = Label(window,text = ':בחר מחלקה מתוך הרשימה',relief = GROOVE, bg = 'white',font = ('BN cloud',8)).grid(column = 1, row = 3)
lbl6 = Label(window,text = ':בחר מחלקה מתוך הרשימה',relief = GROOVE, bg = 'white',font = ('BN cloud',8)).grid(column = 2, row = 3)
combo1 = ttk.Combobox(window,textvariable=combo1_value, values = ['','הנדסת חשמל ואלקטרוניקה','הנדסה כימית','הנדסת תוכנה','הנדסת תעשייה וניהול','הנדסת חומרים פולימרים']).grid(column = 1 , row = 4)
combo2 = ttk.Combobox(window, textvariable=combo3_value, values = ['','אומנות רב-תחומית']).grid(column = 2 , row = 4)
combo3 = ttk.Combobox(window, textvariable=combo2_value, values = ['','עיצוב תעשייתי','תקשורת חזותית','עיצוב אופנה','עיצוב טקסטיל','עיצוב תכשיטים','עיצוב פנים מבנה וסביבה']).grid(column = 0 , row = 4)

lbl4 = Label(window,text = '').grid(column = 1 , row = 7)
btn1 = Button(window,text = 'המשך',relief = SOLID, padx = 30, command = submit,font = 18).grid(column = 1 , row = 8)
btn2 = Button(window,text = 'המשך',relief = SOLID, padx = 30, command = submit2,font = 18).grid(column = 0 , row = 8)
btn3 = Button(window,text = 'המשך',relief = SOLID, padx = 30, command = submit3,font = 18).grid(column = 2 , row = 8)
window.call('wm', 'iconphoto', window._w, PhotoImage(file='logo.png'))
window.configure(bg = 'white')

for i in range(3):
    window.columnconfigure(i, weight=1, minsize=75)
    window.rowconfigure(i, weight=1, minsize=50)

window.mainloop()

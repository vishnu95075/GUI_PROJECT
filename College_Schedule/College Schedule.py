from tkinter import *
from time import strftime
from tkinter import Canvas, messagebox

if __name__ == '__main__':
    root = Tk()
    width = root.winfo_screenwidth()
    height = root.winfo_screenheight()
    root.geometry("%dx%d" % (width, height))
    root.configure(bg="blue")
    root.title("REC COLLEGE SCHEDULE")

    menu = Menu(root)
    file = Menu(menu, tearoff=0)
    menu.add_cascade(label='EDIT', menu=file)
    file.add_command(label='1st Semester', command=None)
    file.add_command(label='2nd Semester', command=None)
    file.add_command(label='3rd Semester', command=None)
    file.add_command(label='4th Semester', command=None)
    file.add_command(label='5th Semester', command=None)
    file.add_command(label='6th Semester', command=None)
    file.add_command(label='7th Semester', command=None)
    file.add_command(label='8th Semester', command=None)

    st_font = "Times 20 italic bold "
    label_College_Name = Label(root, text="Ramgarh Engineering College Schedule CSE Department",
                               font=st_font, bg="red").pack(side=TOP)


    def time():
        string = strftime('%A  %H:%M:%S %p')
        time_label.config(text=f"{string}")
        time_label.after(1000, time)


    time_label = Label(root, font=('calibri', 20, 'bold'),
                       background='purple',
                       foreground='white')

    time_label.place(x=1200, y=2)
    time()

    ProName1semCseSub = "DELD-   MR.NILESH KUMAR \n\nBE-  MR.KUNDAN KUAMR \n\nMATH-  DR.ADITYA KUMAR SINGH \n\nOOP-  " \
                        "BHASKAR DAS \n\nDS-  ASHIM KUAMR MAHATO \n\nDELD LAB-   MR.NILESH KUMAR\n\nOOP LAB-  PIJUSH " \
                        "MONDAL\n\nCOMMUN LAB-  KOMAL KUMARI\n\nDS LAB-  DIPAK KUMAR "

    sem1_sub_list = [
        ["", "", "", "",
         "LIBRARY0", "DELD0", "BE0", "EV0S", "  LIBRARY0", "\tDELD LAB0"],
        ["", "", "", "", "LIBRARY1", "DELD1", "BE1", "EVS1", "  LIBRARY1", "\tDELD LAB1"],
        ["", "", "", "", "LIBRARY", "DELD", "BE", "EVS", "  LIBRARY", "\tDELD LAB"],
        ["TUE", "", "", "", "OOP", "MATH", "DS", "BE", "  LIBRARY", "\tOOP LAB"],
        ["WED", "", "", "", "MATH", "MATH", "DELD", "DS", "  LIBRARY", "\tCOMMUN  LAB"],
        ["THU", "", "", "", "DS", "MATH", "OOP", "DELD", "  LIBRARY", "\tDS LAB5"],
        ["FRI", "", "", "", "BE", "OOP", "DS(T)", "DELD(T)", "  LIBRARY", "\t  EXTRA ACTIVITY"],
        ["SAT", "", "", "", "BE(T)", "MATH(T)", "OOP(T)", "EVS", "  LIBRARY", "\tQUIZ"]]

    day_list = [" ", "Time--\nDay", "MON", "TUE", "WED", "THUR", "FRI", "SAT"]
    TimeList = [" ", " ", " ", "9:00\n9:50", "9:50\n10:40", "10:40\n11:30", "11:30\n12:20", "1:20\n2:10", "2:10\n3:00",
                "\t 3:00 -- 4:40"]


    def Time_Date_List_set():
        for i in range(4, 10):
            geeks.canvas.create_text(i * 133 + 50, 133, fill="blue", font=st_font,
                                     text=TimeList[i])
        geeks.canvas.create_text(160, 50, fill="#FFFFFF", font=st_font,
                                 text="Select Semester")
        geeks.canvas.create_text(1290, 60, fill="#FFFFFF", font=st_font,
                                 text="Lunch Time 12:20 - 1:20")


    def day_set():
        for i in range(1, 8):
            geeks.canvas.create_text(455, i * 90 + 50, fill="darkblue", font=st_font,
                                     text=day_list[i])


    def button_set(x, y, command, title_name):
        sem1btn = Button(root, text=title_name, font=('calibri', 10, 'bold'), width=6, fg="#000000",
                         background="#FF48FF", command=command)
        geeks.canvas.create_window(x, y, anchor="nw", window=sem1btn)


    class REC:
        canvas: Canvas

        def __init__(self, root_canvas=None):
            self.root = root_canvas
            self.create()

        def create(self):
            self.canvas = Canvas(self.root)
            self.canvas.configure(bg="#fc03ca")

            # (straight horizontal line)
            for i in range(1, 9):
                self.canvas.create_line(400, 90 * i, 1466, 90 * i, fill="yellow", width=5)

            # (straight vertical line)
            for i in range(3, 12):
                if i == 10:
                    continue
                self.canvas.create_line(i * 133, 88, i * 133, 722, fill="yellow", width=5)

            self.canvas.pack(fill=BOTH, expand=True)


    def Sem_Set_Button():
        button_set(20, 100, sem1, "1st sem")
        button_set(100, 100, sem2, "2nd sem")
        button_set(180, 100, sem3, "3rd sem")
        button_set(260, 100, sem4, "4th sem")
        button_set(20, 150, sem5, "5th sem")
        button_set(100, 150, sem6, "6th sem")
        button_set(180, 150, sem7, "7th sem")
        button_set(260, 150, sem8, "8th sem")


    def sem1():
        messagebox.showinfo("Information", "This is not available now")


    def sem2():
        messagebox.showinfo("Information", "This is not available now")


    def sem3():
        for i in range(4, 10):
            for j in range(2, 8):
                geeks.canvas.create_text(i * 130 + 80, 45 + 90 * j, fill="black", font=st_font,
                                         text=sem1_sub_list[j][i])
        geeks.canvas.create_text(950, 33, fill="#0f0f0f", font="Times 20 italic bold",
                                 text="3rd Semester CSE Department\n\t Routine")
        geeks.canvas.create_text(182, 433, fill="#FFFFFF", font="Times 16 italic bold",
                                 text=ProName1semCseSub)


    def sem4():
        messagebox.showinfo("Information", "This is not available now")


    def sem5():
        messagebox.showinfo("Information", "This is not available now")


    def sem6():
        messagebox.showinfo("Information", "This is not available now")


    def sem7():
        messagebox.showinfo("Information", "This is not available now")


    def sem8():
        messagebox.showinfo("Information", "This is not available now")


    geeks = REC(root)
    Time_Date_List_set()
    day_set()
    Sem_Set_Button()

    root.config(menu=menu)
    root.mainloop()

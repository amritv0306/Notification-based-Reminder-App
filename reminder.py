from tkinter import *
from tkinter import Tk, messagebox
from plyer import notification
# from PIL import Image, ImageTk
import time
# root = Tk()
# root.title("Destop Reminder")
# frm = ttk.Frame(root, padding=10)
# frm.grid(column=3, row=2)
# ttk.Label(frm, text="Hello World!").grid(column=0, row=0)
# ttk.Button(frm, text="Quit", command=root.destroy).grid(column=1, row=0)
# root.mainloop()

# # from plyer import notification
# # def notify(title, messgaes):
# #     notification.notify(title = title, messgaes = messgaes, timeout = 10)

# import datetime
# import time
# import schedule
# from plyer import notification

# def notify(title, message):
#     notification.notify(
#         title=title,
#         message=message,
#         timeout=10  # Duration in seconds
#     )

# def schedule_reminder(time_str, title, message):
#     schedule_time = datetime.datetime.strptime(time_str, '%Y-%m-%d %H:%M:%S')
#     schedule.every().day.at(schedule_time.strftime('%H:%M')).do(notify, title=title, message=message)

# def main():
#     # Example reminder
#     schedule_reminder('2024-06-25 12:15:00', 'Meeting', 'Attend the project meeting.')

#     while True:
#         schedule.run_pending()
#         time.sleep(1)

# if __name__ == "__main__":
#     main()

# import time
# from plyer import notification
# notification.notify(title='Title', message='msg', app_name='Notifier', app_icon=None, timeout = 2)
# print(time.time())

# root = Tk()
# root.title("Yo!!!!!!!")
# root.geometry("300x300")
# root.config(background="Yellow")
# root.resizable(0,0)
# #lable
# # var = StringVar()
# # var.set("hellooicmds")
# l1 = Label(root, text="Hello", background="Light Blue", font="Time 20 underline italic", relief="raised", cursor="dot")
# # l1.pack()
# # l1.grid(row=0, column=0)
# l1.place(x=120, y=20)

# #button
# def clickme():
#     print("Button is clicked")
# b1 = Button(root, text="Click me", background="red", fg="pink", width=20, border=10, relief="raised", command=clickme)
# b1.place(x= 60, y = 100)

# def exit_button():
#     return 0
# b2 = Button(root, text="Exit", width=20, border=10, relief="raised", command=exit_button)
# b2.place(x=60, y=50)

# root.mainloop()


#get details

class App:
    def __init__(self, root):
        self.root = root
        self.root.title('Notifier')
        self.root.geometry("500x300")

        # # Initial Canvas
        # self.canvas = self.root.Canvas(root, width=500, height=300)
        # self.canvas.pack()
        
        # # Welcome Page
        # self.welcome_label = self.root.Label(self.canvas, text="Welcome to the Notification App", font=("underline", 20), background="light pink", border=5, relief="ridge")
        # self.welcome_label.place(x=50, y=125)

        # # Start button on the welcome page
        # self.start_button = self.root.Button(self.canvas, text="Start", font=("poppins", 10, "bold"), fg="#ffffff", bg="#528DFF", width=20, relief="raised", command=self.slide_up)
        # self.start_button.place(x=170, y=200)

        # # Main Page (Initially hidden)
        # self.main_frame = self.root.Frame(root, width=500, height=300, bg="light pink")

        #main Title
        main_title = Label(root, text="Notification App", font=("underline", 20 ), background="light pink",border=5, relief="ridge" )
        main_title.place(x=160, y= 3)
        # Label - Title
        t_label = Label(root, text="Title to Notify",font=("poppins", 10))
        t_label.place(x=12, y=70)
        # ENTRY - Title
        self.title = Entry(root, width="25",font=("poppins", 13))
        self.title.place(x=123, y=70)

        # Label - Message
        m_label = Label(root, text="Display Message", font=("poppins", 10))
        m_label.place(x=12, y=120)
        # ENTRY - Message
        self.msg = Entry(root, width="40", font=("poppins", 13))
        self.msg.place(x=123,height=30, y=120)

        # Label - Time
        time_label = Label(root, text="Set Time", font=("poppins", 10))
        time_label.place(x=12, y=175)
        # ENTRY - Time
        self.time1 = Entry(root, width="5", font=("poppins", 13))
        self.time1.place(x=123, y=175)

        # Label - min
        time_min_label = Label(root, text="min", font=("poppins", 10))
        time_min_label.place(x=175, y=180)
        # Button
        but = Button(root, text="SET NOTIFICATION", font=("poppins", 10, "bold"), fg="#ffffff", bg="#528DFF", width=20, relief="raised", command=self.get_details)
        but.place(x=170, y=230)

        root.resizable(0,0)

    # def slide_up(self):
    #     for i in range(30):
    #         y = i * 10
    #         self.canvas.move(self.welcome_label, 0, -10)
    #         self.canvas.move(self.start_button, 0, -10)
    #         self.root.update()
    #         self.root.after(10)
        
    #     self.canvas.destroy()
    #     self.main_frame.pack()

    def get_details(self):
        
        get_title = self.title.get()
        get_message = self.msg.get()
        get_time = self.time1.get()
        
        if get_title == "" or get_message == "" or get_time == "":
            print("Got error")
            messagebox.showerror("ALERT", "All fields are required")
        else:
            time_in_sec = float(get_time)*60
            # messagebox.showinfo("Notifier Set", "Show Notification")
            print("Reminder is successfully set")
            time.sleep(time_in_sec)
            notification.notify(title=get_title, message=get_message, app_name='Notifier', app_icon=None, timeout = float(get_time))
            print("Notification send successfully")
            self.root.quit()

if __name__=="__main__":
    root = Tk()
    app = App(root)
    root.mainloop()
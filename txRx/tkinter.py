import Tkinter 
window = tk.Tk()
window.title('frame test')
window.geometry('600x450')

label1 = tk.Label(window, text='In the left side of window', bg='red',
                  fg='white').pack(side='left')

frameShow = tk.Frame(window, bg='yellow', width=100,height=50)
frameShow.pack()

label2 = tk.Label(frameShow, text='In the left side of yellow frame',
                  bg='pink').pack(side='left')

subFramel = tk.Frame(frameShow, bg='green', width=200,height=200).pack()

label3 = tk.Label(subFramel, text='Inside the green frame',
                  bg='brown', fg='white').pack(side='right')

subFrame2 = tk.Frame(frameShow, bg='blue',
                     width=180,height=200).pack(side='left')

label3 = tk.Label(subFrame2, text='Inside the blue frame',
                  bg='brown', fg='white').pack()

window.mainloop()
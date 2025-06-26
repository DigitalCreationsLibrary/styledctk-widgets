import  styledctk_widgets.CTK_Buttons.SCTkButton as SCTk_B


import customtkinter as ctk


def oneB():
    main_window = ctk.CTk()
    main_window.geometry("300x200")
    main_window.title("Testing the library")
    
    but= SCTk_B.SCTkButton(main_window, theme=1,style=3)
    but.pack(padx=20,pady=20)
    
    main_window.mainloop()
    
    
if __name__=="__main__":
    oneB()
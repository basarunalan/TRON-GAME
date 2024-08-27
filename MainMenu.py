from turtle import *
from freegames import vector
from PIL import Image
import tkinter as tk
root = tk.Tk()
root.geometry("650x530+620+300")
root.title("TRON GAME")
global map_choice
map_choice = 1
def Menu():
    bg_image = tk.PhotoImage(file='Documents/mainmenu.gif')
    canvas = tk.Canvas(root, width=900, height=700, bg='#211951')
    canvas.create_image(-180, -30, anchor=tk.NW, image=bg_image)
    canvas.pack()
        
    start_image = tk.PhotoImage(file='Documents/play_button.gif')
    start_button = tk.Button(root, image=start_image, command=lambda: [canvas.destroy(),start_button.destroy(),SideMenu()], bd=0, bg='#211951', activebackground="#211951")
    start_button.place(relx=0.49, rely=0.93, anchor="center")
    root.mainloop()

def SideMenu(): 
    bg_image = tk.PhotoImage(file='Documents/side_menu.gif')
    canvas = tk.Canvas(root, width=900, height=700, bg='#211951')
    canvas.create_image(-180, -30, anchor=tk.NW, image=bg_image)
    canvas.pack()
    
    match_history_image = tk.PhotoImage(file='Documents/match_history_button.gif')
    match_history_button = tk.Button(root, image=match_history_image, command=lambda:[canvas.destroy(),match_history_button.destroy(),match_history()], bd=0, bg='#211951', activebackground="#211951")
    match_history_button.place(relx=0.49, rely=0.27, anchor="center")

    how_to_play_image = tk.PhotoImage(file='Documents/how_to_play_button.gif')
    how_to_play_button = tk.Button(root, image=how_to_play_image, command=lambda:[canvas.destroy(),how_to_play_button.destroy(),how_to_play()], bd=0, bg='#211951', activebackground="#211951")
    how_to_play_button.place(relx=0.365, rely=0.515, anchor="center")
    
    maps_image = tk.PhotoImage(file='Documents/Maps_button.gif')
    maps_button = tk.Button(root, image=maps_image, command=lambda:[canvas.destroy(),maps_button.destroy(),Maps()], bd=0, bg='#211951', activebackground="#211951")
    maps_button.place(relx=0.610, rely=0.515, anchor="center")

    start_image = tk.PhotoImage(file='Documents/second_play_button.gif')
    start_button = tk.Button(root, image=start_image, command=lambda:[canvas.destroy(),start_button.destroy(),player_names()], bd=0, bg='#211951', activebackground="#211951")
    start_button.place(relx=0.49, rely=0.82, anchor="center")
    root.mainloop()

def match_history():
    import import_mysql
    bg_image = tk.PhotoImage(file='Documents/match_history.gif')
    canvas = tk.Canvas(root, width=900, height=700, bg='#211951')
    canvas.create_image(-180, -19, anchor=tk.NW, image=bg_image)
    canvas.pack()

    back_image = tk.PhotoImage(file='Documents/back_button.gif')
    back_button = tk.Button(root, image=back_image, command=lambda:[canvas.destroy(),back_button.destroy(),SideMenu()], bd=0, bg='#211951', activebackground="#211951")
    back_button.place(relx=0.05, rely=0.05, anchor="center")

    import_mysql.my_cursor.execute("SELECT * FROM players_data")
    data = import_mysql.my_cursor.fetchall()


    y_position = 100  

    headers = ["Player1", "Score1", "Score2", "Player2", "Time", "Map"]
    x_positions = [40, 150, 250, 350, 470, 570] 

    for i, header in enumerate(headers):
        canvas.create_text(x_positions[i], 70, text=header, fill='#FFDB00', font=("Gill Sans Ultra Bold", 14), anchor='w')
    
    x_positions = [60, 180, 280, 370, 470, 570]
    for row in data:
        for i, item in enumerate(row):
            canvas.create_text(x_positions[i], y_position, text=str(item), fill='#A6F6FF', font=("Algerian", 12,"bold"), anchor='w')
        y_position += 30 
    root.mainloop()


def how_to_play():
    bg_image = tk.PhotoImage(file='Documents/how_to_play.gif')
    canvas = tk.Canvas(root, width=900, height=700, bg='#211951')
    canvas.create_image(-170, -30, anchor=tk.NW, image=bg_image)
    canvas.pack()

    back_image = tk.PhotoImage(file='Documents/back_button.gif')
    back_button = tk.Button(root, image=back_image, command=lambda:[canvas.destroy(),back_button.destroy(),SideMenu()], bd=0, bg='#211951', activebackground="#211951")
    back_button.place(relx=0.1, rely=0.1, anchor="center")

    power_up_button_image = tk.PhotoImage(file='Documents/power_ups_menu_button.gif')
    power_up_button = tk.Button(root, image=power_up_button_image, command=lambda:[canvas.destroy(),power_up_button.destroy(),power_up_info()], bd=0, bg='#211951', activebackground="#211951")
    power_up_button.place(relx=0.505, rely=0.68, anchor="center")

    root.mainloop()

def power_up_info():
    bg_image = tk.PhotoImage(file='Documents/power_ups_info.gif')
    canvas = tk.Canvas(root, width=900, height=700, bg='#211951')
    canvas.create_image(-60, -30, anchor=tk.NW, image=bg_image)
    canvas.pack()
    back_image = tk.PhotoImage(file='Documents/back_button.gif')
    back_button = tk.Button(root, image=back_image, command=lambda:[canvas.destroy(),back_button.destroy(),how_to_play()], bd=0, bg='#211951', activebackground="#211951")
    back_button.place(relx=0.1, rely=0.1, anchor="center")

    root.mainloop()

def Maps():
    def change_choice_3():
     global map_choice
     map_choice = 3
    def change_choice_2():
     global map_choice
     map_choice = 2
    def change_choice_1():
     global map_choice
     map_choice = 1
    
    bg_image = tk.PhotoImage(file='Documents/maps.gif')
    canvas = tk.Canvas(root, width=900, height=700, bg='#211951')
    canvas.create_image(1, 1, anchor=tk.NW, image=bg_image)
    canvas.pack()
    space_button_image = tk.PhotoImage(file='Documents/space_map_button.gif')
    space_map_button = tk.Button(root, image=space_button_image, command=lambda:[canvas.destroy(),space_map_button.destroy(),change_choice_1(),SideMenu()], bd=0, bg='#211951', activebackground="#211951")
    space_map_button.place(relx=0.17, rely=0.565, anchor="center")

    desert_button_image = tk.PhotoImage(file='Documents/desert_map_button.gif')
    desert_map_button = tk.Button(root, image=desert_button_image, command=lambda:[canvas.destroy(),desert_map_button.destroy(),change_choice_2(),SideMenu()], bd=0, bg='#211951', activebackground="#211951")
    desert_map_button.place(relx=0.49, rely=0.565, anchor="center")

    forest_button_image = tk.PhotoImage(file='Documents/forest_map_button.gif')
    forest_map_button = tk.Button(root, image=forest_button_image, command=lambda:[canvas.destroy(),forest_map_button.destroy(),change_choice_3(),SideMenu()], bd=0, bg='#211951', activebackground="#211951")
    forest_map_button.place(relx=0.81, rely=0.565, anchor="center")
    root.mainloop()

def start_game_with_names(_entry1,_entry2):
    import Start
    global player1_name, player2_name
    player1_name = _entry1.get()
    player2_name = _entry2.get()
    if player1_name == '':
         player1_name = "PLAYER 1"
    if player2_name == '':
        player2_name = "PLAYER 2"
    root.destroy()
    Start.start_game(map_choice)

def player_names():
    bg_image = tk.PhotoImage(file='Documents/Player_names.gif')
    canvas = tk.Canvas(root, width=900, height=700, bg='#211951')
    canvas.create_image(-180, -30, anchor=tk.NW, image=bg_image)
    canvas.pack()
    entry1 = tk.Entry(root, font=("Arial", 12), bg='#77ACF1', borderwidth = 4,width = 25)
    entry1.place(relx=0.56, rely=0.265, anchor="center")
    entry2 = tk.Entry(root, font=("Arial", 12), bg='Pink', borderwidth = 4,width=25)
    entry2.place(relx=0.56, rely=0.335, anchor="center")
    start_image = tk.PhotoImage(file='Documents/second_play_button.gif')
    start_button = tk.Button(root, image=start_image, command=lambda:[canvas.destroy(),start_button.destroy(),start_game_with_names(entry1,entry2),entry1.destroy(),entry2.destroy()], bd=0, bg='#211951', activebackground="#211951")
    start_button.place(relx=0.49, rely=0.7, anchor="center")
    root.mainloop()

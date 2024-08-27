import time
from tkinter import ttk
from turtle import *
import turtle
from freegames import vector
from PIL import Image
import tkinter as tk
import pygame
import MainMenu
import random
counter = 0
counter2 = 0
health1 = 3
health2 =  3
running = 40
length1 = 60
length2 = 60
longerx = 165
longery = 135
shorterx = 135
shortery = 165
fasterx = 165
fastery = 135
slowerx = 135
slowery = 165
shapes_1 = ["Documents/full_power_up.gif", "Documents/yarim_power_up.gif","Documents/ceyrek_power_up.gif","Documents/power_up_null.gif"]
shapes_2 = ["Documents/full_power_up.gif", "Documents/yarim_power_up.gif","Documents/ceyrek_power_up.gif","Documents/power_up_null.gif"]
current_shape_index_1 = 3
current_shape_index_2 = 3
start_time = time.time()
def start_space_race():
    screen = Screen()
    screen.setup(width=715, height=630)
    screen.bgcolor("Royal Blue4")
    screen.bgpic("Documents/space_buyuk.gif")
    screen.addshape("Documents/Motor_blue_right.gif")
    screen.addshape("Documents/Motor_blue_up.gif")
    screen.addshape("Documents/Motor_blue_down.gif")
    screen.addshape("Documents/Motor_blue_left.gif")
    screen.addshape("Documents/Motor_yellow_right.gif")
    screen.addshape("Documents/Motor_yellow_up.gif")
    screen.addshape("Documents/Motor_yellow_down.gif")
    screen.addshape("Documents/Motor_yellow_left.gif")
    screen.addshape("Documents/0_can.gif")
    screen.addshape("Documents/1_can.gif")
    screen.addshape("Documents/2_can.gif")
    screen.addshape("Documents/3_can.gif")
    screen.addshape("Documents/pause_menu.gif")
    screen.addshape("Documents/longer.gif")
    screen.addshape("Documents/shorter.gif")
    screen.addshape("Documents/ceyrek_power_up.gif")
    screen.addshape("Documents/yarim_power_up.gif")
    screen.addshape("Documents/full_power_up.gif")
    screen.addshape("Documents/power_up_null.gif")
    screen.addshape("Documents/fast.gif")
    screen.addshape("Documents/slow.gif")
    screen.addshape("Documents/blue_motor.gif")
    screen.addshape("Documents/yellow_motor.gif")

    health_bar_1 = Turtle()
    health_bar_1.shape(f"Documents/{health1}_can.gif")
    health_bar_1.penup()
    health_bar_1.goto(-230,260)
    
    health_bar_2 = Turtle()
    health_bar_2.shape(f"Documents/{health2}_can.gif")
    health_bar_2.penup()
    health_bar_2.goto(230,260)

    yellow_motor = Turtle()
    yellow_motor.shape("Documents/yellow_motor.gif")
    yellow_motor.penup()
    yellow_motor.goto(-278,260)

    blue_motor = Turtle()
    blue_motor.shape("Documents/blue_motor.gif")
    blue_motor.penup()
    blue_motor.goto(182,260)

    
    player1_label = tk.Label(text=MainMenu.player1_name, fg="dark blue", bg="#8B93FF",font=("Elephant", 9))
    player1_label.place(relx=0.20, rely=0.042, anchor="center")
    player2_label = tk.Label(text=MainMenu.player2_name, fg="dark blue", bg="#8B93FF",font=("Elephant", 9))
    player2_label.place(relx=0.85, rely=0.042, anchor="center")
    

    random_location_x = random.randint(-250, 100)
    random_location_y = random.randint(-200, 100)

    p1xy = vector(random_location_x,random_location_y)
    p1aim = vector(4, 0)
    p1body = []

    p2xy = vector(random_location_x + 200,random_location_y)
    p2aim = vector(-4, 0)
    p2body = []

    Motor1 = Turtle()
    Motor1.shape("Documents/Motor_yellow_right.gif")
    Motor1.penup()
    Motor1.goto(p1xy.x, p1xy.y)

    Motor2 = Turtle()
    Motor2.shape("Documents/Motor_blue_left.gif")
    Motor2.penup()
    Motor2.goto(p2xy.x, p2xy.y)

    longer_power_up = Turtle()
    longer_power_up.shape("Documents/longer.gif")
    longer_power_up.penup()
    longer_power_up.goto(-150,150)

    shorter_power_up = Turtle()
    shorter_power_up.shape("Documents/shorter.gif")
    shorter_power_up.penup()
    shorter_power_up.goto(150,-150)

    faster_power_up = Turtle()
    faster_power_up.shape("Documents/fast.gif")
    faster_power_up.penup()
    faster_power_up.goto(-150,-150)

    slower_power_up = Turtle()
    slower_power_up.shape("Documents/slow.gif")
    slower_power_up.penup()
    slower_power_up.goto(150,150)

    
    def end_game_due_to_time():
        import import_mysql
        import MainMenu
        global running
        if health1 == health2:
            draw_label = tk.Label(text="DRAW!", fg="dark blue", bg="#8B93FF", font=("Elephant", 40))
            draw_label.place(relx=0.5, rely=0.5, anchor="center")
            draw_label.update()
            running=100000
            elapsed_time = time.time() - start_time 
            import_mysql.add_data(MainMenu.player1_name,(3 - health2),(3 - health1),MainMenu.player2_name,elapsed_time,'Space')
            time.sleep(999999999999)  
            draw_label.destroy()
            
            
        elif health1 > health2:
            running = 1000000
            elapsed_time = time.time() - start_time 
            import_mysql.add_data(MainMenu.player1_name,(3 - health2),(3 - health1),MainMenu.player2_name,elapsed_time,'Space')
            display_winner("yellow")
            time.sleep(999999999999)
        else:
            running = 1000000
            elapsed_time = time.time() - start_time 
            import_mysql.add_data(MainMenu.player1_name,(3 - health2),(3 - health1),MainMenu.player2_name,elapsed_time,'Space')
            display_winner("blue")
            time.sleep(999999999999)
    
    screen.ontimer(end_game_due_to_time, 150000)

    def display_winner(winner):
        pygame.mixer.music.stop()
        penup()
        if winner == "yellow":
           winner_label = tk.Label(text=f"{MainMenu.player1_name} WINS!", fg="dark blue", bg="#8B93FF",font=("Elephant", 40))
           winner_label.place(relx=0.5, rely=0.5, anchor="center")
        elif winner == "blue":
           winner_label = tk.Label(text=f"{MainMenu.player2_name} WINS!", fg="dark blue", bg="#8B93FF",font=("Elephant", 40))
           winner_label.place(relx=0.5, rely=0.5, anchor="center")
        done()
    
    def display_counter():
     for i in range(3, 0, -1):
      title_label = tk.Label(text=i, fg="dark blue", bg="#8B93FF",font=("Goudy Stout", 50,'bold'))
      title_label.place(relx=0.5, rely=0.5, anchor="center")
      title_label.update()  
      time.sleep(1)
      title_label.destroy()
    
     title_label2 = tk.Label(text="GO!", fg="dark blue", bg="#8B93FF", font=("Goudy Stout", 50,'bold'))
     title_label2.place(relx=0.5, rely=0.5, anchor="center")
     title_label2.update()
     time.sleep(1)
     title_label2.destroy()
    
    display_counter()

    def inside(head):
        return -332 < head.x < 326 and -262 < head.y < 204
    
    def change_motor_shape_a():
        global counter
        if counter == 0:
            Motor1.shape("Documents/Motor_yellow_up.gif")
            counter += 1
        elif counter == 1:
            Motor1.shape("Documents/Motor_yellow_left.gif")
            counter += 1
        elif counter == 2:
            Motor1.shape("Documents/Motor_yellow_down.gif")
            counter += 1
        elif counter == 3:
            Motor1.shape("Documents/Motor_yellow_right.gif")
            counter = 0
    def change_motor_shape_d():
        global counter
        if counter == 3:
            Motor1.shape("Documents/Motor_yellow_left.gif")
            counter -= 1
        elif counter == 2:
            Motor1.shape("Documents/Motor_yellow_up.gif")
            counter -= 1
        elif counter == 1:
            Motor1.shape("Documents/Motor_yellow_right.gif")
            counter -= 1
        elif counter == 0:
            Motor1.shape("Documents/Motor_yellow_down.gif")
            counter = 3

    def change_motor_shape_left():
        global counter2
        if counter2 == 0:
            Motor2.shape("Documents/Motor_blue_down.gif")
            counter2 += 1
        elif counter2 == 1:
            Motor2.shape("Documents/Motor_blue_right.gif")
            counter2 += 1
        elif counter2 == 2:
            Motor2.shape("Documents/Motor_blue_up.gif")
            counter2 += 1
        elif counter2 == 3:
            Motor2.shape("Documents/Motor_blue_left.gif")
            counter2 = 0

    def change_motor_shape_right():
        global counter2
        if counter2 == 3:
            Motor2.shape("Documents/Motor_blue_right.gif")
            counter2 -= 1
        elif counter2 == 2:
            Motor2.shape("Documents/Motor_blue_down.gif")
            counter2 -= 1
        elif counter2 == 1:
            Motor2.shape("Documents/Motor_blue_left.gif")
            counter2 -= 1
        elif counter2 == 0:
            Motor2.shape("Documents/Motor_blue_up.gif")
            counter2 = 3
            
    def reset():
     global counter, counter2,running,longerx,longery,current_shape_index_1,current_shape_index_2,shorterx,shortery,length1,length2,slowerx,slowery,fasterx,fastery
     counter = 0
     counter2 = 0
     running = 40
     longerx = 165
     longery = 135
     shorterx = 135
     shortery = 165
     length1 = 60
     length2 = 60
     fasterx = 165
     fastery = 135
     slowerx = 135
     slowery = 165
     current_shape_index_1 = 3
     current_shape_index_2 = 3
     longer_power_up.hideturtle()
     shorter_power_up.hideturtle()
     faster_power_up.hideturtle()
     slower_power_up.hideturtle()
     clear()
     Motor1.goto(-1000, 0)
     Motor2.goto(1000, 0)
     start_space_race()

    def crashSound():
       pygame.mixer.music.pause()
       pygame.mixer.music.load("Documents/Crashing (Sound Effect).mp3")
       pygame.mixer.music.play()
       time.sleep(1)
       pygame.mixer.music.load("Documents/Foo Fighters - Everlong (Instrumental).mp3")
       pygame.mixer.music.play()
    
    def laserSound():
       pygame.mixer.music.pause()
       pygame.mixer.music.load("Documents/Laser Sound Effect.mp3")
       pygame.mixer.music.play()
       time.sleep(1)
       pygame.mixer.music.load("Documents/Foo Fighters - Everlong (Instrumental).mp3")
       pygame.mixer.music.play()

    pausemenu = Turtle()
    pausemenu.hideturtle()
    
    def pause_menu():
     global running
     pausemenu.showturtle()
     clear()
     turtle.update()
     pausemenu.shape("Documents/pause_menu.gif")
     pausemenu.penup()
     pausemenu.goto(-20,0)
     resume_button = tk.Button(text="    RESUME" ,command=lambda: [volume_100_button.destroy(),volume_50_button.destroy(),volume_0_button.destroy(),resume_button.destroy(),restart_button.destroy(),quit_button.destroy(),resume_game()], bd=0, bg='black',fg= "white",font=("Elephant", 14),width = 12, activebackground="black")
     resume_button.place(relx=0.49, rely=0.53, anchor="center")
     restart_button = tk.Button(text="   RESTART" ,command=lambda: [volume_100_button.destroy(),volume_50_button.destroy(),volume_0_button.destroy(),restart_button.destroy(),resume_button.destroy(),quit_button.destroy(),restart_game()], bd=0, bg='black',fg= "white",font=("Elephant", 14),width = 12, activebackground="black")
     restart_button.place(relx=0.19, rely=0.53, anchor="center")
     quit_button = tk.Button(text=" QUIT" ,command=lambda: [volume_100_button.destroy(),volume_50_button.destroy(),volume_0_button.destroy(),restart_button.destroy(),resume_button.destroy(),quit_button.destroy(),screen.bye()], bd=0, bg='black',fg= "white",font=("Elephant", 14),width = 12, activebackground="black")
     quit_button.place(relx=0.805, rely=0.53, anchor="center")
     volume_0_button = tk.Button(text=" 0 %" ,command=lambda: [volume(0)], bd=0, bg='#FF5BAE',fg= "white",font=("Cooper Black", 20),width = 6,height = 1, activebackground="#D10363",borderwidth=5)
     volume_0_button.place(relx=0.282, rely=0.734, anchor="center")
     volume_50_button = tk.Button(text="50 %" ,command=lambda: [volume(50)], bd=0, bg='#FF5BAE',fg= "white",font=("Cooper Black", 20),width = 6,height = 1, activebackground="#D10363",borderwidth=5)
     volume_50_button.place(relx=0.51, rely=0.734, anchor="center")
     volume_100_button = tk.Button(text="100 %" ,command=lambda: [volume(100)], bd=0, bg='#FF5BAE',fg= "white",font=("Cooper Black", 20),width = 6,height = 1, activebackground="#D10363",borderwidth=5)
     volume_100_button.place(relx=0.742, rely=0.734, anchor="center")
     running = 1000000
     
    def resume_game():
      global running
      running = 40
      turtle.update()
      pausemenu.hideturtle()
      draw()

    def restart_game():
     global counter, counter2,health1,health2,running,longerx,longery,current_shape_index_1,current_shape_index_2,shorterx,shortery,length1,length2,fastery,fasterx,slowerx,slowery,start_time
     counter = 0
     counter2 = 0
     health1 = 3
     health2 = 3
     running = 40
     longerx = 165
     longery = 135
     shorterx = 135
     shortery = 165 
     length1 = 60
     length2 = 60
     fasterx = 165
     fastery = 135
     slowerx = 135
     slowery = 165
     current_shape_index_1 = 3
     current_shape_index_2 = 3
     longer_power_up.hideturtle()
     shorter_power_up.hideturtle()
     faster_power_up.hideturtle()
     slower_power_up.hideturtle()
     pausemenu.hideturtle()
     start_time = time.time()
     clear()
     Motor1.goto(-1000, 0)
     Motor2.goto(1000, 0)
     start_space_race()

    def volume(level):
       if level == 0:
          pygame.mixer.music.set_volume(0.0)
       elif level == 50:
          pygame.mixer.music.set_volume(0.5)
       else:
          pygame.mixer.music.set_volume(1.0)
          
    def change_length_1():
      global current_shape_index_1,length1,length2
      if length1 > 60:
         longer_power_up.goto(-255,257)
      elif length2 < 60:
         shorter_power_up.goto(-255,257)
      power_up_bar = Turtle()
      power_up_bar.hideturtle()
      if(current_shape_index_1 <= 2):
       power_up_bar.shape(shapes_1[current_shape_index_1])
       power_up_bar.penup()
       power_up_bar.goto(-230,260)
       power_up_bar.showturtle()
       ontimer(change_length_1,8000)
       current_shape_index_1 += 1
      else:
         power_up_bar.shape(shapes_1[current_shape_index_1])
         power_up_bar.penup()
         power_up_bar.goto(-230,260)
         power_up_bar.showturtle()
         if(length1 > 60):
          longer_power_up.hideturtle()
          length1 = 60
          p1body.clear()
          
         elif(length2 < 60):
            shorter_power_up.hideturtle()
            length2 = 60
            p2body.clear()

    def change_speed_1():
      global current_shape_index_1,running
      if running < 40:
         faster_power_up.goto(-255,257)
      elif running > 40:
         slower_power_up.goto(-255,257)
      power_up_bar = Turtle()
      power_up_bar.hideturtle()
      if(current_shape_index_1 <= 2):
       power_up_bar.shape(shapes_1[current_shape_index_1])
       power_up_bar.penup()
       power_up_bar.goto(-230,260)
       power_up_bar.showturtle()
       ontimer(change_speed_1,8000)
       current_shape_index_1 += 1
      else:
         power_up_bar.shape(shapes_1[current_shape_index_1])
         power_up_bar.penup()
         power_up_bar.goto(-230,260)
         power_up_bar.showturtle()
         if running < 40:
            faster_power_up.hideturtle()
            running = 40
         elif running > 40:
            slower_power_up.hideturtle()
            running = 40

         

    def change_length_2():
      global current_shape_index_2,length1,length2
      if length2 > 60:
         longer_power_up.goto(205,257)
      elif length1 < 60:
         shorter_power_up.goto(205,257)
      power_up_bar = Turtle()
      power_up_bar.hideturtle()
      if(current_shape_index_2 <= 2):
       power_up_bar.shape(shapes_2[current_shape_index_2])
       power_up_bar.penup()
       power_up_bar.goto(230,260)
       power_up_bar.showturtle()
       ontimer(change_length_2,8000)
       current_shape_index_2 += 1
      else:
         power_up_bar.shape(shapes_2[current_shape_index_2])
         power_up_bar.penup()
         power_up_bar.goto(230,260)
         power_up_bar.showturtle()
         if(length1 < 60):
          shorter_power_up.hideturtle()
          length1 = 60
          p1body.clear()
          
         elif(length2 > 60):
            longer_power_up.hideturtle()
            length2 = 60
            p2body.clear()
    
    def change_speed_2():
      global current_shape_index_2,running
      if running < 40:
         faster_power_up.goto(205,257)
      elif running > 40:
         slower_power_up.goto(205,257)
      power_up_bar = Turtle()
      power_up_bar.hideturtle()
      if(current_shape_index_2 <= 2):
       power_up_bar.shape(shapes_2[current_shape_index_2])
       power_up_bar.penup()
       power_up_bar.goto(230,260)
       power_up_bar.showturtle()
       ontimer(change_speed_2,8000)
       current_shape_index_2 += 1
      else:
         power_up_bar.shape(shapes_2[current_shape_index_2])
         power_up_bar.penup()
         power_up_bar.goto(230,260)
         power_up_bar.showturtle()
         if running < 40:
            faster_power_up.hideturtle()
            running = 40
         elif running > 40:
            slower_power_up.hideturtle()
            running = 40

    

    def draw():
        global counter,counter2,health1,health2,running,length1,length2,longerx,longery,shorterx,shortery,current_shape_index_1,current_shape_index_2,fasterx,fastery,slowerx,slowery
        p1xy.move(p1aim)
        p1head = p1xy.copy()
        
        p2xy.move(p2aim)
        p2head = p2xy.copy()

        if (p1head.x >= -longerx and p1head.x <= -longery and p1head.y <= longerx and p1head.y >= longery):
            if current_shape_index_1 == 3:
             current_shape_index_1 = 0
             length1 = 200
             longerx = 1000
             longery = 1000
             change_length_1()

        if (p1head.x >= shorterx and p1head.x <= shortery and p1head.y <= -shorterx and p1head.y >= -shortery):
            if current_shape_index_1 == 3:
             p2body.clear()
             length2 = 20
             shorterx = 1000
             shortery = 1000
             current_shape_index_1 = 0
             change_length_1()
        
        if (p1head.x >= -fasterx and p1head.x <= -fastery and p1head.y >= -fasterx and p1head.y <= -fastery):
            if current_shape_index_1 == 3:
             running = 20
             fasterx = 1000
             fastery = 1000
             current_shape_index_1 = 0
             change_speed_1()
        
        if (p1head.x >= slowerx and p1head.x <= slowery and p1head.y >= slowerx and p1head.y <= slowery):
            if current_shape_index_1 == 3:
             running = 60
             slowerx = 1000
             slowery = 1000
             current_shape_index_1 = 0
             change_speed_1()
            
        
        if not inside(p1head):
           crashSound()
           health1 -= 1
           if health1 == 0:
            health_bar_1.shape(f"Documents/{health1}_can.gif")
            update() 
            end_game_due_to_time()
            return    
           reset()
           return
        
        elif p1head in p2body or p1head  in p1body:
            laserSound()
            if (p1xy.x == p2xy.x + 8 and p1xy.y == p2xy.y) or (p1xy.y + 8 == p2xy.y and p1xy.x == p2xy.x):
             draw_label = tk.Label(text=" DRAW!", fg="dark blue", bg="#8B93FF",font=("Elephant", 40))
             draw_label.place(relx=0.5, rely=0.5, anchor="center")
             draw_label.update()
             time.sleep(1)
             draw_label.destroy()
             reset()
             return
            health1 -= 1
            if health1 == 0:
             health_bar_1.shape(f"Documents/{health1}_can.gif")
             update() 
             end_game_due_to_time()
             return    
            reset()
            return
                 
        if (p2head.x >= -longerx and p2head.x <= -longery and p2head.y <= longerx and p2head.y >= longery):
            if current_shape_index_2 == 3:
             current_shape_index_2 = 0
             length2 = 200
             longerx = 1000
             longery = 1000
             change_length_2()
        
        if (p2head.x >= shorterx and p2head.x <= shortery and p2head.y <= -shorterx and p2head.y >= -shortery):
          if current_shape_index_2 == 3:
             p1body.clear()
             length1 = 20
             shorterx = 1000
             shortery = 1000
             current_shape_index_2 = 0
             change_length_2()
        
        if (p2head.x >= -fasterx and p2head.x <= -fastery and p2head.y >= -fasterx and p2head.y <= -fastery):
            if current_shape_index_2 == 3:
             running = 20
             fasterx = 1000
             fastery = 1000
             current_shape_index_2 = 0
             change_speed_2()
        
        if (p2head.x >= slowerx and p2head.x <= slowery and p2head.y >= slowerx and p2head.y <= slowery):
            if current_shape_index_2 == 3:
             running = 60
             slowerx = 1000
             slowery = 1000
             current_shape_index_2 = 0
             change_speed_2()

        if not inside(p2head):
           crashSound()
           health2 -= 1
           if health2 == 0:
            health_bar_2.shape(f"Documents/{health2}_can.gif")
            update()
            end_game_due_to_time()
            return 
           reset()
           return
        
        elif p2head  in p1body or p2head in p2body :
           laserSound()
           if (p1xy.x == p2xy.x + 8 and p1xy.y == p2xy.y) or (p1xy.y + 8 == p2xy.y and p1xy.x == p2xy.x):
             draw_label = tk.Label(text=" DRAW!", fg="dark blue", bg="#8B93FF",font=("Elephant", 40))
             draw_label.place(relx=0.5, rely=0.5, anchor="center")
             draw_label.update()
             time.sleep(1)
             draw_label.destroy()
             reset()
             return
           health2 -= 1
           if health2 == 0:
            health_bar_2.shape(f"Documents/{health2}_can.gif")
            update()
            end_game_due_to_time()
            return 
           reset()
           return
        

        if len(p1body) < length1:
          p1body.append(p1head)
          penup()
          color('yellow')
          goto(p1xy.x, p1xy.y)
          pendown()
          dot(7)
           
           
        if len(p2body) < length2:
         p2body.append(p2head)
         penup()
         color('blue')
         goto(p2xy.x, p2xy.y)
         pendown()
         dot(7)
         
        if (len(p1body) == length1) or (len(p2body) == length2):
           p1body.pop(0)  
           p2body.pop(0)  
           clear()  
           for point in p1body:  
               penup()
               goto(point.x, point.y)
               pendown()
               dot(7, "yellow")
           p1body.append(p1head)
           penup()
           color('yellow')
           goto(p1xy.x, p1xy.y)
           pendown()
           dot(7)
           for point in p2body:  
               penup()
               goto(point.x, point.y)
               pendown()
               dot(7, "blue")
           p2body.append(p2head)    
           penup()
           color('blue')
           goto(p2xy.x, p2xy.y)
           pendown()
           dot(7)
        
        
     
        if counter == 0 :
         Motor1.goto(p1xy.x + 12 , p1xy.y - 8)
        elif counter == 1 :
         Motor1.goto(p1xy.x + 8 , p1xy.y + 12)
        elif counter == 2 :
         Motor1.goto(p1xy.x - 12 , p1xy.y + 8)
        elif counter == 3 :
         Motor1.goto(p1xy.x - 8 , p1xy.y - 12)
    
        if counter2 == 0 :
         Motor2.goto(p2xy.x - 12, p2xy.y + 8)
        elif counter2 == 1 :
         Motor2.goto(p2xy.x - 8, p2xy.y - 12)
        elif counter2 == 2 :
         Motor2.goto(p2xy.x + 12, p2xy.y - 8)
        elif counter2 == 3 :
         Motor2.goto(p2xy.x + 8, p2xy.y + 12)

        update()
        ontimer(draw, running)
        
    hideturtle()
    tracer(False)
    listen()
    onkey(lambda: (p1aim.rotate(90), change_motor_shape_a()), 'a' or 'A')
    onkey(lambda: (p1aim.rotate(-90), change_motor_shape_d()), 'd' or 'D')
    onkey(lambda: (p2aim.rotate(90), change_motor_shape_left()), 'Left')
    onkey(lambda: (p2aim.rotate(-90),change_motor_shape_right()), 'Right')
    onkey(lambda: (pause_menu()), 'Escape')

    draw()
    done()

def start_desert_race():
    screen = Screen()
    screen.setup(width=720, height=640)
    screen.bgcolor("#884A39")
    screen.bgpic("Documents/col_buyuk.gif")
    screen.addshape("Documents/blue_atv_right.gif")
    screen.addshape("Documents/blue_atv_left.gif")
    screen.addshape("Documents/blue_atv_up.gif")
    screen.addshape("Documents/blue_atv_down.gif")
    screen.addshape("Documents/yellow_atv_left.gif")
    screen.addshape("Documents/yellow_atv_down.gif")
    screen.addshape("Documents/yellow_atv_up.gif")
    screen.addshape("Documents/yellow_atv_right.gif")
    screen.addshape("Documents/0_can.gif")
    screen.addshape("Documents/1_can.gif")
    screen.addshape("Documents/2_can.gif")
    screen.addshape("Documents/3_can.gif")
    screen.addshape("Documents/pause_menu.gif")
    screen.addshape("Documents/bariyer.gif")
    screen.addshape("Documents/longer.gif")
    screen.addshape("Documents/shorter.gif")
    screen.addshape("Documents/ceyrek_power_up.gif")
    screen.addshape("Documents/yarim_power_up.gif")
    screen.addshape("Documents/full_power_up.gif")
    screen.addshape("Documents/power_up_null.gif")
    screen.addshape("Documents/fast.gif")
    screen.addshape("Documents/slow.gif")
    screen.addshape("Documents/yellow_atv.gif")
    screen.addshape("Documents/blue_atv.gif")

    health_bar_1 = Turtle()
    health_bar_1.shape(f"Documents/{health1}_can.gif")
    health_bar_1.penup()
    health_bar_1.goto(-230,260)
    

    health_bar_2 = Turtle()
    health_bar_2.shape(f"Documents/{health2}_can.gif")
    health_bar_2.penup()
    health_bar_2.goto(230,260)
    
    yellow_atv = Turtle()
    yellow_atv.shape("Documents/yellow_atv.gif")
    yellow_atv.penup()
    yellow_atv.goto(-290,260)

    blue_atv = Turtle()
    blue_atv.shape("Documents/blue_atv.gif")
    blue_atv.penup()
    blue_atv.goto(170,260)

    player1_label = tk.Label(text=MainMenu.player1_name, fg="dark blue", bg="#8B93FF",font=("Elephant", 9))
    player1_label.place(relx=0.20, rely=0.042, anchor="center")
    player2_label = tk.Label(text=MainMenu.player2_name, fg="dark blue", bg="#8B93FF",font=("Elephant", 9))
    player2_label.place(relx=0.85, rely=0.042, anchor="center")
    
    random_location_x = random.randint(-250, 100)
    random_location_y = random.randint(-200, 100)

    p1xy = vector(random_location_x, random_location_y)
    p1aim = vector(4, 0)
    p1body = []

    p2xy = vector(random_location_x + 200, random_location_y)
    p2aim = vector(-4, 0)
    p2body = []

    Atv1 = Turtle()
    Atv1.shape("Documents/yellow_atv_right.gif")
    Atv1.penup()
    Atv1.goto(p1xy.x, p1xy.y)

    Atv2 = Turtle()
    Atv2.shape("Documents/blue_atv_left.gif")
    Atv2.penup()
    Atv2.goto(p2xy.x, p2xy.y)
    
    longer_power_up = Turtle()
    longer_power_up.shape("Documents/longer.gif")
    longer_power_up.penup()
    longer_power_up.goto(-150,150)

    shorter_power_up = Turtle()
    shorter_power_up.shape("Documents/shorter.gif")
    shorter_power_up.penup()
    shorter_power_up.goto(150,-150)

    faster_power_up = Turtle()
    faster_power_up.shape("Documents/fast.gif")
    faster_power_up.penup()
    faster_power_up.goto(-150,-150)

    slower_power_up = Turtle()
    slower_power_up.shape("Documents/slow.gif")
    slower_power_up.penup()
    slower_power_up.goto(150,150)

    def end_game_due_to_time():
        import import_mysql
        import MainMenu
        global running
        if health1 == health2:
            draw_label = tk.Label(text="DRAW!", fg="dark blue", bg="#8B93FF", font=("Elephant", 40))
            draw_label.place(relx=0.5, rely=0.5, anchor="center")
            draw_label.update()
            running=100000
            elapsed_time = time.time() - start_time 
            import_mysql.add_data(MainMenu.player1_name,(3 - health2),(3 - health1),MainMenu.player2_name,elapsed_time,'Desert')
            time.sleep(999999999999)  
            draw_label.destroy()
            
            
        elif health1 > health2:
            running = 1000000
            elapsed_time = time.time() - start_time 
            import_mysql.add_data(MainMenu.player1_name,(3 - health2),(3 - health1),MainMenu.player2_name,elapsed_time,'Desert')
            display_winner("yellow")
            time.sleep(999999999999)
        else:
            running = 1000000
            elapsed_time = time.time() - start_time 
            import_mysql.add_data(MainMenu.player1_name,(3 - health2),(3 - health1),MainMenu.player2_name,elapsed_time,'Desert')
            display_winner("blue")
            time.sleep(999999999999)
    
    screen.ontimer(end_game_due_to_time, 150000)

    def display_winner(winner):
        pygame.mixer.music.stop()
        penup()
        if winner == "yellow":
           winner_label = tk.Label(text=f"{MainMenu.player1_name} WINS!", fg="dark blue", bg="#8B93FF",font=("Elephant", 40))
           winner_label.place(relx=0.5, rely=0.5, anchor="center")
        elif winner == "blue":
           winner_label = tk.Label(text=f"{MainMenu.player2_name} WINS!", fg="dark blue", bg="#8B93FF",font=("Elephant", 40))
           winner_label.place(relx=0.5, rely=0.5, anchor="center")
        done()
    
    def display_counter():
     for i in range(3, 0, -1):
      title_label = tk.Label(text=i, fg="dark blue", bg="#8B93FF",font=("Goudy Stout", 50,'bold'))
      title_label.place(relx=0.5, rely=0.5, anchor="center")
      title_label.update()  
      time.sleep(1)
      title_label.destroy()
    
     title_label2 = tk.Label(text="GO!", fg="dark blue", bg="#8B93FF", font=("Goudy Stout", 50,'bold'))
     title_label2.place(relx=0.5, rely=0.5, anchor="center")
     title_label2.update()
     time.sleep(1)
     title_label2.destroy()
    
    display_counter()
    def inside(head):
        return -336 < head.x < 334 and -266 < head.y < 212
    
    def inside_obstacle(head):
        return -25 < head.x < 25 and -25 < head.y < 25
    
    def change_atv_shape_a():
        global counter
        if counter == 0:
            Atv1.shape("Documents/yellow_atv_up.gif")
            counter += 1
        elif counter == 1:
            Atv1.shape("Documents/yellow_atv_left.gif")
            counter += 1
        elif counter == 2:
            Atv1.shape("Documents/yellow_atv_down.gif")
            counter += 1
        elif counter == 3:
            Atv1.shape("Documents/yellow_atv_right.gif")
            counter = 0
    def change_atv_shape_d():
        global counter
        if counter == 3:
            Atv1.shape("Documents/yellow_atv_left.gif")
            counter -= 1
        elif counter == 2:
            Atv1.shape("Documents/yellow_atv_up.gif")
            counter -= 1
        elif counter == 1:
            Atv1.shape("Documents/yellow_atv_right.gif")
            counter -= 1
        elif counter == 0:
            Atv1.shape("Documents/yellow_atv_down.gif")
            counter = 3

    def change_atv_shape_left():
        global counter2
        if counter2 == 0:
            Atv2.shape("Documents/blue_atv_down.gif")
            counter2 += 1
        elif counter2 == 1:
            Atv2.shape("Documents/blue_atv_right.gif")
            counter2 += 1
        elif counter2 == 2:
            Atv2.shape("Documents/blue_atv_up.gif")
            counter2 += 1
        elif counter2 == 3:
            Atv2.shape("Documents/blue_atv_left.gif")
            counter2 = 0

    def change_atv_shape_right():
        global counter2
        if counter2 == 3:
            Atv2.shape("Documents/blue_atv_right.gif")
            counter2 -= 1
        elif counter2 == 2:
            Atv2.shape("Documents/blue_atv_down.gif")
            counter2 -= 1
        elif counter2 == 1:
            Atv2.shape("Documents/blue_atv_left.gif")
            counter2 -= 1
        elif counter2 == 0:
            Atv2.shape("Documents/blue_atv_up.gif")
            counter2 = 3

    def reset():
     global counter, counter2,running,longerx,longery,current_shape_index_1,current_shape_index_2,shorterx,shortery,length1,length2,slowerx,slowery,fasterx,fastery
     counter = 0
     counter2 = 0
     running = 40
     longerx = 165
     longery = 135
     shorterx = 135
     shortery = 165
     length1 = 60
     length2 = 60
     fasterx = 165
     fastery = 135
     slowerx = 135
     slowery = 165
     current_shape_index_1 = 3
     current_shape_index_2 = 3
     longer_power_up.hideturtle()
     shorter_power_up.hideturtle()
     faster_power_up.hideturtle()
     slower_power_up.hideturtle()
     clear()
     Atv1.goto(-1000, 0)
     Atv2.goto(1000, 0)
     start_desert_race()
    
    def crashSound():
       pygame.mixer.music.pause()
       pygame.mixer.music.load("Documents/Crashing (Sound Effect).mp3")
       pygame.mixer.music.play()
       time.sleep(1)
       pygame.mixer.music.load("Documents/Desert_theme_song.mp3")
       pygame.mixer.music.play()
    
    def laserSound():
       pygame.mixer.music.pause()
       pygame.mixer.music.load("Documents/Laser Sound Effect.mp3")
       pygame.mixer.music.play()
       time.sleep(1)
       pygame.mixer.music.load("Documents/Desert_theme_song.mp3")
       pygame.mixer.music.play()

    pausemenu = Turtle()
    pausemenu.hideturtle()
    
    def pause_menu():
     global running
     pausemenu.showturtle()
     clear()
     turtle.update()
     pausemenu.shape("Documents/pause_menu.gif")
     pausemenu.penup()
     pausemenu.goto(-20,0)
     resume_button = tk.Button(text="    RESUME" ,command=lambda: [volume_100_button.destroy(),volume_50_button.destroy(),volume_0_button.destroy(),resume_button.destroy(),restart_button.destroy(),quit_button.destroy(),resume_game()], bd=0, bg='black',fg= "white",font=("Elephant", 14),width = 12, activebackground="black")
     resume_button.place(relx=0.49, rely=0.53, anchor="center")
     restart_button = tk.Button(text="   RESTART" ,command=lambda: [volume_100_button.destroy(),volume_50_button.destroy(),volume_0_button.destroy(),restart_button.destroy(),resume_button.destroy(),quit_button.destroy(),restart_game()], bd=0, bg='black',fg= "white",font=("Elephant", 14),width = 12, activebackground="black")
     restart_button.place(relx=0.19, rely=0.53, anchor="center")
     quit_button = tk.Button(text=" QUIT" ,command=lambda: [volume_100_button.destroy(),volume_50_button.destroy(),volume_0_button.destroy(),restart_button.destroy(),resume_button.destroy(),quit_button.destroy(),screen.bye()], bd=0, bg='black',fg= "white",font=("Elephant", 14),width = 12, activebackground="black")
     quit_button.place(relx=0.805, rely=0.53, anchor="center")
     volume_0_button = tk.Button(text=" 0 %" ,command=lambda: [volume(0)], bd=0, bg='#FF5BAE',fg= "white",font=("Cooper Black", 20),width = 6,height = 1, activebackground="#D10363",borderwidth=5)
     volume_0_button.place(relx=0.282, rely=0.734, anchor="center")
     volume_50_button = tk.Button(text="50 %" ,command=lambda: [volume(50)], bd=0, bg='#FF5BAE',fg= "white",font=("Cooper Black", 20),width = 6,height = 1, activebackground="#D10363",borderwidth=5)
     volume_50_button.place(relx=0.51, rely=0.734, anchor="center")
     volume_100_button = tk.Button(text="100 %" ,command=lambda: [volume(100)], bd=0, bg='#FF5BAE',fg= "white",font=("Cooper Black", 20),width = 6,height = 1, activebackground="#D10363",borderwidth=5)
     volume_100_button.place(relx=0.742, rely=0.734, anchor="center")
     clear()
     running = 1000000 
     
      
    def resume_game():
      global running
      running = 40
      turtle.update()
      pausemenu.hideturtle()
      draw()
    
    def restart_game():
     global counter, counter2,health1,health2,running,longerx,longery,current_shape_index_1,current_shape_index_2,shorterx,shortery,length1,length2,fastery,fasterx,slowerx,slowery,start_time
     counter = 0
     counter2 = 0
     health1 = 3
     health2 = 3
     running = 40
     longerx = 165
     longery = 135
     shorterx = 135
     shortery = 165 
     length1 = 60
     length2 = 60
     fasterx = 165
     fastery = 135
     slowerx = 135
     slowery = 165
     current_shape_index_1 = 3
     current_shape_index_2 = 3
     longer_power_up.hideturtle()
     shorter_power_up.hideturtle()
     faster_power_up.hideturtle()
     slower_power_up.hideturtle()
     pausemenu.hideturtle()
     start_time = time.time()
     clear()
     Atv1.goto(-1000, 0)
     Atv2.goto(1000, 0)
     start_desert_race()
     
    def volume(level):
       if level == 0:
          pygame.mixer.music.set_volume(0.0)
       elif level == 50:
          pygame.mixer.music.set_volume(0.5)
       else:
          pygame.mixer.music.set_volume(1.0)

    def draw_obstacle():
         barrier = Turtle()
         barrier.shape("Documents/bariyer.gif")
         barrier.penup()
         barrier.goto(+150,-60)

    def change_length_1():
      global current_shape_index_1,length1,length2
      if length1 > 60:
         longer_power_up.goto(-255,257)
      elif length2 < 60:
         shorter_power_up.goto(-255,257)
      power_up_bar = Turtle()
      power_up_bar.hideturtle()
      if(current_shape_index_1 <= 2):
       power_up_bar.shape(shapes_1[current_shape_index_1])
       power_up_bar.penup()
       power_up_bar.goto(-230,260)
       power_up_bar.showturtle()
       ontimer(change_length_1,8000)
       current_shape_index_1 += 1
      else:
         power_up_bar.shape(shapes_1[current_shape_index_1])
         power_up_bar.penup()
         power_up_bar.goto(-230,260)
         power_up_bar.showturtle()
         if(length1 > 60):
          longer_power_up.hideturtle()
          length1 = 60
          p1body.clear()
          
         elif(length2 < 60):
            shorter_power_up.hideturtle()
            length2 = 60
            p2body.clear()

    def change_speed_1():
      global current_shape_index_1,running
      if running < 40:
         faster_power_up.goto(-255,257)
      elif running > 40:
         slower_power_up.goto(-255,257)
      power_up_bar = Turtle()
      power_up_bar.hideturtle()
      if(current_shape_index_1 <= 2):
       power_up_bar.shape(shapes_1[current_shape_index_1])
       power_up_bar.penup()
       power_up_bar.goto(-230,260)
       power_up_bar.showturtle()
       ontimer(change_speed_1,8000)
       current_shape_index_1 += 1
      else:
         power_up_bar.shape(shapes_1[current_shape_index_1])
         power_up_bar.penup()
         power_up_bar.goto(-230,260)
         power_up_bar.showturtle()
         if running < 40:
            faster_power_up.hideturtle()
            running = 40
         elif running > 40:
            slower_power_up.hideturtle()
            running = 40

         

    def change_length_2():
      global current_shape_index_2,length1,length2
      if length2 > 60:
         longer_power_up.goto(205,257)
      elif length1 < 60:
         shorter_power_up.goto(205,257)
      power_up_bar = Turtle()
      power_up_bar.hideturtle()
      if(current_shape_index_2 <= 2):
       power_up_bar.shape(shapes_2[current_shape_index_2])
       power_up_bar.penup()
       power_up_bar.goto(230,260)
       power_up_bar.showturtle()
       ontimer(change_length_2,8000)
       current_shape_index_2 += 1
      else:
         power_up_bar.shape(shapes_2[current_shape_index_2])
         power_up_bar.penup()
         power_up_bar.goto(230,260)
         power_up_bar.showturtle()
         if(length1 < 60):
          shorter_power_up.hideturtle()
          length1 = 60
          p1body.clear()
          
         elif(length2 > 60):
            longer_power_up.hideturtle()
            length2 = 60
            p2body.clear()
    
    def change_speed_2():
      global current_shape_index_2,running
      if running < 40:
         faster_power_up.goto(205,257)
      elif running > 40:
         slower_power_up.goto(205,257)
      power_up_bar = Turtle()
      power_up_bar.hideturtle()
      if(current_shape_index_2 <= 2):
       power_up_bar.shape(shapes_2[current_shape_index_2])
       power_up_bar.penup()
       power_up_bar.goto(230,260)
       power_up_bar.showturtle()
       ontimer(change_speed_2,8000)
       current_shape_index_2 += 1
      else:
         power_up_bar.shape(shapes_2[current_shape_index_2])
         power_up_bar.penup()
         power_up_bar.goto(230,260)
         power_up_bar.showturtle()
         if running < 40:
            faster_power_up.hideturtle()
            running = 40
         elif running > 40:
            slower_power_up.hideturtle()
            running = 40

    def draw():
        global counter,counter2,health1,health2,running,length1,length2,longerx,longery,shorterx,shortery,current_shape_index_1,current_shape_index_2,fasterx,fastery,slowerx,slowery
        p1xy.move(p1aim)
        p1head = p1xy.copy()
        
        p2xy.move(p2aim)
        p2head = p2xy.copy()

        if (p1head.x >= -longerx and p1head.x <= -longery and p1head.y <= longerx and p1head.y >= longery):
            if current_shape_index_1 == 3:
             current_shape_index_1 = 0
             length1 = 200
             longerx = 1000
             longery = 1000
             change_length_1()

        if (p1head.x >= shorterx and p1head.x <= shortery and p1head.y <= -shorterx and p1head.y >= -shortery):
            if current_shape_index_1 == 3:
             p2body.clear()
             length2 = 20
             shorterx = 1000
             shortery = 1000
             current_shape_index_1 = 0
             change_length_1()
        
        if (p1head.x >= -fasterx and p1head.x <= -fastery and p1head.y >= -fasterx and p1head.y <= -fastery):
            if current_shape_index_1 == 3:
             running = 20
             fasterx = 1000
             fastery = 1000
             current_shape_index_1 = 0
             change_speed_1()
        
        if (p1head.x >= slowerx and p1head.x <= slowery and p1head.y >= slowerx and p1head.y <= slowery):
            if current_shape_index_1 == 3:
             running = 60
             slowerx = 1000
             slowery = 1000
             current_shape_index_1 = 0
             change_speed_1()
            
        
        if not inside(p1head) or inside_obstacle(p1head):
           crashSound()
           health1 -= 1
           if health1 == 0:
            health_bar_1.shape(f"Documents/{health1}_can.gif")
            update() 
            end_game_due_to_time()
            return    
           reset()
           return
        
        elif p1head in p2body or p1head  in p1body:
            laserSound()
            if (p1xy.x == p2xy.x + 8 and p1xy.y == p2xy.y) or (p1xy.y + 8 == p2xy.y and p1xy.x == p2xy.x):
             draw_label = tk.Label(text=" DRAW!", fg="dark blue", bg="#8B93FF",font=("Elephant", 40))
             draw_label.place(relx=0.5, rely=0.5, anchor="center")
             draw_label.update()
             time.sleep(1)
             draw_label.destroy()
             reset()
             return
            health1 -= 1
            if health1 == 0:
             health_bar_1.shape(f"Documents/{health1}_can.gif")
             update() 
             end_game_due_to_time()
             return    
            reset()
            return
                 
        if (p2head.x >= -longerx and p2head.x <= -longery and p2head.y <= longerx and p2head.y >= longery):
            if current_shape_index_2 == 3:
             current_shape_index_2 = 0
             length2 = 200
             longerx = 1000
             longery = 1000
             change_length_2()
        
        if (p2head.x >= shorterx and p2head.x <= shortery and p2head.y <= -shorterx and p2head.y >= -shortery):
          if current_shape_index_2 == 3:
             p1body.clear()
             length1 = 20
             shorterx = 1000
             shortery = 1000
             current_shape_index_2 = 0
             change_length_2()
        
        if (p2head.x >= -fasterx and p2head.x <= -fastery and p2head.y >= -fasterx and p2head.y <= -fastery):
            if current_shape_index_2 == 3:
             running = 20
             fasterx = 1000
             fastery = 1000
             current_shape_index_2 = 0
             change_speed_2()
        
        if (p2head.x >= slowerx and p2head.x <= slowery and p2head.y >= slowerx and p2head.y <= slowery):
            if current_shape_index_2 == 3:
             running = 60
             slowerx = 1000
             slowery = 1000
             current_shape_index_2 = 0
             change_speed_2()

        if not inside(p2head) or inside_obstacle(p2head):
           crashSound()
           health2 -= 1
           if health2 == 0:
            health_bar_2.shape(f"Documents/{health2}_can.gif")
            update()
            end_game_due_to_time()
            return 
           reset()
           return
        
        elif p2head  in p1body or p2head in p2body :
           laserSound()
           if (p1xy.x == p2xy.x + 8 and p1xy.y == p2xy.y) or (p1xy.y + 8 == p2xy.y and p1xy.x == p2xy.x):
             draw_label = tk.Label(text=" DRAW!", fg="dark blue", bg="#8B93FF",font=("Elephant", 40))
             draw_label.place(relx=0.5, rely=0.5, anchor="center")
             draw_label.update()
             time.sleep(1)
             draw_label.destroy()
             reset()
             return
           health2 -= 1
           if health2 == 0:
            health_bar_2.shape(f"Documents/{health2}_can.gif")
            update()
            end_game_due_to_time()
            return 
           reset()
           return
        

        if len(p1body) < length1:
          p1body.append(p1head)
          penup()
          color('yellow')
          goto(p1xy.x, p1xy.y)
          pendown()
          dot(10)
           
           
        if len(p2body) < length2:
         p2body.append(p2head)
         penup()
         color('blue')
         goto(p2xy.x, p2xy.y)
         pendown()
         dot(10)
         
        if (len(p1body) == length1) or (len(p2body) == length2):
           p1body.pop(0)  
           p2body.pop(0)  
           clear()  
           for point in p1body:  
               penup()
               goto(point.x, point.y)
               pendown()
               dot(10, "yellow")
           p1body.append(p1head)
           penup()
           color('yellow')
           goto(p1xy.x, p1xy.y)
           pendown()
           dot(10)
           for point in p2body:  
               penup()
               goto(point.x, point.y)
               pendown()
               dot(10, "blue")
           p2body.append(p2head)    
           penup()
           color('blue')
           goto(p2xy.x, p2xy.y)
           pendown()
           dot(10)
        
     
        if counter == 0 :
         Atv1.goto(p1xy.x + 14 , p1xy.y + 1)
        elif counter == 1 :
         Atv1.goto(p1xy.x - 1 , p1xy.y + 14)
        elif counter == 2 :
         Atv1.goto(p1xy.x - 14 , p1xy.y - 1)
        elif counter == 3 :
         Atv1.goto(p1xy.x + 1 , p1xy.y - 14)
    
        if counter2 == 0 :
         Atv2.goto(p2xy.x - 14, p2xy.y - 1)
        elif counter2 == 1 :
         Atv2.goto(p2xy.x + 1, p2xy.y - 14)
        elif counter2 == 2 :
         Atv2.goto(p2xy.x + 14, p2xy.y + 1)
        elif counter2 == 3 :
         Atv2.goto(p2xy.x - 1, p2xy.y + 14)

        update()
        ontimer(draw, running)
        
    hideturtle()
    tracer(False)
    listen()
    onkey(lambda: (p1aim.rotate(90), change_atv_shape_a()), 'a' or 'A')
    onkey(lambda: (p1aim.rotate(-90), change_atv_shape_d()), 'd' or 'D')
    onkey(lambda: (p2aim.rotate(90), change_atv_shape_left()), 'Left')
    onkey(lambda: (p2aim.rotate(-90),change_atv_shape_right()), 'Right')
    onkey(lambda: [pause_menu()], 'Escape')

    draw_obstacle()
    draw()
    done()

def start_forest_race():
    screen = Screen()
    screen.setup(width=720, height=640)
    screen.bgcolor("#0A6847")
    screen.bgpic("Documents/cim_buyuk.gif")
    screen.addshape("Documents/blue_atv_right.gif")
    screen.addshape("Documents/blue_atv_left.gif")
    screen.addshape("Documents/blue_atv_up.gif")
    screen.addshape("Documents/blue_atv_down.gif")
    screen.addshape("Documents/yellow_atv_left.gif")
    screen.addshape("Documents/yellow_atv_down.gif")
    screen.addshape("Documents/yellow_atv_up.gif")
    screen.addshape("Documents/yellow_atv_right.gif")
    screen.addshape("Documents/0_can.gif")
    screen.addshape("Documents/1_can.gif")
    screen.addshape("Documents/2_can.gif")
    screen.addshape("Documents/3_can.gif")
    screen.addshape("Documents/pause_menu.gif")
    screen.addshape("Documents/bariyer.gif")
    screen.addshape("Documents/longer.gif")
    screen.addshape("Documents/shorter.gif")
    screen.addshape("Documents/ceyrek_power_up.gif")
    screen.addshape("Documents/yarim_power_up.gif")
    screen.addshape("Documents/full_power_up.gif")
    screen.addshape("Documents/power_up_null.gif")
    screen.addshape("Documents/fast.gif")
    screen.addshape("Documents/slow.gif")
    screen.addshape("Documents/yellow_atv.gif")
    screen.addshape("Documents/blue_atv.gif")

    health_bar_1 = Turtle()
    health_bar_1.shape(f"Documents/{health1}_can.gif")
    health_bar_1.penup()
    health_bar_1.goto(-230,260)
    

    health_bar_2 = Turtle()
    health_bar_2.shape(f"Documents/{health2}_can.gif")
    health_bar_2.penup()
    health_bar_2.goto(230,260)
    
    yellow_atv = Turtle()
    yellow_atv.shape("Documents/yellow_atv.gif")
    yellow_atv.penup()
    yellow_atv.goto(-290,260)

    blue_atv = Turtle()
    blue_atv.shape("Documents/blue_atv.gif")
    blue_atv.penup()
    blue_atv.goto(170,260)
    
    player1_label = tk.Label(text=MainMenu.player1_name, fg="dark blue", bg="#8B93FF",font=("Elephant", 9))
    player1_label.place(relx=0.20, rely=0.042, anchor="center")
    player2_label = tk.Label(text=MainMenu.player2_name, fg="dark blue", bg="#8B93FF",font=("Elephant", 9))
    player2_label.place(relx=0.85, rely=0.042, anchor="center")
    
    random_location_x = random.randint(-250, 100)
    random_location_y = random.randint(-200, 100)

    p1xy = vector(random_location_x, random_location_y)
    p1aim = vector(4, 0)
    p1body = []

    p2xy = vector(random_location_x + 200, random_location_y)
    p2aim = vector(-4, 0)
    p2body = []

    Atv1 = Turtle()
    Atv1.shape("Documents/yellow_atv_right.gif")
    Atv1.penup()
    Atv1.goto(p1xy.x, p1xy.y)

    Atv2 = Turtle()
    Atv2.shape("Documents/blue_atv_left.gif")
    Atv2.penup()
    Atv2.goto(p2xy.x, p2xy.y)
    
    longer_power_up = Turtle()
    longer_power_up.shape("Documents/longer.gif")
    longer_power_up.penup()
    longer_power_up.goto(-150,150)

    shorter_power_up = Turtle()
    shorter_power_up.shape("Documents/shorter.gif")
    shorter_power_up.penup()
    shorter_power_up.goto(150,-150)

    faster_power_up = Turtle()
    faster_power_up.shape("Documents/fast.gif")
    faster_power_up.penup()
    faster_power_up.goto(-150,-150)

    slower_power_up = Turtle()
    slower_power_up.shape("Documents/slow.gif")
    slower_power_up.penup()
    slower_power_up.goto(150,150)

    
    def end_game_due_to_time():
        import import_mysql
        import MainMenu
        global running
        if health1 == health2:
            draw_label = tk.Label(text="DRAW!", fg="dark blue", bg="#8B93FF", font=("Elephant", 40))
            draw_label.place(relx=0.5, rely=0.5, anchor="center")
            draw_label.update()
            running=100000
            elapsed_time = time.time() - start_time 
            import_mysql.add_data(MainMenu.player1_name,(3 - health2),(3 - health1),MainMenu.player2_name,elapsed_time,'Forest')
            time.sleep(999999999999)  
            draw_label.destroy()
            
            
        elif health1 > health2:
            running = 1000000
            elapsed_time = time.time() - start_time 
            import_mysql.add_data(MainMenu.player1_name,(3 - health2),(3 - health1),MainMenu.player2_name,elapsed_time,'Forest')
            display_winner("yellow")
            time.sleep(999999999999)
        else:
            running = 1000000
            elapsed_time = time.time() - start_time 
            import_mysql.add_data(MainMenu.player1_name,(3 - health2),(3 - health1),MainMenu.player2_name,elapsed_time,'Forest')
            display_winner("blue")
            time.sleep(999999999999)
    
    screen.ontimer(end_game_due_to_time, 150000)
    
    def display_winner(winner):
        pygame.mixer.music.stop()
        penup()
        if winner == "yellow":
           winner_label = tk.Label(text=f"{MainMenu.player1_name} WINS!", fg="dark blue", bg="#8B93FF",font=("Elephant", 40))
           winner_label.place(relx=0.5, rely=0.5, anchor="center")
        elif winner == "blue":
           winner_label = tk.Label(text=f"{MainMenu.player2_name} WINS!", fg="dark blue", bg="#8B93FF",font=("Elephant", 40))
           winner_label.place(relx=0.5, rely=0.5, anchor="center")
        done()
    
    def display_counter():
     for i in range(3, 0, -1):
      title_label = tk.Label(text=i, fg="dark blue", bg="#8B93FF",font=("Goudy Stout", 50,'bold'))
      title_label.place(relx=0.5, rely=0.5, anchor="center")
      title_label.update()  
      time.sleep(1)
      title_label.destroy()
    
     title_label2 = tk.Label(text="GO!", fg="dark blue", bg="#8B93FF", font=("Goudy Stout", 50,'bold'))
     title_label2.place(relx=0.5, rely=0.5, anchor="center")
     title_label2.update()
     time.sleep(1)
     title_label2.destroy()
    
    display_counter()
    def inside(head):
        return -336 < head.x < 334 and -266 < head.y < 212
    
    def inside_obstacle_1(head):
        return -290 < head.x < -240 and 125 < head.y < 175
    
    def inside_obstacle_2(head):
        return 260 < head.x < 310 and 125 < head.y < 175
    
    def inside_obstacle_3(head):
        return 260 < head.x < 310 and -215 < head.y < -165
    
    def inside_obstacle_4(head):
        return -290 < head.x < -240 and -215 < head.y < -165

    def change_atv_shape_a():
        global counter
        if counter == 0:
            Atv1.shape("Documents/yellow_atv_up.gif")
            counter += 1
        elif counter == 1:
            Atv1.shape("Documents/yellow_atv_left.gif")
            counter += 1
        elif counter == 2:
            Atv1.shape("Documents/yellow_atv_down.gif")
            counter += 1
        elif counter == 3:
            Atv1.shape("Documents/yellow_atv_right.gif")
            counter = 0
    def change_atv_shape_d():
        global counter
        if counter == 3:
            Atv1.shape("Documents/yellow_atv_left.gif")
            counter -= 1
        elif counter == 2:
            Atv1.shape("Documents/yellow_atv_up.gif")
            counter -= 1
        elif counter == 1:
            Atv1.shape("Documents/yellow_atv_right.gif")
            counter -= 1
        elif counter == 0:
            Atv1.shape("Documents/yellow_atv_down.gif")
            counter = 3

    def change_atv_shape_left():
        global counter2
        if counter2 == 0:
            Atv2.shape("Documents/blue_atv_down.gif")
            counter2 += 1
        elif counter2 == 1:
            Atv2.shape("Documents/blue_atv_right.gif")
            counter2 += 1
        elif counter2 == 2:
            Atv2.shape("Documents/blue_atv_up.gif")
            counter2 += 1
        elif counter2 == 3:
            Atv2.shape("Documents/blue_atv_left.gif")
            counter2 = 0

    def change_atv_shape_right():
        global counter2
        if counter2 == 3:
            Atv2.shape("Documents/blue_atv_right.gif")
            counter2 -= 1
        elif counter2 == 2:
            Atv2.shape("Documents/blue_atv_down.gif")
            counter2 -= 1
        elif counter2 == 1:
            Atv2.shape("Documents/blue_atv_left.gif")
            counter2 -= 1
        elif counter2 == 0:
            Atv2.shape("Documents/blue_atv_up.gif")
            counter2 = 3

    def reset():
     global counter, counter2,running,longerx,longery,current_shape_index_1,current_shape_index_2,shorterx,shortery,length1,length2,slowerx,slowery,fasterx,fastery
     counter = 0
     counter2 = 0
     running = 40
     longerx = 165
     longery = 135
     shorterx = 135
     shortery = 165
     length1 = 60
     length2 = 60
     fasterx = 165
     fastery = 135
     slowerx = 135
     slowery = 165
     current_shape_index_1 = 3
     current_shape_index_2 = 3
     longer_power_up.hideturtle()
     shorter_power_up.hideturtle()
     faster_power_up.hideturtle()
     slower_power_up.hideturtle()
     clear()
     Atv1.goto(-1000, 0)
     Atv2.goto(1000, 0)
     start_forest_race()
    
    def crashSound():
       pygame.mixer.music.pause()
       pygame.mixer.music.load("Documents/Crashing (Sound Effect).mp3")
       pygame.mixer.music.play()
       time.sleep(1)
       pygame.mixer.music.load("Documents/Hill Climb Racing - Theme Song.mp3")
       pygame.mixer.music.play()
    
    def laserSound():
       pygame.mixer.music.pause()
       pygame.mixer.music.load("Documents/Laser Sound Effect.mp3")
       pygame.mixer.music.play()
       time.sleep(1)
       pygame.mixer.music.load("Documents/Hill Climb Racing - Theme Song.mp3")
       pygame.mixer.music.play()

    pausemenu = Turtle()
    pausemenu.hideturtle()
    
    def pause_menu():
     global running
     pausemenu.showturtle()
     clear()
     turtle.update()
     pausemenu.shape("Documents/pause_menu.gif")
     pausemenu.penup()
     pausemenu.goto(-20,0)
     resume_button = tk.Button(text="    RESUME" ,command=lambda: [volume_100_button.destroy(),volume_50_button.destroy(),volume_0_button.destroy(),resume_button.destroy(),restart_button.destroy(),quit_button.destroy(),resume_game()], bd=0, bg='black',fg= "white",font=("Elephant", 14),width = 12, activebackground="black")
     resume_button.place(relx=0.49, rely=0.53, anchor="center")
     restart_button = tk.Button(text="   RESTART" ,command=lambda: [volume_100_button.destroy(),volume_50_button.destroy(),volume_0_button.destroy(),restart_button.destroy(),resume_button.destroy(),quit_button.destroy(),restart_game()], bd=0, bg='black',fg= "white",font=("Elephant", 14),width = 12, activebackground="black")
     restart_button.place(relx=0.19, rely=0.53, anchor="center")
     quit_button = tk.Button(text=" QUIT" ,command=lambda: [volume_100_button.destroy(),volume_50_button.destroy(),volume_0_button.destroy(),restart_button.destroy(),resume_button.destroy(),quit_button.destroy(),screen.bye()], bd=0, bg='black',fg= "white",font=("Elephant", 14),width = 12, activebackground="black")
     quit_button.place(relx=0.805, rely=0.53, anchor="center")
     volume_0_button = tk.Button(text=" 0 %" ,command=lambda: [volume(0)], bd=0, bg='#FF5BAE',fg= "white",font=("Cooper Black", 20),width = 6,height = 1, activebackground="#D10363",borderwidth=5)
     volume_0_button.place(relx=0.282, rely=0.734, anchor="center")
     volume_50_button = tk.Button(text="50 %" ,command=lambda: [volume(50)], bd=0, bg='#FF5BAE',fg= "white",font=("Cooper Black", 20),width = 6,height = 1, activebackground="#D10363",borderwidth=5)
     volume_50_button.place(relx=0.51, rely=0.734, anchor="center")
     volume_100_button = tk.Button(text="100 %" ,command=lambda: [volume(100)], bd=0, bg='#FF5BAE',fg= "white",font=("Cooper Black", 20),width = 6,height = 1, activebackground="#D10363",borderwidth=5)
     volume_100_button.place(relx=0.742, rely=0.734, anchor="center")
     clear()
     running = 1000000 
     
      
    def resume_game():
      global running
      running = 40
      turtle.update()
      pausemenu.hideturtle()
      draw()
    
    def restart_game():
     global counter, counter2,health1,health2,running,longerx,longery,current_shape_index_1,current_shape_index_2,shorterx,shortery,length1,length2,fastery,fasterx,slowerx,slowery,start_time
     counter = 0
     counter2 = 0
     health1 = 3
     health2 = 3
     running = 40
     longerx = 165
     longery = 135
     shorterx = 135
     shortery = 165 
     length1 = 60
     length2 = 60
     fasterx = 165
     fastery = 135
     slowerx = 135
     slowery = 165
     current_shape_index_1 = 3
     current_shape_index_2 = 3
     longer_power_up.hideturtle()
     shorter_power_up.hideturtle()
     faster_power_up.hideturtle()
     slower_power_up.hideturtle()
     pausemenu.hideturtle()
     start_time = time.time()
     clear()
     Atv1.goto(-1000, 0)
     Atv2.goto(1000, 0)
     start_forest_race()
     
    def volume(level):
       if level == 0:
          pygame.mixer.music.set_volume(0.0)
       elif level == 50:
          pygame.mixer.music.set_volume(0.5)
       else:
          pygame.mixer.music.set_volume(1.0)

    def draw_obstacle():
         barrier_1 = Turtle()
         barrier_1.shape("Documents/bariyer.gif")
         barrier_1.penup()
         barrier_1.goto(-120,90)

         barrier_2 = Turtle()
         barrier_2.shape("Documents/bariyer.gif")
         barrier_2.penup()
         barrier_2.goto(430,90)

         barrier_3 = Turtle()
         barrier_3.shape("Documents/bariyer.gif")
         barrier_3.penup()
         barrier_3.goto(430,-250)

         barrier_4 = Turtle()
         barrier_4.shape("Documents/bariyer.gif")
         barrier_4.penup()
         barrier_4.goto(-120,-250)

    def change_length_1():
      global current_shape_index_1,length1,length2
      if length1 > 60:
         longer_power_up.goto(-255,257)
      elif length2 < 60:
         shorter_power_up.goto(-255,257)
      power_up_bar = Turtle()
      power_up_bar.hideturtle()
      if(current_shape_index_1 <= 2):
       power_up_bar.shape(shapes_1[current_shape_index_1])
       power_up_bar.penup()
       power_up_bar.goto(-230,260)
       power_up_bar.showturtle()
       ontimer(change_length_1,8000)
       current_shape_index_1 += 1
      else:
         power_up_bar.shape(shapes_1[current_shape_index_1])
         power_up_bar.penup()
         power_up_bar.goto(-230,260)
         power_up_bar.showturtle()
         if(length1 > 60):
          longer_power_up.hideturtle()
          length1 = 60
          p1body.clear()
          
         elif(length2 < 60):
            shorter_power_up.hideturtle()
            length2 = 60
            p2body.clear()

    def change_speed_1():
      global current_shape_index_1,running
      if running < 40:
         faster_power_up.goto(-255,257)
      elif running > 40:
         slower_power_up.goto(-255,257)
      power_up_bar = Turtle()
      power_up_bar.hideturtle()
      if(current_shape_index_1 <= 2):
       power_up_bar.shape(shapes_1[current_shape_index_1])
       power_up_bar.penup()
       power_up_bar.goto(-230,260)
       power_up_bar.showturtle()
       ontimer(change_speed_1,8000)
       current_shape_index_1 += 1
      else:
         power_up_bar.shape(shapes_1[current_shape_index_1])
         power_up_bar.penup()
         power_up_bar.goto(-230,260)
         power_up_bar.showturtle()
         if running < 40:
            faster_power_up.hideturtle()
            running = 40
         elif running > 40:
            slower_power_up.hideturtle()
            running = 40

         

    def change_length_2():
      global current_shape_index_2,length1,length2
      if length2 > 60:
         longer_power_up.goto(205,257)
      elif length1 < 60:
         shorter_power_up.goto(205,257)
      power_up_bar = Turtle()
      power_up_bar.hideturtle()
      if(current_shape_index_2 <= 2):
       power_up_bar.shape(shapes_2[current_shape_index_2])
       power_up_bar.penup()
       power_up_bar.goto(230,260)
       power_up_bar.showturtle()
       ontimer(change_length_2,8000)
       current_shape_index_2 += 1
      else:
         power_up_bar.shape(shapes_2[current_shape_index_2])
         power_up_bar.penup()
         power_up_bar.goto(230,260)
         power_up_bar.showturtle()
         if(length1 < 60):
          shorter_power_up.hideturtle()
          length1 = 60
          p1body.clear()
          
         elif(length2 > 60):
            longer_power_up.hideturtle()
            length2 = 60
            p2body.clear()
    
    def change_speed_2():
      global current_shape_index_2,running
      if running < 40:
         faster_power_up.goto(205,257)
      elif running > 40:
         slower_power_up.goto(205,257)
      power_up_bar = Turtle()
      power_up_bar.hideturtle()
      if(current_shape_index_2 <= 2):
       power_up_bar.shape(shapes_2[current_shape_index_2])
       power_up_bar.penup()
       power_up_bar.goto(230,260)
       power_up_bar.showturtle()
       ontimer(change_speed_2,8000)
       current_shape_index_2 += 1
      else:
         power_up_bar.shape(shapes_2[current_shape_index_2])
         power_up_bar.penup()
         power_up_bar.goto(230,260)
         power_up_bar.showturtle()
         if running < 40:
            faster_power_up.hideturtle()
            running = 40
         elif running > 40:
            slower_power_up.hideturtle()
            running = 40
       

    def draw():

        global counter,counter2,health1,health2,running,length1,length2,longerx,longery,shorterx,shortery,current_shape_index_1,current_shape_index_2,fasterx,fastery,slowerx,slowery
        p1xy.move(p1aim)
        p1head = p1xy.copy()
        
        p2xy.move(p2aim)
        p2head = p2xy.copy()

        if (p1head.x >= -longerx and p1head.x <= -longery and p1head.y <= longerx and p1head.y >= longery):
            if current_shape_index_1 == 3:
             current_shape_index_1 = 0
             length1 = 200
             longerx = 1000
             longery = 1000
             change_length_1()

        if (p1head.x >= shorterx and p1head.x <= shortery and p1head.y <= -shorterx and p1head.y >= -shortery):
            if current_shape_index_1 == 3:
             p2body.clear()
             length2 = 20
             shorterx = 1000
             shortery = 1000
             current_shape_index_1 = 0
             change_length_1()
        
        if (p1head.x >= -fasterx and p1head.x <= -fastery and p1head.y >= -fasterx and p1head.y <= -fastery):
            if current_shape_index_1 == 3:
             running = 20
             fasterx = 1000
             fastery = 1000
             current_shape_index_1 = 0
             change_speed_1()
        
        if (p1head.x >= slowerx and p1head.x <= slowery and p1head.y >= slowerx and p1head.y <= slowery):
            if current_shape_index_1 == 3:
             running = 60
             slowerx = 1000
             slowery = 1000
             current_shape_index_1 = 0
             change_speed_1()
            
        
        if not inside(p1head) or inside_obstacle_1(p1head) or inside_obstacle_2(p1head) or inside_obstacle_3(p1head) or inside_obstacle_4(p1head):
           crashSound()
           health1 -= 1
           if health1 == 0:
            health_bar_1.shape(f"Documents/{health1}_can.gif")
            update() 
            end_game_due_to_time()
            return    
           reset()
           return
        
        elif p1head in p2body or p1head  in p1body:
            laserSound()
            if (p1xy.x == p2xy.x + 8 and p1xy.y == p2xy.y) or (p1xy.y + 8 == p2xy.y and p1xy.x == p2xy.x):
             draw_label = tk.Label(text=" DRAW!", fg="dark blue", bg="#8B93FF",font=("Elephant", 40))
             draw_label.place(relx=0.5, rely=0.5, anchor="center")
             draw_label.update()
             time.sleep(1)
             draw_label.destroy()
             reset()
             return
            health1 -= 1
            if health1 == 0:
             health_bar_1.shape(f"Documents/{health1}_can.gif")
             update() 
             end_game_due_to_time()
             return    
            reset()
            return
                 
        if (p2head.x >= -longerx and p2head.x <= -longery and p2head.y <= longerx and p2head.y >= longery):
            if current_shape_index_2 == 3:
             current_shape_index_2 = 0
             length2 = 200
             longerx = 1000
             longery = 1000
             change_length_2()
        
        if (p2head.x >= shorterx and p2head.x <= shortery and p2head.y <= -shorterx and p2head.y >= -shortery):
          if current_shape_index_2 == 3:
             p1body.clear()
             length1 = 20
             shorterx = 1000
             shortery = 1000
             current_shape_index_2 = 0
             change_length_2()
        
        if (p2head.x >= -fasterx and p2head.x <= -fastery and p2head.y >= -fasterx and p2head.y <= -fastery):
            if current_shape_index_2 == 3:
             running = 20
             fasterx = 1000
             fastery = 1000
             current_shape_index_2 = 0
             change_speed_2()
        
        if (p2head.x >= slowerx and p2head.x <= slowery and p2head.y >= slowerx and p2head.y <= slowery):
            if current_shape_index_2 == 3:
             running = 60
             slowerx = 1000
             slowery = 1000
             current_shape_index_2 = 0
             change_speed_2()

        if not inside(p2head) or inside_obstacle_1(p2head) or inside_obstacle_2(p2head) or inside_obstacle_3(p2head) or inside_obstacle_4(p2head):
           crashSound()
           health2 -= 1
           if health2 == 0:
            health_bar_2.shape(f"Documents/{health2}_can.gif")
            update()
            end_game_due_to_time()
            return 
           reset()
           return
        
        elif p2head  in p1body or p2head in p2body :
           laserSound()
           if (p1xy.x == p2xy.x + 8 and p1xy.y == p2xy.y) or (p1xy.y + 8 == p2xy.y and p1xy.x == p2xy.x):
             draw_label = tk.Label(text=" DRAW!", fg="dark blue", bg="#8B93FF",font=("Elephant", 40))
             draw_label.place(relx=0.5, rely=0.5, anchor="center")
             draw_label.update()
             time.sleep(1)
             draw_label.destroy()
             reset()
             return
           health2 -= 1
           if health2 == 0:
            health_bar_2.shape(f"Documents/{health2}_can.gif")
            update()
            end_game_due_to_time()
            return 
           reset()
           return
        

        if len(p1body) < length1:
          p1body.append(p1head)
          penup()
          color('yellow')
          goto(p1xy.x, p1xy.y)
          pendown()
          dot(10)
           
           
        if len(p2body) < length2:
         p2body.append(p2head)
         penup()
         color('blue')
         goto(p2xy.x, p2xy.y)
         pendown()
         dot(10)
         
        if (len(p1body) == length1) or (len(p2body) == length2):
           p1body.pop(0)  
           p2body.pop(0)  
           clear()  
           for point in p1body:  
               penup()
               goto(point.x, point.y)
               pendown()
               dot(10, "yellow")
           p1body.append(p1head)
           penup()
           color('yellow')
           goto(p1xy.x, p1xy.y)
           pendown()
           dot(10)
           for point in p2body:  
               penup()
               goto(point.x, point.y)
               pendown()
               dot(10, "blue")
           p2body.append(p2head)    
           penup()
           color('blue')
           goto(p2xy.x, p2xy.y)
           pendown()
           dot(10)
        
     
        if counter == 0 :
         Atv1.goto(p1xy.x + 14 , p1xy.y + 1)
        elif counter == 1 :
         Atv1.goto(p1xy.x - 1 , p1xy.y + 14)
        elif counter == 2 :
         Atv1.goto(p1xy.x - 14 , p1xy.y - 1)
        elif counter == 3 :
         Atv1.goto(p1xy.x + 1 , p1xy.y - 14)
    
        if counter2 == 0 :
         Atv2.goto(p2xy.x - 14, p2xy.y - 1)
        elif counter2 == 1 :
         Atv2.goto(p2xy.x + 1, p2xy.y - 14)
        elif counter2 == 2 :
         Atv2.goto(p2xy.x + 14, p2xy.y + 1)
        elif counter2 == 3 :
         Atv2.goto(p2xy.x - 1, p2xy.y + 14)

        update()
        ontimer(draw, running)
        
    hideturtle()
    tracer(False)
    listen()
    onkey(lambda: (p1aim.rotate(90), change_atv_shape_a()), 'a' or 'A')
    onkey(lambda: (p1aim.rotate(-90), change_atv_shape_d()), 'd' or 'D')
    onkey(lambda: (p2aim.rotate(90), change_atv_shape_left()), 'Left')
    onkey(lambda: (p2aim.rotate(-90),change_atv_shape_right()), 'Right')
    onkey(lambda: [pause_menu()], 'Escape')
    
    draw_obstacle()
    draw()
    done()
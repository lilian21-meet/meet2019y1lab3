import turtle
import time
import pygame
pygame.mixer.init()
pygame.mixer.music.load('WrongBuzzer.mp3')

turtle.bgcolor("cornflowerblue")
pygame.mixer.pre_init(44100, -16, 2, 2048) # setup mixer to avoid sound lag

pygame.init()

pygame.mixer.init()

pygame.mixer.music.load("bellaciao.wav")

pygame.mixer.music.play(-1)


screen = turtle.Screen()
turtle.bgpic('earth.gif')
pen =turtle.Turtle()
flag = turtle.Turtle()
pen.hideturtle()
pen.hideturtle()
flag.hideturtle()
turtle.register_shape('austrelia.gif')
pen.up()
pen.goto(-70,-360)
current_page= 'welcome'
pen.down()
for i in range(2):
    pen.pencolor('red')
    pen.pensize(6)
    pen.forward(120)
    pen.left(90)
    pen.forward(35)
    pen.left(90)

    

pen.penup()
pen.forward(30)
pen.write("start", font=('Arial',20,
                         "normal"))
    
def btnclick (x,y):
    global current_page
    if current_page == "welcome":

        if x > -80 and x < 40 and y > -360 and y < -300 :
            current_page="new page"
            flag_pages()

    if current_page=="new page":
        if x > 0 and x < 300 and y > 0 and y < 100:
            flag.clear()
            coral_reef_puzzle()
            

    if x > -350 and x < -20 and y > 0 and y < 178 :
            print('aaa')  


def coral_reef_puzzle():

    turtle.hideturtle()
    turtle.speed(10)
    turtle.pensize(10)
    turtle.goto(0,200)

    turtle.goto(0,0)

    turtle.goto(-200,0)
    turtle.goto(-200,200)
    turtle.goto(0,200)
    turtle.penup()
    turtle.goto(-200,0)
    turtle.pendown()
    turtle.goto(-400,0)
    turtle.goto(-400,200)
    turtle.goto(-200,200)
    turtle.penup()
    turtle.goto(-400,0)
    turtle.pendown()
    turtle.goto(-400,-200)
    turtle.goto(-200,-200)
    turtle.goto(-200,0)
    turtle.penup()
    turtle.goto(0,0)
    turtle.pendown()
    turtle.goto(0,-200)
    turtle.goto(-200,-200)
    turtle.penup()
    turtle.showturtle()
    turtle.speed(3)
  
   

    #connecting peices to drag
    turtle.register_shape("lilian2.gif")
    l = turtle.clone()
    l.penup()
    l.shape("lilian2.gif")
    l.goto(-85,-85)
    turtle.register_shape("hiba.gif")
    h = turtle.clone()
    h.penup()
    h.shape("hiba.gif")
    h.goto(400,50)

    turtle.register_shape("neriya.gif")
    s = turtle.clone()
    s.penup()
    s.shape("neriya.gif")
    s.goto(500,-200)

    turtle.register_shape("asaad.gif")
    a = turtle.clone()
    a.penup()
    a.shape("asaad.gif")
    a.goto(400,-300)

    time_turtle=turtle.Turtle()

    e = 100
    g = 200
    def drag_1(x, y):
        print("in drag 1")
        gotoresult = l.goto(x, y)
        print(l.xcor(), l.ycor())
        global e
        e = l.xcor()
        global g
        g = l.ycor()
        return l.pos()
    ##    turtle.onscreenclick(l.goto)
    ##    
    ##    turtle.getscreen()._root.mainloop()
    ##    turtle.update()
    ##    return l.pos()

    def drag_2():
        turtle.onscreenclick(h.goto)
        turtle.getscreen()._root.mainloop()
        
    def drag_3():
        turtle.onscreenclick(s.goto)
        turtle.getscreen()._root.mainloop()

    def drag_4():
        turtle.onscreenclick(a.goto)
        turtle.getscreen()._root.mainloop()
    z = turtle.onscreenclick(drag_1)
    print(z)
    turtle.onkeypress(drag_1, '1')
    turtle.onkeypress(drag_2, '2')
    turtle.onkeypress(drag_3, '3')
    turtle.onkeypress(drag_4, '4')
    turtle.listen()
  



    n = 0
    time_turtle.goto(-400,200)
    time_turtle.penup()
    def countdown():
        global n
        time_turtle.clear()
        time_turtle.write(str(n), move=False, align="left", font=("Arial", 24, "normal"))
        if n>0:
            print(n)
            n= n-1
        elif n==0:
            
            pygame.mixer.music.play(0)


            quit()

        turtle.ontimer(countdown,1000)

    n=45
    countdown()

                 
    def endgame_win():
        #time.sleep(10)
        print(l.pos())
        
        if (abs(g - (-100))<= 10) and (abs(e - (-100) ) <= 10):
            print("test")
    ##        if (abs(h.ycor() - ) <= 10) and (abs(h.xcor() - ) <= 10):
    ##            if (abs(n.ycor() - ) <=10) and (abs(n.ycor() - <=10):
    ##                if (abs(a.ycor() - ) <=10 and (abs(a.ycor() -<=10):
            print("awesome")
    endgame_win()

##########################################################
          

            
        

def flag_pages():
    turtle.bgpic('bsc.gif')
    flag.shape('austrelia.gif')
    flag.goto(150,0)
    flag.stamp()
##    turtle.register_shape('china.gif')
##    flag.shape('china.gif')
    flag.goto(-200,0)
    flag.stamp()
    pen.clear()

turtle.onscreenclick(btnclick,1)
turtle.listen()

turtle.done()

turtle.mainloop()

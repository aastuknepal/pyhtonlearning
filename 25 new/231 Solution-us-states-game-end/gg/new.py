import turtle

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "r.gif"
screen.addshape(image)
turtle.shape(image)



def display_coordinates(x, y):
    print(x,y)
    



turtle.onscreenclick(display_coordinates)

turtle.mainloop()








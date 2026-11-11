import turtle

t = turtle.Turtle()
t.speed(0)
t.pensize(2)
turtle.bgcolor("black")                          # fond noir comme sur l'image

couleurs = ["cyan", "magenta", "yellow", "orange"]   # couleurs de l'image

C = 175                        # rayon du grand cercle

def petale(r):              
    t.circle(r, 60)
    t.left(120)
    t.circle(r, 60)
    t.left(120)

def couronne(r, nb):
    for i in range(nb):
        t.pencolor(couleurs[i % len(couleurs)])  # MODIFIÉ : couleur du contour en cycle
        petale(r)
        t.left(360 / nb)

# Les couches : de la plus grande (r = C) à la plus petite
for r in range(C, 10, -15):
    couronne(r, 16)

# Cercle rouge autour : les grands pétales le touchent
t.penup()
t.goto(0, -C)
t.setheading(0)
t.pendown()
t.pencolor("red")
t.pensize(4)
t.circle(C)

t.hideturtle()
turtle.done()
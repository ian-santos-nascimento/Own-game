#   Tela
import turtle
tela = turtle.Screen()
tela.tracer(0)
tela.bgcolor("black")
tela.title("Jogo de Futebol")
tela.setup(width= 800, height= 600)


#  Bola
bola = turtle.Turtle()
bola.speed(0)
bola.up()
bola.color("white")
bola.shape("circle")
bola.goto(0, -250)


#  Trave central
trave_central = turtle.Turtle()
trave_central.speed(0)
trave_central.up()
trave_central.color("white")
trave_central.shape("square")
trave_central.goto(0, 300)
trave_central.shapesize(stretch_wid=2, stretch_len=15)
#Defensor
defensor = turtle.Turtle()
defensor.speed(0)
defensor.up()
defensor.goto(0, 270)
defensor.color("red")
defensor.shape('square')
defensor.shapesize(stretch_len=5, stretch_wid= 1)

# Placar
placar = turtle.Turtle()
placar.hideturtle()
placar.speed(0)
placar.up()
placar.color("blue")
placar.write('Gols: 0', align="center", font=('Arial', 20, 'normal'))
placar.goto(-300, -175)
x = 0


#  Velocidade da bola e do defensor:
bola.dx = float(1.0)
bola.dy = float(0.1)
defensor.dx = float(1.0)

#  Funções
def movimento_horizontal():

    bola.setx(bola.xcor() + bola.dx)

def movimento_vertical():
    bola.sety(bola.ycor() + bola.dy)

def movimento_defensor():
    defensor.setx((defensor.xcor() + defensor.dx))
while True:
    tela.update()

    #  Movimento Horizontal da Bola
    movimento_horizontal()
    if bola.xcor() >= 380:
        bola.dx *= -1
    if bola.xcor() <= -380:
        bola.dx *= - 1

    # Movimento Vertical e retorno
    tela.listen()
    tela.onkeypress(movimento_vertical, "w")
    if bola.ycor() != -250:
        for i in range(30):
            movimento_vertical()
    if bola.ycor() > 290:
        bola.goto(0, -250)
        movimento_horizontal()

#  Movimento Do goleiro
    movimento_defensor()
    if  defensor.xcor() > 150 or -150 > defensor.xcor():
        defensor.dx *= -1


#   Quando fizer um gol
    if bola.ycor() < trave_central.ycor() + 30 and bola.ycor() > trave_central.ycor() - 30 and -150 <bola.xcor() < 150:
        x += 1
        placar.clear()
        placar.write(f'Gols: {x //6}')

#  Quando bater no defensor
    if bola.ycor() < (defensor.ycor() + 10) and (bola.ycor() > defensor.ycor() - 10) and defensor.xcor() - 50 < bola.xcor() < defensor.xcor() + 50:
        bola.goto(0, -250)

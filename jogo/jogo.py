# Nesse teste vamos tentar criar uma janela ambiente para rodar algum tipo de jogo em cima dela.
# Primeiro, temos que importar o turtle, ao que parece é o que nos permitirá criar janelas e, em cima dele,
# definir o aspecto dessa janela, onde o jogo se ambientará.

import turtle

# Depois de importado, vamos definir as características da janela que se deseja usar:

wn = turtle.Screen()
wn.title('Esse vai ser o ambiente do jogo.')
wn.bgcolor('white')
wn.setup(width=800, height=600)
# Esse último comando eu ainda não identifiquei para que serve...
wn.tracer(0)

#Aqui serão criadas algumas variáveis para ajustar O PLACAR do jogo:
placar_A = 0
placar_B = 0


# Agora que isso foi feito, temos que usar um comando para que essa tela permaneça ativa o tempo.
# Se trata de um loop, na verdade.

#Nesse momento já fizemos a janela funcionar, mas antes disso temos que configurar as barras de cada jogador,
#bem como a 'bola' que será utilizada nesse jogo simples. Vamos nessa.

#Barra do jogador A - Esquerda.
barra_A = turtle.Turtle()
#no caso o primeiro turtle fica com t minúsculo porque é o nome principal e o segundo T
#em maiúsculo porque se trata da 'classe' que se está utilizando dentro do turtle.

barra_A.speed(0)
#Essa não é a velocidade de movimento da barra, mas da permanência da animação, pelo que eu entendi.
barra_A.shape('square')
#Esse comando é pra dizer a forma da barra, no caso de um quadrado.
barra_A.color('blue')
#Após isso, vamos definir as dimensões da barra:
barra_A.shapesize(stretch_wid=5, stretch_len=1)
barra_A.penup()
#Definimos a cor da barra e esse outro comando eu não entendi para que funciona.
#Próximo passo é definir o local onde essa barra vai aparecer inicialmente na tela:
barra_A.goto(-350,0)

#Barra do jogador B - Direita.
barra_B = turtle.Turtle()

barra_B.speed(0)
#Essa não é a velocidade de movimento da barra, mas da permanência da animação, pelo que eu entendi.
barra_B.shape('square')
#Esse comando é pra dizer a forma da barra, no caso de um quadrado.
barra_B.color('red')
#Após isso, vamos definir as dimensões da barra:
barra_B.shapesize(stretch_wid=5, stretch_len=1)
barra_B.penup()
#Definimos a cor da barra e esse outro comando eu não entendi para que funciona.
#Próximo passo é definir o local onde essa barra vai aparecer inicialmente na tela:
barra_B.goto(350,0)

#Bola que será utilizada. Vamos copiar um dos códigos das barras para ser essa nossa bola.
bola = turtle.Turtle()

bola.speed(0)
bola.shape('circle')
bola.color('black')
#bola.shapesize(stretch_wid=5, stretch_len=1) - não precisa definir o tamanho, porque vamos usar
#o que já vem predefinido.
bola.penup()
bola.goto(0,0)
#As coordenadas são (0,0) porque queremos que ela inicie no centro da tela.

#Os movimentos da bola vão entrar em dois campos separados, no eixo X e eixo Y.
(bola.dx) = 0.2
(bola.dy) = 0.2
#Essas informações de cima dizem que a bola sempre vai se mover pra direita e pra cima em 2 pixels.

#Nesse momento vamos inserir as indicações de placar referentes ao jogo criado:
placar = turtle.Turtle()
placar.speed(0)
placar.color('red')
placar.penup()
placar.hideturtle()
placar.goto(0, 260)
placar.write('Jogador A: 0 Jogador B: 0', align='center', font=('Courier', 24, 'normal'))


#Após isso, vamos DEFINIR as funções, para que as barras possam ser movimentadas pelo nosso teclado.
def barra_A_up():
    y = barra_A.ycor()
    y+= 20
    barra_A.sety(y)
def barra_A_down():
    y = barra_A.ycor()
    y -= 20
    barra_A.sety(y)

def barra_B_up():
    y = barra_B.ycor()
    y+= 20
    barra_B.sety(y)
def barra_B_down():
    y = barra_B.ycor()
    y -= 20
    barra_B.sety(y)

#Agora temos que fazer a janela reconhecer ou receber o comando vindo do teclado, para mexer a barra:
wn.listen()
wn.onkeypress(barra_A_up, 'w')
wn.onkeypress(barra_A_down, 's')
wn.onkeypress(barra_B_up, '8')
wn.onkeypress(barra_B_down, '2')

while True:
    wn.update()
# Desta forma a janela permanece aberta o tempo que quisermos.
# Nesse momento sim, vamos fazer a bola se mexer.
    bola.setx(bola.xcor() + bola.dx)
    bola.sety(bola.ycor() + bola.dy)

#Após isso, a bola tem que reconhecer as bordas da janela que criamos inicialmente.
    if bola.ycor() > 290:
        bola.sety(290)
        bola.dy *= -1
#Isso funciona para dizer que quando a bola chegar numa certa altura ela vai inverter a direção do movimento.
    if bola.ycor() < -290:
        bola.sety(-290)
        bola.dy *= -1
    if bola.xcor() > 390:
        bola.goto(0, 0)
        bola.dx *= -1
        placar.clear()
        placar_A += 1
        placar.write('Jogador A: {} Jogador B: {}'.format(placar_A, placar_B), align='center', font=('Courier', 24, 'normal'))
    if bola.xcor() < -390:
        bola.goto(0, 0)
        bola.dx *= -1
        placar.clear()
        placar_B += 1
        placar.write('Jogador A: {} Jogador B: {}'.format(placar_A, placar_B), align='center', font=('Courier', 24, 'normal'))
#Agora temos que definir como vai ocorrer a colisão entre a bola e as barras:

    if (bola.xcor() > 340 and bola.xcor() < 350) and (bola.ycor() < barra_B.ycor() + 40 and bola.ycor() > barra_B.ycor() - 40):
        bola.setx(340)
        bola.dx *= -1
    if (bola.xcor() < -340 and bola.xcor() > -350) and (bola.ycor() > barra_A.ycor() - 40 and bola.ycor() < barra_A.ycor() + 40):
        bola.setx(-340)
        bola.dx *= -1



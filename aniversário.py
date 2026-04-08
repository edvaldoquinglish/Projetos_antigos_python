import turtle
import time

# Configuração da tela
tela = turtle.Screen()
tela.bgcolor("black")
tela.title("Feliz Aniversário Pai ")

t = turtle.Turtle()
t.speed(0)
t.hideturtle()

# Função para escrever texto animado
def escrever(texto, x, y, tamanho=15, cor="white"):
    t.penup()
    t.goto(x, y)
    t.color(cor)
    t.write(texto, align="center", font=("Arial", tamanho, "bold"))

# Função para desenhar bolo
def desenhar_bolo():
    t.penup()
    t.goto(-100,-50)
    t.pendown()
    t.color("brown")
    t.begin_fill()
    for _ in range(2):
        t.forward(200)
        t.left(90)
        t.forward(100)
        t.left(90)
    t.end_fill()

# Função para desenhar velas
def desenhar_velas():
    cores = ["red", "blue", "yellow"]
    posicoes = [-60, 0, 60]

    for i in range(3):
        t.penup()
        t.goto(posicoes[i], 50)
        t.pendown()
        t.color(cores[i])
        t.begin_fill()
        t.left(90)
        t.forward(40)
        t.right(90)
        t.forward(10)
        t.right(90)
        t.forward(40)
        t.left(90)
        t.end_fill()

        # chama a função chama
        desenhar_chama(posicoes[i] + 5, 90)

# Função para desenhar chama
def desenhar_chama(x, y):
    t.penup()
    t.goto(x, y)
    t.color("orange")
    t.begin_fill()
    t.circle(5)
    t.end_fill()

# Animação do texto
def animacao_texto():
    mensagens = [
        "Feliz Aniversário",
        "Pai ",
        "Muita saúde, felicidade",
        "E sucesso sempre!"
    ]

    y = 150
    for msg in mensagens:
        escrever(msg, 0, y)
        y += 50
        time.sleep(1)

# Função principal
def main():
    animacao_texto()
    time.sleep(1)

    desenhar_bolo()
    desenhar_velas()

    time.sleep(1)

    escrever("Te amo Pai ", 0, -120, 25, "yellow")

# Executar
main()

turtle.done()

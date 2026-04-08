import tkinter as tk
import random

janela = tk.Tk()
janela.title("Pedido de Namoro ")
janela.geometry("400x300")
janela.config(bg="#ff7eb3")

# Texto
label = tk.Label(janela, text="Tenho algo importante pra te dizer...",
                 font=("Arial", 12), bg="#ff7eb3", fg="white")
label.pack(pady=20)

# Função SIM
def sim():
    label.config(text="EU SABIA \nAgora somos um casal ")

# Função NÃO (foge)
def fugir(event):
    x = random.randint(0, 500)
    y = random.randint(0, 200)
    btn_nao.place(x=x, y=y)

# Botões
btn_sim = tk.Button(janela, text="SIM ", command=sim, bg="green", fg="white")
btn_sim.pack(pady=10)

btn_nao = tk.Button(janela, text="NÃO ", bg="red", fg="white")
btn_nao.place(x=150, y=150)
btn_nao.bind("<Enter>", fugir)

janela.mainloop()

import tkinter as tk
from tkinter import ttk
from tkinter.scrolledtext import ScrolledText


def criar_interface():
    janela = tk.Tk()

    janela.title("Text Based RPG")
    janela.geometry("1100x700")
    janela.configure(bg="#e7e7e7")

    janela.columnconfigure(0, weight=2, minsize=200)
    janela.columnconfigure(1, weight=3, minsize=350)
    janela.columnconfigure(2, weight=2, minsize=200)
    janela.minsize(900, 550)

    janela.rowconfigure(0, weight=1)

    #Painéis pais
    painel_esquerdo = tk.Frame(janela, bg="#E2E2E2")
    painel_esquerdo.grid(row=0, column=0, sticky="nsew")

    painel_central = tk.Frame(janela, bg="#E2E2E2")
    painel_central.grid(row=0, column=1, sticky="nsew")

    painel_direito = tk.Frame(janela, bg="#E2E2E2")
    painel_direito.grid(row=0, column=2, sticky="nsew")


    #Configurações do Painel Esquerdo
    painel_esquerdo.rowconfigure(0, weight=55)
    painel_esquerdo.rowconfigure(1, weight=45)

    painel_esquerdo.columnconfigure(0, weight=1)

    #Configurações do Painel Direito
    painel_direito.rowconfigure(0, weight=1)

    painel_direito.columnconfigure(0, weight=1)

    # Configurações do Painel Central
    painel_central.rowconfigure(0, weight=59)
    painel_central.rowconfigure(1, weight=1)
    painel_central.columnconfigure(0, weight=1)

    lista_inventario = criar_inventario(painel_esquerdo)
    campo_anotacoes = criar_anotacoes(painel_esquerdo)
    ficha = criar_ficha(painel_direito)
    atualizar_vida(ficha, 75, 100)
    atualizar_xp(ficha, 25, 100)
    atualizar_atributos(ficha, 8, 5, 9)
    atualizar_nome(ficha, "Arthur")
    atualizar_nivel(ficha, 1)

    historia, caixa_texto = criar_historia(painel_central)
    configurar_eventos_historia(historia, caixa_texto)
    configurar_eventos_inventario(lista_inventario, janela)

    
    janela.mainloop()

def atualizar_vida(ficha, vida_atual, vida_maxima):
    ficha["vida"]["value"] = vida_atual
    ficha["vida"]["maximum"] = vida_maxima
    ficha["texto_vida"].config(
        text=f"HP: {vida_atual} / {vida_maxima}"
    )

def atualizar_xp(ficha, xp_atual, xp_maxima):
    ficha["xp"]["value"] = xp_atual
    ficha["xp"]["maximum"] = xp_maxima
    ficha["texto_xp"].config(
        text=f"XP: {xp_atual} / {xp_maxima}"
    )

def atualizar_atributos(ficha, forca, defesa, agilidade):
    ficha["atributos"].config(
        text=f"Força = {forca}\nDefesa = {defesa}\nAgilidade = {agilidade}"
    )

def atualizar_nome(ficha, personagem):
    ficha["personagem"].config(
        text=f"{personagem}"
    )

def atualizar_nivel(ficha, nivel):
    ficha["nivel"].config(
        text=f"Nível = {nivel}"
    )

def criar_ficha(painel_direito):
    #Configurações Personagem
    painel_personagem = tk.Frame(painel_direito, bg="#D2D2D2", highlightbackground="black", highlightthickness=1)
    painel_personagem.grid(row=0, column=0, sticky="nsew", padx=5, pady=2.5)

    titulo_personagem = tk.Label(
        painel_personagem,
        text="PERSONAGEM",
        bg="#D2D2D2",
        fg="#070707",
        font=("Times New Roman", 13, "bold")
    )
    titulo_personagem.pack(pady=12)

    #Descrições Personagem
    nome_personagem = tk.Label(
        painel_personagem,
        text=" ",
        anchor="w",
        justify="left",
        bg="#D2D2D2",
        fg="#070707",
        font=("Times New Roman", 9, "bold")
    )
    nome_personagem.pack(fill="x", padx=12, pady=6)


    texto_nivel = tk.Label(
        painel_personagem,
        text=f"Nível = 0",
        anchor="w",
        justify="left",
        bg="#D2D2D2",
        fg="#070707",
        font=("Times New Roman", 9, "bold")
    )
    texto_nivel.pack(fill="x", padx=12, pady=6)

    atributos_personagem = tk.Label(
        painel_personagem,
        text="Força = 0\nDefesa = 0\nAgilidade = 0",
        anchor="w",
        justify="left",
        bg="#D2D2D2",
        fg="#070707",
        font=("Times New Roman", 9, "bold")
    )
    atributos_personagem.pack(fill="x", padx=12, pady=6)

    #Barra de Vida e Experiencia
    texto_vida = tk.Label(
        painel_personagem,
        text="HP: 100 / 100",
        bg="#D2D2D2",
        fg="#070707",
        font=("Times New Roman", 12)
    )

    texto_vida.pack(pady=5)

    barra_vida = ttk.Progressbar(
        painel_personagem,
        orient="horizontal",
        length=200,
        mode="determinate",
        maximum=100,
        value=100
    )

    barra_vida.pack(padx=15, pady=5, fill="x")

    texto_xp = tk.Label(
        painel_personagem,
        text="XP: 75 / 100",
        bg="#D2D2D2",
        fg="#070707",
        font=("Times New Roman", 12)
    )

    texto_xp.pack(pady=5)

    barra_xp = ttk.Progressbar(
        painel_personagem,
        orient="horizontal",
        length=200,
        mode="determinate",
        maximum=100,
        value=75
    )

    barra_xp.pack(padx=15, pady=5, fill="x")
    
    return {
    "vida": barra_vida,
    "texto_vida": texto_vida,
    "xp": barra_xp,
    "texto_xp": texto_xp,
    "atributos": atributos_personagem,
    "personagem": nome_personagem,
    "nivel": texto_nivel
}


def criar_anotacoes(painel_esquerdo):
    #Configurações Anotações
    painel_anotacoes = tk.Frame(painel_esquerdo, bg="#D2D2D2", highlightbackground="black", highlightthickness=1)
    painel_anotacoes.grid(row=1, column=0, sticky="nsew", padx=5, pady=2.5)

    titulo_anotacoes = tk.Label(
        painel_anotacoes,
        text="ANOTAÇÕES",
        bg="#D2D2D2",
        fg="#070707",
        font=("Times New Roman", 13, "bold") 
    )
    titulo_anotacoes.pack(pady=12)

    campo_anotacoes = tk.Text(
        painel_anotacoes,
        font=("Times New Roman", 11),
        bg="#D2D2D2",
        fg="#070707",
        wrap="word",
        relief="flat",
        width=1,
        height=1
    )

    campo_anotacoes.pack(
        fill="both",
        expand=True,
        padx=10,
        pady=10
    )

    return campo_anotacoes

def criar_inventario(painel_esquerdo):
    #Configurações Inventário
    painel_inventario = tk.Frame(painel_esquerdo, bg="#D2D2D2", highlightbackground="black", highlightthickness=1)
    painel_inventario.grid(row=0, column=0, sticky="nsew", padx=5, pady=2.5)

    titulo_inventario = tk.Label(
        painel_inventario,
        text="INVENTÁRIO",
        bg="#D2D2D2",
        fg="#070707",
        font=("Times New Roman", 13, "bold")
    )
    titulo_inventario.pack(pady=12)

    lista_inventario = tk.Listbox(
        painel_inventario,
        font=("Times New Roman", 12),
        bg="#D2D2D2",
        fg="#070707",
        relief="flat",
        selectbackground="#A0A0A0"
    )

    lista_inventario.pack(
        fill="both",
        expand=True,
        padx=10,
        pady=5
    )

    itens = ["Espada enferrujada", "Poção de vida", "Chave antiga"]

    for item in itens:
        lista_inventario.insert(tk.END, item)

    return lista_inventario

def criar_historia(painel_central):
    #Configurações História
    painel_historia = tk.Frame(painel_central, bg="#D2D2D2", highlightbackground="black", highlightthickness=1)
    painel_historia.grid(row=0, column=0, sticky="nsew", padx=5, pady=2.5)

    historia = ScrolledText(
        painel_historia,
        font=("Times New Roman", 12),
        bg="#D2D2D2",
        fg="#070707",
        wrap="word",
        relief="flat",
        insertbackground="white",
        width=1,
        height =1
    )
    historia.pack(fill="both", expand=True, padx=10, pady=10)
    historia.config(state="disabled")

    # Configurações Entrada de Comandos
    painel_comandos = tk.Frame(painel_central, bg="#D2D2D2", highlightbackground="black", highlightthickness=1)
    painel_comandos.grid(
        row=1,
        column=0,
        sticky="nsew",
        padx=5,
        pady=2.5
    )

    caixa_texto = tk.Entry(
        painel_comandos,
        font=("Times New Roman", 12),
        bg="#B2B2B2",
        fg="#070707",
        insertbackground="white",
        relief="flat"
    )

    caixa_texto.pack(fill="both", padx=10, pady=10)

    return historia, caixa_texto

def configurar_eventos_historia(historia, caixa_texto):
    #Função Responsável por Inserir Mensagens
    def adicionar_historia(mensagem):
        historia.config(state="normal")

        historia.insert(tk.END, f"{mensagem}\n")
        historia.see(tk.END)

        historia.config(state="disabled")
    #Configurações Recebimento de Comandos
    def enviar_comando(event):
        comando = caixa_texto.get().strip()
        if comando:
            adicionar_historia(f"> {comando}")
        caixa_texto.delete(0, tk.END)

    caixa_texto.bind("<Return>", enviar_comando)

    adicionar_historia("Você desperta em uma floresta desconhecida.")
    adicionar_historia("Uma trilha estreita segue em direção ao norte.")
    adicionar_historia("O que deseja fazer?")

def configurar_eventos_inventario(lista_inventario, janela):
    #Função para Selecionar Itens
    def abrir_nova_janela(valor):
        nova_janela = tk.Toplevel(janela)
        nova_janela.title(f"Descrição de {valor}")
        nova_janela.geometry("350x200") 

        if valor == "Espada enferrujada":
            label = tk.Label(nova_janela, text=f"Uma {valor}, marcada por anos de guerra,\njaz em uma situação deplorável.", justify="center")
            label.pack(pady=20)
    
        elif valor == "Poção de vida":
            label = tk.Label(nova_janela, text=f"Uma {valor} com efeitos desconhecidos.\nTome por conta própria.", justify="center")
            label.pack(pady=20)

        elif valor == "Chave antiga":
            label = tk.Label(nova_janela, text=f"Uma {valor} encontrada em um baú escondido.", justify="center")
            label.pack(pady=20)
    
        else:

            label = tk.Label(nova_janela, text=f"Item: {valor}\nSem descrição disponível.", justify="center")
            label.pack(pady=20)

        botao_fechar = tk.Button(nova_janela, text="Fechar", command=nova_janela.destroy)
        botao_fechar.pack(pady=10)

    def ao_selecionar(event):
        widget = event.widget
        selecao = widget.curselection()
        if selecao:
            indice = selecao[0]
            valor = widget.get(indice)
            print(f"Índice: {indice} | Item selecionado: {valor}")
        

            abrir_nova_janela(valor) 
    lista_inventario.bind('<Double-Button-1>', ao_selecionar)
import tkinter as tk
from tkinter import messagebox

def converter():
    try:
        # Obtém o número digitado e a base escolhida
        numero = entrada.get()
        base = variavel_base.get()

        # Converte o número para decimal
        if base == 'Decimal':
            valor_decimal = int(numero)
        elif base == 'Octal':
            valor_decimal = int(numero, 8)
        elif base == 'Hexadecimal':
            valor_decimal = int(numero, 16)
        elif base == 'Binário':
            valor_decimal = int(numero, 2)
        else:
            raise ValueError("Base não reconhecida")

        # Realiza as conversões e exibe os resultados
        resultado = (
            f"Decimal: {valor_decimal}\n"
            f"Octal: {oct(valor_decimal)[2:]}\n"
            f"Hexadecimal: {hex(valor_decimal)[2:].upper()}\n"
            f"Binário: {bin(valor_decimal)[2:]}"
        )

        # Exibe o resultado em uma caixa de mensagem
        messagebox.showinfo("Resultado", resultado)
    except ValueError as e:
        messagebox.showerror("Erro", str(e))
    except Exception as e:
        messagebox.showerror("Erro", "Erro desconhecido.")

# Cria a janela principal
janela = tk.Tk()
janela.title("Conversão de Números")
janela.config(bg="#f5f5f5")  # Cor de fundo suave

# Cria e posiciona os elementos da interface com melhorias
tk.Label(janela, text="Digite o número:", font=("Arial", 12, "bold"), bg="#f5f5f5", fg="#333").pack(pady=10)

entrada = tk.Entry(janela, font=("Arial", 12), bd=2, relief="solid", width=20, justify="center")
entrada.pack(pady=5)

tk.Label(janela, text="Escolha a base do número:", font=("Arial", 12, "bold"), bg="#f5f5f5", fg="#333").pack(pady=10)

variavel_base = tk.StringVar(value='Decimal')
opcao_base = tk.OptionMenu(janela, variavel_base, 'Decimal', 'Octal', 'Hexadecimal', 'Binário')
opcao_base.config(font=("Arial", 12), bd=2, relief="solid", width=18)
opcao_base.pack(pady=5)

botao_converter = tk.Button(janela, text="Converter", command=converter, font=("Arial", 12, "bold"), bg="#4CAF50", fg="white", bd=2, relief="solid", width=20)
botao_converter.pack(pady=20)

# Inicia o loop principal da interface
janela.mainloop()

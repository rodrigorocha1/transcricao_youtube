class MyClass:
    def __init__(self):
        print("Objeto criado")
        self.arquivo = open("meu_arquivo.txt", "w")


obj = MyClass()
# ... (código que utiliza o objeto)
del obj  # Chamada explícita do destructor

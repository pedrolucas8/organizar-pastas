# Organizar arquivos por extensão

**Requisitos:** tkinter

* Como instalar o pacote _tkinter_:
```
pip install tkinter
```

* Como usar:
    - Executar o arquivo princial: main.py;
        ```
        python main.py
        ```
    - Selecionar o diretório que queira organizar;
    - Digitar a extensão do arquivo, o programa criará uma pasta com o nome da extensão dentro da pasta selecionada anteriormente.

* Exemplo:
    - Antes:
        ```
        Pasta raíz -> C:\Outros

        Outros
        |__ exemplo1.txt
        |__ exemplo1.py
        |__ exemplo1.png
        |__ exemplo2.txt
        |__ exemplo2.py
        |__ exemplo2.png
        |__ exemplo3.txt
        |__ exemplo3.py
        |__ exemplo3.png
        ```

    - Depois:
        ```
        Pasta raíz -> C:\Outros

        Outros
        |__ txt
        |   |__ exemplo1.txt
        |   |__ exemplo2.txt
        |   |__ exemplo3.txt
        |
        |__ py
        |    |__ exemplo1.py
        |    |__ exemplo2.py
        |    |__ exemplo3.py
        |
        |__ png
            |__ exemplo1.png
            |__ exemplo2.png
            |__ exemplo3.png
        ```

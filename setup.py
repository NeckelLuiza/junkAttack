from cx_Freeze import setup, Executable

executables = [Executable("main.py", base=None)]

setup(
    name="Junk Attack",
    version="1.0",
    description="Jogo criado no curso de Ciência da Computação para testar conhecimentos em Python de forma lúdica.",
    executables=executables,
)

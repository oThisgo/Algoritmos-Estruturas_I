from notebook import Notebook
from desktop import Desktop

note = Notebook('Apple', 'Prata', 12000, 8)
print(note.getInformacoes())
note.cadastrar()
print(note.getInformacoes())

desk = Desktop('AMD', 'Branco', 8000, 500)
print(desk.getInformacoes())
desk.cadastrar()
print(desk.getInformacoes())

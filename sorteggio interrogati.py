import random

def estrai_ed_elimina_nome(lista_nomi):
    if not lista_nomi:
        print("La lista è vuota.")
        return None

    nome_estratto = random.choice(lista_nomi)
    lista_nomi.remove(nome_estratto)

    return nome_estratto

# Esempio di utilizzo:
lista_nomi = ["Barbanotti", "Barretta", "Gravinese", "Spada", "Brocero", "Paradiso", "Corrado", "Pezzuto", "Timpa", "Radice", "Fornelli", "Biroli", "Pastori", "Buglino", "Bogo", "Longhi", "Russo", "Peratello", "Perugini", "Pirovano", "Bertoni", "Garofalo", "De Sciscio", "Zheng"]

nome_estratto = estrai_ed_elimina_nome(lista_nomi)

if nome_estratto:
    print(f"Nome estratto: {nome_estratto}")
    print(f"Lista aggiornata: {lista_nomi}")
else:
    print("Operazione non riuscita.")

contacts = [{
  "name": "Jonas",
  "phone": 123456789,
  "mail": "jonas@jonas.com",
  "favorite": True
}]

def listContacts():
  for i, contact in enumerate(contacts, start=1):
      favorite = "★" if contact["favorite"] else "✩"
      print(f"{favorite} {i} - {contact["name"]} ")

while True:
  print("\nLista de Contatos")
  print("1. Mostrar Contatos")
  print("2. Adicioanr Contato")
  print("3. Mostrar Favoritos")
  print("4. Editar Contato")
  print("5. Excluir Contato")
  print("6. Fechar Lista")

  chose = int(input("\nSelecione uma opção para continuar:"))

  if(chose == 6):
    break
  elif(chose == 1):
    listContacts()


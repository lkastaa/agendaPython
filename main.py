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

def createContact():
  name = input("Digite o nome do contato: ")
  phone = int(input(f"Digite o telefone para o novo contato {name}: "))
  mail = input(f"Digite um email para o novo contato {name}: ")
  favorite = False

  contacts.append({
    "name":name,
    "phone": phone,
    "maill": mail,
    "favorite":favorite
  })

def toggleFavorite(index):
  correctIndex = index -1
  contacts[correctIndex]["favorite"] = not contacts[correctIndex]["favorite"]

def edditContact(index):
  correctIndex = index -1
  newName = input(f"Digite o novo nome para {contacts[correctIndex]["name"]}: ")
  newPhone = int(input(f"Digite o novo numero para {newName}: "))
  newMail = input("Digite o novo endereco de email: ")

  contacts[correctIndex] = {
    "name": newName,
    "phone": newPhone,
    "mail": newMail,
    "favorite": contacts[correctIndex]["favorite"]
  }

while True:
  print("\nLista de Contatos")
  print("1. Mostrar Contatos")
  print("2. Adicioanr Contato")
  print("3. Mostrar Favoritos")
  print("4. Editar Contato")
  print("5. Excluir Contato")
  print("6. Fechar Lista")

  chose = int(input("\nSelecione uma opção para continuar: "))

  if(chose == 6):
    break
  elif(chose == 1): #Listar Contatos
    listContacts()
  elif(chose == 2): #Adicionar Contato
    print("\nAdicionar novo contato.")
    createContact()
  elif(chose == 3): #Favoritar Contato
    toggleFavoriteIndex = int(input("\nQual contato voce deseja favoritar ou desfavoritar: "))
    listContacts()
    toggleFavorite(toggleFavoriteIndex)
    print('\nLista de Contatos Atualizada: ')
    listContacts()
  elif(chose == 4):
    toggleEdditIndex = int(input("\nQual contato voce deseja editar: "))
    listContacts()
    edditContact(toggleEdditIndex)
    listContacts()


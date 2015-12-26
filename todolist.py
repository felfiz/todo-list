todo_list = []

def show_list():
  print("Here's your list")

  for item in todo_list:
    print(item)

def show_instructions():
  print('press HELP to get some help.')
  print('press DONE finish list')
  print("Add a new item to your list...")

show_instructions()

while True:
  new_item = raw_input("> ")

  if new_item == "DONE":
    show_list()
    break
  elif new_item == "HELP":
    show_instructions()
    continue
  else:
    todo_list.append(new_item)
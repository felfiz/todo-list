todo_list = []

print("What to add?")
print("Enter DONE to stop adding items.")

while True:
  new_item = raw_input("> ")

  if new_item == "DONE":
    break
  else:
    todo_list.append(new_item)

print("Here's your list")

for item in todo_list:
  print(item)
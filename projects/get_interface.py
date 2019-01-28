string = "abc.11"

def get_interface(string):
  new_string = string.split(".")
  name = ''
  index = 0
  for s in new_string:
    if s.isdigit() == True:
      index = s
    else:
      name = s
  return name,int(index)
      
print(get_interface("abc.11"))

#Or if interface contains number also

def get_interface(string):
  new_string = string.split(".")
  name = new_string[0]
  index = new_string[1]
  return name,int(index)
      
name, index = get_interface("abc12.11")

print(name)
print(index)

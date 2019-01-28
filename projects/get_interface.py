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

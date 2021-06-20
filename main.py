from tkinter import Tk, simpledialog, messagebox
NAME = input("NAME:")
print('Hello ' + NAME + ', you can ask me about capitals for the countries around the world!')

# This function handles the file reading from a data file
def read_from_file():
  with open('Capital_City.txt') as file:
    for line in file:
      line = line.rstrip('\n')
      country, city = line.split('/')
      the_world[country] = city

root = Tk()
root.withdraw()
the_world = {}

read_from_file() 

while True:
  query_country = simpledialog.askstring('ASK ME', 'Type The Name of a Country:')
  if query_country in the_world:
    result = the_world[query_country]
    print(result)
  else:
    print('~~This country is currently not in our database. Sorry for the inconvenience~~')
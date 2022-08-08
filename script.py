import sys
from wsgiref.util import guess_scheme

guests = {}

def read_guestlist(file_name):
  text_file = open(file_name,'r')
  val = None
  while True:
    if val is not None:
        line_data = val.strip().split(",")
    else:
        line_data = text_file.readline().strip().split(",")
    # line_data = text_file.readline().strip().split(",")

    if len(line_data) < 2:
    # If no more lines, close file
      text_file.close()
      break
    name = line_data[   0]
    age = int(line_data[1])
    guests[name] = age
    # yield name
    # yield age
    val = yield name, age

guests_ = read_guestlist('guest_list.txt')

# print(sys.getsizeof(guests_), 'list')
def guest_list():
  try:
    for i in range(20):
        next(guests_)
        if i == 10:
          guests_.send("Jane, 35")
  except:
    pass
  return 
list1= guest_list()

print("")

def guests_over_21(guest_list):
  age_21 = {}
  for guest in guest_list:
    if guest_list[guest] >= 21:
      age_21[guest] = guest_list[guest]
  print(age_21, '< 21 years old')
print()

# guest_list()
guests_over_21(guests)

def table(table):
  while True:
    try:
      yield (food, table, seat)
    except:
      pass






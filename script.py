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
list1= guest_list()
print("")


over_21 = (key for key, val in guests.items() if int(val) > 21)

def chicken():
  food = 'Chicken'
  table = 1
  for i in range(5):
    seat = i + 1
    yield f'Menu: {food}'
    yield f'Table: {table}'
    yield f'Seat: {seat}'      

def beef():
  food = 'Beef'
  table = 2
  for i in range(5):
    seat = i + 1
    yield f'Menu: {food}'
    yield f'Table: {table}'
    yield f'Seat: {seat}'

def fish():
  food = 'Fish'
  table = 3
  for i in range(5):
    seat = i + 1
    yield f'Menu: {food}'
    yield f'Table: {table}'
    yield f'Seat: {seat}'

def meal_assigner(guests, gen1, gen2, gen3):
  names = list(guests.keys())
  for i in range(5):
    yield (names[i], next(gen1))
  for i in range(5):
    i += 5
    yield (names[i], next(gen2))
  for i in range(5):
    i += 10
    yield (names[i], next(gen3))

meal_plans = meal_assigner(guests, chicken(), fish(), beef())

try:
  for i in range(30):
    print(next(meal_plans))
except:
  pass
            
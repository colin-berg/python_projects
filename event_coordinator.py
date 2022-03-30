import itertools

guests = {}
def read_guestlist(file_name):
  text_file = open(file_name,'r')
  val = None
  while True:
    if val is not None:
      line_data = val.strip().split(",")
    else:
      line_data = text_file.readline().strip().split(",")

    if len(line_data) < 2:
    # If no more lines, close file
      text_file.close()
      break
    name = line_data[0]
    age = int(line_data[1])
    guests[name] = age
    val = yield name, age
    
    

guest_list = read_guestlist('guest_list.txt')


for i in range(10):
  print(next(guest_list)) 

print(guest_list.send('Jane, 35'))

for i in guest_list:
  print(i)

over_21 = (name for name, age in guests.items() if age >= 21)

for i in over_21:
  print(i)

def table_1():
  food = 'Food: Chicken'
  table = 'Table ' + str(1)
  for i in range(1,6):
    seat = 'Seat ' + str(i) 
    yield food, table, seat

def table_2():
  food = 'Food: Beef'
  table = 'Table ' + str(2)
  for i in range(1,6):
    seat = 'Seat ' + str(i)
    yield food, table, seat

def table_3():
  food = 'Food: Fish'
  table = "Table: " + str(3)
  for i in range(1,6):
    seat = 'Seat ' + str(i)
    yield food, table, seat

chicken_table = table_1()

for i in range(5):
  print(next(chicken_table))

def all_tables():
  yield from table_1()
  yield from table_2()
  yield from table_3()

tables = all_tables()

assign = ((guest, table) for guest, table in zip(guests, tables))

for i in range(15):
  print(next(assign))

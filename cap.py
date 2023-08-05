from replit import db

def cap(amount):
  keys = db.keys()
  max = 0

  for i in keys:
    max += int(db[i])

  if max < (6000000 - int(amount)):
    print(max)
    return True
  else:
    return False

def balance():
  keys = db.keys()
  max = 0

  for i in keys:
    max += int(db[i])

  return max
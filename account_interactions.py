from replit import db

def findaccount(id1:str):
  if id1 in db.prefix(id1):
    return True
  else:
    return False

def add(id1:str, amount):
  if findaccount(id1):
    dollars = db[id1]
    db[id1] = int(dollars) + int(amount)
  else:
    db[id1] = amount
  total = db[id1]
  return total

def set(id1:str, amount):
  db[id1] = int(amount)
  total = db[id1]
  return total

def bal(id1):
  if findaccount(id1):
    coins = db[id1]
    return str(coins)
  else:
    return "0"

def gift(id1, amount, id2):
  if findaccount(id1):
    amount_ = db[id1]
    if int(amount_) < int(amount) or "-" in amount:
      return "N/AC"
    else:
      db[id1] = int(amount_) - int(amount)
      if findaccount(id2):
        amount_ = db[id2]
        db[id2] = int(amount) + int(amount_)
      else:
        db[id2] = int(amount)
      return "AC"
  else:
    return "N/AC"
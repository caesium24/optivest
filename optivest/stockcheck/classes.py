class Stock:
  def __init__(self, ticker, c_price,):
    self.ticker = ticker
    self.c_price = c_price

class Session:
  def __init__(self, name, email, password, pin, mfa):
    self.name = name
    self.email = email
    self.password = password
    self.pin = pin
    self.mfa = mfa

import random
class item:
   def __init__(self, name, power):
      self.name = name
      self.power = power

   def __eq__(self, other):
      return type(other) == item and other.name == self.name and other.power == self.power

   def __repr__(self):
      return "Item(%r, %r)"%(self.name, self.power)

class Player:
   def __init__(self, name, item):
      self.name = name
      self.item = item

   def __eq__(self, other):
      return type(other) == Player and other.name == self.item

   def __repr__(self):
      return "Item(%r, %r)"%(self.name, item)

def compare(Players):
    OutPlayers = []
    InPlayers = []
    for p in Players:
        out = p.item.power
        for x in range(len(Players)):
            if Players[x].item.name == out:
                if Players[x].name not in OutPlayers:
                    OutPlayers.append(Players[x].name)
        for x in Players:
            if x.name not in OutPlayers and x.name not in InPlayers:
                InPlayers.append(x.name)
    return InPlayers


def play():
    Players = []
    InPlayers = []
    More = raw_input("Add Player? (Y/N)")
    num = 1
    while (More == "Y"):
        Name = raw_input("Player %r name:" %(num))
        Players.append(Name)
        num +=1
        More = raw_input("Add Player? (Y/N)")
    InPlayers = Players
    while len(InPlayers) != 1 :
        InPlayers= reset(Players)
        InPlayers = compare(InPlayers)
        while len(InPlayers) == 0:
            InPlayers = reset(Players)
            InPlayers = compare(InPlayers)
        Players = InPlayers

    print ("The Winner is %r" %InPlayers[0])
    return

def reset(Players):
    InPlayers = []
    for x in Players:
        Item_val = random.randint(1,3)
        if Item_val == 1:
            player = Player(x, item("rock", "scissors"))
        elif Item_val == 2:
            player = Player(x, item("paper", "rock"))
        else: player = Player(x, item("scissors", "paper"))
        InPlayers.append(player)
    return InPlayers


if __name__ == "__main__":
    play()
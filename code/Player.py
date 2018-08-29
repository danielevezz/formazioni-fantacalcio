class Player:
    def __init__(self, name, team, position, cost):
        self.name = name
        self.team = team
        self.position = position
        self.cost = cost

    def __str__(self):
        return f"{self.name} - {self.team}: {self.position} - {self.cost}"
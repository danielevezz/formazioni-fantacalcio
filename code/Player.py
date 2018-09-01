class Player:
    isPlaying = False
    percentage = 0
    def __init__(self, name, team, position, cost):
        self.name = name
        self.team = team
        self.position = position
        self.cost = cost


    def __str__(self):
        return f"{self.name} - {self.team}: {self.position} - {self.cost} \ gioca: {self.isPlaying} col {self.percentage}%"


    def to_dict(self):
        return {
            "name": self.name,
            "team": self.team,
            "position": self.position,
            "cost": self.cost,
            "isPlaying": self.isPlaying,
            "percentage": self.percentage,
        }

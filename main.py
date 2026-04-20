# 14-m
class GamePlayer:
    def __init__(self, name, score):
        self.name = name
        self.score = score

    def result(self):
        if self.score >= 50:
            print("You win!")
        else:
            print("You lose!")

g1 = GamePlayer("Bunyod", 100)

g1.result()

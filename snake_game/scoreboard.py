from turtle import Turtle

class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.score=0
        self.color('white')
        self.penup()
        self.goto(0,270)
        self.write(f'Score:{self.score}',False,'center',('Arial',20,'normal'))
        self.hideturtle()
        
    
    def update_score(self):
        self.score +=1
        self.clear()
        self.write(f'Score:{self.score}',False,'center',('Arial',20,'normal'))
    
    def game_over(self):
        self.goto(0,0)
        self.write('GAME OVER',False,'center',('Arial',20,'normal'))
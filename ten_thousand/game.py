try:
    from ten_thousand.game_logic import GameLogic
except:
    from game_logic import GameLogic
    
def play():
    GameLogic().play_dice()
    
class Game(GameLogic):
    def play(self):
         GameLogic().play_dice()
   

if __name__ == "__main__":
    play()
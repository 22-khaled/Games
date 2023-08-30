class Player:
    def __init__(self, name, symbol, initial_score=0):
        self.name= name
        self.symbol= symbol
        self.score= initial_score

    def won_match(self):
        self.score+= 100

    def lost_match(self):
        self.score-= 50

    def show_score(self):
        print(f'Player {self.name}: {self.score} points')

class PlayingField:
    def __init__(self):
        self.field= [
                     [None, None, None],
                     [None, None, None],
                     [None, None, None]
                    ]

    def set_player(self, x, y, player):
        if self.field[y][x] is not None:
            return False

        self.field[y][x]= player

        return True
    
    def show_field(self):
        for row in self.field:
            for player in row:
                if player is None:
                    print('_' , end = ' ' )
                else :
                   print( player.symbol ,end=' ')
            print()


    def check_won(self, x, y, player):
        if self.field[0][x] == player and self.field[1][x] == player and self.field[2][x] == player:
            return True
        elif self.field[y][0] == player and self.field[y][1] == player and self.field[y][2] == player:
            return True
        elif self.field[0][0] == player and  self.field[1][1] == player and self.field[2][2] == player:
            return True
        elif self.field[0][2] == player and  self.field[1][1] == player and  self.field[2][0] == player:
            return True
        else:
            return False
        
def main() :
    name_1  =input('namme of player1')  
    name_2  =input('namme of player2') 
    players =[Player( name_1,'X') , Player( name_2,'O') ]

    field = PlayingField () 
    while(True):
        for player in players :
            field.show_field()
            x = int(input(f'player {player.name} choose yor column : ')) - 1
            y= int(input(f'player {player.name} choose yor row : ')) - 1
            
            if not field.set_player(x,y,player) :
                print(' data fieled already full ')
            elif  field.check_won(x, y, player)  :
                field.show_field()
                print(f'{player.name} won the game')
                print('Score')
                for player in players :
                    if field.check_won( x , y, player) == True :
                        player.won_match()
                    else : 
                        player.lost_match()  
                    player.show_score() 
                field = PlayingField () 
main()
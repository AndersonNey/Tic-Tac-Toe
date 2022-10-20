
# -*- coding: utf-8 -*-
#----------------------------------------------------------------------------
# Created By : Anderson Ney       
# Github : https://github.com/AndersonNey  
# Created Date: 10/10/2022 
# version ='1.0'
#----------------------------------------------------------------------------


from os import system

class Move:
    def __init__(self,name_player1='player1',name_player2 ='player2',player_piece1 = 'X',player_piece2 = 'O'):

        self.players = {'player1':{'name':name_player1,'option':player_piece1},
                          'player2':{'name':name_player2,'option':player_piece2}}

        self.places_played = {'7':' ','8': ' ','9': ' ',
                               '4': ' ','5': ' ','6': ' ',
                               '1': ' ','2': ' ','3': ' '} 

        self.scoreboard = {'player1':0,'player2':0,'deadlock':0}
        
        self.answers =  [
        ['7','4','1'],
        ['8','5','2'],
        ['9','6','3'],
        ['7','8','9'],
        ['4','5','6'], 
        ['1','2','3'],
        ['7','5','3'],
        ['9','5','1']
    ]

    # CLEANING GAME BOARD
    def prepare_next_match(self):
        for x in  self.places_played.keys():
            self.places_played[x]= ' '


    def move(self,player_of_the_time,opposing_player):
        # SHOWING GAME BOARD
        def tela():
            system('clear')
            print('====== Tic Tac Toe ======        Player of the time {0}  ---> {1}'.format(self.players[player_of_the_time]['name'],self.players[player_of_the_time]['option']))       
            print('     {0}  |   {1}  |   {2}'.format(self.places_played['7'],self.places_played['8'],self.places_played['9']))
            print('   ---- + ---- + ----              Current Score: {0} victories for  -> {1}'.format(self.scoreboard['player1'],self.players['player1']['name']))
            print('     {0}  |   {1}  |   {2}                              {3} victories for  -> {4}'.format(self.places_played['4'],self.places_played['5'],self.places_played['6'],self.scoreboard['player2'],self.players['player2']['name']))
            print('   ---- + ---- + ----                             {0} deadlock'.format(self.scoreboard['deadlock']))
            print('     {0}  |   {1}  |   {2}'.format(self.places_played['1'],self.places_played['2'],self.places_played['3']))
            print()
            print('===Choose by number======')
            print(f'     7  |   8  |  9                Select the corresponding number to insert in the table above.')
            print(f'   ---- + ---- + ----              To [exit] type :  0')
            print(f'     4  |   5  |  6 ')
            print(f'   ---- + ---- + ----')
            print(f'     1  |   2  |  3 ')
        
        tela()

        #RECEIVING A QUESTION FROM THE PLAYER OF THE TIME
        while True:   
            try:
                resp = input('Choose a place:')
                if resp == '0':
                    return 0
                if resp not in self.places_played:
                    raise Exception                                         #if there is already an option in place, returns an error
                if self.places_played[resp] == self.players[player_of_the_time]['option'] or self.places_played[resp] == self.players[opposing_player]['option']:
                    raise Exception
                self.places_played[resp] = self.players[player_of_the_time]['option']
                break
            except Exception:
                print('Invalid option, try again')

        for x in self.answers:
        #CHECK IF PLAYER OF THE TIME WON                                
            if self.places_played[x[0]] == self.players[player_of_the_time]['option'] and self.places_played[x[1]] == self.players[player_of_the_time]['option'] and self.places_played[x[2]]== self.players[player_of_the_time]['option']:
                self.scoreboard[player_of_the_time] = self.scoreboard[player_of_the_time] + 1
                tela()
                print('{0} ({1})  Won!!!!'.format(self.players[player_of_the_time]['name'],self.players[player_of_the_time]['option']))
                return 1
        #CHECKING IF A TIE OCCURRED
        cont = 0
        for x in self.places_played.values():
            try:
                if x == self.players[player_of_the_time]['option'] or x==self.players[opposing_player]['option']: 
                    cont+=1               
                if cont == 9:
                    raise Exception
            except:
                self.scoreboard['deadlock'] = self.scoreboard['deadlock'] + 1
                tela()
                print('Players drew')
                return 2       



class GameMode(Move):
    def continuous_game(self):
        while True:
            r = self.single_game()
            if r == 0:
                break
            self.prepare_next_match()


    def single_game(self):
        while True:
            r = self.move('player1','player2')
            if r == 0:
                return 0
            if r is not None:
                break

            r = self.move('player2','player1')
            if r == 0:
                return 0
            if r is not None:
                break


start = GameMode()
start.continuous_game()




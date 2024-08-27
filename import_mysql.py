import mysql.connector

baglanti = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    password = '123456',
    database = 'score_table'
)
my_cursor = baglanti.cursor()

def add_data(_player1,_score1,_score2,player2,_time,_map):
 player1 = _player1
 score1 = _score1
 score2 = _score2
 player2 = player2
 time = _time
 map = _map
 my_cursor.execute("INSERT INTO players_data (Player1, Score1, Score2,Player2,Time,Map) VALUES ('{}', {}, {},'{}',{},'{}')".format(player1, score1, score2,player2,time,map))
 baglanti.commit()


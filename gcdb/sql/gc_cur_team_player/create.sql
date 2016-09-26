CREATE TABLE gc_cur_team_player (
    _id INTEGER PRIMARY KEY
  , player_id TEXT
  , esbid TEXT
  , fn TEXT
  , ln TEXT
  , hometown TEXT
  , bdate TEXT
  , age INTEGER
  , exp TEXT
  , pos TEXT
  , ht TEXT
  , wt INTEGER
  , college TEXT
  , team TEXT
  , uniformnumber INTEGER
  , _gc_cur_team_id INTEGER
  , FOREIGN KEY (_gc_cur_team_id) REFERENCES gc_cur_team (_id)
)
;

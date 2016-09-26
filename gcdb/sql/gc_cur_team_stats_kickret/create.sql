CREATE TABLE gc_cur_team_stats_kickret (
    _id INTEGER PRIMARY KEY
  , player_id TEXT
  , name TEXT
  , ret INTEGER
  , "avg" INTEGER
  , lng INTEGER
  , tds INTEGER
  , _gc_cur_team_id INTEGER
  , FOREIGN KEY (_gc_cur_team_id) REFERENCES gc_cur_team (_id)
)
;

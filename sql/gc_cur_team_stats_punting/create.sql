CREATE TABLE gc_cur_team_stats_punting (
    _id INTEGER PRIMARY KEY
  , player_id TEXT
  , name TEXT
  , pts INTEGER
  , yds INTEGER
  , "avg" INTEGER
  , lng INTEGER
  , i20 INTEGER
  , _gc_cur_team_id INTEGER
  , FOREIGN KEY (_gc_cur_team_id) REFERENCES gc_cur_team (_id)
)
;

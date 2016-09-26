CREATE TABLE gc_cur_team_stats_defense (
    _id INTEGER PRIMARY KEY
  , player_id TEXT
  , name TEXT
  , tkl INTEGER
  , ast INTEGER
  , sk INTEGER
  , ffum INTEGER
  , "int" INTEGER
  , _gc_cur_team_id INTEGER
  , FOREIGN KEY (_gc_cur_team_id) REFERENCES gc_cur_team (_id)
)
;

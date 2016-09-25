CREATE TABLE gc_cur_team_stats_fumbles (
    _id INTEGER PRIMARY KEY
  , player_id TEXT
  , name TEXT
  , tot INTEGER
  , yds INTEGER
  , lost INTEGER
  , rcv INTEGER
  , trcv INTEGER
  , _gc_cur_team_id INTEGER
  , FOREIGN KEY (_gc_cur_team_id) REFERENCES gc_cur_team (_id)
)
;

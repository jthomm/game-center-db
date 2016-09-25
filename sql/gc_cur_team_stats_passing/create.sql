CREATE TABLE gc_cur_team_stats_passing (
    _id INTEGER PRIMARY KEY
  , player_id TEXT
  , name TEXT
  , att INTEGER
  , cmp INTEGER
  , yds INTEGER
  , tds INTEGER
  , ints INTEGER
  , twopta INTEGER
  , twoptm INTEGER
  , _gc_cur_team_id INTEGER
  , FOREIGN KEY (_gc_cur_team_id) REFERENCES gc_cur_team (_id)
)
;

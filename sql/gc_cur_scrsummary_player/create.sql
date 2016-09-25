CREATE TABLE gc_cur_scrsummary_player (
    _id INTEGER PRIMARY KEY
  , player_id TEXT
  , player_name TEXT
  , _gc_cur_scrsummary_id INTEGER
  , FOREIGN KEY (_gc_cur_scrsummary_id) REFERENCES gc_cur_scrsummary (_id)
)
;

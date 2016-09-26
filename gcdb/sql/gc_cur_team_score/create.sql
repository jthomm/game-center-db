CREATE TABLE gc_cur_team_score (
    _id INTEGER PRIMARY KEY
  , qtr TEXT
  , points INTEGER
  , _gc_cur_team_id INTEGER
  , FOREIGN KEY (_gc_cur_team_id) REFERENCES gc_cur_team (_id)
)
;

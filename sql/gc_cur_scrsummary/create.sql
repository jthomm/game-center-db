CREATE TABLE gc_cur_scrsummary (
    _id INTEGER PRIMARY KEY
  , play_id TEXT
  , qtr TEXT
  , team TEXT
  , "type" TEXT
  , "desc" TEXT
  , _gc_cur_id INTEGER
  , FOREIGN KEY (_gc_cur_id) REFERENCES gc_cur (_id)
)
;

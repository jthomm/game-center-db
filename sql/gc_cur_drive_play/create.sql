CREATE TABLE gc_cur_drive_play (
    _id INTEGER PRIMARY KEY
  , play_id TEXT
  , "desc" TEXT
  , posteam TEXT
  , qtr TEXT
  , time TEXT
  , down INTEGER
  , ydstogo INTEGER
  , yrdln TEXT
  , ydsnet INTEGER
  , note TEXT
  , sp INTEGER
  , _gc_cur_drive_id INTEGER
  , FOREIGN KEY (_gc_cur_drive_id) REFERENCES gc_cur_drive (_id)
)
;

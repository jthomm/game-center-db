CREATE TABLE gc_cur (
    _id INTEGER PRIMARY KEY
  , redzone INTEGER
  , rooftype TEXT
  , qtr TEXT
  , yl TEXT
  , clock TEXT
  , down INTEGER
  , togo INTEGER
  , posteam TEXT
  , stadium TEXT
  , _gc_id INTEGER
  , FOREIGN KEY (_gc_id) REFERENCES gc (_id)
)
;

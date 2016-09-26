CREATE TABLE gc_team (
    _id INTEGER PRIMARY KEY
  , ah TEXT
  , standing TEXT
  , abbr TEXT
  , _gc_id INTEGER
  , FOREIGN KEY (_gc_id) REFERENCES gc (_id)
)
;

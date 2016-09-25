CREATE TABLE gc_cur_team (
    _id INTEGER PRIMARY KEY
  , ah TEXT
  , teamcode TEXT
  , abbr TEXT
  , fullname TEXT
  , comurl TEXT
  , cluburl TEXT
  , smscode TEXT
  , color TEXT
  , teamcolor TEXT
  , phone TEXT
  , standing TEXT
  , "to" INTEGER
  , _gc_cur_id INTEGER
  , FOREIGN KEY (_gc_cur_id) REFERENCES gc_cur (_id)
)
;

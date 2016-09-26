CREATE TABLE gc_game (
    _id INTEGER PRIMARY KEY
  , game_id TEXT
  , game_key TEXT
  , uri TEXT
  , gamebook TEXT
  , seasontype TEXT
  , week INTEGER
  , cp INTEGER
  , year INTEGER
  , "date" TEXT
  , "time" TEXT
  , day TEXT
  , state TEXT
  , _gc_id INTEGER
  , FOREIGN KEY (_gc_id) REFERENCES gc (_id)
);

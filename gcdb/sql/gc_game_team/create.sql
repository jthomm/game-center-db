CREATE TABLE gc_game_team (
    _id INTEGER PRIMARY KEY
  , abbr TEXT
  , fullname TEXT
  , link TEXT
  , standing TEXT
  , _gc_game_id INTEGER
  , FOREIGN KEY (_gc_game_id) REFERENCES gc_game (_id)
)
;

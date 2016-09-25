CREATE TABLE gc_cur_drive_play_event (
    _id INTEGER PRIMARY KEY
  , player_id TEXT
  , playername TEXT
  , clubcode TEXT
  , yards INTEGER
  , statid INTEGER
  , sequence INTEGER
  , _gc_cur_drive_play_id INTEGER
  , FOREIGN KEY (_gc_cur_drive_play_id) REFERENCES gc_cur_drive_play (_id)
)
;

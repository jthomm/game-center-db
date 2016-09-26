CREATE TABLE gc_cur_drive (
    _id INTEGER PRIMARY KEY
  , drive_num INTEGER
  , redzone INTEGER
  , postime TEXT
  , fds INTEGER
  , result TEXT
  , numplays INTEGER
  , qtr TEXT
  , penyds INTEGER
  , posteam TEXT
  , ydsgained INTEGER
  , start_yrdln TEXT
  , start_team TEXT
  , start_qtr TEXT
  , start_time TEXT
  , end_yrdln TEXT
  , end_team TEXT
  , end_qtr TEXT
  , end_time TEXT
  , _gc_cur_id INTEGER
  , FOREIGN KEY (_gc_cur_id) REFERENCES gc_cur (_id)
)
;

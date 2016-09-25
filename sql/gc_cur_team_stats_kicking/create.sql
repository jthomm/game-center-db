CREATE TABLE gc_cur_team_stats_kicking (
    _id INTEGER PRIMARY KEY
  , player_id TEXT
  , name TEXT
  , totpfg INTEGER
  , fga INTEGER
  , fgm INTEGER
  , fgyds INTEGER
  , xptot INTEGER
  , xpa INTEGER
  , xpmade INTEGER
  , xpmissed INTEGER
  , xpb INTEGER
  , _gc_cur_team_id INTEGER
  , FOREIGN KEY (_gc_cur_team_id) REFERENCES gc_cur_team (_id)
)
;

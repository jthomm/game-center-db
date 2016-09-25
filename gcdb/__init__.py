__version__ = '0.0.1'



"""Reading and executing SQL"""

from os import path

class Table(object):

    """Given a table name and a `sqlite3.Cursor`, execute `CREATE TABLE` and
    `INSERT INTO`.
    """

    SQL_PATH = path.abspath(
        path.join(path.dirname(path.dirname(__file__)), 'sql'))

    def __init__(self, name):
        self.name = name

    def _sql(self, operation):
        """A helper that finds and reads the SQL script for the given operation
        """
        if operation not in ('create', 'insert',):
            raise Exception("Invalid operation: '{0}'".format(operation))
        file_path = path.join(self.SQL_PATH, self.name, operation + '.sql')
        with open(file_path, 'rb') as file_handle: return file_handle.read()

    @property
    def create_sql(self):
        return self._sql('create')

    @property
    def insert_sql(self):
        return self._sql('insert')

    def insert(self, cursor, values):
        cursor.execute(self.insert_sql, values)
        return cursor.lastrowid

    def create(self, cursor):
        cursor.execute(self.create_sql)



"""Traversing the NFL Game Center JSON object"""

import abc

class InserterABC(object):

    __metaclass__ = abc.ABCMeta

    # This has to be an instance of `Table`
    table = None

    def __init__(self, cursor, _parent_id):
        self.cursor = cursor
        # `parent_id` is the foreign key to the "parent" table
        self._parent_id = _parent_id

    @abc.abstractmethod
    def __call__(self, *args):
        pass

class GcCurDrivePlayEvent(InserterABC):

    table = Table('gc_cur_drive_play_event')

    def __call__(self, player_id, dct):
        self.table.insert(self.cursor, (
            player_id,
            dct['playerName'],
            dct['clubcode'],
            dct['yards'],
            dct['statId'],
            dct['sequence'],
            self._parent_id,))

class GcCurDrivePlay(InserterABC):

    table = Table('gc_cur_drive_play')

    def __call__(self, play_id, dct):
        _id = self.table.insert(self.cursor, (
            play_id,
            dct['desc'],
            dct['posteam'],
            dct['qtr'],
            dct['time'],
            dct['down'],
            dct['ydstogo'],
            dct['yrdln'],
            dct['ydsnet'],
            dct['note'],
            dct['sp'],
            self._parent_id,))
        # Insert play events
        gc_cur_drive_play_event = GcCurDrivePlayEvent(self.cursor, _id)
        for player_id, event_dcts in dct['players'].iteritems():
            for event_dct in event_dcts:
                gc_cur_drive_play_event(player_id, event_dct)

class GcCurDrive(InserterABC):

    table = Table('gc_cur_drive')

    def __call__(self, drive_num, dct):
        _id = self.table.insert(self.cursor, (
            drive_num,
            None if 'redzone' not in dct else int(dct['redzone']),
            dct['postime'],
            dct['fds'],
            dct['result'],
            dct['numplays'],
            dct.get('qtr'),
            dct['penyds'],
            dct['posteam'],
            dct['ydsgained'],
            dct['start']['yrdln'],
            dct['start']['team'],
            dct['start']['qtr'],
            dct['start']['time'],
            dct['end']['yrdln'],
            dct['end']['team'],
            dct['end']['qtr'],
            dct['end']['time'],
            self._parent_id,))
        # Insert plays
        gc_cur_drive_play = GcCurDrivePlay(self.cursor, _id)
        for play_id, play_dct in dct['plays'].iteritems():
            gc_cur_drive_play(play_id, play_dct)

class GcCurTeamScore(InserterABC):

    table = Table('gc_cur_team_score')

    def __call__(self, qtr, points):
        self.table.insert(self.cursor, (
            qtr,
            points,
            self._parent_id,))

class GcCurTeamStatsTeam(InserterABC):

    table = Table('gc_cur_team_stats_team')

    def __call__(self, dct):
        self.table.insert(self.cursor, (
            dct['totfd'],
            dct['trnovr'],
            dct['pyds'],
            dct['ryds'],
            dct['totyds'],
            dct['pt'],
            dct['ptyds'],
            dct['ptavg'],
            dct['pen'],
            dct['penyds'],
            dct['top'],
            self._parent_id,))

class GcCurTeamStatsKickret(InserterABC):

    table = Table('gc_cur_team_stats_kickret')

    def __call__(self, player_id, dct):
        self.table.insert(self.cursor, (
            player_id,
            dct['name'],
            dct['ret'],
            dct['avg'],
            dct['lng'],
            dct['tds'],
            self._parent_id,))

class GcCurTeamStatsPuntret(InserterABC):

    table = Table('gc_cur_team_stats_puntret')

    def __call__(self, player_id, dct):
        self.table.insert(self.cursor, (
            player_id,
            dct['name'],
            dct['ret'],
            dct['avg'],
            dct['lng'],
            dct['tds'],
            self._parent_id,))

class GcCurTeamStatsDefense(InserterABC):

    table = Table('gc_cur_team_stats_defense')

    def __call__(self, player_id, dct):
        self.table.insert(self.cursor, (
            player_id,
            dct['name'],
            dct['tkl'],
            dct['ast'],
            dct['sk'],
            dct['ffum'],
            dct['int'],
            self._parent_id,))

class GcCurTeamStatsFumbles(InserterABC):

    table = Table('gc_cur_team_stats_fumbles')

    def __call__(self, player_id, dct):
        self.table.insert(self.cursor, (
            player_id,
            dct['name'],
            dct['tot'],
            dct['yds'],
            dct['lost'],
            dct['rcv'],
            dct['trcv'],
            self._parent_id,))

class GcCurTeamStatsKicking(InserterABC):

    table = Table('gc_cur_team_stats_kicking')

    def __call__(self, player_id, dct):
        self.table.insert(self.cursor, (
            player_id,
            dct['name'],
            dct['totpfg'],
            dct['fga'],
            dct['fgm'],
            dct['fgyds'],
            dct['xptot'],
            dct['xpa'],
            dct['xpmade'],
            dct['xpmissed'],
            dct['xpb'],
            self._parent_id,))

class GcCurTeamStatsPunting(InserterABC):

    table = Table('gc_cur_team_stats_punting')

    def __call__(self, player_id, dct):
        self.table.insert(self.cursor, (
            player_id,
            dct['name'],
            dct['pts'],
            dct['yds'],
            dct['avg'],
            dct['lng'],
            dct['i20'],
            self._parent_id,))

class GcCurTeamStatsPassing(InserterABC):

    table = Table('gc_cur_team_stats_passing')

    def __call__(self, player_id, dct):
        self.table.insert(self.cursor, (
            player_id,
            dct['name'],
            dct['att'],
            dct['cmp'],
            dct['yds'],
            dct['tds'],
            dct['ints'],
            dct['twopta'],
            dct['twoptm'],
            self._parent_id,))

class GcCurTeamStatsReceiving(InserterABC):

    table = Table('gc_cur_team_stats_receiving')

    def __call__(self, player_id, dct):
        self.table.insert(self.cursor, (
            player_id,
            dct.get('name'),
            dct.get('rec'),
            dct.get('yds'),
            dct.get('tds'),
            dct.get('lng'),
            dct.get('lngtd'),
            dct.get('twopta'),
            dct.get('twoptm'),
            self._parent_id,))

class GcCurTeamStatsRushing(InserterABC):

    table = Table('gc_cur_team_stats_rushing')

    def __call__(self, player_id, dct):
        self.table.insert(self.cursor, (
            player_id,
            dct.get('name'),
            dct.get('att'),
            dct.get('yds'),
            dct.get('tds'),
            dct.get('lng'),
            dct.get('lngtd'),
            dct.get('twopta'),
            dct.get('twoptm'),
            self._parent_id,))

class GcCurTeamPlayer(InserterABC):

    table = Table('gc_cur_team_player')

    def __call__(self, player_id, dct):
        self.table.insert(self.cursor, (
            player_id,
            dct['esbid'],
            dct['fn'],
            dct['ln'],
            dct['hometown'],
            dct['bdate'],
            dct['age'],
            dct['exp'],
            dct['pos'],
            dct['ht'],
            dct['wt'],
            dct['college'],
            dct['team'],
            dct['uniformNumber'],
            self._parent_id,))

class GcCurTeam(InserterABC):

    table = Table('gc_cur_team')

    def __call__(self, ah, dct):
        _id = self.table.insert(self.cursor, (
            ah,
            dct['teamCode'],
            dct['abbr'],
            dct['fullName'],
            dct['comUrl'],
            dct['clubUrl'],
            dct['smsCode'],
            dct['color'],
            dct['teamColor'],
            dct['phone'],
            dct['standing'],
            dct['to'],
            self._parent_id,))
        # Insert score
        gc_cur_team_score = GcCurTeamScore(self.cursor, _id)
        for qtr, points in dct['score'].iteritems():
            gc_cur_team_score(qtr, points)
        # Insert player
        gc_cur_team_player = GcCurTeamPlayer(self.cursor, _id)
        for player_id, player_dct in dct['players'].iteritems():
            gc_cur_team_player(player_id, player_dct)
        # Insert stats team
        gc_cur_team_stats_team = GcCurTeamStatsTeam(self.cursor, _id)
        gc_cur_team_stats_team(dct['stats']['team'])
        # Insert stats kickret
        if 'kickret' in dct['stats']:
            gc_cur_team_stats_kickret = GcCurTeamStatsKickret(self.cursor, _id)
            for player_id, kickret_dct in dct['stats']['kickret'].iteritems():
                gc_cur_team_stats_kickret(player_id, kickret_dct)
        # Insert stats puntret
        if 'puntret' in dct['stats']:
            gc_cur_team_stats_puntret = GcCurTeamStatsPuntret(self.cursor, _id)
            for player_id, puntret_dct in dct['stats']['puntret'].iteritems():
                gc_cur_team_stats_puntret(player_id, puntret_dct)
        # Insert stats defense
        if 'defense' in dct['stats']:
            gc_cur_team_stats_defense = GcCurTeamStatsDefense(self.cursor, _id)
            for player_id, defense_dct in dct['stats']['defense'].iteritems():
                gc_cur_team_stats_defense(player_id, defense_dct)
        # Insert stats fumbles
        if 'fumbles' in dct['stats']:
            gc_cur_team_stats_fumbles = GcCurTeamStatsFumbles(self.cursor, _id)
            for player_id, fumbles_dct in dct['stats']['fumbles'].iteritems():
                gc_cur_team_stats_fumbles(player_id, fumbles_dct)
        # Insert stats kicking
        if 'kicking' in dct['stats']:
            gc_cur_team_stats_kicking = GcCurTeamStatsKicking(self.cursor, _id)
            for player_id, kicking_dct in dct['stats']['kicking'].iteritems():
                gc_cur_team_stats_kicking(player_id, kicking_dct)
        # Insert stats punting
        if 'punting' in dct['stats']:
            gc_cur_team_stats_punting = GcCurTeamStatsPunting(self.cursor, _id)
            for player_id, punting_dct in dct['stats']['punting'].iteritems():
                gc_cur_team_stats_punting(player_id, punting_dct)
        # Insert stats passing
        if 'passing' in dct['stats']:
            gc_cur_team_stats_passing = GcCurTeamStatsPassing(self.cursor, _id)
            for player_id, passing_dct in dct['stats']['passing'].iteritems():
                gc_cur_team_stats_passing(player_id, passing_dct)
        # Insert stats receiving
        if 'receiving' in dct['stats']:
            gc_cur_team_stats_receiving = GcCurTeamStatsReceiving(self.cursor, _id)
            for player_id, receiving_dct in dct['stats']['receiving'].iteritems():
                gc_cur_team_stats_receiving(player_id, receiving_dct)
        # Insert stats rushing
        if 'rushing' in dct['stats']:
            gc_cur_team_stats_rushing = GcCurTeamStatsRushing(self.cursor, _id)
            for player_id, rushing_dct in dct['stats']['rushing'].iteritems():
                gc_cur_team_stats_rushing(player_id, rushing_dct)

class GcCurScrsummaryPlayer(InserterABC):

    table = Table('gc_cur_scrsummary_player')

    def __call__(self, player_name, player_id):
        self.table.insert(self.cursor, (
            player_id,
            player_name,
            self._parent_id,))

class GcCurScrsummary(InserterABC):

    table = Table('gc_cur_scrsummary')

    def __call__(self, play_id, dct):
        _id = self.table.insert(self.cursor, (
            play_id,
            dct['qtr'],
            dct['team'],
            dct['type'],
            dct['desc'],
            self._parent_id,))
        # Insert players
        gc_cur_scrsummary_player = GcCurScrsummaryPlayer(self.cursor, _id)
        for player_name, player_id in dct['players'].iteritems():
            gc_cur_scrsummary_player(player_name, player_id)

class GcCur(InserterABC):

    table = Table('gc_cur')

    def __call__(self, dct):
        _id = self.table.insert(self.cursor, (
            int(dct['redzone']),
            dct['rooftype'],
            dct['qtr'],
            dct['yl'],
            dct['clock'],
            dct['down'],
            dct['togo'],
            dct['posteam'],
            dct['stadium'],
            self._parent_id,))
        # Insert drives
        gc_cur_drive = GcCurDrive(self.cursor, _id)
        for drive_num, drive_dct in dct['drives'].iteritems():
            # Most keys in `dct['drives']` will be a drive number and their 
            # values will be a drive dictionary.  One exception:  the key 
            # 'crntdrv', which has an integer value.  Skip this key.
            if drive_num != 'crntdrv':
                gc_cur_drive(drive_num, drive_dct)
        # Insert teams
        gc_cur_team = GcCurTeam(self.cursor, _id)
        for ah in ('away', 'home',):
            gc_cur_team(ah, dct[ah])
        # Insert score summary
        gc_cur_scrsummary = GcCurScrsummary(self.cursor, _id)
        for play_id, scrsummary_dct in dct['scrsummary'].iteritems():
            gc_cur_scrsummary(play_id, scrsummary_dct)

class GcGameTeam(InserterABC):

    table = Table('gc_game_team')

    def __call__(self, abbr, dct):
        self.table.insert(self.cursor, (
            abbr,
            dct['fullname'],
            dct['link'],
            dct['standing'],
            self._parent_id,))

class GcGame(InserterABC):

    table = Table('gc_game')

    def __call__(self, dct):
        _id = self.table.insert(self.cursor, (
            dct['id'],
            dct['key'],
            dct['uri'],
            dct['gamebook'],
            dct['seasontype'],
            dct['week'],
            dct['cp'],
            dct['year'],
            dct['date'],
            dct['time'],
            dct['day'],
            dct['state'],
            self._parent_id,))
        # Insert teams
        gc_game_team = GcGameTeam(self.cursor, _id)
        for abbr, team_dct in dct['teams'].iteritems():
            gc_game_team(abbr, team_dct)

class GcTeam(InserterABC):

    table = Table('gc_team')

    def __call__(self, dct):
        for ah in ('away', 'home',):
            self.table.insert(self.cursor, (
                ah,
                dct[ah]['standing'],
                dct[ah]['abbr'],
                self._parent_id,))

class Gc(InserterABC):

    table = Table('gc')

    def __call__(self, dct):
        _id = self.table.insert(self.cursor, (self._parent_id,))
        GcGame(self.cursor, _id)(dct['game'])
        GcTeam(self.cursor, _id)(dct['teams'])
        GcCur(self.cursor, _id)(dct['current'][self._parent_id])



"""Command line arguments"""

import argparse

argument_parser = argparse.ArgumentParser(
    description='Inserter data for a given game')
argument_parser.add_argument(
    '-d', '--database', help='path to the SQLite database file')
argument_parser.add_argument(
    '-f', '--filename', help='path to the Game Center .json file')
argument_parser.add_argument(
    '-g', '--gameid', help="Game Center ID of the game (e.g. '2014092800')")

def parse_args():
    """Parse command line arguments but infer `gameid` based on file name if
    not explicitly provided.
    """
    args = argument_parser.parse_args()
    if args.gameid is None:
        file_base_name = path.basename(args.filename)
        file_name_without_ext, ext = path.splitext(file_base_name)
        args.gameid = file_name_without_ext
    return args



"""Reading the data from disk and deserializing"""

try:
    import simplejson as json
except ImportError:
    import json

def read_data_from_file_and_deserialize(file_path):
    json_string = ''
    with open(file_path, 'rb') as f:
        json_string = f.read()
    return json.loads(json_string)



"""Building the database"""

import sqlite3

def database_is_empty(cursor):
    results = cursor.execute('SELECT COUNT (*) FROM sqlite_master').fetchall()
    return results[0][0] == 0

def create_tables(cursor):
    for table_name in (
        'gc',
        'gc_game',
        'gc_game_team',
        'gc_team',
        'gc_cur',
        'gc_cur_scrsummary',
        'gc_cur_scrsummary_player',
        'gc_cur_team',
        'gc_cur_team_score',
        'gc_cur_team_stats_team',
        'gc_cur_team_stats_kickret',
        'gc_cur_team_stats_puntret',
        'gc_cur_team_stats_defense',
        'gc_cur_team_stats_fumbles',
        'gc_cur_team_stats_kicking',
        'gc_cur_team_stats_punting',
        'gc_cur_team_stats_passing',
        'gc_cur_team_stats_receiving',
        'gc_cur_team_stats_rushing',
        'gc_cur_team_player',
        'gc_cur_drive',
        'gc_cur_drive_play',
        'gc_cur_drive_play_event',):
        table = Table(table_name)
        table.create(cursor)

def insert_into_tables(cursor, game_id, dct):
    Gc(cursor, game_id)(dct)



"""Logging"""

import logging

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger('gcdb')



"""Main function"""

def main():
    args = parse_args()
    dct = read_data_from_file_and_deserialize(args.filename)
    with sqlite3.connect(args.database) as connection:
        cursor = connection.cursor()
        # Make sure foreign key constraints are enforced
        cursor.execute('PRAGMA foreign_keys = ON')
        # If tables aren't already there, create them
        if database_is_empty(cursor):
            logger.info(
                'No objects found in database - creating tables first...')
            create_tables(cursor)
        # Insert the data
        logger.info('Inserting {}'.format(args.gameid))
        try:
            insert_into_tables(cursor, args.gameid, dct)
        except:
            logger.error('There was an issue - aborting...')
            raise
        else:
            # If no errors, commit
            connection.commit()



if __name__ == '__main__': main()

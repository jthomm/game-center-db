from setuptools import setup
import re

name = 'gcdb'

version = ''
with open('{0}/__init__.py'.format(name), 'rb') as f:
    match_object = re.search(
        r'^__version__\s*=\s*[\'"]([^\'"]*)[\'"]',
        f.read(),
        re.MULTILINE)
    version = match_object.group(1)

setup(
    name=name,
    version=version,
    packages=[name],
    entry_points={'console_scripts': ['gcdb = gcdb:main']},
    package_data={'gcdb': [
        'sql/gc/*.sql',
        'sql/gc_cur/*.sql',
        'sql/gc_cur_drive/*.sql',
        'sql/gc_cur_drive_play/*.sql',
        'sql/gc_cur_drive_play_event/*.sql',
        'sql/gc_cur_scrsummary/*.sql',
        'sql/gc_cur_scrsummary_player/*.sql',
        'sql/gc_cur_team/*.sql',
        'sql/gc_cur_team_player/*.sql',
        'sql/gc_cur_team_score/*.sql',
        'sql/gc_cur_team_stats_defense/*.sql',
        'sql/gc_cur_team_stats_fumble/*.sql',
        'sql/gc_cur_team_stats_fumbles/*.sql',
        'sql/gc_cur_team_stats_kicking/*.sql',
        'sql/gc_cur_team_stats_kickret/*.sql',
        'sql/gc_cur_team_stats_passing/*.sql',
        'sql/gc_cur_team_stats_punting/*.sql',
        'sql/gc_cur_team_stats_puntret/*.sql',
        'sql/gc_cur_team_stats_receiving/*.sql',
        'sql/gc_cur_team_stats_rushing/*.sql',
        'sql/gc_cur_team_stats_team/*.sql',
        'sql/gc_game/*.sql',
        'sql/gc_game_team/*.sql',
        'sql/gc_team/*.sql',]
    }
)

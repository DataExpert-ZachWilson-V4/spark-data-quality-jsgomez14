from chispa.dataframe_comparer import assert_df_equality
from ..jobs.job_1 import job_1
from collections import namedtuple

NbaGameDetail = namedtuple(
    "NbaGameDetail",
    "game_id team_id player_id dim_team_abbreviation dim_player_name dim_start_position dim_din_not_dress dim_not_with_tea dim_game_date dim_season dim_team_did_win m_seconds_played m_field_goals_made m_field_goals_attempted m_3_pointers_made m_3_pinters_attempted m_free_throws_made m_free_throws_attempted m_offensive_rebounds m_defensive_rebounds m_rebounds m_assists m_steals m_blocks m_turnovers m_personal_fouls m_points m_plus_minus",
)
NbaGameDetailDedup = namedtuple(
    "NbaGameDetailDedup",
    "game_id team_id player_id dim_team_abbreviation dim_player_name dim_start_position dim_din_not_dress dim_not_with_tea dim_game_date dim_season dim_team_did_win m_seconds_played m_field_goals_made m_field_goals_attempted m_3_pointers_made m_3_pinters_attempted m_free_throws_made m_free_throws_attempted m_offensive_rebounds m_defensive_rebounds m_rebounds m_assists m_steals m_blocks m_turnovers m_personal_fouls m_points m_plus_minus rn",
)

input_data = [
    NbaGameDetail(
        game_id=22000070, team_id=1610612765, player_id=1630165, dim_team_abbreviation="DET", dim_player_name="Killian Hayes", dim_start_position="G", dim_din_not_dress=None,
        dim_not_with_tea=None, dim_game_date="2021-01-01", dim_season=2020, dim_team_did_win=True, m_seconds_played=1404, m_field_goals_made=0, m_field_goals_attempted=5,
        m_3_pointers_made=0, m_3_pinters_attempted=2, m_free_throws_made=0, m_free_throws_attempted=0, m_offensive_rebounds=0, m_defensive_rebounds=1, m_rebounds=1, m_assists=6, m_steals=0,
        m_blocks=0, m_turnovers=2, m_personal_fouls=2, m_points=0, m_plus_minus=-2
    ),
    NbaGameDetail(
        game_id=22000070, team_id=1610612765, player_id=1630165, dim_team_abbreviation="DET", dim_player_name="Killian Hayes", dim_start_position="G", dim_din_not_dress=None,
        dim_not_with_tea=None, dim_game_date="2021-01-01", dim_season=2020, dim_team_did_win=True, m_seconds_played=1404, m_field_goals_made=0, m_field_goals_attempted=6,
        m_3_pointers_made=0, m_3_pinters_attempted=2, m_free_throws_made=0, m_free_throws_attempted=0, m_offensive_rebounds=0, m_defensive_rebounds=1, m_rebounds=1, m_assists=6, m_steals=0,
        m_blocks=0, m_turnovers=2, m_personal_fouls=2, m_points=0, m_plus_minus=-2
    ),
    NbaGameDetail(
        game_id=22000070, team_id=1610612765, player_id=1630240, dim_team_abbreviation="DET", dim_player_name="Saben Lee", dim_start_position=None, dim_din_not_dress=False,
        dim_not_with_tea=False, dim_game_date="2021-01-01", dim_season=2020, dim_team_did_win=True, m_seconds_played=None, m_field_goals_made=None, m_field_goals_attempted=None,
        m_3_pointers_made=None, m_3_pinters_attempted=None, m_free_throws_made=None, m_free_throws_attempted=None, m_offensive_rebounds=None, m_defensive_rebounds=None, m_rebounds=None, m_assists=None,
        m_steals=None, m_blocks=None, m_turnovers=None, m_personal_fouls=None, m_points=None, m_plus_minus=None
    ),
    NbaGameDetail(
        game_id=22000070, team_id=1610612765, player_id=1630240, dim_team_abbreviation="DET", dim_player_name="Saben Lee", dim_start_position=None, dim_din_not_dress=False, dim_not_with_tea=False,
        dim_game_date="2021-01-01", dim_season=2020, dim_team_did_win=True, m_seconds_played=None, m_field_goals_made=None, m_field_goals_attempted=None, m_3_pointers_made=None, m_3_pinters_attempted=None,
        m_free_throws_made=None, m_free_throws_attempted=None, m_offensive_rebounds=None, m_defensive_rebounds=None, m_rebounds=None, m_assists=None, m_steals=None, m_blocks=None, m_turnovers=None,
        m_personal_fouls=None, m_points=None, m_plus_minus=None
    )
]


def test_job_1(spark_session):
    fake_input_data = spark_session.createDataFrame(input_data)
    print(fake_input_data)
    actual_output_data = job_1(spark_session, fake_input_data)
    expected_output_data = [
        NbaGameDetailDedup(
            game_id=22000070, team_id=1610612765, player_id=1630165, dim_team_abbreviation="DET", dim_player_name="Killian Hayes", dim_start_position="G", dim_din_not_dress=None, dim_not_with_tea=None,
            dim_game_date="2021-01-01", dim_season=2020, dim_team_did_win=True, m_seconds_played=1404, m_field_goals_made=0, m_field_goals_attempted=5, m_3_pointers_made=0, m_3_pinters_attempted=2,
            m_free_throws_made=0, m_free_throws_attempted=0, m_offensive_rebounds=0, m_defensive_rebounds=1, m_rebounds=1, m_assists=6, m_steals=0, m_blocks=0, m_turnovers=2, m_personal_fouls=2,
            m_points=0, m_plus_minus=-2, rn=1
        ),
        NbaGameDetailDedup(
            game_id=22000070, team_id=1610612765, player_id=1630240, dim_team_abbreviation="DET", dim_player_name="Saben Lee", dim_start_position=None, dim_din_not_dress=False, dim_not_with_tea=False,
            dim_game_date="2021-01-01", dim_season=2020, dim_team_did_win=True, m_seconds_played=None, m_field_goals_made=None, m_field_goals_attempted=None, m_3_pointers_made=None, m_3_pinters_attempted=None,
            m_free_throws_made=None, m_free_throws_attempted=None, m_offensive_rebounds=None, m_defensive_rebounds=None, m_rebounds=None, m_assists=None, m_steals=None, m_blocks=None, m_turnovers=None,
            m_personal_fouls=None, m_points=None, m_plus_minus=None, rn=1
        )
    ]
    expected_output_data_df = spark_session.createDataFrame(expected_output_data)
    assert_df_equality(
        actual_output_data, expected_output_data_df, ignore_nullable=True
    )

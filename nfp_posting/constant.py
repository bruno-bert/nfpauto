QUERY_SELECT_SCRIPT="select * from scripts where name = '{}'"
QUERY_SELECT_STEPS="select * from steps where script_id = {} and is_check_session_timeout = '{}' ORDER BY sort_number ASC"

QUERY_SELECT_SCRIPT="select * from scripts where id = {}"
QUERY_SELECT_STEPS="select * from steps where script_id = {} order by sort_number asc"
QUERY_SELECT_START_CONFIG="select * from start_config where script_id = {}"
DATABASE_FILE="seleniumdb/seleniumdb.db"
RESET_SKIP_INDICATOR="none"
class Script:
   
    def __init__(self):
        self.id = None
        self.name = None        
        self.description = None
        self.version = None
        self.status = None
        self.delete_on_sync = None
        self.wait_message_between_steps = None
        self.minimize_message = None

class Start_Config:
   
    def __init__(self):
        self.id = None
        self.script_id = None        
        self.driver_name = None
        self.debugger_host = None
        self.browser_path = None
        self.browser_args = None    
        self.browser_kill_cmd = None  
        self.browser_start_cmd = None  
        self.initial_url = None  
        self.attempt_attach_message = None
        self.delay_between_attempt = None
        self.wait_after_refresh = None



class Step:
    
    def __init__(self):
        self.id = None
        self.script_id = None        
        self.step_id = None
        self.step_name = None
        self.step_description = None
        self.sort_number = None
        self.skip = None
        self.on_success_goto = None
        self.on_error_goto = None
        self.find_method = None
        self.expression = None
        self.action = None
        self.text_to_type = None
        self.check_session = None
        self.is_check_session_timeout = None
        self.session_timeout__step_id = None
        self.on_session_timeout_start_from = None
        self.base_element = None
        self.element_from_step = None
        self.error_message_finder = None
        self.success_message_finder = None
        self.must_wait_element = None
        self.timeout_to_element = None
        self.log_message_before = None
        self.log_message_after = None
        self.wait_manual_action = None
        self.steps_to_skip_on_next_run = None
        self.is_end_step = None
        self.manual_action_message = None
        self.show_error_log = None
        self.wait_next = None
        self.id_tela = None
        self.refresh_on_error = None
        self.refresh_on_success = None
        self.minimize_after_step = None
        self.maximize_after_step = None

        #estas colunas não são do banco de dados
        self.resulted_element = None
        self.resulted_success_message = None
        self.resulted_error_message = None
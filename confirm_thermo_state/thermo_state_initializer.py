from thermo_state import ThermoState
from location import Location

class ThermoStateInitializer:
    def __init__(self):
        self.thermo_states = []

    def init_state_options(self):
        #INIT POPUPS BEFORE MENUS TO IDENTIFY MORE EASILY MENUS
        self.init_battery_low_pop()
        self.init_confirm_protocol_pop()
        self.init_keyboard_pop()
        self.init_main_menu()
        self.init_incubate_menu()
        self.init_saved_protocols_menu()
        #INIT PROTOCOL DONE BEFORE RUNNING PROTOCOL TO USE STATUS AS A FEATURE
        self.init_protocol_done_menu()
        self.init_running_protocol_menu()
        return self.thermo_states

    def init_main_menu(self):
        main_menu = ThermoState('Main Menu')
        main_menu.add_feature(word="Protocol", location=Location(left_top_corner=(508,297),right_bottom_corner=(590,328)))
        main_menu.add_feature(word="Saved", location=Location(left_top_corner=(423,298),right_bottom_corner=(485,330)))
        main_menu.add_feature(word="Protocols", location=Location(left_top_corner=(351,297),right_bottom_corner=(439,330)))
        main_menu.add_feature(word="Incubate", location=Location(left_top_corner=(231,298),right_bottom_corner=(311,329)))
        main_menu.add_feature(word="Tools", location=Location(left_top_corner=(92,297),right_bottom_corner=(149,330)))
        main_menu.add_feature(word="Thermal", location=Location(left_top_corner=(283,431),right_bottom_corner=(397,475)))
        main_menu.add_feature(word="Cycler", location=Location(left_top_corner=(202,429),right_bottom_corner=(299,473)))
        self.thermo_states.append(main_menu)

    def init_battery_low_pop(self):
        battery_menu = ThermoState('Battery Low Pop Up')
        battery_menu.add_feature(word="Battery", location=Location(left_top_corner=(398,392),right_bottom_corner=(474,428)))
        battery_menu.add_feature(word="low", location=Location(left_top_corner=(368,392),right_bottom_corner=(415,427)))
        battery_menu.add_feature(word="Needs", location=Location(left_top_corner=(312,392),right_bottom_corner=(381,427)))
        battery_menu.add_feature(word="replacement", location=Location(left_top_corner=(212,392),right_bottom_corner=(328,427)))
        battery_menu.add_feature(word="Date", location=Location(left_top_corner=(392,375),right_bottom_corner=(449,409)))
        battery_menu.add_feature(word="will", location=Location(left_top_corner=(329,375),right_bottom_corner=(374,408)))
        battery_menu.add_feature(word="lost", location=Location(left_top_corner=(271,375),right_bottom_corner=(321,408)))
        battery_menu.add_feature(word="power", location=Location(left_top_corner=(438,354),right_bottom_corner=(506,390)))
        battery_menu.add_feature(word="failure", location=Location(left_top_corner=(388,354),right_bottom_corner=(457,389)))
        battery_menu.add_feature(word="protection", location=Location(left_top_corner=(307,352),right_bottom_corner=(404,389)))
        battery_menu.add_feature(word="function", location=Location(left_top_corner=(183,352),right_bottom_corner=(266,389)))
        battery_menu.add_feature(word="OK", location=Location(left_top_corner=(321,281),right_bottom_corner=(365,315)))
        self.thermo_states.append(battery_menu)

    def init_incubate_menu(self):
        incubate_menu = ThermoState('Incubate Menu')
        incubate_menu.add_feature(word="Incubate", location=Location(left_top_corner=(299,568),right_bottom_corner=(386,600)))
        incubate_menu.add_feature(word="Block", location=Location(left_top_corner=(423,400),right_bottom_corner=(497,439)))
        incubate_menu.add_feature(word="temperature", location=Location(left_top_corner=(307,398),right_bottom_corner=(440,438)))
        incubate_menu.add_feature(word="Hold", location=Location(left_top_corner=(352,343),right_bottom_corner=(413,378)))
        incubate_menu.add_feature(word="Lid", location=Location(left_top_corner=(424,286),right_bottom_corner=(472,322)))
        incubate_menu.add_feature(word="temperature", location=Location(left_top_corner=(307,283),right_bottom_corner=(440,322)))
        self.thermo_states.append(incubate_menu)

    def init_running_protocol_menu(self):
        running_protocol_menu = ThermoState('Running Protocol Menu')
        running_protocol_menu.add_feature(word="Status", location=Location(left_top_corner=(309,568),right_bottom_corner=(378,600)))
        running_protocol_menu.add_feature(word="Pause", location=Location(left_top_corner=(312,123),right_bottom_corner=(371,154)))
        running_protocol_menu.add_feature(word="Skip", location=Location(left_top_corner=(209,121),right_bottom_corner=(257,153)))
        running_protocol_menu.add_feature(word="Step", location=Location(left_top_corner=(178,121),right_bottom_corner=(226,153)))
        running_protocol_menu.add_feature(word="Cancel", location=Location(left_top_corner=(57,121),right_bottom_corner=(125,152)))
        self.thermo_states.append(running_protocol_menu)

    def init_protocol_done_menu(self):
        protocol_done_menu = ThermoState('Protocol Done Menu')
        protocol_done_menu.add_feature(word="Run", location=Location(left_top_corner=(352,527),right_bottom_corner=(406,562)))
        protocol_done_menu.add_feature(word="complete", location=Location(left_top_corner=(277,526),right_bottom_corner=(369,561)))
        protocol_done_menu.add_feature(word="Idle", location=Location(left_top_corner=(320,191),right_bottom_corner=(368,225)))
        self.thermo_states.append(protocol_done_menu)

    def init_confirm_protocol_pop(self):
        confirm_protocol_pop = ThermoState('Confirm Protocol Pop Up')
        confirm_protocol_pop.add_feature(word="Run", location=Location(left_top_corner=(352,406),right_bottom_corner=(404,440)))
        confirm_protocol_pop.add_feature(word="Volume", location=Location(left_top_corner=(371,339),right_bottom_corner=(451,374)))
        confirm_protocol_pop.add_feature(word="Cancel", location=Location(left_top_corner=(240,263),right_bottom_corner=(315,296)))
        confirm_protocol_pop.add_feature(word="OK", location=Location(left_top_corner=(384,263),right_bottom_corner=(430,297)))
        self.thermo_states.append(confirm_protocol_pop)

    def init_saved_protocols_menu(self):
        saved_protocols_menu = ThermoState('Saved Protocols Menu')
        saved_protocols_menu.add_feature(word="Saved", location=Location(left_top_corner=(348,567),right_bottom_corner=(416,601)))
        saved_protocols_menu.add_feature(word="Protocols", location=Location(left_top_corner=(269,567),right_bottom_corner=(363,600)))
        saved_protocols_menu.add_feature(word="Folders", location=Location(left_top_corner=(572,520),right_bottom_corner=(649,553)))
        saved_protocols_menu.add_feature(word="Files", location=Location(left_top_corner=(379,517),right_bottom_corner=(434,552)))
        saved_protocols_menu.add_feature(word="RECENT", location=Location(left_top_corner=(514,471),right_bottom_corner=(602,504)))
        saved_protocols_menu.add_feature(word="Folder", location=Location(left_top_corner=(461,127),right_bottom_corner=(522,160)))
        saved_protocols_menu.add_feature(word="File", location=Location(left_top_corner=(345,126),right_bottom_corner=(389,159)))
        saved_protocols_menu.add_feature(word="Edit", location=Location(left_top_corner=(196,128),right_bottom_corner=(239,158)))
        self.thermo_states.append(saved_protocols_menu)

    def init_keyboard_pop(self):
        keyboard_pop = ThermoState('Keyboard Pop Up')
        keyboard_pop.add_feature(word="Sample", location=Location(left_top_corner=(405,532),right_bottom_corner=(481,569)))
        keyboard_pop.add_feature(word="volume", location=Location(left_top_corner=(344,532),right_bottom_corner=(420,568)))
        keyboard_pop.add_feature(word="Lid", location=Location(left_top_corner=(437,532),right_bottom_corner=(481,568)))
        keyboard_pop.add_feature(word="temperature", location=Location(left_top_corner=(341,532),right_bottom_corner=(454,567)))
        keyboard_pop.add_feature(word="Hold", location=Location(left_top_corner=(424,532),right_bottom_corner=(480,569)))
        keyboard_pop.add_feature(word="time", location=Location(left_top_corner=(388,532),right_bottom_corner=(441,569)))
        keyboard_pop.add_feature(word="Block", location=Location(left_top_corner=(416,532),right_bottom_corner=(480,569)))
        keyboard_pop.add_feature(word="temperature", location=Location(left_top_corner=(319,532),right_bottom_corner=(432,569)))
        keyboard_pop.add_feature(word="OK", location=Location(left_top_corner=(383, 170), right_bottom_corner=(428, 203)))
        keyboard_pop.add_feature(word="Cancel", location=Location(left_top_corner=(241, 169), right_bottom_corner=(316, 202)))
        self.thermo_states.append(keyboard_pop)
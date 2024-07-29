from thermo_state import ThermoState
from location import Location

class ThermoStateInitializer:
    def __init__(self):
        self.thermo_states = []

    def init_state_options(self):
        #INIT POPUPS BEFORE MENUS TO IDENTIFY MORE EASILY MENUS
        self.init_keyboard_pop()
        self.init_warning_pop()
        self.init_are_you_sure_pop()
        self.init_insert_step_pop()
        self.init_step_option_pop()
        self.init_confirm_protocol_pop()
        self.init_file_folder_option_pop()
        self.init_copy_pop()
        self.init_big_keyboard_pop()
        self.init_save_before_exit_pop()
        self.init_main_menu()
        self.init_saved_protocols_menu()
        self.init_incubate_menu()
        #INIT PROTOCOL DONE BEFORE RUNNING PROTOCOL TO USE STATUS AS A FEATURE
        self.init_protocol_done_menu()
        self.init_running_protocol_menu()
        self.init_edit_protcol_menu()
        self.init_tools_menu()
        self.init_settings_menu()
        self.init_logs_menu()
        self.init_system_logs_menu()
        self.init_self_test_menu()
        self.init_about_menu()
        self.init_update_menu()

        return self.thermo_states

    def init_main_menu(self):
        main_menu = ThermoState('Main Menu')
        main_menu.add_feature(word='New', location=Location(left_top_corner=(566, 280), right_bottom_corner=(609, 309)))
        main_menu.add_feature(word='Protocol',
                              location=Location(left_top_corner=(517, 280), right_bottom_corner=(583, 309)))
        main_menu.add_feature(word='Thermal',
                              location=Location(left_top_corner=(344, 385), right_bottom_corner=(436, 425)))
        main_menu.add_feature(word='Cycler',
                              location=Location(left_top_corner=(284, 384), right_bottom_corner=(360, 424)))
        main_menu.add_feature(word='Saved',
                              location=Location(left_top_corner=(450, 281), right_bottom_corner=(504, 311)))
        main_menu.add_feature(word='Protocols',
                              location=Location(left_top_corner=(395, 281), right_bottom_corner=(468, 310)))
        main_menu.add_feature(word='Incubate',
                              location=Location(left_top_corner=(302, 282), right_bottom_corner=(369, 311)))
        main_menu.add_feature(word='Tools',
                              location=Location(left_top_corner=(197, 284), right_bottom_corner=(245, 312)))

        self.thermo_states.append(main_menu)

    def init_logs_menu(self):
        logs_menu = ThermoState('Logs Menu')
        logs_menu.add_feature(word='Logs',
                              location=Location(left_top_corner=(369, 486), right_bottom_corner=(420, 518)))
        logs_menu.add_feature(word='Run', location=Location(left_top_corner=(310, 439), right_bottom_corner=(354, 469)))
        logs_menu.add_feature(word='Status',
                              location=Location(left_top_corner=(270, 439), right_bottom_corner=(326, 469)))
        logs_menu.add_feature(word='File',
                              location=Location(left_top_corner=(582, 436), right_bottom_corner=(625, 466)))
        logs_menu.add_feature(word='Protocol',
                              location=Location(left_top_corner=(439, 436), right_bottom_corner=(511, 467)))
        logs_menu.add_feature(word='System',
                              location=Location(left_top_corner=(411, 145), right_bottom_corner=(466, 175)))
        logs_menu.add_feature(word='Log', location=Location(left_top_corner=(391, 145), right_bottom_corner=(431, 175)))
        logs_menu.add_feature(word='Export',
                              location=Location(left_top_corner=(329, 148), right_bottom_corner=(383, 177)))
        logs_menu.add_feature(word='All', location=Location(left_top_corner=(315, 148), right_bottom_corner=(349, 177)))
        logs_menu.add_feature(word='Export',
                              location=Location(left_top_corner=(254, 148), right_bottom_corner=(307, 178)))
        logs_menu.add_feature(word='Log', location=Location(left_top_corner=(233, 147), right_bottom_corner=(272, 177)))
        self.thermo_states.append(logs_menu)

    def init_copy_pop(self):
        copy_pop_up = ThermoState('Copy Pop Up')
        copy_pop_up.add_feature(word='Save',
                                  location=Location(left_top_corner=(520, 418), right_bottom_corner=(570, 449)))
        copy_pop_up.add_feature(word='Folder',
                                  location=Location(left_top_corner=(477, 391), right_bottom_corner=(536, 424)))
        copy_pop_up.add_feature(word='name',
                                  location=Location(left_top_corner=(442, 392), right_bottom_corner=(494, 423)))
        copy_pop_up.add_feature(word='Location',
                                  location=Location(left_top_corner=(441, 351), right_bottom_corner=(511, 382)))
        copy_pop_up.add_feature(word='Cycler',
                                  location=Location(left_top_corner=(315, 351), right_bottom_corner=(374, 381)))
        copy_pop_up.add_feature(word='USB',
                                  location=Location(left_top_corner=(326, 309), right_bottom_corner=(373, 338)))
        copy_pop_up.add_feature(word='Protocol',
                                  location=Location(left_top_corner=(439, 384), right_bottom_corner=(511, 415)))
        copy_pop_up.add_feature(word='Folder',
                                  location=Location(left_top_corner=(476, 346), right_bottom_corner=(535, 378)))
        copy_pop_up.add_feature(word='name',
                                  location=Location(left_top_corner=(442, 345), right_bottom_corner=(494, 377)))
        self.thermo_states.append(copy_pop_up)

    def init_are_you_sure_pop(self):
        are_you_sure_pop = ThermoState('Are you Sure Pop Up')
        are_you_sure_pop.add_feature(word='Are', location=Location(left_top_corner=(480, 339),
                                                                           right_bottom_corner=(521, 372)))
        are_you_sure_pop.add_feature(word='sure', location=Location(left_top_corner=(426, 339),
                                                                            right_bottom_corner=(473, 372)))
        are_you_sure_pop.add_feature(word='want', location=Location(left_top_corner=(369, 340),
                                                                            right_bottom_corner=(419, 373)))
        are_you_sure_pop.add_feature(word='Yes', location=Location(left_top_corner=(418, 268),
                                                                           right_bottom_corner=(463, 300)))
        are_you_sure_pop.add_feature(word='No', location=Location(left_top_corner=(320, 270),
                                                                          right_bottom_corner=(360, 300)))
        are_you_sure_pop.add_feature(word='Are',
                                     location=Location(left_top_corner=(515, 346), right_bottom_corner=(556, 378)))
        are_you_sure_pop.add_feature(word='sure',
                                     location=Location(left_top_corner=(462, 346), right_bottom_corner=(508, 379)))
        are_you_sure_pop.add_feature(word='want',
                                     location=Location(left_top_corner=(404, 348), right_bottom_corner=(454, 380)))
        are_you_sure_pop.add_feature(word='delete',
                                     location=Location(left_top_corner=(350, 349), right_bottom_corner=(407, 381)))
        are_you_sure_pop.add_feature(word='cancel',
                                     location=Location(left_top_corner=(313, 333), right_bottom_corner=(372, 366)))
        self.thermo_states.append(are_you_sure_pop)
    def init_save_before_exit_pop(self):
        save_before_exit_pop = ThermoState('Save Before Exit Pop Up')
        save_before_exit_pop.add_feature(word='Yes',
                                         location=Location(left_top_corner=(471, 259), right_bottom_corner=(515, 290)))
        save_before_exit_pop.add_feature(word='Do',
                                         location=Location(left_top_corner=(463, 331), right_bottom_corner=(501, 363)))
        save_before_exit_pop.add_feature(word='want',
                                         location=Location(left_top_corner=(406, 331), right_bottom_corner=(456, 363)))
        save_before_exit_pop.add_feature(word='save',
                                         location=Location(left_top_corner=(363, 331), right_bottom_corner=(410, 363)))
        save_before_exit_pop.add_feature(word='changes',
                                         location=Location(left_top_corner=(288, 332), right_bottom_corner=(359, 364)))
        save_before_exit_pop.add_feature(word='No',
                                         location=Location(left_top_corner=(374, 262), right_bottom_corner=(413, 292)))
        self.thermo_states.append(save_before_exit_pop)



    def init_warning_pop(self):
        warning_pop = ThermoState('Warning Pop Up')
        # Battery Pop Up
        warning_pop.add_feature(word='Battery',
                                 location=Location(left_top_corner=(431, 354), right_bottom_corner=(495, 387)))
        warning_pop.add_feature(word='low',
                                 location=Location(left_top_corner=(410, 354), right_bottom_corner=(450, 387)))
        warning_pop.add_feature(word='Needs',
                                 location=Location(left_top_corner=(366, 354), right_bottom_corner=(423, 388)))
        warning_pop.add_feature(word='replacement',
                                 location=Location(left_top_corner=(290, 355), right_bottom_corner=(384, 388)))
        warning_pop.add_feature(word='Date',
                                 location=Location(left_top_corner=(427, 342), right_bottom_corner=(475, 373)))
        warning_pop.add_feature(word='will',
                                 location=Location(left_top_corner=(378, 342), right_bottom_corner=(419, 373)))
        warning_pop.add_feature(word='lost',
                                 location=Location(left_top_corner=(336, 342), right_bottom_corner=(379, 373)))
        warning_pop.add_feature(word='power',
                                 location=Location(left_top_corner=(463, 325), right_bottom_corner=(520, 357)))
        warning_pop.add_feature(word='failure',
                                 location=Location(left_top_corner=(423, 325), right_bottom_corner=(480, 357)))
        warning_pop.add_feature(word='protection',
                                 location=Location(left_top_corner=(362, 325), right_bottom_corner=(441, 358)))
        warning_pop.add_feature(word='function',
                                 location=Location(left_top_corner=(266, 327), right_bottom_corner=(335, 360)))
        # Log Pop Up
        warning_pop.add_feature(word='Log',
                                location=Location(left_top_corner=(458, 347), right_bottom_corner=(502, 381)))
        warning_pop.add_feature(word='file',
                                location=Location(left_top_corner=(437, 347), right_bottom_corner=(477, 381)))
        warning_pop.add_feature(word='truncated',
                                location=Location(left_top_corner=(354, 347), right_bottom_corner=(429, 381)))
        warning_pop.add_feature(word='viewing',
                                location=Location(left_top_corner=(285, 348), right_bottom_corner=(350, 382)))
        warning_pop.add_feature(word='view',
                                location=Location(left_top_corner=(490, 331), right_bottom_corner=(537, 365)))
        warning_pop.add_feature(word='full',
                                location=Location(left_top_corner=(468, 331), right_bottom_corner=(508, 365)))
        warning_pop.add_feature(word='log',
                                location=Location(left_top_corner=(447, 331), right_bottom_corner=(486, 365)))
        warning_pop.add_feature(word='file',
                                location=Location(left_top_corner=(428, 331), right_bottom_corner=(466, 365)))
        warning_pop.add_feature(word='please',
                                location=Location(left_top_corner=(383, 332), right_bottom_corner=(441, 366)))
        warning_pop.add_feature(word='export',
                                location=Location(left_top_corner=(343, 332), right_bottom_corner=(401, 366)))
        warning_pop.add_feature(word='Flash',
                                location=Location(left_top_corner=(265, 333), right_bottom_corner=(316, 367)))
        warning_pop.add_feature(word='Drive',
                                location=Location(left_top_corner=(230, 333), right_bottom_corner=(281, 367)))

        # Read Only Pop Up
        warning_pop.add_feature(word='RECENT',
                                location=Location(left_top_corner=(440, 340), right_bottom_corner=(511, 372)))
        warning_pop.add_feature(word='folder',
                                location=Location(left_top_corner=(401, 340), right_bottom_corner=(458, 372)))
        warning_pop.add_feature(word='read',
                                location=Location(left_top_corner=(360, 340), right_bottom_corner=(406, 372)))
        warning_pop.add_feature(word='only',
                                location=Location(left_top_corner=(330, 340), right_bottom_corner=(377, 372)))
        warning_pop.add_feature(word='cannot',
                                location=Location(left_top_corner=(262, 341), right_bottom_corner=(324, 373)))
        # No USB Flash Drive
        warning_pop.add_feature(word='USB',
                                location=Location(left_top_corner=(418, 341), right_bottom_corner=(465, 372)))
        warning_pop.add_feature(word='flash',
                                location=Location(left_top_corner=(386, 341), right_bottom_corner=(436, 372)))
        warning_pop.add_feature(word='drive',
                                location=Location(left_top_corner=(354, 341), right_bottom_corner=(403, 373)))
        warning_pop.add_feature(word='detected',
                                location=Location(left_top_corner=(300, 343), right_bottom_corner=(371, 373)))
        warning_pop.add_feature(word='Insert',
                                location=Location(left_top_corner=(455, 325), right_bottom_corner=(509, 358)))
        warning_pop.add_feature(word='USB',
                                location=Location(left_top_corner=(417, 325), right_bottom_corner=(464, 357)))
        warning_pop.add_feature(word='flash',
                                location=Location(left_top_corner=(386, 325), right_bottom_corner=(436, 357)))
        warning_pop.add_feature(word='drive',
                                location=Location(left_top_corner=(353, 325), right_bottom_corner=(402, 357)))
        # Wrong Password
        warning_pop.add_feature(word='Incorrect',
                                location=Location(left_top_corner=(385, 339), right_bottom_corner=(459, 372)))
        warning_pop.add_feature(word='password',
                                location=Location(left_top_corner=(325, 339), right_bottom_corner=(404, 371)))
        warning_pop.add_feature(word='Try',
                                location=Location(left_top_corner=(388, 325), right_bottom_corner=(430, 357)))
        warning_pop.add_feature(word='again',
                                location=Location(left_top_corner=(355, 325), right_bottom_corner=(407, 356)))

        # All
        warning_pop.add_feature(word='OK',
                                location=Location(left_top_corner=(372, 271), right_bottom_corner=(411, 300)))
        self.thermo_states.append(warning_pop)

    def init_about_menu(self):
        about_menu = ThermoState('About Menu')
        about_menu.add_feature(word='About',
                               location=Location(left_top_corner=(364, 480), right_bottom_corner=(422, 511)))
        about_menu.add_feature(word='Serial',
                               location=Location(left_top_corner=(446, 331), right_bottom_corner=(507, 363)))
        about_menu.add_feature(word='number',
                               location=Location(left_top_corner=(388, 331), right_bottom_corner=(463, 363)))
        about_menu.add_feature(word='Total',
                               location=Location(left_top_corner=(449, 259), right_bottom_corner=(506, 291)))
        about_menu.add_feature(word='hours',
                               location=Location(left_top_corner=(404, 259), right_bottom_corner=(467, 291)))
        self.thermo_states.append(about_menu)

    def init_self_test_menu(self):
        self_test_menu = ThermoState('Self Test Menu')
        self_test_menu.add_feature(word='Self',
                                   location=Location(left_top_corner=(384, 481), right_bottom_corner=(429, 510)))
        self_test_menu.add_feature(word='Test',
                                   location=Location(left_top_corner=(357, 481), right_bottom_corner=(402, 510)))
        self_test_menu.add_feature(word='Press',
                                   location=Location(left_top_corner=(451, 346), right_bottom_corner=(520, 381)))
        self_test_menu.add_feature(word='Start',
                                   location=Location(left_top_corner=(404, 346), right_bottom_corner=(467, 381)))
        self_test_menu.add_feature(word='Self',
                                   location=Location(left_top_corner=(307, 347), right_bottom_corner=(362, 382)))
        self_test_menu.add_feature(word='Test',
                                   location=Location(left_top_corner=(263, 347), right_bottom_corner=(322, 382)))
        self.thermo_states.append(self_test_menu)

    def init_system_logs_menu(self):
        system_logs_menu = ThermoState('System Logs Menu')
        system_logs_menu.add_feature(word='System',
                                     location=Location(left_top_corner=(376, 487), right_bottom_corner=(439, 519)))
        system_logs_menu.add_feature(word='Log',
                                     location=Location(left_top_corner=(349, 487), right_bottom_corner=(392, 519)))
        system_logs_menu.add_feature(word='Export',
                                     location=Location(left_top_corner=(179, 146), right_bottom_corner=(233, 178)))
        system_logs_menu.add_feature(word='Log',
                                     location=Location(left_top_corner=(159, 147), right_bottom_corner=(198, 177)))
        system_logs_menu.add_feature(word='Run',
                                  location=Location(left_top_corner=(383, 478), right_bottom_corner=(428, 511)))
        system_logs_menu.add_feature(word='Log',
                                  location=Location(left_top_corner=(357, 478), right_bottom_corner=(401, 510)))

        self.thermo_states.append(system_logs_menu)

    def init_insert_step_pop(self):
        insert_step_pop = ThermoState('Insert Step Pop Up')
        insert_step_pop.add_feature(word='Insert',
                                     location=Location(left_top_corner=(447, 439), right_bottom_corner=(503, 473)))
        insert_step_pop.add_feature(word='step',
                                     location=Location(left_top_corner=(421, 438), right_bottom_corner=(466, 471)))
        insert_step_pop.add_feature(word='Temperature',
                                     location=Location(left_top_corner=(345, 403), right_bottom_corner=(440, 434)))
        insert_step_pop.add_feature(word='Gradient',
                                     location=Location(left_top_corner=(351, 341), right_bottom_corner=(426, 382)))
        insert_step_pop.add_feature(word='GOTO',
                                     location=Location(left_top_corner=(363, 299), right_bottom_corner=(418, 328)))
        insert_step_pop.add_feature(word='Cancel',
                                     location=Location(left_top_corner=(358, 232), right_bottom_corner=(422, 264)))
        self.thermo_states.append(insert_step_pop)

    def init_settings_menu(self):
        settings_menu = ThermoState('Settings Menu')
        settings_menu.add_feature(word='Cycler',
                                  location=Location(left_top_corner=(575, 430), right_bottom_corner=(629, 461)))
        settings_menu.add_feature(word='name',
                                  location=Location(left_top_corner=(544, 430), right_bottom_corner=(593, 460)))
        settings_menu.add_feature(word='Settings',
                                  location=Location(left_top_corner=(359, 487), right_bottom_corner=(429, 518)))
        settings_menu.add_feature(word='Default',
                                  location=Location(left_top_corner=(312, 439), right_bottom_corner=(369, 470)))
        settings_menu.add_feature(word='sample',
                                  location=Location(left_top_corner=(274, 439), right_bottom_corner=(332, 469)))
        settings_menu.add_feature(word='volume',
                                  location=Location(left_top_corner=(274, 427), right_bottom_corner=(332, 455)))
        settings_menu.add_feature(word='Date',
                                  location=Location(left_top_corner=(544, 380), right_bottom_corner=(589, 410)))
        settings_menu.add_feature(word='Standby',
                                  location=Location(left_top_corner=(271, 381), right_bottom_corner=(331, 413)))
        settings_menu.add_feature(word='mode',
                                  location=Location(left_top_corner=(275, 368), right_bottom_corner=(321, 397)))
        settings_menu.add_feature(word='Standby',
                                  location=Location(left_top_corner=(302, 338), right_bottom_corner=(364, 370)))
        settings_menu.add_feature(word='delay',
                                  location=Location(left_top_corner=(272, 338), right_bottom_corner=(320, 369)))
        settings_menu.add_feature(word='Display',
                                  location=Location(left_top_corner=(535, 280), right_bottom_corner=(595, 313)))
        settings_menu.add_feature(word='brightness',
                                  location=Location(left_top_corner=(538, 267), right_bottom_corner=(611, 297)))
        settings_menu.add_feature(word='End',
                                  location=Location(left_top_corner=(283, 287), right_bottom_corner=(322, 316)))
        settings_menu.add_feature(word='of',
                                  location=Location(left_top_corner=(269, 287), right_bottom_corner=(300, 315)))
        settings_menu.add_feature(word='beep',
                                  location=Location(left_top_corner=(272, 269), right_bottom_corner=(315, 300)))
        settings_menu.add_feature(word='Restore',
                                  location=Location(left_top_corner=(284, 148), right_bottom_corner=(341, 177)))
        settings_menu.add_feature(word='Defaults',
                                  location=Location(left_top_corner=(243, 148), right_bottom_corner=(302, 176)))
        self.thermo_states.append(settings_menu)

    def init_step_option_pop(self):
        step_option_pop = ThermoState('Step Option Pop Up')
        step_option_pop.add_feature(word='Step',
                                    location=Location(left_top_corner=(558, 439), right_bottom_corner=(606, 472)))
        step_option_pop.add_feature(word='Options',
                                    location=Location(left_top_corner=(489, 429), right_bottom_corner=(577, 481)))
        step_option_pop.add_feature(word='Gradient',
                                    location=Location(left_top_corner=(512, 400), right_bottom_corner=(584, 431)))
        step_option_pop.add_feature(word='Extend',
                                    location=Location(left_top_corner=(512, 298), right_bottom_corner=(573, 329)))
        step_option_pop.add_feature(word='Increment',
                                    location=Location(left_top_corner=(332, 353), right_bottom_corner=(412, 385)))
        step_option_pop.add_feature(word='Ramp',
                                    location=Location(left_top_corner=(333, 297), right_bottom_corner=(389, 330)))
        step_option_pop.add_feature(word='rate',
                                    location=Location(left_top_corner=(333, 282), right_bottom_corner=(376, 311)))
        self.thermo_states.append(step_option_pop)

    def init_edit_protcol_menu(self):
        edit_protocol_menu = ThermoState('Edit Protocol Menu')
        edit_protocol_menu.add_feature(word='New',
                                      location=Location(left_top_corner=(398, 489), right_bottom_corner=(443, 519)))
        edit_protocol_menu.add_feature(word='Protocol',
                                      location=Location(left_top_corner=(343, 489), right_bottom_corner=(415, 519)))
        edit_protocol_menu.add_feature(word='Edit',
                                      location=Location(left_top_corner=(398, 489), right_bottom_corner=(443, 519)))
        edit_protocol_menu.add_feature(word='Protocol',
                                      location=Location(left_top_corner=(345, 489), right_bottom_corner=(417, 518)))
        edit_protocol_menu.add_feature(word='Insert',
                                      location=Location(left_top_corner=(484, 148), right_bottom_corner=(532, 176)))
        edit_protocol_menu.add_feature(word='Delete',
                                      location=Location(left_top_corner=(402, 149), right_bottom_corner=(453, 177)))

        self.thermo_states.append(edit_protocol_menu)

    def init_incubate_menu(self):
        incubate_menu = ThermoState('Incubate Menu')
        incubate_menu.add_feature(word='Incubate',
                                  location=Location(left_top_corner=(358, 488), right_bottom_corner=(428, 519)))
        incubate_menu.add_feature(word='Block',
                                  location=Location(left_top_corner=(453, 359), right_bottom_corner=(513, 393)))
        incubate_menu.add_feature(word='temperature',
                                  location=Location(left_top_corner=(361, 358), right_bottom_corner=(470, 393)))
        incubate_menu.add_feature(word='Hold',
                                  location=Location(left_top_corner=(397, 316), right_bottom_corner=(447, 348)))
        incubate_menu.add_feature(word='Lid',
                                  location=Location(left_top_corner=(451, 270), right_bottom_corner=(495, 304)))
        incubate_menu.add_feature(word='temperature',
                                  location=Location(left_top_corner=(362, 270), right_bottom_corner=(468, 303)))

        self.thermo_states.append(incubate_menu)

    def init_running_protocol_menu(self):
        running_protocol_menu = ThermoState('Running Protocol Menu')
        running_protocol_menu.add_feature(word='Status',
                                          location=Location(left_top_corner=(365, 488), right_bottom_corner=(424, 519)))
        running_protocol_menu.add_feature(word='Pause',
                                          location=Location(left_top_corner=(363, 146), right_bottom_corner=(413, 175)))
        running_protocol_menu.add_feature(word='Skip',
                                          location=Location(left_top_corner=(284, 147), right_bottom_corner=(325, 175)))
        running_protocol_menu.add_feature(word='Step',
                                          location=Location(left_top_corner=(259, 147), right_bottom_corner=(302, 175)))
        running_protocol_menu.add_feature(word='Cancel',
                                          location=Location(left_top_corner=(168, 148), right_bottom_corner=(223, 177)))

        self.thermo_states.append(running_protocol_menu)

    def init_protocol_done_menu(self):
        protocol_done_menu = ThermoState('Protocol Done Menu')
        protocol_done_menu.add_feature(word='Run',
                                       location=Location(left_top_corner=(399, 460), right_bottom_corner=(445, 491)))
        protocol_done_menu.add_feature(word='canceled',
                                       location=Location(left_top_corner=(344, 460), right_bottom_corner=(417, 491)))
        protocol_done_menu.add_feature(word='complete',
                                       location=Location(left_top_corner=(342, 459), right_bottom_corner=(416, 490)))
        protocol_done_menu.add_feature(word='Idle',
                                       location=Location(left_top_corner=(368, 199), right_bottom_corner=(412, 230)))
        self.thermo_states.append(protocol_done_menu)

    def init_confirm_protocol_pop(self):
        confirm_protocol_pop = ThermoState('Confirm Protocol Pop Up')
        confirm_protocol_pop.add_feature(word='Run',
                                         location=Location(left_top_corner=(406, 365), right_bottom_corner=(451, 396)))
        confirm_protocol_pop.add_feature(word='Volume',
                                         location=Location(left_top_corner=(412, 314), right_bottom_corner=(478, 345)))
        confirm_protocol_pop.add_feature(word='OK',
                                         location=Location(left_top_corner=(421, 257), right_bottom_corner=(460, 286)))
        confirm_protocol_pop.add_feature(word='Cancel',
                                         location=Location(left_top_corner=(309, 255), right_bottom_corner=(372, 286)))
        self.thermo_states.append(confirm_protocol_pop)
    def init_file_folder_option_pop(self):
        folder_options_pop = ThermoState('File/Folder Options Pop up')
        folder_options_pop.add_feature(word='Folder',
                                       location=Location(left_top_corner=(440, 433), right_bottom_corner=(500, 467)))
        folder_options_pop.add_feature(word='options',
                                       location=Location(left_top_corner=(394, 432), right_bottom_corner=(459, 466)))
        folder_options_pop.add_feature(word='New',
                                       location=Location(left_top_corner=(422, 393), right_bottom_corner=(468, 424)))
        folder_options_pop.add_feature(word='Copy',
                                       location=Location(left_top_corner=(314, 393), right_bottom_corner=(367, 426)))
        folder_options_pop.add_feature(word='Rename',
                                       location=Location(left_top_corner=(409, 322), right_bottom_corner=(477, 351)))
        folder_options_pop.add_feature(word='Delete',
                                       location=Location(left_top_corner=(313, 322), right_bottom_corner=(369, 352)))
        folder_options_pop.add_feature(word='Copy',
                                       location=Location(left_top_corner=(417, 394), right_bottom_corner=(470, 425)))
        folder_options_pop.add_feature(word='Rename',
                                       location=Location(left_top_corner=(307, 396), right_bottom_corner=(376, 426)))
        folder_options_pop.add_feature(word='Delete',
                                       location=Location(left_top_corner=(415, 323), right_bottom_corner=(472, 352)))
        folder_options_pop.add_feature(word='options',
                                       location=Location(left_top_corner=(411, 433), right_bottom_corner=(476, 466)))
        self.thermo_states.append(folder_options_pop)

    def init_tools_menu(self):
        tools_menu = ThermoState('Tools Menu')
        tools_menu.add_feature(word='Settings',
                               location=Location(left_top_corner=(487, 372), right_bottom_corner=(546, 402)))
        tools_menu.add_feature(word='Update',
                               location=Location(left_top_corner=(488, 257), right_bottom_corner=(544, 287)))
        tools_menu.add_feature(word='Tools',
                               location=Location(left_top_corner=(368, 489), right_bottom_corner=(422, 519)))
        tools_menu.add_feature(word='Test',
                               location=Location(left_top_corner=(357, 375), right_bottom_corner=(397, 402)))
        tools_menu.add_feature(word='Logs',
                               location=Location(left_top_corner=(235, 374), right_bottom_corner=(280, 405)))
        tools_menu.add_feature(word='About',
                               location=Location(left_top_corner=(361, 255), right_bottom_corner=(410, 282)))
        tools_menu.add_feature(word='Service',
                               location=Location(left_top_corner=(247, 253), right_bottom_corner=(301, 284)))
        tools_menu.add_feature(word='Log',
                               location=Location(left_top_corner=(226, 253), right_bottom_corner=(265, 283)))
        tools_menu.add_feature(word='in', location=Location(left_top_corner=(215, 253), right_bottom_corner=(244, 283)))


        self.thermo_states.append(tools_menu)

    def init_saved_protocols_menu(self):
        saved_protocols_menu = ThermoState('Saved Protocols Menu')
        saved_protocols_menu.add_feature(word='Folders',
                                         location=Location(left_top_corner=(567, 449), right_bottom_corner=(630, 480)))
        saved_protocols_menu.add_feature(word='Saved',
                                         location=Location(left_top_corner=(395, 488), right_bottom_corner=(453, 519)))
        saved_protocols_menu.add_feature(word='Protocols',
                                         location=Location(left_top_corner=(335, 488), right_bottom_corner=(413, 518)))
        saved_protocols_menu.add_feature(word='Preview',
                                         location=Location(left_top_corner=(241, 454), right_bottom_corner=(305, 483)))
        saved_protocols_menu.add_feature(word='Files',
                                         location=Location(left_top_corner=(418, 450), right_bottom_corner=(466, 481)))
        saved_protocols_menu.add_feature(word='RECENT',
                                         location=Location(left_top_corner=(522, 414), right_bottom_corner=(594, 444)))
        saved_protocols_menu.add_feature(word='Folder',
                                         location=Location(left_top_corner=(477, 148), right_bottom_corner=(529, 179)))
        saved_protocols_menu.add_feature(word='Options',
                                         location=Location(left_top_corner=(439, 147), right_bottom_corner=(497, 179)))
        saved_protocols_menu.add_feature(word='File',
                                         location=Location(left_top_corner=(389, 150), right_bottom_corner=(427, 180)))
        saved_protocols_menu.add_feature(word='Options',
                                         location=Location(left_top_corner=(350, 150), right_bottom_corner=(408, 179)))
        saved_protocols_menu.add_feature(word='Edit',
                                         location=Location(left_top_corner=(273, 153), right_bottom_corner=(312, 180)))
        self.thermo_states.append(saved_protocols_menu)

    def init_keyboard_pop(self):
        keyboard_pop = ThermoState('Keyboard Pop Up')
        keyboard_pop.add_feature(word='Sample',
                                 location=Location(left_top_corner=(436, 462), right_bottom_corner=(501, 494)))
        keyboard_pop.add_feature(word='volume',
                                 location=Location(left_top_corner=(392, 462), right_bottom_corner=(454, 493)))
        keyboard_pop.add_feature(word='0-100',
                                 location=Location(left_top_corner=(349, 462), right_bottom_corner=(405, 493)))
        keyboard_pop.add_feature(word='Lid',
                                 location=Location(left_top_corner=(462, 462), right_bottom_corner=(501, 495)))
        keyboard_pop.add_feature(word='temperature',
                                 location=Location(left_top_corner=(389, 462), right_bottom_corner=(480, 495)))
        keyboard_pop.add_feature(word='40-110',
                                 location=Location(left_top_corner=(339, 462), right_bottom_corner=(402, 495)))
        keyboard_pop.add_feature(word='Block',
                                 location=Location(left_top_corner=(446, 463), right_bottom_corner=(500, 495)))
        keyboard_pop.add_feature(word='temperature',
                                 location=Location(left_top_corner=(373, 463), right_bottom_corner=(465, 494)))
        keyboard_pop.add_feature(word='Hold',
                                 location=Location(left_top_corner=(453, 462), right_bottom_corner=(501, 495)))
        keyboard_pop.add_feature(word='HH',
                                 location=Location(left_top_corner=(398, 462), right_bottom_corner=(439, 494)))
        keyboard_pop.add_feature(word='MM',
                                 location=Location(left_top_corner=(374, 462), right_bottom_corner=(416, 494)))
        keyboard_pop.add_feature(word='SS',
                                 location=Location(left_top_corner=(355, 462), right_bottom_corner=(392, 494)))
        keyboard_pop.add_feature(word='Month',
                                 location=Location(left_top_corner=(443, 463), right_bottom_corner=(501, 494)))
        keyboard_pop.add_feature(word='Day',
                                 location=Location(left_top_corner=(456, 460), right_bottom_corner=(501, 493)))
        keyboard_pop.add_feature(word='Year',
                                 location=Location(left_top_corner=(451, 463), right_bottom_corner=(502, 494)))
        keyboard_pop.add_feature(word='Hours',
                                 location=Location(left_top_corner=(443, 462), right_bottom_corner=(501, 493)))
        keyboard_pop.add_feature(word='Minutes',
                                 location=Location(left_top_corner=(435, 463), right_bottom_corner=(501, 494)))
        keyboard_pop.add_feature(word='Seconds',
                                 location=Location(left_top_corner=(428, 463), right_bottom_corner=(502, 494)))
        keyboard_pop.add_feature(word='Standby',
                                 location=Location(left_top_corner=(431, 461), right_bottom_corner=(501, 494)))
        keyboard_pop.add_feature(word='mode',
                                 location=Location(left_top_corner=(396, 461), right_bottom_corner=(449, 493)))
        keyboard_pop.add_feature(word='delay',
                                 location=Location(left_top_corner=(359, 461), right_bottom_corner=(413, 493)))
        keyboard_pop.add_feature(word='OK',
                                 location=Location(left_top_corner=(418, 184), right_bottom_corner=(458, 214)))
        keyboard_pop.add_feature(word='Cancel',
                                 location=Location(left_top_corner=(309, 183), right_bottom_corner=(372, 214)))
        self.thermo_states.append(keyboard_pop)

    def init_update_menu(self):
        update_menu = ThermoState('Update Menu')
        update_menu.add_feature(word='Update',
                                location=Location(left_top_corner=(390, 479), right_bottom_corner=(453, 510)))
        update_menu.add_feature(word='Firmware',
                                location=Location(left_top_corner=(332, 479), right_bottom_corner=(408, 510)))
        update_menu.add_feature(word='update',
                                location=Location(left_top_corner=(463, 307), right_bottom_corner=(532, 342)))
        update_menu.add_feature(word='firmware',
                                location=Location(left_top_corner=(398, 308), right_bottom_corner=(481, 343)))
        update_menu.add_feature(word='Insert',
                                location=Location(left_top_corner=(349, 309), right_bottom_corner=(411, 344)))
        update_menu.add_feature(word='latest',
                                location=Location(left_top_corner=(434, 292), right_bottom_corner=(493, 325)))
        update_menu.add_feature(word='firmware',
                                location=Location(left_top_corner=(369, 292), right_bottom_corner=(452, 325)))
        update_menu.add_feature(word='press',
                                location=Location(left_top_corner=(270, 292), right_bottom_corner=(331, 326)))
        self.thermo_states.append(update_menu)

    def init_big_keyboard_pop(self):
        big_keyboard_pop = ThermoState('Big Keyboard Pop Up')
        big_keyboard_pop.add_feature(word='Password',
                                     location=Location(left_top_corner=(559, 428), right_bottom_corner=(637, 458)))
        big_keyboard_pop.add_feature(word='Name',
                                     location=Location(left_top_corner=(582, 435), right_bottom_corner=(638, 467)))
        big_keyboard_pop.add_feature(word='Folder',
                                     location=Location(left_top_corner=(362, 438), right_bottom_corner=(422, 469)))
        big_keyboard_pop.add_feature(word='Folder',
                                     location=Location(left_top_corner=(579, 435), right_bottom_corner=(638, 467)))
        big_keyboard_pop.add_feature(word='1238',
                                     location=Location(left_top_corner=(552, 275), right_bottom_corner=(606, 306)))
        big_keyboard_pop.add_feature(word='123&',
                                     location=Location(left_top_corner=(552, 275), right_bottom_corner=(606, 306)))
        self.thermo_states.append(big_keyboard_pop)

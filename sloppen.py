import pygame

class game_data:
    def __init__(self, window_name, fps, res):
        self.map = map_manager(self)
        self.keyboard = keyboard_manager(self)
        self.screen = screen_manager(window_name, res, self)
        self.run = True
        self.events = None
        self.fps = fps
        self.fpsclock = None

    def set_fps(self, frames_per_second):
        self.fps = frames_per_second
        self.fpsclock = pygame.time.Clock()

    def initalize(self):
        self.set_fps(self.fps)

    def update_game(self):
        self.events = pygame.event.get()

        for cur_ev in self.events:
            if cur_ev.type == pygame.QUIT:
                self.run = False

        self.keyboard.update_keys()
        self.map.run_map()
        self.screen.draw()
        self.fpsclock.tick(self.fps)

    def game_loop(self): 
        while self.run == True: 
            self.update_game() 
        pygame.quit() 

class keyboard_manager:
    def __init__(self, game):
        self.game = game
        self.keys = [
            ["K_BACKSPACE", 0, 0, pygame.K_BACKSPACE],
            ["K_TAB", 0, 0, pygame.K_TAB],
            ["K_CLEAR", 0, 0, pygame.K_CLEAR],
            ["K_RETURN", 0, 0, pygame.K_RETURN],
            ["K_PAUSE", 0, 0, pygame.K_PAUSE],
            ["K_ESCAPE", 0, 0, pygame.K_ESCAPE],
            ["K_SPACE", 0, 0, pygame.K_SPACE],
            ["K_EXCLAIM", 0, 0, pygame.K_EXCLAIM],
            ["K_QUOTEDBL", 0, 0, pygame.K_QUOTEDBL],
            ["K_HASH", 0, 0, pygame.K_HASH],
            ["K_DOLLAR", 0, 0, pygame.K_DOLLAR],
            ["K_AMPERSAND", 0, 0, pygame.K_AMPERSAND],
            ["K_QUOTE", 0, 0, pygame.K_QUOTE],
            ["K_LEFTPAREN", 0, 0, pygame.K_LEFTPAREN],
            ["K_RIGHTPAREN", 0, 0, pygame.K_RIGHTPAREN],
            ["K_ASTERISK", 0, 0, pygame.K_ASTERISK],
            ["K_PLUS", 0, 0, pygame.K_PLUS],
            ["K_COMMA", 0, 0, pygame.K_COMMA],
            ["K_MINUS", 0, 0, pygame.K_MINUS],
            ["K_PERIOD", 0, 0, pygame.K_PERIOD],
            ["K_SLASH", 0, 0, pygame.K_SLASH],
            ["K_0", 0, 0, pygame.K_0],
            ["K_1", 0, 0, pygame.K_1],
            ["K_2", 0, 0, pygame.K_2],
            ["K_3", 0, 0, pygame.K_3],
            ["K_4", 0, 0, pygame.K_4],
            ["K_5", 0, 0, pygame.K_5],
            ["K_6", 0, 0, pygame.K_6],
            ["K_7", 0, 0, pygame.K_7],
            ["K_8", 0, 0, pygame.K_8],
            ["K_9", 0, 0, pygame.K_9],
            ["K_COLON", 0, 0, pygame.K_COLON],
            ["K_SEMICOLON", 0, 0, pygame.K_SEMICOLON],
            ["K_LESS", 0, 0, pygame.K_LESS],
            ["K_EQUALS", 0, 0, pygame.K_EQUALS],
            ["K_GREATER", 0, 0, pygame.K_GREATER],
            ["K_QUESTION", 0, 0, pygame.K_QUESTION],
            ["K_AT", 0, 0, pygame.K_AT],
            ["K_LEFTBRACKET", 0, 0, pygame.K_LEFTBRACKET],
            ["K_BACKSLASH", 0, 0, pygame.K_BACKSLASH],
            ["K_RIGHTBRACKET", 0, 0, pygame.K_RIGHTBRACKET],
            ["K_CARET", 0, 0, pygame.K_CARET],
            ["K_UNDERSCORE", 0, 0, pygame.K_UNDERSCORE],
            ["K_BACKQUOTE", 0, 0, pygame.K_BACKQUOTE],
            ["K_a", 0, 0, pygame.K_a],
            ["K_b", 0, 0, pygame.K_b],
            ["K_c", 0, 0, pygame.K_c],
            ["K_d", 0, 0, pygame.K_d],
            ["K_e", 0, 0, pygame.K_e],
            ["K_f", 0, 0, pygame.K_f],
            ["K_g", 0, 0, pygame.K_g],
            ["K_h", 0, 0, pygame.K_h],
            ["K_i", 0, 0, pygame.K_i],
            ["K_j", 0, 0, pygame.K_j],
            ["K_k", 0, 0, pygame.K_k],
            ["K_l", 0, 0, pygame.K_l],
            ["K_m", 0, 0, pygame.K_m],
            ["K_n", 0, 0, pygame.K_n],
            ["K_o", 0, 0, pygame.K_o],
            ["K_p", 0, 0, pygame.K_p],
            ["K_q", 0, 0, pygame.K_q],
            ["K_r", 0, 0, pygame.K_r],
            ["K_s", 0, 0, pygame.K_s],
            ["K_t", 0, 0, pygame.K_t],
            ["K_u", 0, 0, pygame.K_u],
            ["K_v", 0, 0, pygame.K_v],
            ["K_w", 0, 0, pygame.K_w],
            ["K_x", 0, 0, pygame.K_x],
            ["K_y", 0, 0, pygame.K_y],
            ["K_z", 0, 0, pygame.K_z],
            ["K_DELETE", 0, 0, pygame.K_DELETE],
            ["K_KP0", 0, 0, pygame.K_KP0],
            ["K_KP1", 0, 0, pygame.K_KP1],
            ["K_KP2", 0, 0, pygame.K_KP2],
            ["K_KP3", 0, 0, pygame.K_KP3],
            ["K_KP4", 0, 0, pygame.K_KP4],
            ["K_KP5", 0, 0, pygame.K_KP5],
            ["K_KP6", 0, 0, pygame.K_KP6],
            ["K_KP7", 0, 0, pygame.K_KP7],
            ["K_KP8", 0, 0, pygame.K_KP8],
            ["K_KP9", 0, 0, pygame.K_KP9],
            ["K_KP_PERIOD", 0, 0, pygame.K_KP_PERIOD],
            ["K_KP_DIVIDE", 0, 0, pygame.K_KP_DIVIDE],
            ["K_KP_MULTIPLY", 0, 0, pygame.K_KP_MULTIPLY],
            ["K_KP_MINUS", 0, 0, pygame.K_KP_MINUS],
            ["K_KP_PLUS", 0, 0, pygame.K_KP_PLUS],
            ["K_KP_ENTER", 0, 0, pygame.K_KP_ENTER],
            ["K_KP_EQUALS", 0, 0, pygame.K_KP_EQUALS],
            ["K_UP", 0, 0, pygame.K_UP],
            ["K_DOWN", 0, 0, pygame.K_DOWN],
            ["K_RIGHT", 0, 0, pygame.K_RIGHT],
            ["K_LEFT", 0, 0, pygame.K_LEFT],
            ["K_INSERT", 0, 0, pygame.K_INSERT],
            ["K_HOME", 0, 0, pygame.K_HOME],
            ["K_END", 0, 0, pygame.K_END],
            ["K_PAGEUP", 0, 0, pygame.K_PAGEUP],
            ["K_PAGEDOWN", 0, 0, pygame.K_PAGEDOWN],
            ["K_F1", 0, 0, pygame.K_F1],
            ["K_F2", 0, 0, pygame.K_F2],
            ["K_F3", 0, 0, pygame.K_F3],
            ["K_F4", 0, 0, pygame.K_F4],
            ["K_F5", 0, 0, pygame.K_F5],
            ["K_F6", 0, 0, pygame.K_F6],
            ["K_F7", 0, 0, pygame.K_F7],
            ["K_F8", 0, 0, pygame.K_F8],
            ["K_F9", 0, 0, pygame.K_F9],
            ["K_F10", 0, 0, pygame.K_F10],
            ["K_F11", 0, 0, pygame.K_F11],
            ["K_F12", 0, 0, pygame.K_F12],
            ["K_F13", 0, 0, pygame.K_F13],
            ["K_F14", 0, 0, pygame.K_F14],
            ["K_F15", 0, 0, pygame.K_F15],
            ["K_NUMLOCK", 0, 0, pygame.K_NUMLOCK],
            ["K_CAPSLOCK", 0, 0, pygame.K_CAPSLOCK],
            ["K_SCROLLOCK", 0, 0, pygame.K_SCROLLOCK],
            ["K_RSHIFT", 0, 0, pygame.K_RSHIFT],
            ["K_LSHIFT", 0, 0, pygame.K_LSHIFT],
            ["K_RCTRL", 0, 0, pygame.K_RCTRL],
            ["K_LCTRL", 0, 0, pygame.K_LCTRL],
            ["K_RALT", 0, 0, pygame.K_RALT],
            ["K_LALT", 0, 0, pygame.K_LALT],
            ["K_RMETA", 0, 0, pygame.K_RMETA],
            ["K_LMETA", 0, 0, pygame.K_LMETA],
            ["K_LSUPER", 0, 0, pygame.K_LSUPER],
            ["K_RSUPER", 0, 0, pygame.K_RSUPER],
            ["K_MODE", 0, 0, pygame.K_MODE],
            ["K_HELP", 0, 0, pygame.K_HELP],
            ["K_PRINT", 0, 0, pygame.K_PRINT],
            ["K_SYSREQ", 0, 0, pygame.K_SYSREQ],
            ["K_BREAK", 0, 0, pygame.K_BREAK],
            ["K_MENU", 0, 0, pygame.K_MENU],
            ["K_POWER", 0, 0, pygame.K_POWER],
            ["K_EURO", 0, 0, pygame.K_EURO],
            ["K_AC_BACK", 0, 0, pygame.K_AC_BACK]
        ]

    def update_keys(self):
        for i in self.keys:
            i[2] = i[1]

        for ce in self.game.events:
            for i in self.keys:
                if ce.type == pygame.KEYDOWN:
                    if ce.key == i[3]:
                        i[1] = 1
                elif ce.type == pygame.KEYUP:
                    if ce.key == i[3]:
                        i[1] = 0


    def check(self, key):
        for i in self.keys:
            if i[0] == key:
                return i[1]
        return False

    def check_pressed(self, key):
        for i in self.keys:
            if i[0] == key:
                return i[1] == 1 and i[2] == 0
        return False

    def check_released(self, key):
        for i in self.keys:
            if i[0] == key:
                return i[1] == 1 and i[2] == 0
        return False    

class map_manager:
    def __init__(self, game):
        self.game = game
        self.current_map = None
        self.all_maps = []

    
    def switch_map(self, new_map, destroy = True):
        for i in self.all_maps:
            if i.name == new_map:
                if destroy == True and self.current_map != None:
                    self.current_map.destroy_map()
                self.current_map = i
                self.current_map.create_map()

    def create_map(self, name, map_need, args, needed_files, width, height):
        self.all_maps.append(map_game(name, map_need, args, needed_files, width, height, self.game))

    def create_map_file(self, file):
        map_file = open(file, "r")

        lines = map_file.readlines()

        imports = []
        args = []
        properties = []
        objects = []

        #imports
        for i in range(0, len(lines)):
            if "@imports_start" in lines[i]:
                for b in range(i + 1, len(lines)):
                    if "@imports_end" in lines[b]:
                        break
                    else:
                        imports.append(lines[b].split('\n')[0])
                break

        #args
        for i in range(0, len(lines)):
            if "@args_start" in lines[i]:
                for b in range(i + 1, len(lines)):
                    if "@args_end" in lines[b]:
                        break
                    else:
                        args.append(lines[b].split('\n')[0])
                break
        
        #properties
        for i in range(0, len(lines)):
            if "@properties_start" in lines[i]:
                for b in range(i + 1, len(lines)):
                    if "@properties_end" in lines[b]:
                        break
                    else:
                        properties.append(lines[b].split('\n')[0])
                break

        #objects
        for i in range(0, len(lines)):
            if "@objects_start" in lines[i]:
                for b in range(i + 1, len(lines)):
                    if "@objects_end" in lines[b]:
                        break
                    elif lines[b] == '\n':
                        pass
                    else:
                        objects.append(lines[b].split('\n')[0])
                break

        map_file.close()

        self.all_maps.append(map_game(properties[0], objects, args, imports, int(properties[1]), int(properties[2]), self.game))

    def run_map(self):
        self.current_map.run_map()

class map_game:
    def __init__(self, name, map_need, args, needed_files, width, height, game):
        self.name = name
        self.game = game
        self.map_need = map_need
        self.args = args
        self.needed_files = needed_files
        self.map_objects = []
        self.width = width
        self.height = height
        self.add_buffer = []
        self.remove_buffer = []

    def create_map(self):
        execute_string = ""
        for i in self.needed_files:
            execute_string = execute_string + "import " + i + "\n"
        for i in self.map_need:
            execute_string = execute_string + "self.map_objects.append(" + i + ")\n"
        exec(execute_string)

    def destroy_map(self):
        for i in range(len(self.map_objects) - 1, -1, -1):
            self.map_objects.pop(i)

    def add_object(self, object_add, index):
        self.add_buffer.append([index, object_add])

    def remove_object(self, index):
        self.remove_buffer.append(index)

    def run_map(self):
        for i in range(0, len(self.map_objects)):
            self.map_objects[i].update(i)
            self.map_objects[i].instance_code() 
            self.map_objects[i].instance_draw() 

        for i in self.remove_buffer:
            self.map_objects[i] = 0

        while True:
            not_found = True
            for i in range(0, len(self.map_objects)):
                if self.map_objects[i] == 0:
                    self.map_objects.pop(i)
                    not_found = False
                    break
            if not_found:
                break

        self.remove_buffer = []

        for i in self.add_buffer:
            self.map_objects.insert(i[0], i[1])
        self.add_buffer = []

class sprite:
    def __init__(self, name, source_frames, fps, frame_index, game):
        self.name = name
        self.source_frames = source_frames
        self.fps = fps
        self.frame_index = frame_index
        self.frames = []
        self.counter = 0
        self.width = 0
        self.height = 0
        self.rect = None
        self.game = game
        self.init_sprite()

    def init_sprite(self):
        for i in self.source_frames:
            self.frames.append(pygame.image.load(i).convert_alpha())
        self.width = self.frames[0].get_size()[0]
        self.height = self.frames[0].get_size()[1]
        self.rect = self.frames[0].get_rect()

    def flip(self, horizontal, vertical):
        for i in range(0, len(self.frames)):
            self.frames[i] = pygame.transform.flip(self.frames[i], horizontal, vertical)
    
    def draw_sprite(self, x, y, viewport_number = 0, offset = [0, 0]):
        if self.fps != 0:
            if self.counter >= self.game.fps / self.fps:
                if self.frame_index < len(self.frames) - 1:
                    self.frame_index = self.frame_index + 1
                else: 
                    self.frame_index = 0
                self.counter = 0
            self.counter += 1
        self.game.screen.queue_for_blit(self.frames[self.frame_index], x, y, offset, False, self.name, viewport_number)

    def draw_sprite_gui(self, x, y, viewport_number = 0, offset = [0, 0]):
        if self.fps != 0:
            if self.counter >= self.game.fps / self.fps:
                if self.frame_index < len(self.frames) - 1:
                    self.frame_index = self.frame_index + 1
                else: 
                    self.frame_index = 0
                self.counter = 0
            self.counter += 1
        self.game.screen.queue_for_blit(self.frames[self.frame_index], x, y, offset, True, self.name, viewport_number)

class screen_manager:
    def __init__(self, window_name, resolution, game):
        self.game = game
        self.window = None
        self.window_name = window_name
        self.resolution = resolution
        self.viewports = [viewport(self.resolution, self.game), 0, 0, 0, 0, 0, 0, 0, 0, 0]
        self.init_window()

    def init_window(self): 
        pygame.init() 
        pygame.display.set_caption(self.window_name) 
        self.window = pygame.display.set_mode((self.resolution[0], self.resolution[1])) 

    def add_viewport(self, number):
        if self.viewports[number] == 0:
            self.viewports[number] = viewport(self.resolution, self.game)

    def remove_viewport(self, number):
        self.viewports[number] = 0

    def queue_for_blit(self, surface, x, y, offset, gui, name, viewport_number):
        self.viewports[viewport_number].queue_for_blit(surface, x, y, offset, gui, name)

    def draw(self):
        self.window.fill([0, 0, 0])
        for i in self.viewports:
            if i != 0:
                i.draw()
                self.window.blit(i.surface, (i.offset[0], i.offset[1]))
        pygame.display.update()

    def update_offset(self, x, y, viewport_number = 0):
        self.viewports[viewport_number].update_offset(x, y)

    def update_offset_non_gui(self, x, y, viewport_number = 0):
        self.viewports[viewport_number].update_offset_non_gui(x, y)

    def update_offset_gui(self, x, y, viewport_number = 0):
        self.viewports[viewport_number].update_offset_gui(x, y)

    def update_offset_name(self, x, y, name, viewport_number = 0):
        self.viewports[viewport_number].update_offset_name(x, y, name)

    def scale(self, width, height, viewport_number = 0):
        self.viewports[viewport_number].scale(width, height)

    def rotate(self, angle, viewport_number = 0):
        self.viewports[viewport_number].rotate(angle)

class viewport:
    def __init__(self, resolution, game):
        self.game = game
        self.blit_array = []
        self.offset = [0, 0]
        self.scale_amount = [resolution[0], resolution[1]]
        self.rotation_angle = 0
        self.resolution = resolution
        self.surface = pygame.Surface((resolution[0], resolution[1]))

    def queue_for_blit(self, surface, x, y, offset, gui, name):
        self.blit_array.append([surface, x, y, offset, gui, name])

    def draw(self):
        self.surface = pygame.Surface((self.resolution[0], self.resolution[1]))
        self.surface.fill((0, 0, 0))
        for i in self.blit_array:
            self.surface.blit(i[0], (i[1] + i[3][0], i[2] + i[3][1]))
        #self.surface = self.rotate_surface(self.surface, self.rotation_angle)
        self.surface = pygame.transform.scale(self.surface, (self.scale_amount[0], self.scale_amount[1]))
        self.offset[0] = (self.resolution[0] - self.scale_amount[0]) / 2
        self.offset[1] = (self.resolution[1] - self.scale_amount[1]) / 2
        self.blit_array = []

    def update_offset(self, x, y):
        for i in self.blit_array:
            i[1] -= x
            i[2] -= y

    def update_offset_non_gui(self, x, y):
        for i in self.blit_array:
            if not i[4]:
                i[1] -= x
                i[2] -= y

    def update_offset_gui(self, x, y):
        for i in self.blit_array:
            if i[4]:
                i[1] -= x
                i[2] -= y

    def update_offset_name(self, x, y, name):
        for i in self.blit_array:
            if i[5] == name:
                i[1] -= x
                i[2] -= y

    def scale_non_gui(self, width, height):
        pass

    def scale(self, width, height):
        self.scale_amount = [width, height]

    def rotate_surface(self, surface, angle):
        surface = pygame.transform.rotate(surface, angle)
        new_surface = pygame.Surface((self.resolution[0], self.resolution[1]))
        new_surface.blit(surface, (0, 0))
        return new_surface

    def rotate(self, angle):
        self.rotation_angle = angle

class obj:
    def __init__(self, name, x, y, visible, frozen, game):
        self.pos = 0

        self.game = game

        self.x = x
        self.y = y

        self.visible = visible
        self.frozen = frozen

        self.sprite = None

        rectangle = pygame.Rect(0, 0, 0, 0)
        self.collision = rectangle
        self.collision.center = (self.x + (rectangle[2] / 2), self.y + (rectangle[3] / 2))

        #ideally you have some string like 'current_instance.instance_code();current.instance_draw()
        self.inputarray = [""] #[misc_inputs]
        self.returnarray = ["", 0] #[misc_outputs, destroy]
        self.name = name

    def update_collision(self):
        rectangle = self.sprite.rect
        self.collision = rectangle 
        self.collision.center = (self.x + (rectangle[2] / 2), self.y + (rectangle[3] / 2))

    def update(self, position):
        self.pos = position 

    def instance_code(self): 
        pass

    def instance_draw(self):
        self.draw_self()

    def draw_self(self):
        if self.visible == True:
            self.sprite.draw_sprite(self.x, self.y)

    def draw_self_gui(self):
        if self.visible == True:
            self.sprite.draw_sprite_gui(self.x, self.y)

    def instance_edit_array(self, io, index, value): 
        if io == "i": 
            self.inputarray[index] = value  
        elif io == "o": 
            self.returnarray[index] = value 

    def instance_done(self): 
        return self.returnarray
    
    def instance_pre(self): 
        return self.inputarray 
    
    def colliding(self, x, y, rect):
        rectmodxy = [x, y, self.collision[2], self.collision[3]]
        return rect.colliderect(rectmodxy)
        
    def sign(self, just_a_number_smh): 
        if just_a_number_smh > 0: 
            return 1 
        elif just_a_number_smh < 0: 
            return -1 
        elif just_a_number_smh == 0: 
            return 0
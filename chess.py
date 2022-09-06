#libs
import sys, pygame
from typing import Tuple
import os.path
pygame.init()

#main
WINDOW_SIZE = (400, 400)
chess_width, chess_height = 30, 30
screen = pygame.display.set_mode(WINDOW_SIZE)

#assets
class Chessboard(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)

        self.possible_moves = []

        self.coords = {
        "A": [47, [47, 85, 125, 165, 205, 245, 285, 325]],
        "B": [85, [47, 85, 125, 165, 205, 245, 285, 325]],
        "C": [125, [47, 85, 125, 165, 205, 245, 285, 325]],
        "D": [165, [47, 85, 125, 165, 205, 245, 285, 325]],
        "E": [205, [47, 85, 125, 165, 205, 245, 285, 325]],
        "F": [245, [47, 85, 125, 165, 205, 245, 285, 325]],
        "G": [285, [47, 85, 125, 165, 205, 245, 285, 325]],
        "H": [325, [47, 85, 125, 165, 205, 245, 285, 325]],
        }

        self.chess_pos = {
            "wpawn1": (47, 285),
            "wpawn2": (85, 285),
            "wpawn3": (125, 285),
            "wpawn4": (165, 285),
            "wpawn5": (205, 285),
            "wpawn6": (245, 285),
            "wpawn7": (285, 285),
            "wpawn8": (325, 285),

            "wrook1": (47, 325),
            "wrook2": (325, 325),
            
            "wknight1": (85, 325),
            "wknight2": (285, 325),

            "wbishop1": (125, 325),
            "wbishop2": (245, 325),

            "wqueen": (165, 325),

            "wking": (205, 325),

            "bpawn1": (47,  85),
            "bpawn2": (85,  85),
            "bpawn3": (125, 85),
            "bpawn4": (165, 85),
            "bpawn5": (205, 85),
            "bpawn6": (245, 85),
            "bpawn7": (285, 85),
            "bpawn8": (325, 85),

            "brook1": (47, 47),
            "brook2": (325, 47),
            
            "bknight1": (85, 47),
            "bknight2": (285, 47),

            "bbishop1": (125, 47),
            "bbishop2": (245, 47),

            "bqueen": (165, 47),

            "bking": (205, 47),
        }

        self.__load_chessboard_image()
        self.render_chessboard()

        self.__load_chess_image()
        self.render_chess()

    def __load_chessboard_image(self):
        self.chessboard_image = pygame.image.load(str(os.path.curdir)+"\img\chessboard.webp")
        self.chessboard_image = pygame.transform.scale(self.chessboard_image, WINDOW_SIZE)

    def render_chessboard(self):
        self.chessboard_rect = self.chessboard_image.get_rect()
        screen.blit(self.chessboard_image, self.chessboard_rect)

    
    def __load_chess_image(self):
        self.wpawn_image = pygame.image.load(str(os.path.curdir)+"\img\pieces\wpawn.png")
        self.wpawn_image = pygame.transform.scale(self.wpawn_image, (chess_width, chess_height))


        self.bpawn_image = pygame.image.load(str(os.path.curdir)+"\img\pieces\\bpawn.png")
        self.bpawn_image = pygame.transform.scale(self.bpawn_image, (chess_width, chess_height))


        self.wrook_image = pygame.image.load(str(os.path.curdir)+"\img\pieces\wrook.png")
        self.wrook_image = pygame.transform.scale(self.wrook_image, (chess_width, chess_height))


        self.brook_image = pygame.image.load(str(os.path.curdir)+"\img\pieces\\brook.png")
        self.brook_image = pygame.transform.scale(self.brook_image, (chess_width, chess_height))


        self.wknight_image = pygame.image.load(str(os.path.curdir)+"\img\pieces\wknight.png")
        self.wknight_image = pygame.transform.scale(self.wknight_image, (chess_width, chess_height))


        self.bknight_image = pygame.image.load(str(os.path.curdir)+"\img\pieces\\bknight.png")
        self.bknight_image = pygame.transform.scale(self.bknight_image, (chess_width, chess_height))


        self.wbishop_image = pygame.image.load(str(os.path.curdir)+"\img\pieces\wbishop.png")
        self.wbishop_image = pygame.transform.scale(self.wbishop_image, (chess_width, chess_height))

        
        self.bbishop_image = pygame.image.load(str(os.path.curdir)+"\img\pieces\\bbishop.png")
        self.bbishop_image = pygame.transform.scale(self.bbishop_image, (chess_width, chess_height))


        self.wqueen_image = pygame.image.load(str(os.path.curdir)+"\img\pieces\wqueen.png")
        self.wqueen_image = pygame.transform.scale(self.wqueen_image, (chess_width, chess_height))


        self.bqueen_image = pygame.image.load(str(os.path.curdir)+"\img\pieces\\bqueen.png")
        self.bqueen_image = pygame.transform.scale(self.bqueen_image, (chess_width, chess_height))


        self.wking_image = pygame.image.load(str(os.path.curdir)+"\img\pieces\wking.png")
        self.wking_image = pygame.transform.scale(self.wking_image, (chess_width, chess_height))


        self.bking_image = pygame.image.load(str(os.path.curdir)+"\img\pieces\\bking.png")
        self.bking_image = pygame.transform.scale(self.bking_image, (chess_width, chess_height))

    
    def render_chess(self):
        self.rect_list = []

        self.bking_rect = pygame.Rect(self.chess_pos["bking"][0], self.chess_pos["bking"][1], chess_width, chess_height)
        self.wking_rect = pygame.Rect(self.chess_pos["wking"][0], self.chess_pos["wking"][1], chess_width, chess_height)
        self.bqueen_rect = pygame.Rect(self.chess_pos["bqueen"][0], self.chess_pos["bqueen"][1], chess_width, chess_height)
        self.wqueen_rect = pygame.Rect(self.chess_pos["wqueen"][0], self.chess_pos["wqueen"][1], chess_width, chess_height)
        self.bbishop1_rect = pygame.Rect(self.chess_pos["bbishop1"][0], self.chess_pos["bbishop1"][1], chess_width, chess_height)
        self.bbishop2_rect = pygame.Rect(self.chess_pos["bbishop2"][0], self.chess_pos["bbishop2"][1], chess_width, chess_height)
        self.wbishop1_rect = pygame.Rect(self.chess_pos["wbishop1"][0], self.chess_pos["wbishop1"][1], chess_width, chess_height)
        self.wbishop2_rect = pygame.Rect(self.chess_pos["wbishop2"][0], self.chess_pos["wbishop2"][1], chess_width, chess_height)
        self.bknight1_rect = pygame.Rect(self.chess_pos["bknight1"][0], self.chess_pos["bknight1"][1], chess_width, chess_height)
        self.bknight2_rect = pygame.Rect(self.chess_pos["bknight2"][0], self.chess_pos["bknight2"][1], chess_width, chess_height)
        self.wknight1_rect = pygame.Rect(self.chess_pos["wknight1"][0], self.chess_pos["wknight1"][1], chess_width, chess_height)
        self.wknight2_rect = pygame.Rect(self.chess_pos["wknight2"][0], self.chess_pos["wknight2"][1], chess_width, chess_height)
        self.brook1_rect = pygame.Rect(self.chess_pos["brook1"][0], self.chess_pos["brook1"][1], chess_width, chess_height)
        self.brook2_rect = pygame.Rect(self.chess_pos["brook2"][0], self.chess_pos["brook2"][1], chess_width, chess_height)
        self.wrook1_rect = pygame.Rect(self.chess_pos["wrook1"][0], self.chess_pos["wrook1"][1], chess_width, chess_height)
        self.wrook2_rect = pygame.Rect(self.chess_pos["wrook2"][0], self.chess_pos["wrook2"][1], chess_width, chess_height)
        self.bpawn1_rect = pygame.Rect(self.chess_pos["bpawn1"][0], self.chess_pos["bpawn1"][1], chess_width, chess_height)
        self.bpawn2_rect = pygame.Rect(self.chess_pos["bpawn2"][0], self.chess_pos["bpawn2"][1], chess_width, chess_height)
        self.bpawn3_rect = pygame.Rect(self.chess_pos["bpawn3"][0], self.chess_pos["bpawn3"][1], chess_width, chess_height)
        self.bpawn4_rect = pygame.Rect(self.chess_pos["bpawn4"][0], self.chess_pos["bpawn4"][1], chess_width, chess_height)
        self.bpawn5_rect = pygame.Rect(self.chess_pos["bpawn5"][0], self.chess_pos["bpawn5"][1], chess_width, chess_height)
        self.bpawn6_rect = pygame.Rect(self.chess_pos["bpawn6"][0], self.chess_pos["bpawn6"][1], chess_width, chess_height)
        self.bpawn7_rect = pygame.Rect(self.chess_pos["bpawn7"][0], self.chess_pos["bpawn7"][1], chess_width, chess_height)
        self.bpawn8_rect = pygame.Rect(self.chess_pos["bpawn8"][0], self.chess_pos["bpawn8"][1], chess_width, chess_height)
        self.wpawn1_rect = pygame.Rect(self.chess_pos["wpawn1"][0], self.chess_pos["wpawn1"][1], chess_width, chess_height)
        self.wpawn2_rect = pygame.Rect(self.chess_pos["wpawn2"][0], self.chess_pos["wpawn2"][1], chess_width, chess_height)
        self.wpawn3_rect = pygame.Rect(self.chess_pos["wpawn3"][0], self.chess_pos["wpawn3"][1], chess_width, chess_height)
        self.wpawn4_rect = pygame.Rect(self.chess_pos["wpawn4"][0], self.chess_pos["wpawn4"][1], chess_width, chess_height)
        self.wpawn5_rect = pygame.Rect(self.chess_pos["wpawn5"][0], self.chess_pos["wpawn5"][1], chess_width, chess_height)
        self.wpawn6_rect = pygame.Rect(self.chess_pos["wpawn6"][0], self.chess_pos["wpawn6"][1], chess_width, chess_height)
        self.wpawn7_rect = pygame.Rect(self.chess_pos["wpawn7"][0], self.chess_pos["wpawn7"][1], chess_width, chess_height)
        self.wpawn8_rect = pygame.Rect(self.chess_pos["wpawn8"][0], self.chess_pos["wpawn8"][1], chess_width, chess_height)

        self.rect_list.extend((
            self.wpawn1_rect,
            self.wpawn2_rect,
            self.wpawn3_rect,
            self.wpawn4_rect,
            self.wpawn5_rect,
            self.wpawn6_rect,
            self.wpawn7_rect,
            self.wpawn8_rect,

            self.bpawn1_rect,
            self.bpawn2_rect,
            self.bpawn3_rect,
            self.bpawn4_rect,
            self.bpawn5_rect,
            self.bpawn6_rect,
            self.bpawn7_rect,
            self.bpawn8_rect,

            self.wrook1_rect,
            self.wrook2_rect,

            self.brook1_rect,
            self.brook2_rect,

            self.wknight1_rect,
            self.wknight2_rect,            
            
            self.bknight1_rect,            
            self.bknight2_rect,
            
            self.wbishop1_rect,            
            self.wbishop2_rect,        
            
            self.bbishop1_rect,        
            self.bbishop2_rect,

            self.wqueen_rect,            
            
            self.bqueen_rect,        

            self.wking_rect,            
            
            self.bking_rect,        
            
            ))

        screen.blit(self.wpawn_image, self.wpawn1_rect)
        screen.blit(self.wpawn_image, self.wpawn2_rect)
        screen.blit(self.wpawn_image, self.wpawn3_rect)
        screen.blit(self.wpawn_image, self.wpawn4_rect)
        screen.blit(self.wpawn_image, self.wpawn5_rect)
        screen.blit(self.wpawn_image, self.wpawn6_rect)
        screen.blit(self.wpawn_image, self.wpawn7_rect)
        screen.blit(self.wpawn_image, self.wpawn8_rect)

        screen.blit(self.bpawn_image, self.bpawn1_rect)
        screen.blit(self.bpawn_image, self.bpawn2_rect)
        screen.blit(self.bpawn_image, self.bpawn3_rect)
        screen.blit(self.bpawn_image, self.bpawn4_rect)
        screen.blit(self.bpawn_image, self.bpawn5_rect)
        screen.blit(self.bpawn_image, self.bpawn6_rect)
        screen.blit(self.bpawn_image, self.bpawn7_rect)
        screen.blit(self.bpawn_image, self.bpawn8_rect)

        screen.blit(self.wrook_image, self.wrook1_rect)
        screen.blit(self.wrook_image, self.wrook2_rect)

        screen.blit(self.brook_image, self.brook1_rect)
        screen.blit(self.brook_image, self.brook2_rect)

        screen.blit(self.wknight_image, self.wknight1_rect)
        screen.blit(self.wknight_image, self.wknight2_rect)

        screen.blit(self.bknight_image, self.bknight1_rect)
        screen.blit(self.bknight_image, self.bknight2_rect)

        screen.blit(self.wbishop_image, self.wbishop1_rect)
        screen.blit(self.wbishop_image, self.wbishop2_rect)

        screen.blit(self.bbishop_image, self.bbishop1_rect)
        screen.blit(self.bbishop_image, self.bbishop2_rect)

        screen.blit(self.wqueen_image, self.wqueen_rect)

        screen.blit(self.bqueen_image, self.bqueen_rect)

        screen.blit(self.wking_image, self.wking_rect)

        screen.blit(self.bking_image, self.bking_rect)
    
    def choose_chess(self, chosen_chess : pygame.Rect):
        self.pawn_start_pos = {
            "wpawn1": (47, 285),
            "wpawn2": (85, 285),
            "wpawn3": (125, 285),
            "wpawn4": (165, 285),
            "wpawn5": (205, 285),
            "wpawn6": (245, 285),
            "wpawn7": (285, 285),
            "wpawn8": (325, 285),
            "bpawn1": (47,  85),
            "bpawn2": (85,  85),
            "bpawn3": (125, 85),
            "bpawn4": (165, 85),
            "bpawn5": (205, 85),
            "bpawn6": (245, 85),
            "bpawn7": (285, 85),
            "bpawn8": (325, 85)
        }

        self.chess_name = ""

        #Get clicked chess's name
        for chess in self.chess_pos.keys():
            if chosen_chess[0] == self.chess_pos[chess][0] and chosen_chess[1] == self.chess_pos[chess][1]:
                self.chess_name = chess
                pygame.draw.rect(screen, (0, 255, 0), pygame.Rect(chosen_chess[0], chosen_chess[1], 5, 30), border_radius=5)
                break
        
        #White Pawn
        if self.chess_name.startswith("wpawn"):
            self.wpawn(chosen_chess)
        
        #Black Pawn
        if self.chess_name.startswith("bpawn"):
            self.bpawn(chosen_chess)
    
        #White Rook
        if self.chess_name.startswith("wrook"):
            self.wrook(chosen_chess)

    def move_chess(self, dest : Tuple):
        old_pos = self.chess_pos[self.chess_name]
        print(self.chess_name)
        print(self.possible_moves)
        #self.calculate_field(dest)
        if self.calculate_field(dest) in self.possible_moves:
            self.chess_pos[self.chess_name] = self.calculate_field(dest)

        if old_pos == self.chess_pos[self.chess_name]:
            print("Not Moved!")
        else:
            print("Moved!")
        
        self.update()
    
    def calculate_field(self, pos : Tuple):
        posx = 0
        posy = 0
        possible_numbers = []
        for column in self.coords.keys():
            possible_numbers.append(self.coords[column][0])
        posx = min(possible_numbers, key=lambda x:abs(x-pos[0]))
        posy = min(possible_numbers, key=lambda x:abs(x-pos[1]))

        return (posx, posy)

    def update(self):
        global is_chess_chosen
        global chosen_chess_rect
        self.render_chessboard()
        self.render_chess()
        self.possible_moves.clear()
        is_chess_chosen = False
        chosen_chess_rect = ""

    def wpawn(self, chosen_chess : pygame.Rect):
        bpawn_front = False
        bpawn_front_name = ""
        try:
            bpawn_front = list(self.chess_pos.keys())[list(self.chess_pos.values()).index(self.calculate_field((chosen_chess[0], chosen_chess[1]-40)))].startswith("b")
            bpawn_front_name = list(self.chess_pos.keys())[list(self.chess_pos.values()).index(self.calculate_field((chosen_chess[0], chosen_chess[1]-40)))]
        except ValueError:
            pass

        #First Time
        if not bpawn_front:
            try:
                if chosen_chess[0] == self.pawn_start_pos[self.chess_name][0] and chosen_chess[1] == self.pawn_start_pos[self.chess_name][1]:
                    self.possible_moves.append(self.calculate_field((chosen_chess[0], chosen_chess[1]-40)))
                    self.possible_moves.append(self.calculate_field((chosen_chess[0], chosen_chess[1]-80)))

                    pygame.draw.rect(screen, (0, 255, 0), pygame.Rect(chosen_chess[0], chosen_chess[1]-40, chosen_chess[2], chosen_chess[3]))
                    pygame.draw.rect(screen, (0, 255, 0), pygame.Rect(chosen_chess[0], chosen_chess[1]-80, chosen_chess[2], chosen_chess[3]))
                
                #Other times :p
                else:
                    self.possible_moves.append(self.calculate_field((chosen_chess[0], chosen_chess[1]-40)))
                    pygame.draw.rect(screen, (0, 255, 0), pygame.Rect(chosen_chess[0], chosen_chess[1]-40, chosen_chess[2], chosen_chess[3]))
            except ValueError:
                pass
            except IndexError:
                pass
        
        bpawn_front_pos = (0, 0)
        try:
            bpawn_front_pos = self.chess_pos[bpawn_front_name]
        except KeyError:
            pass

        #Check if enemy on top-left
        try:
            if list(self.chess_pos.keys())[list(self.chess_pos.values()).index(self.calculate_field((chosen_chess[0]-40, chosen_chess[1]-40)))].startswith("b"):
                calculated_field = self.calculate_field((chosen_chess[0]-40, chosen_chess[1]-40))
                if bpawn_front_pos != calculated_field:
                    self.possible_moves.append(calculated_field)
                    pygame.draw.rect(screen, (0, 255, 0), pygame.Rect(calculated_field[0], calculated_field[1], chosen_chess[2], chosen_chess[3]))
        except ValueError:
            pass
        except IndexError:
            pass
        #Check if enemy on top-right
        try:
            if list(self.chess_pos.keys())[list(self.chess_pos.values()).index(self.calculate_field((chosen_chess[0]+40, chosen_chess[1]-40)))].startswith("b"):
                calculated_field = self.calculate_field((chosen_chess[0]+40, chosen_chess[1]-40))                             
                if  bpawn_front_pos != calculated_field:
                    self.possible_moves.append(calculated_field)
                    pygame.draw.rect(screen, (0, 255, 0), pygame.Rect(calculated_field[0], calculated_field[1], chosen_chess[2], chosen_chess[3]))
        except ValueError:
            pass
        except IndexError:
            pass

    def bpawn(self, chosen_chess : pygame.Rect):
        wpawn_front = False
        wpawn_front_name = ""
        try:
            wpawn_front = list(self.chess_pos.keys())[list(self.chess_pos.values()).index(self.calculate_field((chosen_chess[0], chosen_chess[1]+40)))].startswith("w")
            wpawn_front_name = list(self.chess_pos.keys())[list(self.chess_pos.values()).index(self.calculate_field((chosen_chess[0], chosen_chess[1]+40)))]
        except ValueError:
            pass

        #First Time
        if not wpawn_front:
            try:
                if chosen_chess[0] == self.pawn_start_pos[self.chess_name][0] and chosen_chess[1] == self.pawn_start_pos[self.chess_name][1]:
                    self.possible_moves.append(self.calculate_field((chosen_chess[0], chosen_chess[1]+40)))
                    self.possible_moves.append(self.calculate_field((chosen_chess[0], chosen_chess[1]+80)))

                    pygame.draw.rect(screen, (0, 255, 0), pygame.Rect(chosen_chess[0], chosen_chess[1]+40, chosen_chess[2], chosen_chess[3]))
                    pygame.draw.rect(screen, (0, 255, 0), pygame.Rect(chosen_chess[0], chosen_chess[1]+80, chosen_chess[2], chosen_chess[3]))
                
                #Other times :p
                else:
                    self.possible_moves.append(self.calculate_field((chosen_chess[0], chosen_chess[1]+40)))
                    pygame.draw.rect(screen, (0, 255, 0), pygame.Rect(chosen_chess[0], chosen_chess[1]+40, chosen_chess[2], chosen_chess[3]))
            except ValueError:
                pass
            except IndexError:
                pass


        wpawn_front_pos = (0, 0)
        try:
            wpawn_front_pos = self.chess_pos[wpawn_front_name]
        except KeyError:
            pass
        #Check if enemy on top-left
        try:
            if list(self.chess_pos.keys())[list(self.chess_pos.values()).index(self.calculate_field((chosen_chess[0]+40, chosen_chess[1]+40)))].startswith("w"):
                calculated_field = self.calculate_field((chosen_chess[0]+40, chosen_chess[1]+40))
                if wpawn_front_pos != calculated_field:
                    self.possible_moves.append(calculated_field)
                    pygame.draw.rect(screen, (0, 255, 0), pygame.Rect(calculated_field[0], calculated_field[1], chosen_chess[2], chosen_chess[3]))
        except ValueError:
            pass
        except IndexError:
            pass
        #Check if enemy on top-right
        try:
            if list(self.chess_pos.keys())[list(self.chess_pos.values()).index(self.calculate_field((chosen_chess[0]-40, chosen_chess[1]+40)))].startswith("w"):
                calculated_field = self.calculate_field((chosen_chess[0]-40, chosen_chess[1]+40))
                if wpawn_front_pos != calculated_field:
                    self.possible_moves.append(calculated_field)
                    pygame.draw.rect(screen, (0, 255, 0), pygame.Rect(calculated_field[0], calculated_field[1], chosen_chess[2], chosen_chess[3]))
        except ValueError:
            pass
        except IndexError:
            pass

    def wrook(self, chosen_chess : pygame.Rect):
        pass



chessboard = Chessboard()
is_chess_chosen = False
chosen_chess_rect = ""
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == pygame.MOUSEBUTTONUP:
            pos = pygame.mouse.get_pos()
            
            #fix wrong mouse pos
            pos = (pos[0]-10, pos[1]-10)

            # get a list of all sprites that are under the mouse cursor
            clicked_sprites = [s for s in chessboard.rect_list if s.collidepoint(pos)]

#First Issue
            if len(clicked_sprites) > 0:
                if not is_chess_chosen:
                    is_chess_chosen = True
                    chosen_chess_rect = clicked_sprites[0]
                    chessboard.choose_chess(chosen_chess_rect)
                
                elif is_chess_chosen and clicked_sprites[0] == chosen_chess_rect:
                    is_chess_chosen = False
                    chessboard.update()
            
            elif is_chess_chosen:
                is_chess_chosen = False
                chosen_chess_rect = ""
                chessboard.move_chess(pos)


    pygame.display.flip()
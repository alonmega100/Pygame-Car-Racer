from utils import *

NUM_OF_MUTATIONS = 10
MAX_VEL = 50
ROTATION_VEL = 5
NUM_OF_RANDOM_CARS_IN_GENERATION = 3
TRACK_LINES = [((35, 130), (35, 650)), ((35, 650), (160, 770)), ((160, 770), (670, 770)), ((670, 770), (760, 640)),
                   ((760, 640), (760, 110)), ((760, 110), (760, 20)), ((760, 20), (370, 20)), ((170, 120), (170, 600)),
                   ((170, 600), (240, 660)), ((240, 660), (580, 670)), ((580, 670), (660, 590)),
                   ((660, 590), (660, 190)),
                   ((35, 130), (35, 20)), ((35, 20), (300, 20)), ((300, 20), (300, 110)), ((300, 110), (300, 510)),
                   ((370, 20), (370, 90)), ((370, 90), (370, 240)), ((370, 240), (420, 240)), ((420, 240), (500, 240)),
                   ((660, 190), (660, 130)), ((660, 130), (500, 130)), ((500, 240), (560, 240)),
                   ((560, 240), (560, 510)),
                   ((560, 510), (500, 560)), ((500, 560), (330, 560)), ((330, 560), (300, 510))]

BONUS_LINES = [((500, 129), (500, 25)), ((374, 132), (501, 132)), ((500, 242), (500, 133)), ((540, 240), (540, 135)),
               ((562, 253), (658, 253)), ((561, 304), (657, 304)), ((566, 370), (660, 370)), ((561, 438), (658, 438)),
               ((563, 510), (658, 523)),
               ((534, 541), (620, 623)), ((464, 567), (464, 660)), ((354, 564), (354, 659)), ((316, 545), (212, 627)),
               ((174, 500), (297, 500)), ((294, 415), (170, 415)),((294, 300), (170, 300)), ((173, 220), (296, 220)), ((170, 120), (290, 120)),
               ((170, 120), (170, 20)), ((40, 160), (170, 160)), ((40, 250), (167, 250)), ((167, 330), (38, 330)),
               ((37, 427), (165, 427)), ((167, 560), (37, 560)), ((190, 621), (100, 708)), ((252, 662), (252, 769)),
               ((344, 666), (344, 764)), ((420, 667), (420, 764)), ((535, 673), (535, 767)), ((582, 672), (671, 768)),
               ((627, 626), (717, 692)), ((660, 590), (760, 641)), ((662, 500), (762, 500)), ((662, 402), (750, 402)),
               ((660, 300), (760, 300)), ((661, 220), (759, 220)), ((662, 150), (758, 150)), ((760, 20), (660, 130)),
               ((650, 130), (650, 25)), ((600, 22), (600, 126))]

RED_CAR = scale_image(pygame.image.load("imgs/red-car.png"), 0.45)

WIN = pygame.display.set_mode((810, 810))

pygame.display.set_caption("Racing Game!")

FPS = 60

INPUT_LAYER_SHAPE = (12, 1)

WI_SHAPE = (6, 12)
BI_SHAPE = (1, 6)

W1_SHAPE = (4, 6)
B1_SHAPE = (1, 4)


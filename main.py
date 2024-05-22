import pygame, sys
from fighter import Fighter
from pygame import mixer
from menubtn import Pindot

pygame.init()

# Utils
WIDTH = 1000
HEIGHT = 600
FPS = 50
clock = pygame.time.Clock()

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Pixel Duels")

# Music 
pygame.mixer.music.load("pixel-duel-main/audio/background.ogg")
pygame.mixer.music.set_volume(0.7)
pygame.mixer.music.play(-1, 0.0, 5000)

slash_fx = pygame.mixer.Sound("pixel-duel-main/audio/slash.wav")
slash_fx.set_volume(0.2)

# Introduction delay
intro_countdown = 3
last_countdown = pygame.time.get_ticks()

# Map / Background
castle_bg = pygame.image.load("pixel-duel-main/assets/background/castle-bridge.png").convert_alpha()

# Character assets
# Golem
# Fire 
fire_golem_idle_1 = pygame.image.load("pixel-duel-main/assets/sprites/fire-golem/idle/0_Golem_Idle_000.png")
fire_golem_idle_2 = pygame.image.load("pixel-duel-main/assets/sprites/fire-golem/idle/0_Golem_Idle_001.png")
fire_golem_idle_3 = pygame.image.load("pixel-duel-main/assets/sprites/fire-golem/idle/0_Golem_Idle_002.png")
fire_golem_idle_4 = pygame.image.load("pixel-duel-main/assets/sprites/fire-golem/idle/0_Golem_Idle_003.png")
fire_golem_idle_5 = pygame.image.load("pixel-duel-main/assets/sprites/fire-golem/idle/0_Golem_Idle_004.png")
fire_golem_idle_6 = pygame.image.load("pixel-duel-main/assets/sprites/fire-golem/idle/0_Golem_Idle_005.png")
fire_golem_idle_7 = pygame.image.load("pixel-duel-main/assets/sprites/fire-golem/idle/0_Golem_Idle_006.png")
fire_golem_idle_8 = pygame.image.load("pixel-duel-main/assets/sprites/fire-golem/idle/0_Golem_Idle_007.png")
fire_golem_idle_9 = pygame.image.load("pixel-duel-main/assets/sprites/fire-golem/idle/0_Golem_Idle_008.png")
fire_golem_idle_10 = pygame.image.load("pixel-duel-main/assets/sprites/fire-golem/idle/0_Golem_Idle_009.png")
fire_golem_idle_11 = pygame.image.load("pixel-duel-main/assets/sprites/fire-golem/idle/0_Golem_Idle_010.png")
fire_golem_idle_12 = pygame.image.load("pixel-duel-main/assets/sprites/fire-golem/idle/0_Golem_Idle_011.png")
fire_golem_idle_13 = pygame.image.load("pixel-duel-main/assets/sprites/fire-golem/idle/0_Golem_Idle_012.png")
fire_golem_idle_14 = pygame.image.load("pixel-duel-main/assets/sprites/fire-golem/idle/0_Golem_Idle_013.png")
fire_golem_idle_15 = pygame.image.load("pixel-duel-main/assets/sprites/fire-golem/idle/0_Golem_Idle_014.png")
fire_golem_idle_16 = pygame.image.load("pixel-duel-main/assets/sprites/fire-golem/idle/0_Golem_Idle_015.png")
fire_golem_idle_17 = pygame.image.load("pixel-duel-main/assets/sprites/fire-golem/idle/0_Golem_Idle_016.png")
fire_golem_idle_18 = pygame.image.load("pixel-duel-main/assets/sprites/fire-golem/idle/0_Golem_Idle_017.png")
fire_golem_idle_list = [fire_golem_idle_1, fire_golem_idle_2, fire_golem_idle_3, fire_golem_idle_4, fire_golem_idle_5, fire_golem_idle_6, fire_golem_idle_7, fire_golem_idle_8, fire_golem_idle_9, fire_golem_idle_10, fire_golem_idle_11, fire_golem_idle_12, fire_golem_idle_13, fire_golem_idle_14, fire_golem_idle_1, fire_golem_idle_15, fire_golem_idle_16, fire_golem_idle_17]

fire_golem_running_1 = pygame.image.load("pixel-duel-main/assets/sprites/fire-golem/running/0_Golem_Running_000.png")
fire_golem_running_2 = pygame.image.load("pixel-duel-main/assets/sprites/fire-golem/running/0_Golem_Running_001.png")
fire_golem_running_3 = pygame.image.load("pixel-duel-main/assets/sprites/fire-golem/running/0_Golem_Running_002.png")
fire_golem_running_4 = pygame.image.load("pixel-duel-main/assets/sprites/fire-golem/running/0_Golem_Running_003.png")
fire_golem_running_5 = pygame.image.load("pixel-duel-main/assets/sprites/fire-golem/running/0_Golem_Running_004.png")
fire_golem_running_6 = pygame.image.load("pixel-duel-main/assets/sprites/fire-golem/running/0_Golem_Running_005.png")
fire_golem_running_7 = pygame.image.load("pixel-duel-main/assets/sprites/fire-golem/running/0_Golem_Running_006.png")
fire_golem_running_8 = pygame.image.load("pixel-duel-main/assets/sprites/fire-golem/running/0_Golem_Running_007.png")
fire_golem_running_9 = pygame.image.load("pixel-duel-main/assets/sprites/fire-golem/running/0_Golem_Running_008.png")
fire_golem_running_10 = pygame.image.load("pixel-duel-main/assets/sprites/fire-golem/running/0_Golem_Running_009.png")
fire_golem_running_11 = pygame.image.load("pixel-duel-main/assets/sprites/fire-golem/running/0_Golem_Running_010.png")
fire_golem_running_list = [fire_golem_running_1, fire_golem_running_2, fire_golem_running_3, fire_golem_running_4, fire_golem_running_5, fire_golem_running_6, fire_golem_running_7, fire_golem_running_8, fire_golem_running_9, fire_golem_running_10, fire_golem_running_11]

fire_golem_attacking_1 = pygame.image.load("pixel-duel-main/assets/sprites/fire-golem/attacking/0_Golem_Slashing_000.png")
fire_golem_attacking_2 = pygame.image.load("pixel-duel-main/assets/sprites/fire-golem/attacking/0_Golem_Slashing_001.png")
fire_golem_attacking_3 = pygame.image.load("pixel-duel-main/assets/sprites/fire-golem/attacking/0_Golem_Slashing_002.png")
fire_golem_attacking_4 = pygame.image.load("pixel-duel-main/assets/sprites/fire-golem/attacking/0_Golem_Slashing_003.png")
fire_golem_attacking_5 = pygame.image.load("pixel-duel-main/assets/sprites/fire-golem/attacking/0_Golem_Slashing_004.png")
fire_golem_attacking_6 = pygame.image.load("pixel-duel-main/assets/sprites/fire-golem/attacking/0_Golem_Slashing_005.png")
fire_golem_attacking_7 = pygame.image.load("pixel-duel-main/assets/sprites/fire-golem/attacking/0_Golem_Slashing_006.png")
fire_golem_attacking_8 = pygame.image.load("pixel-duel-main/assets/sprites/fire-golem/attacking/0_Golem_Slashing_007.png")
fire_golem_attacking_9 = pygame.image.load("pixel-duel-main/assets/sprites/fire-golem/attacking/0_Golem_Slashing_008.png")
fire_golem_attacking_10 = pygame.image.load("pixel-duel-main/assets/sprites/fire-golem/attacking/0_Golem_Slashing_009.png")
fire_golem_attacking_11 = pygame.image.load("pixel-duel-main/assets/sprites/fire-golem/attacking/0_Golem_Slashing_010.png")
fire_golem_attacking_list = [fire_golem_attacking_1, fire_golem_attacking_2, fire_golem_attacking_3, fire_golem_attacking_4, fire_golem_attacking_5, fire_golem_attacking_6, fire_golem_attacking_7, fire_golem_attacking_8, fire_golem_attacking_9, fire_golem_attacking_10, fire_golem_attacking_11]

fire_golem_hurt_1 = pygame.image.load("pixel-duel-main/assets/sprites/fire-golem/hurt/0_Golem_Hurt_000.png")
fire_golem_hurt_2 = pygame.image.load("pixel-duel-main/assets/sprites/fire-golem/hurt/0_Golem_Hurt_001.png")
fire_golem_hurt_3 = pygame.image.load("pixel-duel-main/assets/sprites/fire-golem/hurt/0_Golem_Hurt_002.png")
fire_golem_hurt_4 = pygame.image.load("pixel-duel-main/assets/sprites/fire-golem/hurt/0_Golem_Hurt_003.png")
fire_golem_hurt_5 = pygame.image.load("pixel-duel-main/assets/sprites/fire-golem/hurt/0_Golem_Hurt_004.png")
fire_golem_hurt_6 = pygame.image.load("pixel-duel-main/assets/sprites/fire-golem/hurt/0_Golem_Hurt_005.png")
fire_golem_hurt_7 = pygame.image.load("pixel-duel-main/assets/sprites/fire-golem/hurt/0_Golem_Hurt_006.png")
fire_golem_hurt_8 = pygame.image.load("pixel-duel-main/assets/sprites/fire-golem/hurt/0_Golem_Hurt_007.png")
fire_golem_hurt_9 = pygame.image.load("pixel-duel-main/assets/sprites/fire-golem/hurt/0_Golem_Hurt_008.png")
fire_golem_hurt_10 = pygame.image.load("pixel-duel-main/assets/sprites/fire-golem/hurt/0_Golem_Hurt_009.png")
fire_golem_hurt_11 = pygame.image.load("pixel-duel-main/assets/sprites/fire-golem/hurt/0_Golem_Hurt_010.png")
fire_golem_hurt_12 = pygame.image.load("pixel-duel-main/assets/sprites/fire-golem/hurt/0_Golem_Hurt_011.png")
fire_golem_hurt_list = [fire_golem_hurt_1, fire_golem_hurt_2, fire_golem_hurt_3, fire_golem_hurt_4, fire_golem_hurt_5, fire_golem_hurt_6, fire_golem_hurt_7, fire_golem_hurt_8, fire_golem_hurt_9, fire_golem_hurt_10, fire_golem_hurt_11, fire_golem_hurt_12]

fire_golem_dead_1 = pygame.image.load("pixel-duel-main/assets/sprites/fire-golem/dead/0_Golem_Dying_000.png")
fire_golem_dead_2 = pygame.image.load("pixel-duel-main/assets/sprites/fire-golem/dead/0_Golem_Dying_001.png")
fire_golem_dead_3 = pygame.image.load("pixel-duel-main/assets/sprites/fire-golem/dead/0_Golem_Dying_002.png")
fire_golem_dead_4 = pygame.image.load("pixel-duel-main/assets/sprites/fire-golem/dead/0_Golem_Dying_003.png")
fire_golem_dead_5 = pygame.image.load("pixel-duel-main/assets/sprites/fire-golem/dead/0_Golem_Dying_004.png")
fire_golem_dead_6 = pygame.image.load("pixel-duel-main/assets/sprites/fire-golem/dead/0_Golem_Dying_005.png")
fire_golem_dead_7 = pygame.image.load("pixel-duel-main/assets/sprites/fire-golem/dead/0_Golem_Dying_006.png")
fire_golem_dead_8 = pygame.image.load("pixel-duel-main/assets/sprites/fire-golem/dead/0_Golem_Dying_007.png")
fire_golem_dead_9 = pygame.image.load("pixel-duel-main/assets/sprites/fire-golem/dead/0_Golem_Dying_008.png")
fire_golem_dead_10 = pygame.image.load("pixel-duel-main/assets/sprites/fire-golem/dead/0_Golem_Dying_009.png")
fire_golem_dead_11 = pygame.image.load("pixel-duel-main/assets/sprites/fire-golem/dead/0_Golem_Dying_010.png")
fire_golem_dead_12 = pygame.image.load("pixel-duel-main/assets/sprites/fire-golem/dead/0_Golem_Dying_011.png")
fire_golem_dead_13 = pygame.image.load("pixel-duel-main/assets/sprites/fire-golem/dead/0_Golem_Dying_012.png")
fire_golem_dead_14 = pygame.image.load("pixel-duel-main/assets/sprites/fire-golem/dead/0_Golem_Dying_013.png")
fire_golem_dead_15 = pygame.image.load("pixel-duel-main/assets/sprites/fire-golem/dead/0_Golem_Dying_014.png")
fire_golem_dead_list = [fire_golem_dead_1, fire_golem_dead_2, fire_golem_dead_3, fire_golem_dead_4, fire_golem_dead_5, fire_golem_dead_6, fire_golem_dead_7, fire_golem_dead_8, fire_golem_dead_9, fire_golem_dead_10, fire_golem_dead_11, fire_golem_dead_12, fire_golem_dead_13, fire_golem_dead_14, fire_golem_dead_15]

# Nature
nature_golem_idle_1 = pygame.image.load("pixel-duel-main/assets/sprites/nature-golem/idle/0_Golem_Idle_000.png")
nature_golem_idle_2 = pygame.image.load("pixel-duel-main/assets/sprites/nature-golem/idle/0_Golem_Idle_001.png")
nature_golem_idle_3 = pygame.image.load("pixel-duel-main/assets/sprites/nature-golem/idle/0_Golem_Idle_002.png")
nature_golem_idle_4 = pygame.image.load("pixel-duel-main/assets/sprites/nature-golem/idle/0_Golem_Idle_003.png")
nature_golem_idle_5 = pygame.image.load("pixel-duel-main/assets/sprites/nature-golem/idle/0_Golem_Idle_004.png")
nature_golem_idle_6 = pygame.image.load("pixel-duel-main/assets/sprites/nature-golem/idle/0_Golem_Idle_005.png")
nature_golem_idle_7 = pygame.image.load("pixel-duel-main/assets/sprites/nature-golem/idle/0_Golem_Idle_006.png")
nature_golem_idle_8 = pygame.image.load("pixel-duel-main/assets/sprites/nature-golem/idle/0_Golem_Idle_007.png")
nature_golem_idle_9 = pygame.image.load("pixel-duel-main/assets/sprites/nature-golem/idle/0_Golem_Idle_008.png")
nature_golem_idle_10 = pygame.image.load("pixel-duel-main/assets/sprites/nature-golem/idle/0_Golem_Idle_009.png")
nature_golem_idle_11 = pygame.image.load("pixel-duel-main/assets/sprites/nature-golem/idle/0_Golem_Idle_010.png")
nature_golem_idle_12 = pygame.image.load("pixel-duel-main/assets/sprites/nature-golem/idle/0_Golem_Idle_011.png")
nature_golem_idle_13 = pygame.image.load("pixel-duel-main/assets/sprites/nature-golem/idle/0_Golem_Idle_012.png")
nature_golem_idle_14 = pygame.image.load("pixel-duel-main/assets/sprites/nature-golem/idle/0_Golem_Idle_013.png")
nature_golem_idle_15 = pygame.image.load("pixel-duel-main/assets/sprites/nature-golem/idle/0_Golem_Idle_014.png")
nature_golem_idle_16 = pygame.image.load("pixel-duel-main/assets/sprites/nature-golem/idle/0_Golem_Idle_015.png")
nature_golem_idle_17 = pygame.image.load("pixel-duel-main/assets/sprites/nature-golem/idle/0_Golem_Idle_016.png")
nature_golem_idle_18 = pygame.image.load("pixel-duel-main/assets/sprites/nature-golem/idle/0_Golem_Idle_017.png")
nature_golem_idle_list = [nature_golem_idle_1, nature_golem_idle_2, nature_golem_idle_3, nature_golem_idle_4, nature_golem_idle_5, nature_golem_idle_6, nature_golem_idle_7, nature_golem_idle_8, nature_golem_idle_9, nature_golem_idle_10, nature_golem_idle_11, nature_golem_idle_12, nature_golem_idle_13, nature_golem_idle_14, nature_golem_idle_1, nature_golem_idle_15, nature_golem_idle_16, nature_golem_idle_17]

nature_golem_running_1 = pygame.image.load("pixel-duel-main/assets/sprites/nature-golem/running/0_Golem_Running_000.png")
nature_golem_running_2 = pygame.image.load("pixel-duel-main/assets/sprites/nature-golem/running/0_Golem_Running_001.png")
nature_golem_running_3 = pygame.image.load("pixel-duel-main/assets/sprites/nature-golem/running/0_Golem_Running_002.png")
nature_golem_running_4 = pygame.image.load("pixel-duel-main/assets/sprites/nature-golem/running/0_Golem_Running_003.png")
nature_golem_running_5 = pygame.image.load("pixel-duel-main/assets/sprites/nature-golem/running/0_Golem_Running_004.png")
nature_golem_running_6 = pygame.image.load("pixel-duel-main/assets/sprites/nature-golem/running/0_Golem_Running_005.png")
nature_golem_running_7 = pygame.image.load("pixel-duel-main/assets/sprites/nature-golem/running/0_Golem_Running_006.png")
nature_golem_running_8 = pygame.image.load("pixel-duel-main/assets/sprites/nature-golem/running/0_Golem_Running_007.png")
nature_golem_running_9 = pygame.image.load("pixel-duel-main/assets/sprites/nature-golem/running/0_Golem_Running_008.png")
nature_golem_running_10 = pygame.image.load("pixel-duel-main/assets/sprites/nature-golem/running/0_Golem_Running_009.png")
nature_golem_running_11 = pygame.image.load("pixel-duel-main/assets/sprites/nature-golem/running/0_Golem_Running_010.png")
nature_golem_running_list = [nature_golem_running_1, nature_golem_running_2, nature_golem_running_3, nature_golem_running_4, nature_golem_running_5, nature_golem_running_6, nature_golem_running_7, nature_golem_running_8, nature_golem_running_9, nature_golem_running_10, nature_golem_running_11]

nature_golem_attacking_1 = pygame.image.load("pixel-duel-main/assets/sprites/nature-golem/attacking/0_Golem_Slashing_000.png")
nature_golem_attacking_2 = pygame.image.load("pixel-duel-main/assets/sprites/nature-golem/attacking/0_Golem_Slashing_001.png")
nature_golem_attacking_3 = pygame.image.load("pixel-duel-main/assets/sprites/nature-golem/attacking/0_Golem_Slashing_002.png")
nature_golem_attacking_4 = pygame.image.load("pixel-duel-main/assets/sprites/nature-golem/attacking/0_Golem_Slashing_003.png")
nature_golem_attacking_5 = pygame.image.load("pixel-duel-main/assets/sprites/nature-golem/attacking/0_Golem_Slashing_004.png")
nature_golem_attacking_6 = pygame.image.load("pixel-duel-main/assets/sprites/nature-golem/attacking/0_Golem_Slashing_005.png")
nature_golem_attacking_7 = pygame.image.load("pixel-duel-main/assets/sprites/nature-golem/attacking/0_Golem_Slashing_006.png")
nature_golem_attacking_8 = pygame.image.load("pixel-duel-main/assets/sprites/nature-golem/attacking/0_Golem_Slashing_007.png")
nature_golem_attacking_9 = pygame.image.load("pixel-duel-main/assets/sprites/nature-golem/attacking/0_Golem_Slashing_008.png")
nature_golem_attacking_10 = pygame.image.load("pixel-duel-main/assets/sprites/nature-golem/attacking/0_Golem_Slashing_009.png")
nature_golem_attacking_11 = pygame.image.load("pixel-duel-main/assets/sprites/nature-golem/attacking/0_Golem_Slashing_010.png")
nature_golem_attacking_list = [nature_golem_attacking_1, nature_golem_attacking_2, nature_golem_attacking_3, nature_golem_attacking_4, nature_golem_attacking_5, nature_golem_attacking_6, nature_golem_attacking_7, nature_golem_attacking_8, nature_golem_attacking_9, nature_golem_attacking_10, nature_golem_attacking_11]

nature_golem_hurt_1 = pygame.image.load("pixel-duel-main/assets/sprites/nature-golem/hurt/0_Golem_Hurt_000.png")
nature_golem_hurt_2 = pygame.image.load("pixel-duel-main/assets/sprites/nature-golem/hurt/0_Golem_Hurt_001.png")
nature_golem_hurt_3 = pygame.image.load("pixel-duel-main/assets/sprites/nature-golem/hurt/0_Golem_Hurt_002.png")
nature_golem_hurt_4 = pygame.image.load("pixel-duel-main/assets/sprites/nature-golem/hurt/0_Golem_Hurt_003.png")
nature_golem_hurt_5 = pygame.image.load("pixel-duel-main/assets/sprites/nature-golem/hurt/0_Golem_Hurt_004.png")
nature_golem_hurt_6 = pygame.image.load("pixel-duel-main/assets/sprites/nature-golem/hurt/0_Golem_Hurt_005.png")
nature_golem_hurt_7 = pygame.image.load("pixel-duel-main/assets/sprites/nature-golem/hurt/0_Golem_Hurt_006.png")
nature_golem_hurt_8 = pygame.image.load("pixel-duel-main/assets/sprites/nature-golem/hurt/0_Golem_Hurt_007.png")
nature_golem_hurt_9 = pygame.image.load("pixel-duel-main/assets/sprites/nature-golem/hurt/0_Golem_Hurt_008.png")
nature_golem_hurt_10 = pygame.image.load("pixel-duel-main/assets/sprites/nature-golem/hurt/0_Golem_Hurt_009.png")
nature_golem_hurt_11 = pygame.image.load("pixel-duel-main/assets/sprites/nature-golem/hurt/0_Golem_Hurt_010.png")
nature_golem_hurt_12 = pygame.image.load("pixel-duel-main/assets/sprites/nature-golem/hurt/0_Golem_Hurt_011.png")
nature_golem_hurt_list = [nature_golem_hurt_1, nature_golem_hurt_2, nature_golem_hurt_3, nature_golem_hurt_4, nature_golem_hurt_5, nature_golem_hurt_6, nature_golem_hurt_7, nature_golem_hurt_8, nature_golem_hurt_9, nature_golem_hurt_10, nature_golem_hurt_11, nature_golem_hurt_12]

nature_golem_dead_1 = pygame.image.load("pixel-duel-main/assets/sprites/nature-golem/dead/0_Golem_Dying_000.png")
nature_golem_dead_2 = pygame.image.load("pixel-duel-main/assets/sprites/nature-golem/dead/0_Golem_Dying_001.png")
nature_golem_dead_3 = pygame.image.load("pixel-duel-main/assets/sprites/nature-golem/dead/0_Golem_Dying_002.png")
nature_golem_dead_4 = pygame.image.load("pixel-duel-main/assets/sprites/nature-golem/dead/0_Golem_Dying_003.png")
nature_golem_dead_5 = pygame.image.load("pixel-duel-main/assets/sprites/nature-golem/dead/0_Golem_Dying_004.png")
nature_golem_dead_6 = pygame.image.load("pixel-duel-main/assets/sprites/nature-golem/dead/0_Golem_Dying_005.png")
nature_golem_dead_7 = pygame.image.load("pixel-duel-main/assets/sprites/nature-golem/dead/0_Golem_Dying_006.png")
nature_golem_dead_8 = pygame.image.load("pixel-duel-main/assets/sprites/nature-golem/dead/0_Golem_Dying_007.png")
nature_golem_dead_9 = pygame.image.load("pixel-duel-main/assets/sprites/nature-golem/dead/0_Golem_Dying_008.png")
nature_golem_dead_10 = pygame.image.load("pixel-duel-main/assets/sprites/nature-golem/dead/0_Golem_Dying_009.png")
nature_golem_dead_11 = pygame.image.load("pixel-duel-main/assets/sprites/nature-golem/dead/0_Golem_Dying_010.png")
nature_golem_dead_12 = pygame.image.load("pixel-duel-main/assets/sprites/nature-golem/dead/0_Golem_Dying_011.png")
nature_golem_dead_13 = pygame.image.load("pixel-duel-main/assets/sprites/nature-golem/dead/0_Golem_Dying_012.png")
nature_golem_dead_14 = pygame.image.load("pixel-duel-main/assets/sprites/nature-golem/dead/0_Golem_Dying_013.png")
nature_golem_dead_15 = pygame.image.load("pixel-duel-main/assets/sprites/nature-golem/dead/0_Golem_Dying_014.png")
nature_golem_dead_list = [nature_golem_dead_1, nature_golem_dead_2, nature_golem_dead_3, nature_golem_dead_4, nature_golem_dead_5, nature_golem_dead_6, nature_golem_dead_7, nature_golem_dead_8, nature_golem_dead_9, nature_golem_dead_10, nature_golem_dead_11, nature_golem_dead_12, nature_golem_dead_13, nature_golem_dead_14, nature_golem_dead_15]

# Ice
ice_golem_idle_1 = pygame.image.load("pixel-duel-main/assets/sprites/ice-golem/idle/0_Golem_Idle_000.png")
ice_golem_idle_2 = pygame.image.load("pixel-duel-main/assets/sprites/ice-golem/idle/0_Golem_Idle_001.png")
ice_golem_idle_3 = pygame.image.load("pixel-duel-main/assets/sprites/ice-golem/idle/0_Golem_Idle_002.png")
ice_golem_idle_4 = pygame.image.load("pixel-duel-main/assets/sprites/ice-golem/idle/0_Golem_Idle_003.png")
ice_golem_idle_5 = pygame.image.load("pixel-duel-main/assets/sprites/ice-golem/idle/0_Golem_Idle_004.png")
ice_golem_idle_6 = pygame.image.load("pixel-duel-main/assets/sprites/ice-golem/idle/0_Golem_Idle_005.png")
ice_golem_idle_7 = pygame.image.load("pixel-duel-main/assets/sprites/ice-golem/idle/0_Golem_Idle_006.png")
ice_golem_idle_8 = pygame.image.load("pixel-duel-main/assets/sprites/ice-golem/idle/0_Golem_Idle_007.png")
ice_golem_idle_9 = pygame.image.load("pixel-duel-main/assets/sprites/ice-golem/idle/0_Golem_Idle_008.png")
ice_golem_idle_10 = pygame.image.load("pixel-duel-main/assets/sprites/ice-golem/idle/0_Golem_Idle_009.png")
ice_golem_idle_11 = pygame.image.load("pixel-duel-main/assets/sprites/ice-golem/idle/0_Golem_Idle_010.png")
ice_golem_idle_12 = pygame.image.load("pixel-duel-main/assets/sprites/ice-golem/idle/0_Golem_Idle_011.png")
ice_golem_idle_13 = pygame.image.load("pixel-duel-main/assets/sprites/ice-golem/idle/0_Golem_Idle_012.png")
ice_golem_idle_14 = pygame.image.load("pixel-duel-main/assets/sprites/ice-golem/idle/0_Golem_Idle_013.png")
ice_golem_idle_15 = pygame.image.load("pixel-duel-main/assets/sprites/ice-golem/idle/0_Golem_Idle_014.png")
ice_golem_idle_16 = pygame.image.load("pixel-duel-main/assets/sprites/ice-golem/idle/0_Golem_Idle_015.png")
ice_golem_idle_17 = pygame.image.load("pixel-duel-main/assets/sprites/ice-golem/idle/0_Golem_Idle_016.png")
ice_golem_idle_18 = pygame.image.load("pixel-duel-main/assets/sprites/ice-golem/idle/0_Golem_Idle_017.png")
ice_golem_idle_list = [ice_golem_idle_1, ice_golem_idle_2, ice_golem_idle_3, ice_golem_idle_4, ice_golem_idle_5, ice_golem_idle_6, ice_golem_idle_7, ice_golem_idle_8, ice_golem_idle_9, ice_golem_idle_10, ice_golem_idle_11, ice_golem_idle_12, ice_golem_idle_13, ice_golem_idle_14, ice_golem_idle_1, ice_golem_idle_15, ice_golem_idle_16, ice_golem_idle_17]

ice_golem_running_1 = pygame.image.load("pixel-duel-main/assets/sprites/ice-golem/running/0_Golem_Running_000.png")
ice_golem_running_2 = pygame.image.load("pixel-duel-main/assets/sprites/ice-golem/running/0_Golem_Running_001.png")
ice_golem_running_3 = pygame.image.load("pixel-duel-main/assets/sprites/ice-golem/running/0_Golem_Running_002.png")
ice_golem_running_4 = pygame.image.load("pixel-duel-main/assets/sprites/ice-golem/running/0_Golem_Running_003.png")
ice_golem_running_5 = pygame.image.load("pixel-duel-main/assets/sprites/ice-golem/running/0_Golem_Running_004.png")
ice_golem_running_6 = pygame.image.load("pixel-duel-main/assets/sprites/ice-golem/running/0_Golem_Running_005.png")
ice_golem_running_7 = pygame.image.load("pixel-duel-main/assets/sprites/ice-golem/running/0_Golem_Running_006.png")
ice_golem_running_8 = pygame.image.load("pixel-duel-main/assets/sprites/ice-golem/running/0_Golem_Running_007.png")
ice_golem_running_9 = pygame.image.load("pixel-duel-main/assets/sprites/ice-golem/running/0_Golem_Running_008.png")
ice_golem_running_10 = pygame.image.load("pixel-duel-main/assets/sprites/ice-golem/running/0_Golem_Running_009.png")
ice_golem_running_11 = pygame.image.load("pixel-duel-main/assets/sprites/ice-golem/running/0_Golem_Running_010.png")
ice_golem_running_list = [ice_golem_running_1, ice_golem_running_2, ice_golem_running_3, ice_golem_running_4, ice_golem_running_5, ice_golem_running_6, ice_golem_running_7, ice_golem_running_8, ice_golem_running_9, ice_golem_running_10, ice_golem_running_11]

ice_golem_attacking_1 = pygame.image.load("pixel-duel-main/assets/sprites/ice-golem/attacking/0_Golem_Slashing_000.png")
ice_golem_attacking_2 = pygame.image.load("pixel-duel-main/assets/sprites/ice-golem/attacking/0_Golem_Slashing_001.png")
ice_golem_attacking_3 = pygame.image.load("pixel-duel-main/assets/sprites/ice-golem/attacking/0_Golem_Slashing_002.png")
ice_golem_attacking_4 = pygame.image.load("pixel-duel-main/assets/sprites/ice-golem/attacking/0_Golem_Slashing_003.png")
ice_golem_attacking_5 = pygame.image.load("pixel-duel-main/assets/sprites/ice-golem/attacking/0_Golem_Slashing_004.png")
ice_golem_attacking_6 = pygame.image.load("pixel-duel-main/assets/sprites/ice-golem/attacking/0_Golem_Slashing_005.png")
ice_golem_attacking_7 = pygame.image.load("pixel-duel-main/assets/sprites/ice-golem/attacking/0_Golem_Slashing_006.png")
ice_golem_attacking_8 = pygame.image.load("pixel-duel-main/assets/sprites/ice-golem/attacking/0_Golem_Slashing_007.png")
ice_golem_attacking_9 = pygame.image.load("pixel-duel-main/assets/sprites/ice-golem/attacking/0_Golem_Slashing_008.png")
ice_golem_attacking_10 = pygame.image.load("pixel-duel-main/assets/sprites/ice-golem/attacking/0_Golem_Slashing_009.png")
ice_golem_attacking_11 = pygame.image.load("pixel-duel-main/assets/sprites/ice-golem/attacking/0_Golem_Slashing_010.png")
ice_golem_attacking_list = [ice_golem_attacking_1, ice_golem_attacking_2, ice_golem_attacking_3, ice_golem_attacking_4, ice_golem_attacking_5, ice_golem_attacking_6, ice_golem_attacking_7, ice_golem_attacking_8, ice_golem_attacking_9, ice_golem_attacking_10, ice_golem_attacking_11]

ice_golem_hurt_1 = pygame.image.load("pixel-duel-main/assets/sprites/ice-golem/hurt/0_Golem_Hurt_000.png")
ice_golem_hurt_2 = pygame.image.load("pixel-duel-main/assets/sprites/ice-golem/hurt/0_Golem_Hurt_001.png")
ice_golem_hurt_3 = pygame.image.load("pixel-duel-main/assets/sprites/ice-golem/hurt/0_Golem_Hurt_002.png")
ice_golem_hurt_4 = pygame.image.load("pixel-duel-main/assets/sprites/ice-golem/hurt/0_Golem_Hurt_003.png")
ice_golem_hurt_5 = pygame.image.load("pixel-duel-main/assets/sprites/ice-golem/hurt/0_Golem_Hurt_004.png")
ice_golem_hurt_6 = pygame.image.load("pixel-duel-main/assets/sprites/ice-golem/hurt/0_Golem_Hurt_005.png")
ice_golem_hurt_7 = pygame.image.load("pixel-duel-main/assets/sprites/ice-golem/hurt/0_Golem_Hurt_006.png")
ice_golem_hurt_8 = pygame.image.load("pixel-duel-main/assets/sprites/ice-golem/hurt/0_Golem_Hurt_007.png")
ice_golem_hurt_9 = pygame.image.load("pixel-duel-main/assets/sprites/ice-golem/hurt/0_Golem_Hurt_008.png")
ice_golem_hurt_10 = pygame.image.load("pixel-duel-main/assets/sprites/ice-golem/hurt/0_Golem_Hurt_009.png")
ice_golem_hurt_11 = pygame.image.load("pixel-duel-main/assets/sprites/ice-golem/hurt/0_Golem_Hurt_010.png")
ice_golem_hurt_12 = pygame.image.load("pixel-duel-main/assets/sprites/ice-golem/hurt/0_Golem_Hurt_011.png")
ice_golem_hurt_list = [ice_golem_hurt_1, ice_golem_hurt_2, ice_golem_hurt_3, ice_golem_hurt_4, ice_golem_hurt_5, ice_golem_hurt_6, ice_golem_hurt_7, ice_golem_hurt_8, ice_golem_hurt_9, ice_golem_hurt_10, ice_golem_hurt_11, ice_golem_hurt_12]

ice_golem_dead_1 = pygame.image.load("pixel-duel-main/assets/sprites/ice-golem/dead/0_Golem_Dying_000.png")
ice_golem_dead_2 = pygame.image.load("pixel-duel-main/assets/sprites/ice-golem/dead/0_Golem_Dying_001.png")
ice_golem_dead_3 = pygame.image.load("pixel-duel-main/assets/sprites/ice-golem/dead/0_Golem_Dying_002.png")
ice_golem_dead_4 = pygame.image.load("pixel-duel-main/assets/sprites/ice-golem/dead/0_Golem_Dying_003.png")
ice_golem_dead_5 = pygame.image.load("pixel-duel-main/assets/sprites/ice-golem/dead/0_Golem_Dying_004.png")
ice_golem_dead_6 = pygame.image.load("pixel-duel-main/assets/sprites/ice-golem/dead/0_Golem_Dying_005.png")
ice_golem_dead_7 = pygame.image.load("pixel-duel-main/assets/sprites/ice-golem/dead/0_Golem_Dying_006.png")
ice_golem_dead_8 = pygame.image.load("pixel-duel-main/assets/sprites/ice-golem/dead/0_Golem_Dying_007.png")
ice_golem_dead_9 = pygame.image.load("pixel-duel-main/assets/sprites/ice-golem/dead/0_Golem_Dying_008.png")
ice_golem_dead_10 = pygame.image.load("pixel-duel-main/assets/sprites/ice-golem/dead/0_Golem_Dying_009.png")
ice_golem_dead_11 = pygame.image.load("pixel-duel-main/assets/sprites/ice-golem/dead/0_Golem_Dying_010.png")
ice_golem_dead_12 = pygame.image.load("pixel-duel-main/assets/sprites/ice-golem/dead/0_Golem_Dying_011.png")
ice_golem_dead_13 = pygame.image.load("pixel-duel-main/assets/sprites/ice-golem/dead/0_Golem_Dying_012.png")
ice_golem_dead_14 = pygame.image.load("pixel-duel-main/assets/sprites/ice-golem/dead/0_Golem_Dying_013.png")
ice_golem_dead_15 = pygame.image.load("pixel-duel-main/assets/sprites/ice-golem/dead/0_Golem_Dying_014.png")
ice_golem_dead_list = [ice_golem_dead_1, ice_golem_dead_2, ice_golem_dead_3, ice_golem_dead_4, ice_golem_dead_5, ice_golem_dead_6, ice_golem_dead_7, ice_golem_dead_8, ice_golem_dead_9, ice_golem_dead_10, ice_golem_dead_11, ice_golem_dead_12, ice_golem_dead_13, ice_golem_dead_14, ice_golem_dead_15]

# Minotaur
# Brown
brown_mino_idle_1 = pygame.image.load("pixel-duel-main/assets/sprites/brown-mino/idle/Minotaur_01_Idle_000.png")
brown_mino_idle_2 = pygame.image.load("pixel-duel-main/assets/sprites/brown-mino/idle/Minotaur_01_Idle_001.png")
brown_mino_idle_3 = pygame.image.load("pixel-duel-main/assets/sprites/brown-mino/idle/Minotaur_01_Idle_002.png")
brown_mino_idle_4 = pygame.image.load("pixel-duel-main/assets/sprites/brown-mino/idle/Minotaur_01_Idle_003.png")
brown_mino_idle_5 = pygame.image.load("pixel-duel-main/assets/sprites/brown-mino/idle/Minotaur_01_Idle_004.png")
brown_mino_idle_6 = pygame.image.load("pixel-duel-main/assets/sprites/brown-mino/idle/Minotaur_01_Idle_005.png")
brown_mino_idle_7 = pygame.image.load("pixel-duel-main/assets/sprites/brown-mino/idle/Minotaur_01_Idle_006.png")
brown_mino_idle_8 = pygame.image.load("pixel-duel-main/assets/sprites/brown-mino/idle/Minotaur_01_Idle_007.png")
brown_mino_idle_9 = pygame.image.load("pixel-duel-main/assets/sprites/brown-mino/idle/Minotaur_01_Idle_008.png")
brown_mino_idle_10 = pygame.image.load("pixel-duel-main/assets/sprites/brown-mino/idle/Minotaur_01_Idle_009.png")
brown_mino_idle_11 = pygame.image.load("pixel-duel-main/assets/sprites/brown-mino/idle/Minotaur_01_Idle_010.png")
brown_mino_idle_12 = pygame.image.load("pixel-duel-main/assets/sprites/brown-mino/idle/Minotaur_01_Idle_011.png")
brown_mino_idle_list = [brown_mino_idle_1, brown_mino_idle_2, brown_mino_idle_3, brown_mino_idle_4, brown_mino_idle_5, brown_mino_idle_6, brown_mino_idle_7, brown_mino_idle_8, brown_mino_idle_9, brown_mino_idle_10, brown_mino_idle_11, brown_mino_idle_12]

brown_mino_running_1 = pygame.image.load("pixel-duel-main/assets/sprites/brown-mino/running/Minotaur_01_Walking_000.png")
brown_mino_running_2 = pygame.image.load("pixel-duel-main/assets/sprites/brown-mino/running/Minotaur_01_Walking_001.png")
brown_mino_running_3 = pygame.image.load("pixel-duel-main/assets/sprites/brown-mino/running/Minotaur_01_Walking_002.png")
brown_mino_running_4 = pygame.image.load("pixel-duel-main/assets/sprites/brown-mino/running/Minotaur_01_Walking_003.png")
brown_mino_running_5 = pygame.image.load("pixel-duel-main/assets/sprites/brown-mino/running/Minotaur_01_Walking_004.png")
brown_mino_running_6 = pygame.image.load("pixel-duel-main/assets/sprites/brown-mino/running/Minotaur_01_Walking_005.png")
brown_mino_running_7 = pygame.image.load("pixel-duel-main/assets/sprites/brown-mino/running/Minotaur_01_Walking_006.png")
brown_mino_running_8 = pygame.image.load("pixel-duel-main/assets/sprites/brown-mino/running/Minotaur_01_Walking_007.png")
brown_mino_running_9 = pygame.image.load("pixel-duel-main/assets/sprites/brown-mino/running/Minotaur_01_Walking_008.png")
brown_mino_running_10 = pygame.image.load("pixel-duel-main/assets/sprites/brown-mino/running/Minotaur_01_Walking_009.png")
brown_mino_running_11 = pygame.image.load("pixel-duel-main/assets/sprites/brown-mino/running/Minotaur_01_Walking_010.png")
brown_mino_running_12 = pygame.image.load("pixel-duel-main/assets/sprites/brown-mino/running/Minotaur_01_Walking_011.png")
brown_mino_running_13 = pygame.image.load("pixel-duel-main/assets/sprites/brown-mino/running/Minotaur_01_Walking_012.png")
brown_mino_running_14 = pygame.image.load("pixel-duel-main/assets/sprites/brown-mino/running/Minotaur_01_Walking_013.png")
brown_mino_running_15 = pygame.image.load("pixel-duel-main/assets/sprites/brown-mino/running/Minotaur_01_Walking_014.png")
brown_mino_running_16 = pygame.image.load("pixel-duel-main/assets/sprites/brown-mino/running/Minotaur_01_Walking_015.png")
brown_mino_running_17 = pygame.image.load("pixel-duel-main/assets/sprites/brown-mino/running/Minotaur_01_Walking_016.png")
brown_mino_running_18 = pygame.image.load("pixel-duel-main/assets/sprites/brown-mino/running/Minotaur_01_Walking_017.png")
brown_mino_running_list = [brown_mino_running_1, brown_mino_running_2, brown_mino_running_3, brown_mino_running_4, brown_mino_running_5, brown_mino_running_6, brown_mino_running_7, brown_mino_running_8, brown_mino_running_9, brown_mino_running_10, brown_mino_running_11, brown_mino_running_12, brown_mino_running_13, brown_mino_running_14, brown_mino_running_15, brown_mino_running_16, brown_mino_running_17, brown_mino_running_18]

brown_mino_attacking_1 = pygame.image.load("pixel-duel-main/assets/sprites/brown-mino/attacking/Minotaur_01_Attacking_000.png")
brown_mino_attacking_2 = pygame.image.load("pixel-duel-main/assets/sprites/brown-mino/attacking/Minotaur_01_Attacking_001.png")
brown_mino_attacking_3 = pygame.image.load("pixel-duel-main/assets/sprites/brown-mino/attacking/Minotaur_01_Attacking_002.png")
brown_mino_attacking_4 = pygame.image.load("pixel-duel-main/assets/sprites/brown-mino/attacking/Minotaur_01_Attacking_003.png")
brown_mino_attacking_5 = pygame.image.load("pixel-duel-main/assets/sprites/brown-mino/attacking/Minotaur_01_Attacking_004.png")
brown_mino_attacking_6 = pygame.image.load("pixel-duel-main/assets/sprites/brown-mino/attacking/Minotaur_01_Attacking_005.png")
brown_mino_attacking_7 = pygame.image.load("pixel-duel-main/assets/sprites/brown-mino/attacking/Minotaur_01_Attacking_006.png")
brown_mino_attacking_8 = pygame.image.load("pixel-duel-main/assets/sprites/brown-mino/attacking/Minotaur_01_Attacking_007.png")
brown_mino_attacking_9 = pygame.image.load("pixel-duel-main/assets/sprites/brown-mino/attacking/Minotaur_01_Attacking_008.png")
brown_mino_attacking_10 = pygame.image.load("pixel-duel-main/assets/sprites/brown-mino/attacking/Minotaur_01_Attacking_009.png")
brown_mino_attacking_11 = pygame.image.load("pixel-duel-main/assets/sprites/brown-mino/attacking/Minotaur_01_Attacking_010.png")
brown_mino_attacking_12 = pygame.image.load("pixel-duel-main/assets/sprites/brown-mino/attacking/Minotaur_01_Attacking_011.png")
brown_mino_attacking_list = [brown_mino_attacking_1, brown_mino_attacking_2, brown_mino_attacking_3, brown_mino_attacking_4, brown_mino_attacking_5, brown_mino_attacking_6, brown_mino_attacking_7, brown_mino_attacking_8, brown_mino_attacking_9, brown_mino_attacking_10, brown_mino_attacking_11, brown_mino_attacking_12]

brown_mino_hurt_1 = pygame.image.load("pixel-duel-main/assets/sprites/brown-mino/hurt/Minotaur_01_Hurt_000.png")
brown_mino_hurt_2 = pygame.image.load("pixel-duel-main/assets/sprites/brown-mino/hurt/Minotaur_01_Hurt_001.png")
brown_mino_hurt_3 = pygame.image.load("pixel-duel-main/assets/sprites/brown-mino/hurt/Minotaur_01_Hurt_002.png")
brown_mino_hurt_4 = pygame.image.load("pixel-duel-main/assets/sprites/brown-mino/hurt/Minotaur_01_Hurt_003.png")
brown_mino_hurt_5 = pygame.image.load("pixel-duel-main/assets/sprites/brown-mino/hurt/Minotaur_01_Hurt_004.png")
brown_mino_hurt_6 = pygame.image.load("pixel-duel-main/assets/sprites/brown-mino/hurt/Minotaur_01_Hurt_005.png")
brown_mino_hurt_7 = pygame.image.load("pixel-duel-main/assets/sprites/brown-mino/hurt/Minotaur_01_Hurt_006.png")
brown_mino_hurt_8 = pygame.image.load("pixel-duel-main/assets/sprites/brown-mino/hurt/Minotaur_01_Hurt_007.png")
brown_mino_hurt_9 = pygame.image.load("pixel-duel-main/assets/sprites/brown-mino/hurt/Minotaur_01_Hurt_008.png")
brown_mino_hurt_10 = pygame.image.load("pixel-duel-main/assets/sprites/brown-mino/hurt/Minotaur_01_Hurt_009.png")
brown_mino_hurt_11 = pygame.image.load("pixel-duel-main/assets/sprites/brown-mino/hurt/Minotaur_01_Hurt_010.png")
brown_mino_hurt_12 = pygame.image.load("pixel-duel-main/assets/sprites/brown-mino/hurt/Minotaur_01_Hurt_011.png")
brown_mino_hurt_list = [brown_mino_hurt_1, brown_mino_hurt_2, brown_mino_hurt_3, brown_mino_hurt_4, brown_mino_hurt_5, brown_mino_hurt_6, brown_mino_hurt_7, brown_mino_hurt_8, brown_mino_hurt_9, brown_mino_hurt_10, brown_mino_hurt_11, brown_mino_hurt_12]

brown_mino_dying_1 = pygame.image.load("pixel-duel-main/assets/sprites/brown-mino/dead/Minotaur_01_Dying_000.png")
brown_mino_dying_2 = pygame.image.load("pixel-duel-main/assets/sprites/brown-mino/dead/Minotaur_01_Dying_001.png")
brown_mino_dying_3 = pygame.image.load("pixel-duel-main/assets/sprites/brown-mino/dead/Minotaur_01_Dying_002.png")
brown_mino_dying_4 = pygame.image.load("pixel-duel-main/assets/sprites/brown-mino/dead/Minotaur_01_Dying_003.png")
brown_mino_dying_5 = pygame.image.load("pixel-duel-main/assets/sprites/brown-mino/dead/Minotaur_01_Dying_004.png")
brown_mino_dying_6 = pygame.image.load("pixel-duel-main/assets/sprites/brown-mino/dead/Minotaur_01_Dying_005.png")
brown_mino_dying_7 = pygame.image.load("pixel-duel-main/assets/sprites/brown-mino/dead/Minotaur_01_Dying_006.png")
brown_mino_dying_8 = pygame.image.load("pixel-duel-main/assets/sprites/brown-mino/dead/Minotaur_01_Dying_007.png")
brown_mino_dying_9 = pygame.image.load("pixel-duel-main/assets/sprites/brown-mino/dead/Minotaur_01_Dying_008.png")
brown_mino_dying_10 = pygame.image.load("pixel-duel-main/assets/sprites/brown-mino/dead/Minotaur_01_Dying_009.png")
brown_mino_dying_11 = pygame.image.load("pixel-duel-main/assets/sprites/brown-mino/dead/Minotaur_01_Dying_010.png")
brown_mino_dying_12 = pygame.image.load("pixel-duel-main/assets/sprites/brown-mino/dead/Minotaur_01_Dying_011.png")
brown_mino_dying_13 = pygame.image.load("pixel-duel-main/assets/sprites/brown-mino/dead/Minotaur_01_Dying_012.png")
brown_mino_dying_14 = pygame.image.load("pixel-duel-main/assets/sprites/brown-mino/dead/Minotaur_01_Dying_013.png")
brown_mino_dying_15 = pygame.image.load("pixel-duel-main/assets/sprites/brown-mino/dead/Minotaur_01_Dying_014.png")
brown_mino_dying_list = [brown_mino_dying_1, brown_mino_dying_2, brown_mino_dying_3, brown_mino_dying_4, brown_mino_dying_5, brown_mino_dying_6, brown_mino_dying_7, brown_mino_dying_8, brown_mino_dying_9, brown_mino_dying_10, brown_mino_dying_11, brown_mino_dying_12, brown_mino_dying_13, brown_mino_dying_14, brown_mino_dying_15]

# Blue
blue_mino_idle_1 = pygame.image.load("pixel-duel-main/assets/sprites/blue-mino/idle/Minotaur_02_Idle_000.png")
blue_mino_idle_2 = pygame.image.load("pixel-duel-main/assets/sprites/blue-mino/idle/Minotaur_02_Idle_001.png")
blue_mino_idle_3 = pygame.image.load("pixel-duel-main/assets/sprites/blue-mino/idle/Minotaur_02_Idle_002.png")
blue_mino_idle_4 = pygame.image.load("pixel-duel-main/assets/sprites/blue-mino/idle/Minotaur_02_Idle_003.png")
blue_mino_idle_5 = pygame.image.load("pixel-duel-main/assets/sprites/blue-mino/idle/Minotaur_02_Idle_004.png")
blue_mino_idle_6 = pygame.image.load("pixel-duel-main/assets/sprites/blue-mino/idle/Minotaur_02_Idle_005.png")
blue_mino_idle_7 = pygame.image.load("pixel-duel-main/assets/sprites/blue-mino/idle/Minotaur_02_Idle_006.png")
blue_mino_idle_8 = pygame.image.load("pixel-duel-main/assets/sprites/blue-mino/idle/Minotaur_02_Idle_007.png")
blue_mino_idle_9 = pygame.image.load("pixel-duel-main/assets/sprites/blue-mino/idle/Minotaur_02_Idle_008.png")
blue_mino_idle_10 = pygame.image.load("pixel-duel-main/assets/sprites/blue-mino/idle/Minotaur_02_Idle_009.png")
blue_mino_idle_11 = pygame.image.load("pixel-duel-main/assets/sprites/blue-mino/idle/Minotaur_02_Idle_010.png")
blue_mino_idle_12 = pygame.image.load("pixel-duel-main/assets/sprites/blue-mino/idle/Minotaur_02_Idle_011.png")
blue_mino_idle_list = [blue_mino_idle_1, blue_mino_idle_2, blue_mino_idle_3, blue_mino_idle_4, blue_mino_idle_5, blue_mino_idle_6, blue_mino_idle_7, blue_mino_idle_8, blue_mino_idle_9, blue_mino_idle_10, blue_mino_idle_11, blue_mino_idle_12]

blue_mino_running_1 = pygame.image.load("pixel-duel-main/assets/sprites/blue-mino/running/Minotaur_02_Walking_000.png")
blue_mino_running_2 = pygame.image.load("pixel-duel-main/assets/sprites/blue-mino/running/Minotaur_02_Walking_001.png")
blue_mino_running_3 = pygame.image.load("pixel-duel-main/assets/sprites/blue-mino/running/Minotaur_02_Walking_002.png")
blue_mino_running_4 = pygame.image.load("pixel-duel-main/assets/sprites/blue-mino/running/Minotaur_02_Walking_003.png")
blue_mino_running_5 = pygame.image.load("pixel-duel-main/assets/sprites/blue-mino/running/Minotaur_02_Walking_004.png")
blue_mino_running_6 = pygame.image.load("pixel-duel-main/assets/sprites/blue-mino/running/Minotaur_02_Walking_005.png")
blue_mino_running_7 = pygame.image.load("pixel-duel-main/assets/sprites/blue-mino/running/Minotaur_02_Walking_006.png")
blue_mino_running_8 = pygame.image.load("pixel-duel-main/assets/sprites/blue-mino/running/Minotaur_02_Walking_007.png")
blue_mino_running_9 = pygame.image.load("pixel-duel-main/assets/sprites/blue-mino/running/Minotaur_02_Walking_008.png")
blue_mino_running_10 = pygame.image.load("pixel-duel-main/assets/sprites/blue-mino/running/Minotaur_02_Walking_009.png")
blue_mino_running_11 = pygame.image.load("pixel-duel-main/assets/sprites/blue-mino/running/Minotaur_02_Walking_010.png")
blue_mino_running_12 = pygame.image.load("pixel-duel-main/assets/sprites/blue-mino/running/Minotaur_02_Walking_011.png")
blue_mino_running_13 = pygame.image.load("pixel-duel-main/assets/sprites/blue-mino/running/Minotaur_02_Walking_012.png")
blue_mino_running_14 = pygame.image.load("pixel-duel-main/assets/sprites/blue-mino/running/Minotaur_02_Walking_013.png")
blue_mino_running_15 = pygame.image.load("pixel-duel-main/assets/sprites/blue-mino/running/Minotaur_02_Walking_014.png")
blue_mino_running_16 = pygame.image.load("pixel-duel-main/assets/sprites/blue-mino/running/Minotaur_02_Walking_015.png")
blue_mino_running_17 = pygame.image.load("pixel-duel-main/assets/sprites/blue-mino/running/Minotaur_02_Walking_016.png")
blue_mino_running_18 = pygame.image.load("pixel-duel-main/assets/sprites/blue-mino/running/Minotaur_02_Walking_017.png")
blue_mino_running_list = [blue_mino_running_1, blue_mino_running_2, blue_mino_running_3, blue_mino_running_4, blue_mino_running_5, blue_mino_running_6, blue_mino_running_7, blue_mino_running_8, blue_mino_running_9, blue_mino_running_10, blue_mino_running_11, blue_mino_running_12, blue_mino_running_13, blue_mino_running_14, blue_mino_running_15, blue_mino_running_16, blue_mino_running_17, blue_mino_running_18]

blue_mino_attacking_1 = pygame.image.load("pixel-duel-main/assets/sprites/blue-mino/attacking/Minotaur_02_Attacking_000.png")
blue_mino_attacking_2 = pygame.image.load("pixel-duel-main/assets/sprites/blue-mino/attacking/Minotaur_02_Attacking_001.png")
blue_mino_attacking_3 = pygame.image.load("pixel-duel-main/assets/sprites/blue-mino/attacking/Minotaur_02_Attacking_002.png")
blue_mino_attacking_4 = pygame.image.load("pixel-duel-main/assets/sprites/blue-mino/attacking/Minotaur_02_Attacking_003.png")
blue_mino_attacking_5 = pygame.image.load("pixel-duel-main/assets/sprites/blue-mino/attacking/Minotaur_02_Attacking_004.png")
blue_mino_attacking_6 = pygame.image.load("pixel-duel-main/assets/sprites/blue-mino/attacking/Minotaur_02_Attacking_005.png")
blue_mino_attacking_7 = pygame.image.load("pixel-duel-main/assets/sprites/blue-mino/attacking/Minotaur_02_Attacking_006.png")
blue_mino_attacking_8 = pygame.image.load("pixel-duel-main/assets/sprites/blue-mino/attacking/Minotaur_02_Attacking_007.png")
blue_mino_attacking_9 = pygame.image.load("pixel-duel-main/assets/sprites/blue-mino/attacking/Minotaur_02_Attacking_008.png")
blue_mino_attacking_10 = pygame.image.load("pixel-duel-main/assets/sprites/blue-mino/attacking/Minotaur_02_Attacking_009.png")
blue_mino_attacking_11 = pygame.image.load("pixel-duel-main/assets/sprites/blue-mino/attacking/Minotaur_02_Attacking_010.png")
blue_mino_attacking_12 = pygame.image.load("pixel-duel-main/assets/sprites/blue-mino/attacking/Minotaur_02_Attacking_011.png")
blue_mino_attacking_list = [blue_mino_attacking_1, blue_mino_attacking_2, blue_mino_attacking_3, blue_mino_attacking_4, blue_mino_attacking_5, blue_mino_attacking_6, blue_mino_attacking_7, blue_mino_attacking_8, blue_mino_attacking_9, blue_mino_attacking_10, blue_mino_attacking_11, blue_mino_attacking_12]

blue_mino_hurt_1 = pygame.image.load("pixel-duel-main/assets/sprites/blue-mino/hurt/Minotaur_02_Hurt_000.png")
blue_mino_hurt_2 = pygame.image.load("pixel-duel-main/assets/sprites/blue-mino/hurt/Minotaur_02_Hurt_001.png")
blue_mino_hurt_3 = pygame.image.load("pixel-duel-main/assets/sprites/blue-mino/hurt/Minotaur_02_Hurt_002.png")
blue_mino_hurt_4 = pygame.image.load("pixel-duel-main/assets/sprites/blue-mino/hurt/Minotaur_02_Hurt_003.png")
blue_mino_hurt_5 = pygame.image.load("pixel-duel-main/assets/sprites/blue-mino/hurt/Minotaur_02_Hurt_004.png")
blue_mino_hurt_6 = pygame.image.load("pixel-duel-main/assets/sprites/blue-mino/hurt/Minotaur_02_Hurt_005.png")
blue_mino_hurt_7 = pygame.image.load("pixel-duel-main/assets/sprites/blue-mino/hurt/Minotaur_02_Hurt_006.png")
blue_mino_hurt_8 = pygame.image.load("pixel-duel-main/assets/sprites/blue-mino/hurt/Minotaur_02_Hurt_007.png")
blue_mino_hurt_9 = pygame.image.load("pixel-duel-main/assets/sprites/blue-mino/hurt/Minotaur_02_Hurt_008.png")
blue_mino_hurt_10 = pygame.image.load("pixel-duel-main/assets/sprites/blue-mino/hurt/Minotaur_02_Hurt_009.png")
blue_mino_hurt_11 = pygame.image.load("pixel-duel-main/assets/sprites/blue-mino/hurt/Minotaur_02_Hurt_010.png")
blue_mino_hurt_12 = pygame.image.load("pixel-duel-main/assets/sprites/blue-mino/hurt/Minotaur_02_Hurt_011.png")
blue_mino_hurt_list = [blue_mino_hurt_1, blue_mino_hurt_2, blue_mino_hurt_3, blue_mino_hurt_4, blue_mino_hurt_5, blue_mino_hurt_6, blue_mino_hurt_7, blue_mino_hurt_8, blue_mino_hurt_9, blue_mino_hurt_10, blue_mino_hurt_11, blue_mino_hurt_12]

blue_mino_dying_1 = pygame.image.load("pixel-duel-main/assets/sprites/blue-mino/dead/Minotaur_02_Dying_000.png")
blue_mino_dying_2 = pygame.image.load("pixel-duel-main/assets/sprites/blue-mino/dead/Minotaur_02_Dying_001.png")
blue_mino_dying_3 = pygame.image.load("pixel-duel-main/assets/sprites/blue-mino/dead/Minotaur_02_Dying_002.png")
blue_mino_dying_4 = pygame.image.load("pixel-duel-main/assets/sprites/blue-mino/dead/Minotaur_02_Dying_003.png")
blue_mino_dying_5 = pygame.image.load("pixel-duel-main/assets/sprites/blue-mino/dead/Minotaur_02_Dying_004.png")
blue_mino_dying_6 = pygame.image.load("pixel-duel-main/assets/sprites/blue-mino/dead/Minotaur_02_Dying_005.png")
blue_mino_dying_7 = pygame.image.load("pixel-duel-main/assets/sprites/blue-mino/dead/Minotaur_02_Dying_006.png")
blue_mino_dying_8 = pygame.image.load("pixel-duel-main/assets/sprites/blue-mino/dead/Minotaur_02_Dying_007.png")
blue_mino_dying_9 = pygame.image.load("pixel-duel-main/assets/sprites/blue-mino/dead/Minotaur_02_Dying_008.png")
blue_mino_dying_10 = pygame.image.load("pixel-duel-main/assets/sprites/blue-mino/dead/Minotaur_02_Dying_009.png")
blue_mino_dying_11 = pygame.image.load("pixel-duel-main/assets/sprites/blue-mino/dead/Minotaur_02_Dying_010.png")
blue_mino_dying_12 = pygame.image.load("pixel-duel-main/assets/sprites/blue-mino/dead/Minotaur_02_Dying_011.png")
blue_mino_dying_13 = pygame.image.load("pixel-duel-main/assets/sprites/blue-mino/dead/Minotaur_02_Dying_012.png")
blue_mino_dying_14 = pygame.image.load("pixel-duel-main/assets/sprites/blue-mino/dead/Minotaur_02_Dying_013.png")
blue_mino_dying_15 = pygame.image.load("pixel-duel-main/assets/sprites/blue-mino/dead/Minotaur_02_Dying_014.png")
blue_mino_dying_list = [blue_mino_dying_1, blue_mino_dying_2, blue_mino_dying_3, blue_mino_dying_4, blue_mino_dying_5, blue_mino_dying_6, blue_mino_dying_7, blue_mino_dying_8, blue_mino_dying_9, blue_mino_dying_10, blue_mino_dying_11, blue_mino_dying_12, blue_mino_dying_13, blue_mino_dying_14, blue_mino_dying_15]

# Dark
dark_mino_idle_1 = pygame.image.load("pixel-duel-main/assets/sprites/dark-mino/idle/Minotaur_03_Idle_000.png")
dark_mino_idle_2 = pygame.image.load("pixel-duel-main/assets/sprites/dark-mino/idle/Minotaur_03_Idle_001.png")
dark_mino_idle_3 = pygame.image.load("pixel-duel-main/assets/sprites/dark-mino/idle/Minotaur_03_Idle_002.png")
dark_mino_idle_4 = pygame.image.load("pixel-duel-main/assets/sprites/dark-mino/idle/Minotaur_03_Idle_003.png")
dark_mino_idle_5 = pygame.image.load("pixel-duel-main/assets/sprites/dark-mino/idle/Minotaur_03_Idle_004.png")
dark_mino_idle_6 = pygame.image.load("pixel-duel-main/assets/sprites/dark-mino/idle/Minotaur_03_Idle_005.png")
dark_mino_idle_7 = pygame.image.load("pixel-duel-main/assets/sprites/dark-mino/idle/Minotaur_03_Idle_006.png")
dark_mino_idle_8 = pygame.image.load("pixel-duel-main/assets/sprites/dark-mino/idle/Minotaur_03_Idle_007.png")
dark_mino_idle_9 = pygame.image.load("pixel-duel-main/assets/sprites/dark-mino/idle/Minotaur_03_Idle_008.png")
dark_mino_idle_10 = pygame.image.load("pixel-duel-main/assets/sprites/dark-mino/idle/Minotaur_03_Idle_009.png")
dark_mino_idle_11 = pygame.image.load("pixel-duel-main/assets/sprites/dark-mino/idle/Minotaur_03_Idle_010.png")
dark_mino_idle_12 = pygame.image.load("pixel-duel-main/assets/sprites/dark-mino/idle/Minotaur_03_Idle_011.png")
dark_mino_idle_list = [dark_mino_idle_1, dark_mino_idle_2, dark_mino_idle_3, dark_mino_idle_4, dark_mino_idle_5, dark_mino_idle_6, dark_mino_idle_7, dark_mino_idle_8, dark_mino_idle_9, dark_mino_idle_10, dark_mino_idle_11, dark_mino_idle_12]

dark_mino_running_1 = pygame.image.load("pixel-duel-main/assets/sprites/dark-mino/running/Minotaur_03_Walking_000.png")
dark_mino_running_2 = pygame.image.load("pixel-duel-main/assets/sprites/dark-mino/running/Minotaur_03_Walking_001.png")
dark_mino_running_3 = pygame.image.load("pixel-duel-main/assets/sprites/dark-mino/running/Minotaur_03_Walking_002.png")
dark_mino_running_4 = pygame.image.load("pixel-duel-main/assets/sprites/dark-mino/running/Minotaur_03_Walking_003.png")
dark_mino_running_5 = pygame.image.load("pixel-duel-main/assets/sprites/dark-mino/running/Minotaur_03_Walking_004.png")
dark_mino_running_6 = pygame.image.load("pixel-duel-main/assets/sprites/dark-mino/running/Minotaur_03_Walking_005.png")
dark_mino_running_7 = pygame.image.load("pixel-duel-main/assets/sprites/dark-mino/running/Minotaur_03_Walking_006.png")
dark_mino_running_8 = pygame.image.load("pixel-duel-main/assets/sprites/dark-mino/running/Minotaur_03_Walking_007.png")
dark_mino_running_9 = pygame.image.load("pixel-duel-main/assets/sprites/dark-mino/running/Minotaur_03_Walking_008.png")
dark_mino_running_10 = pygame.image.load("pixel-duel-main/assets/sprites/dark-mino/running/Minotaur_03_Walking_009.png")
dark_mino_running_11 = pygame.image.load("pixel-duel-main/assets/sprites/dark-mino/running/Minotaur_03_Walking_010.png")
dark_mino_running_12 = pygame.image.load("pixel-duel-main/assets/sprites/dark-mino/running/Minotaur_03_Walking_011.png")
dark_mino_running_13 = pygame.image.load("pixel-duel-main/assets/sprites/dark-mino/running/Minotaur_03_Walking_012.png")
dark_mino_running_14 = pygame.image.load("pixel-duel-main/assets/sprites/dark-mino/running/Minotaur_03_Walking_013.png")
dark_mino_running_15 = pygame.image.load("pixel-duel-main/assets/sprites/dark-mino/running/Minotaur_03_Walking_014.png")
dark_mino_running_16 = pygame.image.load("pixel-duel-main/assets/sprites/dark-mino/running/Minotaur_03_Walking_015.png")
dark_mino_running_17 = pygame.image.load("pixel-duel-main/assets/sprites/dark-mino/running/Minotaur_03_Walking_016.png")
dark_mino_running_18 = pygame.image.load("pixel-duel-main/assets/sprites/dark-mino/running/Minotaur_03_Walking_017.png")
dark_mino_running_list = [dark_mino_running_1, dark_mino_running_2, dark_mino_running_3, dark_mino_running_4, dark_mino_running_5, dark_mino_running_6, dark_mino_running_7, dark_mino_running_8, dark_mino_running_9, dark_mino_running_10, dark_mino_running_11, dark_mino_running_12, dark_mino_running_13, dark_mino_running_14, dark_mino_running_15, dark_mino_running_16, dark_mino_running_17, dark_mino_running_18]

dark_mino_attacking_1 = pygame.image.load("pixel-duel-main/assets/sprites/dark-mino/attacking/Minotaur_03_Attacking_000.png")
dark_mino_attacking_2 = pygame.image.load("pixel-duel-main/assets/sprites/dark-mino/attacking/Minotaur_03_Attacking_001.png")
dark_mino_attacking_3 = pygame.image.load("pixel-duel-main/assets/sprites/dark-mino/attacking/Minotaur_03_Attacking_002.png")
dark_mino_attacking_4 = pygame.image.load("pixel-duel-main/assets/sprites/dark-mino/attacking/Minotaur_03_Attacking_003.png")
dark_mino_attacking_5 = pygame.image.load("pixel-duel-main/assets/sprites/dark-mino/attacking/Minotaur_03_Attacking_004.png")
dark_mino_attacking_6 = pygame.image.load("pixel-duel-main/assets/sprites/dark-mino/attacking/Minotaur_03_Attacking_005.png")
dark_mino_attacking_7 = pygame.image.load("pixel-duel-main/assets/sprites/dark-mino/attacking/Minotaur_03_Attacking_006.png")
dark_mino_attacking_8 = pygame.image.load("pixel-duel-main/assets/sprites/dark-mino/attacking/Minotaur_03_Attacking_007.png")
dark_mino_attacking_9 = pygame.image.load("pixel-duel-main/assets/sprites/dark-mino/attacking/Minotaur_03_Attacking_008.png")
dark_mino_attacking_10 = pygame.image.load("pixel-duel-main/assets/sprites/dark-mino/attacking/Minotaur_03_Attacking_009.png")
dark_mino_attacking_11 = pygame.image.load("pixel-duel-main/assets/sprites/dark-mino/attacking/Minotaur_03_Attacking_010.png")
dark_mino_attacking_12 = pygame.image.load("pixel-duel-main/assets/sprites/dark-mino/attacking/Minotaur_03_Attacking_011.png")
dark_mino_attacking_list = [dark_mino_attacking_1, dark_mino_attacking_2, dark_mino_attacking_3, dark_mino_attacking_4, dark_mino_attacking_5, dark_mino_attacking_6, dark_mino_attacking_7, dark_mino_attacking_8, dark_mino_attacking_9, dark_mino_attacking_10, dark_mino_attacking_11, dark_mino_attacking_12]

dark_mino_hurt_1 = pygame.image.load("pixel-duel-main/assets/sprites/dark-mino/hurt/Minotaur_03_Hurt_000.png")
dark_mino_hurt_2 = pygame.image.load("pixel-duel-main/assets/sprites/dark-mino/hurt/Minotaur_03_Hurt_001.png")
dark_mino_hurt_3 = pygame.image.load("pixel-duel-main/assets/sprites/dark-mino/hurt/Minotaur_03_Hurt_002.png")
dark_mino_hurt_4 = pygame.image.load("pixel-duel-main/assets/sprites/dark-mino/hurt/Minotaur_03_Hurt_003.png")
dark_mino_hurt_5 = pygame.image.load("pixel-duel-main/assets/sprites/dark-mino/hurt/Minotaur_03_Hurt_004.png")
dark_mino_hurt_6 = pygame.image.load("pixel-duel-main/assets/sprites/dark-mino/hurt/Minotaur_03_Hurt_005.png")
dark_mino_hurt_7 = pygame.image.load("pixel-duel-main/assets/sprites/dark-mino/hurt/Minotaur_03_Hurt_006.png")
dark_mino_hurt_8 = pygame.image.load("pixel-duel-main/assets/sprites/dark-mino/hurt/Minotaur_03_Hurt_007.png")
dark_mino_hurt_9 = pygame.image.load("pixel-duel-main/assets/sprites/dark-mino/hurt/Minotaur_03_Hurt_008.png")
dark_mino_hurt_10 = pygame.image.load("pixel-duel-main/assets/sprites/dark-mino/hurt/Minotaur_03_Hurt_009.png")
dark_mino_hurt_11 = pygame.image.load("pixel-duel-main/assets/sprites/dark-mino/hurt/Minotaur_03_Hurt_010.png")
dark_mino_hurt_12 = pygame.image.load("pixel-duel-main/assets/sprites/dark-mino/hurt/Minotaur_03_Hurt_011.png")
dark_mino_hurt_list = [dark_mino_hurt_1, dark_mino_hurt_2, dark_mino_hurt_3, dark_mino_hurt_4, dark_mino_hurt_5, dark_mino_hurt_6, dark_mino_hurt_7, dark_mino_hurt_8, dark_mino_hurt_9, dark_mino_hurt_10, dark_mino_hurt_11, dark_mino_hurt_12]

dark_mino_dying_1 = pygame.image.load("pixel-duel-main/assets/sprites/dark-mino/dead/Minotaur_03_Dying_000.png")
dark_mino_dying_2 = pygame.image.load("pixel-duel-main/assets/sprites/dark-mino/dead/Minotaur_03_Dying_001.png")
dark_mino_dying_3 = pygame.image.load("pixel-duel-main/assets/sprites/dark-mino/dead/Minotaur_03_Dying_002.png")
dark_mino_dying_4 = pygame.image.load("pixel-duel-main/assets/sprites/dark-mino/dead/Minotaur_03_Dying_003.png")
dark_mino_dying_5 = pygame.image.load("pixel-duel-main/assets/sprites/dark-mino/dead/Minotaur_03_Dying_004.png")
dark_mino_dying_6 = pygame.image.load("pixel-duel-main/assets/sprites/dark-mino/dead/Minotaur_03_Dying_005.png")
dark_mino_dying_7 = pygame.image.load("pixel-duel-main/assets/sprites/dark-mino/dead/Minotaur_03_Dying_006.png")
dark_mino_dying_8 = pygame.image.load("pixel-duel-main/assets/sprites/dark-mino/dead/Minotaur_03_Dying_007.png")
dark_mino_dying_9 = pygame.image.load("pixel-duel-main/assets/sprites/dark-mino/dead/Minotaur_03_Dying_008.png")
dark_mino_dying_10 = pygame.image.load("pixel-duel-main/assets/sprites/dark-mino/dead/Minotaur_03_Dying_009.png")
dark_mino_dying_11 = pygame.image.load("pixel-duel-main/assets/sprites/dark-mino/dead/Minotaur_03_Dying_010.png")
dark_mino_dying_12 = pygame.image.load("pixel-duel-main/assets/sprites/dark-mino/dead/Minotaur_03_Dying_011.png")
dark_mino_dying_13 = pygame.image.load("pixel-duel-main/assets/sprites/dark-mino/dead/Minotaur_03_Dying_012.png")
dark_mino_dying_14 = pygame.image.load("pixel-duel-main/assets/sprites/dark-mino/dead/Minotaur_03_Dying_013.png")
dark_mino_dying_15 = pygame.image.load("pixel-duel-main/assets/sprites/dark-mino/dead/Minotaur_03_Dying_014.png")
dark_mino_dying_list = [dark_mino_dying_1, dark_mino_dying_2, dark_mino_dying_3, dark_mino_dying_4, dark_mino_dying_5, dark_mino_dying_6, dark_mino_dying_7, dark_mino_dying_8, dark_mino_dying_9, dark_mino_dying_10, dark_mino_dying_11, dark_mino_dying_12, dark_mino_dying_13, dark_mino_dying_14, dark_mino_dying_15]

# Satyr
gold_satyr_idle_1 = pygame.image.load("pixel-duel-main/assets/sprites/gold-satyr/idle/Satyr_01_Idle_000.png")
gold_satyr_idle_2 = pygame.image.load("pixel-duel-main/assets/sprites/gold-satyr/idle/Satyr_01_Idle_001.png")
gold_satyr_idle_3 = pygame.image.load("pixel-duel-main/assets/sprites/gold-satyr/idle/Satyr_01_Idle_002.png")
gold_satyr_idle_4 = pygame.image.load("pixel-duel-main/assets/sprites/gold-satyr/idle/Satyr_01_Idle_003.png")
gold_satyr_idle_5 = pygame.image.load("pixel-duel-main/assets/sprites/gold-satyr/idle/Satyr_01_Idle_004.png")
gold_satyr_idle_6 = pygame.image.load("pixel-duel-main/assets/sprites/gold-satyr/idle/Satyr_01_Idle_005.png")
gold_satyr_idle_7 = pygame.image.load("pixel-duel-main/assets/sprites/gold-satyr/idle/Satyr_01_Idle_006.png")
gold_satyr_idle_8 = pygame.image.load("pixel-duel-main/assets/sprites/gold-satyr/idle/Satyr_01_Idle_007.png")
gold_satyr_idle_9 = pygame.image.load("pixel-duel-main/assets/sprites/gold-satyr/idle/Satyr_01_Idle_008.png")
gold_satyr_idle_10 = pygame.image.load("pixel-duel-main/assets/sprites/gold-satyr/idle/Satyr_01_Idle_009.png")
gold_satyr_idle_11 = pygame.image.load("pixel-duel-main/assets/sprites/gold-satyr/idle/Satyr_01_Idle_010.png")
gold_satyr_idle_12 = pygame.image.load("pixel-duel-main/assets/sprites/gold-satyr/idle/Satyr_01_Idle_011.png")
gold_satyr_idle_list = [gold_satyr_idle_1, gold_satyr_idle_2, gold_satyr_idle_3, gold_satyr_idle_4, gold_satyr_idle_5, gold_satyr_idle_6, gold_satyr_idle_7, gold_satyr_idle_8, gold_satyr_idle_9, gold_satyr_idle_10, gold_satyr_idle_11, gold_satyr_idle_12]

gold_satyr_running_1 = pygame.image.load("pixel-duel-main/assets/sprites/gold-satyr/running/Satyr_01_Walking_000.png")
gold_satyr_running_2 = pygame.image.load("pixel-duel-main/assets/sprites/gold-satyr/running/Satyr_01_Walking_001.png")
gold_satyr_running_3 = pygame.image.load("pixel-duel-main/assets/sprites/gold-satyr/running/Satyr_01_Walking_002.png")
gold_satyr_running_4 = pygame.image.load("pixel-duel-main/assets/sprites/gold-satyr/running/Satyr_01_Walking_003.png")
gold_satyr_running_5 = pygame.image.load("pixel-duel-main/assets/sprites/gold-satyr/running/Satyr_01_Walking_004.png")
gold_satyr_running_6 = pygame.image.load("pixel-duel-main/assets/sprites/gold-satyr/running/Satyr_01_Walking_005.png")
gold_satyr_running_7 = pygame.image.load("pixel-duel-main/assets/sprites/gold-satyr/running/Satyr_01_Walking_006.png")
gold_satyr_running_8 = pygame.image.load("pixel-duel-main/assets/sprites/gold-satyr/running/Satyr_01_Walking_007.png")
gold_satyr_running_9 = pygame.image.load("pixel-duel-main/assets/sprites/gold-satyr/running/Satyr_01_Walking_008.png")
gold_satyr_running_10 = pygame.image.load("pixel-duel-main/assets/sprites/gold-satyr/running/Satyr_01_Walking_009.png")
gold_satyr_running_11 = pygame.image.load("pixel-duel-main/assets/sprites/gold-satyr/running/Satyr_01_Walking_010.png")
gold_satyr_running_12 = pygame.image.load("pixel-duel-main/assets/sprites/gold-satyr/running/Satyr_01_Walking_011.png")
gold_satyr_running_13 = pygame.image.load("pixel-duel-main/assets/sprites/gold-satyr/running/Satyr_01_Walking_012.png")
gold_satyr_running_14 = pygame.image.load("pixel-duel-main/assets/sprites/gold-satyr/running/Satyr_01_Walking_013.png")
gold_satyr_running_15 = pygame.image.load("pixel-duel-main/assets/sprites/gold-satyr/running/Satyr_01_Walking_014.png")
gold_satyr_running_16 = pygame.image.load("pixel-duel-main/assets/sprites/gold-satyr/running/Satyr_01_Walking_015.png")
gold_satyr_running_17 = pygame.image.load("pixel-duel-main/assets/sprites/gold-satyr/running/Satyr_01_Walking_016.png")
gold_satyr_running_18 = pygame.image.load("pixel-duel-main/assets/sprites/gold-satyr/running/Satyr_01_Walking_017.png")
gold_satyr_running_list = [gold_satyr_running_1, gold_satyr_running_2, gold_satyr_running_3, gold_satyr_running_4, gold_satyr_running_5, gold_satyr_running_6, gold_satyr_running_7, gold_satyr_running_8, gold_satyr_running_9, gold_satyr_running_10, gold_satyr_running_11, gold_satyr_running_12, gold_satyr_running_13, gold_satyr_running_14, gold_satyr_running_15, gold_satyr_running_16, gold_satyr_running_17, gold_satyr_running_18]

gold_satyr_attacking_1 = pygame.image.load("pixel-duel-main/assets/sprites/gold-satyr/attacking/Satyr_01_Attacking_000.png")
gold_satyr_attacking_2 = pygame.image.load("pixel-duel-main/assets/sprites/gold-satyr/attacking/Satyr_01_Attacking_001.png")
gold_satyr_attacking_3 = pygame.image.load("pixel-duel-main/assets/sprites/gold-satyr/attacking/Satyr_01_Attacking_002.png")
gold_satyr_attacking_4 = pygame.image.load("pixel-duel-main/assets/sprites/gold-satyr/attacking/Satyr_01_Attacking_003.png")
gold_satyr_attacking_5 = pygame.image.load("pixel-duel-main/assets/sprites/gold-satyr/attacking/Satyr_01_Attacking_004.png")
gold_satyr_attacking_6 = pygame.image.load("pixel-duel-main/assets/sprites/gold-satyr/attacking/Satyr_01_Attacking_005.png")
gold_satyr_attacking_7 = pygame.image.load("pixel-duel-main/assets/sprites/gold-satyr/attacking/Satyr_01_Attacking_006.png")
gold_satyr_attacking_8 = pygame.image.load("pixel-duel-main/assets/sprites/gold-satyr/attacking/Satyr_01_Attacking_007.png")
gold_satyr_attacking_9 = pygame.image.load("pixel-duel-main/assets/sprites/gold-satyr/attacking/Satyr_01_Attacking_008.png")
gold_satyr_attacking_10 = pygame.image.load("pixel-duel-main/assets/sprites/gold-satyr/attacking/Satyr_01_Attacking_009.png")
gold_satyr_attacking_11 = pygame.image.load("pixel-duel-main/assets/sprites/gold-satyr/attacking/Satyr_01_Attacking_010.png")
gold_satyr_attacking_12 = pygame.image.load("pixel-duel-main/assets/sprites/gold-satyr/attacking/Satyr_01_Attacking_011.png")
gold_satyr_attacking_list = [gold_satyr_attacking_1, gold_satyr_attacking_2, gold_satyr_attacking_3, gold_satyr_attacking_4, gold_satyr_attacking_5, gold_satyr_attacking_6, gold_satyr_attacking_7, gold_satyr_attacking_8, gold_satyr_attacking_9, gold_satyr_attacking_10, gold_satyr_attacking_11, gold_satyr_attacking_12]

gold_satyr_hurt_1 = pygame.image.load("pixel-duel-main/assets/sprites/gold-satyr/hurt/Satyr_01_Hurt_000.png")
gold_satyr_hurt_2 = pygame.image.load("pixel-duel-main/assets/sprites/gold-satyr/hurt/Satyr_01_Hurt_001.png")
gold_satyr_hurt_3 = pygame.image.load("pixel-duel-main/assets/sprites/gold-satyr/hurt/Satyr_01_Hurt_002.png")
gold_satyr_hurt_4 = pygame.image.load("pixel-duel-main/assets/sprites/gold-satyr/hurt/Satyr_01_Hurt_003.png")
gold_satyr_hurt_5 = pygame.image.load("pixel-duel-main/assets/sprites/gold-satyr/hurt/Satyr_01_Hurt_004.png")
gold_satyr_hurt_6 = pygame.image.load("pixel-duel-main/assets/sprites/gold-satyr/hurt/Satyr_01_Hurt_005.png")
gold_satyr_hurt_7 = pygame.image.load("pixel-duel-main/assets/sprites/gold-satyr/hurt/Satyr_01_Hurt_006.png")
gold_satyr_hurt_8 = pygame.image.load("pixel-duel-main/assets/sprites/gold-satyr/hurt/Satyr_01_Hurt_007.png")
gold_satyr_hurt_9 = pygame.image.load("pixel-duel-main/assets/sprites/gold-satyr/hurt/Satyr_01_Hurt_008.png")
gold_satyr_hurt_10 = pygame.image.load("pixel-duel-main/assets/sprites/gold-satyr/hurt/Satyr_01_Hurt_009.png")
gold_satyr_hurt_11 = pygame.image.load("pixel-duel-main/assets/sprites/gold-satyr/hurt/Satyr_01_Hurt_010.png")
gold_satyr_hurt_12 = pygame.image.load("pixel-duel-main/assets/sprites/gold-satyr/hurt/Satyr_01_Hurt_011.png")
gold_satyr_hurt_list = [gold_satyr_hurt_1, gold_satyr_hurt_2, gold_satyr_hurt_3, gold_satyr_hurt_4, gold_satyr_hurt_5, gold_satyr_hurt_6, gold_satyr_hurt_7, gold_satyr_hurt_8, gold_satyr_hurt_9, gold_satyr_hurt_10, gold_satyr_hurt_11, gold_satyr_hurt_12]

gold_satyr_dying_1 = pygame.image.load("pixel-duel-main/assets/sprites/gold-satyr/dead/Satyr_01_Dying_000.png")
gold_satyr_dying_2 = pygame.image.load("pixel-duel-main/assets/sprites/gold-satyr/dead/Satyr_01_Dying_001.png")
gold_satyr_dying_3 = pygame.image.load("pixel-duel-main/assets/sprites/gold-satyr/dead/Satyr_01_Dying_002.png")
gold_satyr_dying_4 = pygame.image.load("pixel-duel-main/assets/sprites/gold-satyr/dead/Satyr_01_Dying_003.png")
gold_satyr_dying_5 = pygame.image.load("pixel-duel-main/assets/sprites/gold-satyr/dead/Satyr_01_Dying_004.png")
gold_satyr_dying_6 = pygame.image.load("pixel-duel-main/assets/sprites/gold-satyr/dead/Satyr_01_Dying_005.png")
gold_satyr_dying_7 = pygame.image.load("pixel-duel-main/assets/sprites/gold-satyr/dead/Satyr_01_Dying_006.png")
gold_satyr_dying_8 = pygame.image.load("pixel-duel-main/assets/sprites/gold-satyr/dead/Satyr_01_Dying_007.png")
gold_satyr_dying_9 = pygame.image.load("pixel-duel-main/assets/sprites/gold-satyr/dead/Satyr_01_Dying_008.png")
gold_satyr_dying_10 = pygame.image.load("pixel-duel-main/assets/sprites/gold-satyr/dead/Satyr_01_Dying_009.png")
gold_satyr_dying_11 = pygame.image.load("pixel-duel-main/assets/sprites/gold-satyr/dead/Satyr_01_Dying_010.png")
gold_satyr_dying_12 = pygame.image.load("pixel-duel-main/assets/sprites/gold-satyr/dead/Satyr_01_Dying_011.png")
gold_satyr_dying_13 = pygame.image.load("pixel-duel-main/assets/sprites/gold-satyr/dead/Satyr_01_Dying_012.png")
gold_satyr_dying_14 = pygame.image.load("pixel-duel-main/assets/sprites/gold-satyr/dead/Satyr_01_Dying_013.png")
gold_satyr_dying_15 = pygame.image.load("pixel-duel-main/assets/sprites/gold-satyr/dead/Satyr_01_Dying_014.png")
gold_satyr_dying_list = [gold_satyr_dying_1, gold_satyr_dying_2, gold_satyr_dying_3, gold_satyr_dying_4, gold_satyr_dying_5, gold_satyr_dying_6, gold_satyr_dying_7, gold_satyr_dying_8, gold_satyr_dying_9, gold_satyr_dying_10, gold_satyr_dying_11, gold_satyr_dying_12]

# Brown
brown_satyr_idle_1 = pygame.image.load("pixel-duel-main/assets/sprites/brown-satyr/idle/Satyr_03_Idle_000.png")
brown_satyr_idle_2 = pygame.image.load("pixel-duel-main/assets/sprites/brown-satyr/idle/Satyr_03_Idle_001.png")
brown_satyr_idle_3 = pygame.image.load("pixel-duel-main/assets/sprites/brown-satyr/idle/Satyr_03_Idle_002.png")
brown_satyr_idle_4 = pygame.image.load("pixel-duel-main/assets/sprites/brown-satyr/idle/Satyr_03_Idle_003.png")
brown_satyr_idle_5 = pygame.image.load("pixel-duel-main/assets/sprites/brown-satyr/idle/Satyr_03_Idle_004.png")
brown_satyr_idle_6 = pygame.image.load("pixel-duel-main/assets/sprites/brown-satyr/idle/Satyr_03_Idle_005.png")
brown_satyr_idle_7 = pygame.image.load("pixel-duel-main/assets/sprites/brown-satyr/idle/Satyr_03_Idle_006.png")
brown_satyr_idle_8 = pygame.image.load("pixel-duel-main/assets/sprites/brown-satyr/idle/Satyr_03_Idle_007.png")
brown_satyr_idle_9 = pygame.image.load("pixel-duel-main/assets/sprites/brown-satyr/idle/Satyr_03_Idle_008.png")
brown_satyr_idle_10 = pygame.image.load("pixel-duel-main/assets/sprites/brown-satyr/idle/Satyr_03_Idle_009.png")
brown_satyr_idle_11 = pygame.image.load("pixel-duel-main/assets/sprites/brown-satyr/idle/Satyr_03_Idle_010.png")
brown_satyr_idle_12 = pygame.image.load("pixel-duel-main/assets/sprites/brown-satyr/idle/Satyr_03_Idle_011.png")
brown_satyr_idle_list = [brown_satyr_idle_1, brown_satyr_idle_2, brown_satyr_idle_3, brown_satyr_idle_4, brown_satyr_idle_5, brown_satyr_idle_6, brown_satyr_idle_7, brown_satyr_idle_8, brown_satyr_idle_9, brown_satyr_idle_10, brown_satyr_idle_11, brown_satyr_idle_12]

brown_satyr_running_1 = pygame.image.load("pixel-duel-main/assets/sprites/brown-satyr/running/Satyr_03_Walking_000.png")
brown_satyr_running_2 = pygame.image.load("pixel-duel-main/assets/sprites/brown-satyr/running/Satyr_03_Walking_001.png")
brown_satyr_running_3 = pygame.image.load("pixel-duel-main/assets/sprites/brown-satyr/running/Satyr_03_Walking_002.png")
brown_satyr_running_4 = pygame.image.load("pixel-duel-main/assets/sprites/brown-satyr/running/Satyr_03_Walking_003.png")
brown_satyr_running_5 = pygame.image.load("pixel-duel-main/assets/sprites/brown-satyr/running/Satyr_03_Walking_004.png")
brown_satyr_running_6 = pygame.image.load("pixel-duel-main/assets/sprites/brown-satyr/running/Satyr_03_Walking_005.png")
brown_satyr_running_7 = pygame.image.load("pixel-duel-main/assets/sprites/brown-satyr/running/Satyr_03_Walking_006.png")
brown_satyr_running_8 = pygame.image.load("pixel-duel-main/assets/sprites/brown-satyr/running/Satyr_03_Walking_007.png")
brown_satyr_running_9 = pygame.image.load("pixel-duel-main/assets/sprites/brown-satyr/running/Satyr_03_Walking_008.png")
brown_satyr_running_10 = pygame.image.load("pixel-duel-main/assets/sprites/brown-satyr/running/Satyr_03_Walking_009.png")
brown_satyr_running_11 = pygame.image.load("pixel-duel-main/assets/sprites/brown-satyr/running/Satyr_03_Walking_010.png")
brown_satyr_running_12 = pygame.image.load("pixel-duel-main/assets/sprites/brown-satyr/running/Satyr_03_Walking_011.png")
brown_satyr_running_13 = pygame.image.load("pixel-duel-main/assets/sprites/brown-satyr/running/Satyr_03_Walking_012.png")
brown_satyr_running_14 = pygame.image.load("pixel-duel-main/assets/sprites/brown-satyr/running/Satyr_03_Walking_013.png")
brown_satyr_running_15 = pygame.image.load("pixel-duel-main/assets/sprites/brown-satyr/running/Satyr_03_Walking_014.png")
brown_satyr_running_16 = pygame.image.load("pixel-duel-main/assets/sprites/brown-satyr/running/Satyr_03_Walking_015.png")
brown_satyr_running_17 = pygame.image.load("pixel-duel-main/assets/sprites/brown-satyr/running/Satyr_03_Walking_016.png")
brown_satyr_running_18 = pygame.image.load("pixel-duel-main/assets/sprites/brown-satyr/running/Satyr_03_Walking_017.png")
brown_satyr_running_list = [brown_satyr_running_1, brown_satyr_running_2, brown_satyr_running_3, brown_satyr_running_4, brown_satyr_running_5, brown_satyr_running_6, brown_satyr_running_7, brown_satyr_running_8, brown_satyr_running_9, brown_satyr_running_10, brown_satyr_running_11, brown_satyr_running_12, brown_satyr_running_13, brown_satyr_running_14, brown_satyr_running_15, brown_satyr_running_16, brown_satyr_running_17, brown_satyr_running_18]

brown_satyr_attacking_1 = pygame.image.load("pixel-duel-main/assets/sprites/brown-satyr/attacking/Satyr_03_Attacking_000.png")
brown_satyr_attacking_2 = pygame.image.load("pixel-duel-main/assets/sprites/brown-satyr/attacking/Satyr_03_Attacking_001.png")
brown_satyr_attacking_3 = pygame.image.load("pixel-duel-main/assets/sprites/brown-satyr/attacking/Satyr_03_Attacking_002.png")
brown_satyr_attacking_4 = pygame.image.load("pixel-duel-main/assets/sprites/brown-satyr/attacking/Satyr_03_Attacking_003.png")
brown_satyr_attacking_5 = pygame.image.load("pixel-duel-main/assets/sprites/brown-satyr/attacking/Satyr_03_Attacking_004.png")
brown_satyr_attacking_6 = pygame.image.load("pixel-duel-main/assets/sprites/brown-satyr/attacking/Satyr_03_Attacking_005.png")
brown_satyr_attacking_7 = pygame.image.load("pixel-duel-main/assets/sprites/brown-satyr/attacking/Satyr_03_Attacking_006.png")
brown_satyr_attacking_8 = pygame.image.load("pixel-duel-main/assets/sprites/brown-satyr/attacking/Satyr_03_Attacking_007.png")
brown_satyr_attacking_9 = pygame.image.load("pixel-duel-main/assets/sprites/brown-satyr/attacking/Satyr_03_Attacking_008.png")
brown_satyr_attacking_10 = pygame.image.load("pixel-duel-main/assets/sprites/brown-satyr/attacking/Satyr_03_Attacking_009.png")
brown_satyr_attacking_11 = pygame.image.load("pixel-duel-main/assets/sprites/brown-satyr/attacking/Satyr_03_Attacking_010.png")
brown_satyr_attacking_12 = pygame.image.load("pixel-duel-main/assets/sprites/brown-satyr/attacking/Satyr_03_Attacking_011.png")
brown_satyr_attacking_list = [brown_satyr_attacking_1, brown_satyr_attacking_2, brown_satyr_attacking_3, brown_satyr_attacking_4, brown_satyr_attacking_5, brown_satyr_attacking_6, brown_satyr_attacking_7, brown_satyr_attacking_8, brown_satyr_attacking_9, brown_satyr_attacking_10, brown_satyr_attacking_11, brown_satyr_attacking_12]

brown_satyr_hurt_1 = pygame.image.load("pixel-duel-main/assets/sprites/brown-satyr/hurt/Satyr_03_Hurt_000.png")
brown_satyr_hurt_2 = pygame.image.load("pixel-duel-main/assets/sprites/brown-satyr/hurt/Satyr_03_Hurt_001.png")
brown_satyr_hurt_3 = pygame.image.load("pixel-duel-main/assets/sprites/brown-satyr/hurt/Satyr_03_Hurt_002.png")
brown_satyr_hurt_4 = pygame.image.load("pixel-duel-main/assets/sprites/brown-satyr/hurt/Satyr_03_Hurt_003.png")
brown_satyr_hurt_5 = pygame.image.load("pixel-duel-main/assets/sprites/brown-satyr/hurt/Satyr_03_Hurt_004.png")
brown_satyr_hurt_6 = pygame.image.load("pixel-duel-main/assets/sprites/brown-satyr/hurt/Satyr_03_Hurt_005.png")
brown_satyr_hurt_7 = pygame.image.load("pixel-duel-main/assets/sprites/brown-satyr/hurt/Satyr_03_Hurt_006.png")
brown_satyr_hurt_8 = pygame.image.load("pixel-duel-main/assets/sprites/brown-satyr/hurt/Satyr_03_Hurt_007.png")
brown_satyr_hurt_9 = pygame.image.load("pixel-duel-main/assets/sprites/brown-satyr/hurt/Satyr_03_Hurt_008.png")
brown_satyr_hurt_10 = pygame.image.load("pixel-duel-main/assets/sprites/brown-satyr/hurt/Satyr_03_Hurt_009.png")
brown_satyr_hurt_11 = pygame.image.load("pixel-duel-main/assets/sprites/brown-satyr/hurt/Satyr_03_Hurt_010.png")
brown_satyr_hurt_12 = pygame.image.load("pixel-duel-main/assets/sprites/brown-satyr/hurt/Satyr_03_Hurt_011.png")
brown_satyr_hurt_list = [brown_satyr_hurt_1, brown_satyr_hurt_2, brown_satyr_hurt_3, brown_satyr_hurt_4, brown_satyr_hurt_5, brown_satyr_hurt_6, brown_satyr_hurt_7, brown_satyr_hurt_8, brown_satyr_hurt_9, brown_satyr_hurt_10, brown_satyr_hurt_11, brown_satyr_hurt_12]

brown_satyr_dying_1 = pygame.image.load("pixel-duel-main/assets/sprites/brown-satyr/dead/Satyr_03_Dying_000.png")
brown_satyr_dying_2 = pygame.image.load("pixel-duel-main/assets/sprites/brown-satyr/dead/Satyr_03_Dying_001.png")
brown_satyr_dying_3 = pygame.image.load("pixel-duel-main/assets/sprites/brown-satyr/dead/Satyr_03_Dying_002.png")
brown_satyr_dying_4 = pygame.image.load("pixel-duel-main/assets/sprites/brown-satyr/dead/Satyr_03_Dying_003.png")
brown_satyr_dying_5 = pygame.image.load("pixel-duel-main/assets/sprites/brown-satyr/dead/Satyr_03_Dying_004.png")
brown_satyr_dying_6 = pygame.image.load("pixel-duel-main/assets/sprites/brown-satyr/dead/Satyr_03_Dying_005.png")
brown_satyr_dying_7 = pygame.image.load("pixel-duel-main/assets/sprites/brown-satyr/dead/Satyr_03_Dying_006.png")
brown_satyr_dying_8 = pygame.image.load("pixel-duel-main/assets/sprites/brown-satyr/dead/Satyr_03_Dying_007.png")
brown_satyr_dying_9 = pygame.image.load("pixel-duel-main/assets/sprites/brown-satyr/dead/Satyr_03_Dying_008.png")
brown_satyr_dying_10 = pygame.image.load("pixel-duel-main/assets/sprites/brown-satyr/dead/Satyr_03_Dying_009.png")
brown_satyr_dying_11 = pygame.image.load("pixel-duel-main/assets/sprites/brown-satyr/dead/Satyr_03_Dying_010.png")
brown_satyr_dying_12 = pygame.image.load("pixel-duel-main/assets/sprites/brown-satyr/dead/Satyr_03_Dying_011.png")
brown_satyr_dying_13 = pygame.image.load("pixel-duel-main/assets/sprites/brown-satyr/dead/Satyr_03_Dying_012.png")
brown_satyr_dying_14 = pygame.image.load("pixel-duel-main/assets/sprites/brown-satyr/dead/Satyr_03_Dying_013.png")
brown_satyr_dying_15 = pygame.image.load("pixel-duel-main/assets/sprites/brown-satyr/dead/Satyr_03_Dying_014.png")
brown_satyr_dying_list = [brown_satyr_dying_1, brown_satyr_dying_2, brown_satyr_dying_3, brown_satyr_dying_4, brown_satyr_dying_5, brown_satyr_dying_6, brown_satyr_dying_7, brown_satyr_dying_8, brown_satyr_dying_9, brown_satyr_dying_10, brown_satyr_dying_11, brown_satyr_dying_12]

# Human
human_satyr_idle_1 = pygame.image.load("pixel-duel-main/assets/sprites/human-satyr/idle/Satyr_02_Idle_000.png")
human_satyr_idle_2 = pygame.image.load("pixel-duel-main/assets/sprites/human-satyr/idle/Satyr_02_Idle_001.png")
human_satyr_idle_3 = pygame.image.load("pixel-duel-main/assets/sprites/human-satyr/idle/Satyr_02_Idle_002.png")
human_satyr_idle_4 = pygame.image.load("pixel-duel-main/assets/sprites/human-satyr/idle/Satyr_02_Idle_003.png")
human_satyr_idle_5 = pygame.image.load("pixel-duel-main/assets/sprites/human-satyr/idle/Satyr_02_Idle_004.png")
human_satyr_idle_6 = pygame.image.load("pixel-duel-main/assets/sprites/human-satyr/idle/Satyr_02_Idle_005.png")
human_satyr_idle_7 = pygame.image.load("pixel-duel-main/assets/sprites/human-satyr/idle/Satyr_02_Idle_006.png")
human_satyr_idle_8 = pygame.image.load("pixel-duel-main/assets/sprites/human-satyr/idle/Satyr_02_Idle_007.png")
human_satyr_idle_9 = pygame.image.load("pixel-duel-main/assets/sprites/human-satyr/idle/Satyr_02_Idle_008.png")
human_satyr_idle_10 = pygame.image.load("pixel-duel-main/assets/sprites/human-satyr/idle/Satyr_02_Idle_009.png")
human_satyr_idle_11 = pygame.image.load("pixel-duel-main/assets/sprites/human-satyr/idle/Satyr_02_Idle_010.png")
human_satyr_idle_12 = pygame.image.load("pixel-duel-main/assets/sprites/human-satyr/idle/Satyr_02_Idle_011.png")
human_satyr_idle_list = [human_satyr_idle_1, human_satyr_idle_2, human_satyr_idle_3, human_satyr_idle_4, human_satyr_idle_5, human_satyr_idle_6, human_satyr_idle_7, human_satyr_idle_8, human_satyr_idle_9, human_satyr_idle_10, human_satyr_idle_11, human_satyr_idle_12]

human_satyr_running_1 = pygame.image.load("pixel-duel-main/assets/sprites/human-satyr/running/Satyr_02_Walking_000.png")
human_satyr_running_2 = pygame.image.load("pixel-duel-main/assets/sprites/human-satyr/running/Satyr_02_Walking_001.png")
human_satyr_running_3 = pygame.image.load("pixel-duel-main/assets/sprites/human-satyr/running/Satyr_02_Walking_002.png")
human_satyr_running_4 = pygame.image.load("pixel-duel-main/assets/sprites/human-satyr/running/Satyr_02_Walking_003.png")
human_satyr_running_5 = pygame.image.load("pixel-duel-main/assets/sprites/human-satyr/running/Satyr_02_Walking_004.png")
human_satyr_running_6 = pygame.image.load("pixel-duel-main/assets/sprites/human-satyr/running/Satyr_02_Walking_005.png")
human_satyr_running_7 = pygame.image.load("pixel-duel-main/assets/sprites/human-satyr/running/Satyr_02_Walking_006.png")
human_satyr_running_8 = pygame.image.load("pixel-duel-main/assets/sprites/human-satyr/running/Satyr_02_Walking_007.png")
human_satyr_running_9 = pygame.image.load("pixel-duel-main/assets/sprites/human-satyr/running/Satyr_02_Walking_008.png")
human_satyr_running_10 = pygame.image.load("pixel-duel-main/assets/sprites/human-satyr/running/Satyr_02_Walking_009.png")
human_satyr_running_11 = pygame.image.load("pixel-duel-main/assets/sprites/human-satyr/running/Satyr_02_Walking_010.png")
human_satyr_running_12 = pygame.image.load("pixel-duel-main/assets/sprites/human-satyr/running/Satyr_02_Walking_011.png")
human_satyr_running_13 = pygame.image.load("pixel-duel-main/assets/sprites/human-satyr/running/Satyr_02_Walking_012.png")
human_satyr_running_14 = pygame.image.load("pixel-duel-main/assets/sprites/human-satyr/running/Satyr_02_Walking_013.png")
human_satyr_running_15 = pygame.image.load("pixel-duel-main/assets/sprites/human-satyr/running/Satyr_02_Walking_014.png")
human_satyr_running_16 = pygame.image.load("pixel-duel-main/assets/sprites/human-satyr/running/Satyr_02_Walking_015.png")
human_satyr_running_17 = pygame.image.load("pixel-duel-main/assets/sprites/human-satyr/running/Satyr_02_Walking_016.png")
human_satyr_running_18 = pygame.image.load("pixel-duel-main/assets/sprites/human-satyr/running/Satyr_02_Walking_017.png")
human_satyr_running_list = [human_satyr_running_1, human_satyr_running_2, human_satyr_running_3, human_satyr_running_4, human_satyr_running_5, human_satyr_running_6, human_satyr_running_7, human_satyr_running_8, human_satyr_running_9, human_satyr_running_10, human_satyr_running_11, human_satyr_running_12, human_satyr_running_13, human_satyr_running_14, human_satyr_running_15, human_satyr_running_16, human_satyr_running_17, human_satyr_running_18]

human_satyr_attacking_1 = pygame.image.load("pixel-duel-main/assets/sprites/human-satyr/attacking/Satyr_02_Attacking_000.png")
human_satyr_attacking_2 = pygame.image.load("pixel-duel-main/assets/sprites/human-satyr/attacking/Satyr_02_Attacking_001.png")
human_satyr_attacking_3 = pygame.image.load("pixel-duel-main/assets/sprites/human-satyr/attacking/Satyr_02_Attacking_002.png")
human_satyr_attacking_4 = pygame.image.load("pixel-duel-main/assets/sprites/human-satyr/attacking/Satyr_02_Attacking_003.png")
human_satyr_attacking_5 = pygame.image.load("pixel-duel-main/assets/sprites/human-satyr/attacking/Satyr_02_Attacking_004.png")
human_satyr_attacking_6 = pygame.image.load("pixel-duel-main/assets/sprites/human-satyr/attacking/Satyr_02_Attacking_005.png")
human_satyr_attacking_7 = pygame.image.load("pixel-duel-main/assets/sprites/human-satyr/attacking/Satyr_02_Attacking_006.png")
human_satyr_attacking_8 = pygame.image.load("pixel-duel-main/assets/sprites/human-satyr/attacking/Satyr_02_Attacking_007.png")
human_satyr_attacking_9 = pygame.image.load("pixel-duel-main/assets/sprites/human-satyr/attacking/Satyr_02_Attacking_008.png")
human_satyr_attacking_10 = pygame.image.load("pixel-duel-main/assets/sprites/human-satyr/attacking/Satyr_02_Attacking_009.png")
human_satyr_attacking_11 = pygame.image.load("pixel-duel-main/assets/sprites/human-satyr/attacking/Satyr_02_Attacking_010.png")
human_satyr_attacking_12 = pygame.image.load("pixel-duel-main/assets/sprites/human-satyr/attacking/Satyr_02_Attacking_011.png")
human_satyr_attacking_list = [human_satyr_attacking_1, human_satyr_attacking_2, human_satyr_attacking_3, human_satyr_attacking_4, human_satyr_attacking_5, human_satyr_attacking_6, human_satyr_attacking_7, human_satyr_attacking_8, human_satyr_attacking_9, human_satyr_attacking_10, human_satyr_attacking_11, human_satyr_attacking_12]

human_satyr_hurt_1 = pygame.image.load("pixel-duel-main/assets/sprites/human-satyr/hurt/Satyr_02_Hurt_000.png")
human_satyr_hurt_2 = pygame.image.load("pixel-duel-main/assets/sprites/human-satyr/hurt/Satyr_02_Hurt_001.png")
human_satyr_hurt_3 = pygame.image.load("pixel-duel-main/assets/sprites/human-satyr/hurt/Satyr_02_Hurt_002.png")
human_satyr_hurt_4 = pygame.image.load("pixel-duel-main/assets/sprites/human-satyr/hurt/Satyr_02_Hurt_003.png")
human_satyr_hurt_5 = pygame.image.load("pixel-duel-main/assets/sprites/human-satyr/hurt/Satyr_02_Hurt_004.png")
human_satyr_hurt_6 = pygame.image.load("pixel-duel-main/assets/sprites/human-satyr/hurt/Satyr_02_Hurt_005.png")
human_satyr_hurt_7 = pygame.image.load("pixel-duel-main/assets/sprites/human-satyr/hurt/Satyr_02_Hurt_006.png")
human_satyr_hurt_8 = pygame.image.load("pixel-duel-main/assets/sprites/human-satyr/hurt/Satyr_02_Hurt_007.png")
human_satyr_hurt_9 = pygame.image.load("pixel-duel-main/assets/sprites/human-satyr/hurt/Satyr_02_Hurt_008.png")
human_satyr_hurt_10 = pygame.image.load("pixel-duel-main/assets/sprites/human-satyr/hurt/Satyr_02_Hurt_009.png")
human_satyr_hurt_11 = pygame.image.load("pixel-duel-main/assets/sprites/human-satyr/hurt/Satyr_02_Hurt_010.png")
human_satyr_hurt_12 = pygame.image.load("pixel-duel-main/assets/sprites/human-satyr/hurt/Satyr_02_Hurt_011.png")
human_satyr_hurt_list = [human_satyr_hurt_1, human_satyr_hurt_2, human_satyr_hurt_3, human_satyr_hurt_4, human_satyr_hurt_5, human_satyr_hurt_6, human_satyr_hurt_7, human_satyr_hurt_8, human_satyr_hurt_9, human_satyr_hurt_10, human_satyr_hurt_11, human_satyr_hurt_12]

human_satyr_dying_1 = pygame.image.load("pixel-duel-main/assets/sprites/human-satyr/dead/Satyr_02_Dying_000.png")
human_satyr_dying_2 = pygame.image.load("pixel-duel-main/assets/sprites/human-satyr/dead/Satyr_02_Dying_001.png")
human_satyr_dying_3 = pygame.image.load("pixel-duel-main/assets/sprites/human-satyr/dead/Satyr_02_Dying_002.png")
human_satyr_dying_4 = pygame.image.load("pixel-duel-main/assets/sprites/human-satyr/dead/Satyr_02_Dying_003.png")
human_satyr_dying_5 = pygame.image.load("pixel-duel-main/assets/sprites/human-satyr/dead/Satyr_02_Dying_004.png")
human_satyr_dying_6 = pygame.image.load("pixel-duel-main/assets/sprites/human-satyr/dead/Satyr_02_Dying_005.png")
human_satyr_dying_7 = pygame.image.load("pixel-duel-main/assets/sprites/human-satyr/dead/Satyr_02_Dying_006.png")
human_satyr_dying_8 = pygame.image.load("pixel-duel-main/assets/sprites/human-satyr/dead/Satyr_02_Dying_007.png")
human_satyr_dying_9 = pygame.image.load("pixel-duel-main/assets/sprites/human-satyr/dead/Satyr_02_Dying_008.png")
human_satyr_dying_10 = pygame.image.load("pixel-duel-main/assets/sprites/human-satyr/dead/Satyr_02_Dying_009.png")
human_satyr_dying_11 = pygame.image.load("pixel-duel-main/assets/sprites/human-satyr/dead/Satyr_02_Dying_010.png")
human_satyr_dying_12 = pygame.image.load("pixel-duel-main/assets/sprites/human-satyr/dead/Satyr_02_Dying_011.png")
human_satyr_dying_13 = pygame.image.load("pixel-duel-main/assets/sprites/human-satyr/dead/Satyr_02_Dying_012.png")
human_satyr_dying_14 = pygame.image.load("pixel-duel-main/assets/sprites/human-satyr/dead/Satyr_02_Dying_013.png")
human_satyr_dying_15 = pygame.image.load("pixel-duel-main/assets/sprites/human-satyr/dead/Satyr_02_Dying_014.png")
human_satyr_dying_list = [human_satyr_dying_1, human_satyr_dying_2, human_satyr_dying_3, human_satyr_dying_4, human_satyr_dying_5, human_satyr_dying_6, human_satyr_dying_7, human_satyr_dying_8, human_satyr_dying_9, human_satyr_dying_10, human_satyr_dying_11, human_satyr_dying_12]

# Health image
heart_one = pygame.image.load("pixel-duel-main/assets/hearts/heart1.png")
heart_two = pygame.image.load("pixel-duel-main/assets/hearts/heart2.png")
heart_three = pygame.image.load("pixel-duel-main/assets/hearts/heart3.png")
heart_list = [heart_one, heart_two, heart_three]

# Functions
def display_bg():
    scaled_img = pygame.transform.scale(castle_bg, (WIDTH, HEIGHT))
    screen.blit(scaled_img, (0,0))

def display_hp(player, hp, x, y):
    if player == 1 and fighter_one.hp > 0:
        screen.blit(hp, (x, y))

    elif player == 2 and fighter_two.hp > 0:
        screen.blit(hp, (x, y))

def draw_text(text, font, color, x, y):
    text_surface = font.render(text, True, color)
    text_rect = text_surface.get_rect(topleft=(x, y))
    screen.blit(text_surface, text_rect)
    return text_rect

# fighter_one = Fighter(1, 200, 310, False, fire_golem_idle_list, fire_golem_running_list, fire_golem_attacking_list, fire_golem_hurt_list, fire_golem_dead_list, heart_list, slash_fx)
# fighter_two = Fighter(2, 700, 310, True, fire_golem_idle_list, fire_golem_running_list, fire_golem_attacking_list, fire_golem_hurt_list, fire_golem_dead_list, heart_list, slash_fx)

game_isRunning = True

round_font = pygame.font.Font("pixel-duel-main/font/FT88-Serif.ttf", 50)
count_font = pygame.font.Font("pixel-duel-main/font/FT88-Serif.ttf", 30)

game_round = 1
round_over = False
ROUND_OVER_COOLDOWN = 2000

player_one_wins = False
player_two_wins = False

character_selection_display = False
main_menu_display = True
game_display = False
credits_display = False

player_one_pick = False
player_two_pick = False

# Character Category
one_mino_picked = False
one_golem_picked = False
one_satyr_picked = False

two_mino_picked = False
two_golem_picked = False
two_satyr_picked = False

player_one_category = False
player_two_category = False

# Golem category
one_ice_golem_picked = False
one_fire_golem_picked = False
one_nature_golem_picked = False

two_ice_golem_picked = False
two_fire_golem_picked = False
two_nature_golem_picked = False

# Minotaur category
one_brown_mino_picked = False
one_blue_mino_picked = False
one_dark_mino_picked = False

two_brown_mino_picked = False
two_blue_mino_picked = False
two_dark_mino_picked = False

# Satyr category
one_gold_satyr_picked = False
one_human_satyr_picked = False
one_brown_satyr_picked = False

two_gold_satyr_picked = False
two_human_satyr_picked = False
two_brown_satyr_picked = False

game_over = True


player_one_points = 0
player_two_points = 0

def get_font(size):
    return pygame.font.Font("pixel-duel-main/font/FT88-Serif.ttf", size)

def player_one_character_choice():
    global fighter_one

    if one_ice_golem_picked:
        fighter_one = Fighter(1, 200, 310, False, ice_golem_idle_list, ice_golem_running_list, ice_golem_attacking_list, ice_golem_hurt_list, ice_golem_dead_list, heart_list, slash_fx, "Golem")
        return fighter_one
    elif one_fire_golem_picked:
        fighter_one = Fighter(1, 200, 310, False, fire_golem_idle_list, fire_golem_running_list, fire_golem_attacking_list, fire_golem_hurt_list, fire_golem_dead_list, heart_list, slash_fx, "Golem")
        return fighter_one   
    elif one_nature_golem_picked:
        fighter_one = Fighter(1, 200, 310, False, nature_golem_idle_list, nature_golem_running_list, nature_golem_attacking_list, nature_golem_hurt_list, nature_golem_dead_list, heart_list, slash_fx, "Golem")
        return fighter_one
    if one_brown_mino_picked:
        fighter_one = Fighter(1, 200, 310, False, brown_mino_idle_list, brown_mino_running_list, brown_mino_attacking_list, brown_mino_hurt_list, brown_mino_dying_list, heart_list, slash_fx, "Mino")
        return fighter_one
    elif one_blue_mino_picked:
        fighter_one = Fighter(1, 200, 310, False, blue_mino_idle_list, blue_mino_running_list, blue_mino_attacking_list, blue_mino_hurt_list, blue_mino_dying_list, heart_list, slash_fx, "Mino")
        return fighter_one
    elif one_dark_mino_picked:
        fighter_one = Fighter(1, 200, 310, False, dark_mino_idle_list, dark_mino_running_list, dark_mino_attacking_list, dark_mino_hurt_list, dark_mino_dying_list, heart_list, slash_fx, "Mino")
        return fighter_one
    if one_human_satyr_picked:
        fighter_one = Fighter(1, 200, 310, False, human_satyr_idle_list, human_satyr_running_list, human_satyr_attacking_list, human_satyr_hurt_list, human_satyr_dying_list, heart_list, slash_fx, "Satyr")
        return fighter_one
    elif one_gold_satyr_picked:
        fighter_one = Fighter(1, 200, 310, False, gold_satyr_idle_list, gold_satyr_running_list, gold_satyr_attacking_list, gold_satyr_hurt_list, gold_satyr_dying_list, heart_list, slash_fx, "Satyr")
        return fighter_one
    elif one_brown_satyr_picked:
        fighter_one = Fighter(1, 200, 310, False, brown_satyr_idle_list, brown_satyr_running_list, brown_satyr_attacking_list, brown_satyr_hurt_list, brown_satyr_dying_list, heart_list, slash_fx, "Satyr")
        return fighter_one
    
def player_two_character_choice():
    global fighter_two

    if two_ice_golem_picked:
        fighter_two = Fighter(2, 700, 310, True, ice_golem_idle_list, ice_golem_running_list, ice_golem_attacking_list, ice_golem_hurt_list, ice_golem_dead_list, heart_list, slash_fx, "Golem")
        return fighter_two
    elif two_fire_golem_picked:
        fighter_two = Fighter(2, 700, 310, True, fire_golem_idle_list, fire_golem_running_list, fire_golem_attacking_list, fire_golem_hurt_list, fire_golem_dead_list, heart_list, slash_fx, "Golem")
        return fighter_two
    elif two_nature_golem_picked:
        fighter_two = Fighter(2, 700, 310, True, nature_golem_idle_list, nature_golem_running_list, nature_golem_attacking_list, nature_golem_hurt_list, nature_golem_dead_list, heart_list, slash_fx, "Golem")
        return fighter_two
    if two_brown_mino_picked:
        fighter_two = Fighter(2, 700, 310, True, brown_mino_idle_list, brown_mino_running_list, brown_mino_attacking_list, brown_mino_hurt_list, brown_mino_dying_list, heart_list, slash_fx, "Mino")
        return fighter_two
    elif two_blue_mino_picked:
        fighter_two = Fighter(2, 700, 310, True, blue_mino_idle_list, blue_mino_running_list, blue_mino_attacking_list, blue_mino_hurt_list, blue_mino_dying_list, heart_list, slash_fx, "Mino")
        return fighter_two
    elif two_dark_mino_picked:
        fighter_two = Fighter(2, 700, 310, True, dark_mino_idle_list, dark_mino_running_list, dark_mino_attacking_list, dark_mino_hurt_list, dark_mino_dying_list, heart_list, slash_fx, "Mino")
        return fighter_two
    if two_human_satyr_picked:
        fighter_two = Fighter(2, 700, 310, True, human_satyr_idle_list, human_satyr_running_list, human_satyr_attacking_list, human_satyr_hurt_list, human_satyr_dying_list, heart_list, slash_fx, "Satyr")
        return fighter_two
    elif two_gold_satyr_picked:
        fighter_two = Fighter(2, 700, 310, True, gold_satyr_idle_list, gold_satyr_running_list, gold_satyr_attacking_list, gold_satyr_hurt_list, gold_satyr_dying_list, heart_list, slash_fx, "Satyr")
        return fighter_two
    elif two_brown_satyr_picked:
        fighter_two = Fighter(2, 700, 310, True, brown_satyr_idle_list, brown_satyr_running_list, brown_satyr_attacking_list, brown_satyr_hurt_list, brown_satyr_dying_list, heart_list, slash_fx, "Satyr")
        return fighter_two
    
def reset_fighters():
    global fighter_one, fighter_two
    # Reset player one's fighter
    player_one_character_choice()
    fighter_one.hp = 3
    fighter_one.rect.x = 200
    fighter_one.rect.y = 310
    fighter_one.alive = True

    # Reset player two's fighter
    player_two_character_choice()
    fighter_two.hp = 3
    fighter_two.rect.x = 700
    fighter_two.rect.y = 310
    fighter_two.alive = True

print(game_round, game_over)

def play():
    global fighter_one, fighter_two, intro_countdown, round_over, last_countdown, player_one_wins, player_two_wins, game_round, ROUND_OVER_COOLDOWN, game_isRunning, game_display, player_one_pick, player_two_pick, game_over, player_one_points, player_two_points
    while game_display:
        clock.tick(FPS)
        screen.fill((0, 0, 0))
        display_bg()
        
        display_hp(1, fighter_one.current_hp, 20, 20)
        display_hp(2, fighter_two.current_hp, 800, 20)

        if intro_countdown <= 0:
            fighter_one.move(WIDTH, HEIGHT, screen, fighter_two, round_over)
            fighter_two.move(WIDTH, HEIGHT, screen, fighter_one, round_over)
        else:
            draw_text(str(intro_countdown), count_font, (255, 0, 0), 480, 170)
            if game_round == 1:
                draw_text("ROUND ONE", round_font, (255, 0, 0), 340, 100)
            elif game_round == 2:
                draw_text("FINAL ROUND", round_font, (255, 0, 0), 300, 100)
            elif game_round == 3:
                game_over = True
                game_display = False

            if (pygame.time.get_ticks() - last_countdown) >= 1000:
                intro_countdown -= 1
                last_countdown = pygame.time.get_ticks()

        # Update fighters
        fighter_one.update(fighter_two)
        fighter_two.update(fighter_one)

        # Draw fighters
        fighter_one.draw(screen)
        fighter_two.draw(screen)

        if not round_over:
            if not fighter_one.alive:
                round_over = True
                round_over_time = pygame.time.get_ticks()
                player_two_points += 1
                player_two_wins = True
                game_round += 1

            elif not fighter_two.alive:
                round_over = True
                round_over_time = pygame.time.get_ticks()
                player_one_points += 1
                player_one_wins = True
                game_round += 1

        else:
            if player_one_wins:
                draw_text("PLAYER ONE WINS!", round_font, (255, 0, 0), 230, 100)
            elif player_two_wins:
                draw_text("PLAYER TWO WINS!", round_font, (255, 0, 0), 230, 100)

            if pygame.time.get_ticks() - round_over_time > ROUND_OVER_COOLDOWN:
                player_two_wins = False
                player_one_wins = False
                round_over = False
                intro_countdown = 3
                reset_fighters()

        # Event handler
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        pygame.display.update()

    if game_over:
        display_game_over()

def check_for_input(rect, pos):
    return rect.collidepoint(pos)

def display_game_over():
    global game_display, main_menu_display, character_selection_display, game_over, game_round, player_one_points, player_two_points
    while game_over:
        screen.fill((0, 0, 0))
        display_bg()
        
        scaled_one_character = pygame.transform.scale(fighter_one.character_idle[0], (100 * 2.2, 80 * 2.2))
        scaled_two_character = pygame.transform.scale(fighter_two.character_idle[0], (100 * 2.2, 80 * 2.2))

        if player_one_points > player_two_points:
            draw_text("PLAYER 1 WINS", round_font, (255, 0, 0), 270, 70)
            screen.blit(scaled_one_character, (390, 150))
        elif player_two_points > player_one_points:
            draw_text("PLAYER 2 WINS", round_font, (255, 0, 0), 270, 70)
            screen.blit(scaled_two_character, (390, 150))
        elif player_two_points == player_one_points:
            draw_text("ITS A DRAW ", round_font, (255, 0, 0), 300, 70)
            screen.blit(scaled_one_character, (330, 150))
            screen.blit(scaled_two_character, (450, 150))


        rematch_btn = pygame.image.load("pixel-duel-main/assets/buttons/button_rematch.png")
        scaled_rematch_btn = pygame.transform.scale(rematch_btn, (150, 80))

        menu_btn = pygame.image.load("pixel-duel-main/assets/buttons/button_menu.png")
        scaled_menu_btn = pygame.transform.scale(menu_btn, (150, 80))

        REMATCH_BUTTON = Pindot(image=scaled_rematch_btn, pos=(370, 400), 
                            text_input="", font=get_font(60), base_color="#000000", hovering_color="White")
        MENU_BUTTON = Pindot(image=scaled_menu_btn, pos=(650, 400), 
                            text_input="", font=get_font(60), base_color="#000000", hovering_color="White")

        MENU_MOUSE_POS = pygame.mouse.get_pos()

        for button in [REMATCH_BUTTON, MENU_BUTTON ]:
            button.update(screen)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        
            if event.type == pygame.MOUSEBUTTONDOWN:
                if REMATCH_BUTTON .check_for_input(MENU_MOUSE_POS):
                    game_over = False
                    game_display = True
                    player_two_points = 0
                    player_one_points = 0
                    game_round = 1
                elif MENU_BUTTON.check_for_input(MENU_MOUSE_POS):
                    main_menu_display = True
                    game_over = False
                    game_display = False
                    character_selection_display = False
                    player_two_points = 0
                    player_one_points = 0
                    game_round = 1

        pygame.display.update()

def main_menu():
    global game_display, main_menu_display, character_selection_display, player_one_pick, player_one_category, credits_display
    while main_menu_display:
        screen.fill((0, 0, 0))
        display_bg()

        MENU_MOUSE_POS = pygame.mouse.get_pos()
        
        game_logo = pygame.image.load("pixel-duel-main/assets/buttons/game-logo.png")
        scaled_game_logo = pygame.transform.scale(game_logo, (400 * 1.5, 85 * 1.5))
        game_logo_rect = scaled_game_logo.get_rect(center=(500, 100))

        start_btn = pygame.image.load("pixel-duel-main/assets/buttons/button_start-game.png")
        scaled_start_btn = pygame.transform.scale(start_btn, (100 * 1.5, 75))

        credits_btn = pygame.image.load("pixel-duel-main/assets/buttons/button_credits.png")
        scaled_credits_btn = pygame.transform.scale(credits_btn, (100 * 1.5, 75))

        exit_btn = pygame.image.load("pixel-duel-main/assets/buttons/button_exit.png")
        scaled_exit_btn = pygame.transform.scale(exit_btn, (100 * 1.5, 75))
        
        PLAY_BUTTON = Pindot(image=scaled_start_btn, pos=(500, 250), 
                            text_input="", font=get_font(40), base_color="#000000", hovering_color="White")
        CREDITS_BUTTON = Pindot(image=scaled_credits_btn, pos=(500, 350), 
                            text_input="", font=get_font(40), base_color="#000000", hovering_color="White")
        QUIT_BUTTON = Pindot(image=scaled_exit_btn, pos=(500, 450), 
                            text_input="", font=get_font(40), base_color="#000000", hovering_color="White")

        screen.blit(scaled_game_logo, game_logo_rect)

        for button in [PLAY_BUTTON, CREDITS_BUTTON, QUIT_BUTTON]:
            button.update(screen)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BUTTON.check_for_input(MENU_MOUSE_POS):
                    game_display = False
                    main_menu_display = False
                    character_selection_display = True
                    player_one_pick = True
                    player_one_category = True
                if CREDITS_BUTTON.check_for_input(MENU_MOUSE_POS):
                    main_menu_display = False
                    credits_display = True
                if QUIT_BUTTON.check_for_input(MENU_MOUSE_POS):
                    pygame.quit()
                    sys.exit()

        pygame.display.update()

        if not main_menu_display:
            break

def credits():
    global credits_display, main_menu_display 
    while credits_display:
        CREDITS_MOUSE_POS = pygame.mouse.get_pos()

        screen.fill("Black")

        stubcode = get_font(40).render('STUB CODE 165', True, 'White' )
        sc_rect = stubcode.get_rect(midtop = (520, 100))
        celda = get_font(20).render('Teofilo Celda Jr.', True , 'White' )
        celda_rect = celda.get_rect(midleft = (120, 240))
        dumangon = get_font(20).render('Selwyn Josh Dumangon', True , 'White' )
        dumangon_rect = dumangon.get_rect(midleft = (120, 330))
        dupaya = get_font(20).render('Jonas Dupaya', True , 'White' )
        dupaya_rect = dupaya.get_rect(midleft = (120, 420))
        obrero = get_font(20).render('RV Mae Obrero', True , 'White' )
        obrero_rect = obrero.get_rect(midright = (800, 240))
        suplico = get_font(20).render('Tristan Suplico', True , 'White' )
        suplico_rect = suplico.get_rect(midright = (800, 350))
        
        screen.blit(stubcode, sc_rect)
        screen.blit(celda, celda_rect)
        screen.blit(dumangon, dumangon_rect)
        screen.blit(dupaya, dupaya_rect)
        screen.blit(obrero, obrero_rect)
        screen.blit(suplico, suplico_rect)

        CREDITS_BACK = Pindot(image=None, pos=(520, 500), 
                            text_input="BACK", font=get_font(50), base_color="White", hovering_color="Green")

        CREDITS_BACK.changeColor(CREDITS_MOUSE_POS)
        CREDITS_BACK.update(screen)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if CREDITS_BACK.check_for_input(CREDITS_MOUSE_POS):
                    main_menu_display = True
                    credits_display = False

        pygame.display.update()

        if not credits_display:
            break

while game_isRunning:
    if character_selection_display:
        main_menu_display = False
        game_display = False

        display_bg()

        if player_one_pick:
            if player_one_category:
                draw_text("Player One", round_font, (255, 255, 0), 330, 40)
                draw_text("Choose fighter type", round_font, (255, 255, 0), 170, 100)

                # Player 1 Fighter Type
                # Minotaur
                scaled_mino_img = pygame.transform.scale(brown_mino_idle_1, (100 * 2.2, 80 * 2.2))
                mino_rect = pygame.Rect(230, 170, 110, 140)
                screen.blit(scaled_mino_img, (170, 150))

                # Golem
                scaled_golem_img = pygame.transform.scale(fire_golem_idle_1, (120 * 2.2, 100 * 2.2))
                golem_rect = pygame.Rect(425, 190, 105, 120)
                screen.blit(scaled_golem_img, (350, 130))

                # Satyr
                scaled_satyr_img = pygame.transform.scale(gold_satyr_idle_1, (120 * 2.2, 95 * 2.2))
                satyr_rect = pygame.Rect(625, 195, 115, 115)
                screen.blit(scaled_satyr_img, (550, 150))

                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        sys.exit()
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        if mino_rect.collidepoint(event.pos):
                            player_one_category = False
                            one_mino_picked = True
                        if golem_rect.collidepoint(event.pos):
                            player_one_category = False
                            one_golem_picked = True
                        if satyr_rect.collidepoint(event.pos):
                            player_one_category = False
                            one_satyr_picked = True

            # Minotaur Picked
            if one_mino_picked == True:
                draw_text("Player One", round_font, (255, 255, 0), 330, 40)
                draw_text("Choose a Minotaur", round_font, (255, 255, 0), 200, 100)

                scaled_brown_mino_img = pygame.transform.scale(brown_mino_idle_1, (100 * 2.2, 80 * 2.2))
                brown_mino_rect = pygame.Rect(230, 170, 110, 140)
                screen.blit(scaled_brown_mino_img, (170, 150))

                scaled_blue_mino_img = pygame.transform.scale(blue_mino_idle_1, (100 * 2.2, 80 * 2.2))
                blue_mino_rect = pygame.Rect(440, 170, 110, 140)
                screen.blit(scaled_blue_mino_img, (380, 150))

                scaled_dark_mino_img = pygame.transform.scale(dark_mino_idle_1, (100 * 2.2, 80 * 2.2))
                dark_mino_rect = pygame.Rect(640, 170, 110, 140)
                screen.blit(scaled_dark_mino_img, (580, 150))

                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        sys.exit()
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        if brown_mino_rect.collidepoint(event.pos):
                            fighter_one = Fighter(1, 200, 310, False, brown_mino_idle_list, brown_mino_running_list, brown_mino_attacking_list, brown_mino_hurt_list, brown_mino_dying_list, heart_list, slash_fx, "Mino")
                            one_mino_picked = False
                            one_brown_mino_picked = True
                            player_one_pick = False
                            player_two_pick = True
                            player_two_category = True
                        if blue_mino_rect.collidepoint(event.pos):
                            fighter_one = Fighter(1, 200, 310, False, blue_mino_idle_list, blue_mino_running_list, blue_mino_attacking_list, blue_mino_hurt_list, blue_mino_dying_list, heart_list, slash_fx, "Mino")
                            one_mino_picked = False
                            one_blue_mino_picked = True
                            player_one_pick = False
                            player_two_pick = True
                            player_two_category = True
                        if dark_mino_rect.collidepoint(event.pos):
                            fighter_one = Fighter(1, 200, 310, False, dark_mino_idle_list, dark_mino_running_list, dark_mino_attacking_list, dark_mino_hurt_list, dark_mino_dying_list, heart_list, slash_fx, "Mino")
                            one_mino_picked = False
                            one_dark_mino_picked = True
                            player_one_pick = False
                            player_two_pick = True
                            player_two_category = True
            # Golem picked
            elif one_golem_picked == True:
                draw_text("Player One", round_font, (255, 255, 0), 330, 40)
                draw_text("Choose a Golem", round_font, (255, 255, 0), 240, 100)

                # Fire
                scaled_fire_golem_img = pygame.transform.scale(fire_golem_idle_1, (115 * 2.2, 100 * 2.2))
                fire_golem_rect = pygame.Rect(240, 190, 110, 120)
                screen.blit(scaled_fire_golem_img , (170, 130))

                # Ice
                scaled_ice_golem_img = pygame.transform.scale(ice_golem_idle_1, (115 * 2.2, 100 * 2.2))
                ice_golem_rect = pygame.Rect(435, 190, 110, 120)
                screen.blit(scaled_ice_golem_img, (370, 130))

                # Nature
                scaled_nature_golem_img = pygame.transform.scale(nature_golem_idle_1, (115 * 2.2, 100 * 2.2))
                nature_golem_rect = pygame.Rect(645, 190, 110, 120)
                screen.blit(scaled_nature_golem_img, (580, 130))

                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        sys.exit()
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        if fire_golem_rect.collidepoint(event.pos):
                            fighter_one = Fighter(1, 200, 310, False, fire_golem_idle_list, fire_golem_running_list, fire_golem_attacking_list, fire_golem_hurt_list, fire_golem_dead_list, heart_list, slash_fx, "Golem" )
                            one_golem_picked = False
                            one_fire_golem_picked = True
                            player_one_pick = False
                            player_two_pick = True
                            player_two_category = True
                        if ice_golem_rect.collidepoint(event.pos):
                            fighter_one = Fighter(1, 200, 310, False, ice_golem_idle_list, ice_golem_running_list, ice_golem_attacking_list, ice_golem_hurt_list, ice_golem_dead_list, heart_list, slash_fx, "Golem")
                            one_golem_picked = False
                            one_fice_golem_picked = True                        
                            player_one_pick = False
                            player_two_pick = True
                            player_two_category = True
                        if nature_golem_rect.collidepoint(event.pos):
                            fighter_one = Fighter(1, 200, 310, False, nature_golem_idle_list, nature_golem_running_list, nature_golem_attacking_list, nature_golem_hurt_list, nature_golem_dead_list, heart_list, slash_fx, "Golem")
                            one_golem_picked = False  
                            one_fnature_golem_picked = True                      
                            player_one_pick = False
                            player_two_pick = True
                            player_two_category = True
            # Satyr picked
            elif one_satyr_picked == True:
                draw_text("Player One", round_font, (255, 255, 0), 330, 40)
                draw_text("Choose a Satyr", round_font, (255, 255, 0), 250, 100)

                scaled_brown_satyr_img = pygame.transform.scale(brown_satyr_idle_1, (100 * 2.2, 80 * 2.2))
                brown_satyr_rect = pygame.Rect(230, 170, 110, 115)
                screen.blit(scaled_brown_satyr_img, (170, 150))

                scaled_human_satyr_img = pygame.transform.scale(human_satyr_idle_1, (100 * 2.2, 80 * 2.2))
                human_satyr_rect = pygame.Rect(440, 170, 110, 115)
                screen.blit(scaled_human_satyr_img, (380, 150))

                scaled_gold_satyr_img = pygame.transform.scale(gold_satyr_idle_1, (100 * 2.2, 80 * 2.2))
                gold_satyr_rect = pygame.Rect(625, 170, 110, 115)
                screen.blit(scaled_gold_satyr_img, (570, 150))

                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        sys.exit()
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        if brown_satyr_rect.collidepoint(event.pos):
                            fighter_one = Fighter(1, 200, 310, False, brown_satyr_idle_list, brown_satyr_running_list, brown_satyr_attacking_list, brown_satyr_hurt_list, brown_satyr_dying_list, heart_list, slash_fx, "Satyr")
                            one_satyr_picked = False
                            one_fbrown_satyr_picked = True
                            player_one_pick = False
                            player_two_pick = True
                            player_two_category = True
                        if human_satyr_rect.collidepoint(event.pos):
                            fighter_one = Fighter(1, 200, 310, False, human_satyr_idle_list, human_satyr_running_list, human_satyr_attacking_list, human_satyr_hurt_list, human_satyr_dying_list, heart_list, slash_fx, "Satyr")
                            one_satyr_picked = False
                            one_fhuman_satyr_picked = True                   
                            player_one_pick = False
                            player_two_pick = True
                            player_two_category = True
                        if gold_satyr_rect.collidepoint(event.pos):
                            fighter_one = Fighter(1, 200, 310, False, gold_satyr_idle_list, gold_satyr_running_list, gold_satyr_attacking_list, gold_satyr_hurt_list, gold_satyr_dying_list, heart_list, slash_fx, "Satyr")
                            one_satyr_picked = False  
                            one_fgold_satyr_picked = True
                            player_one_pick = False
                            player_two_pick = True
                            player_two_category = True


        # Player two pick
        if player_two_pick:
            if player_two_category == True:
                draw_text("Player Two", round_font, (255, 255, 0), 330, 40)
                draw_text("Choose fighter type", round_font, (255, 255, 0), 170, 100)

                # Player 1 Fighter Type
                # Minotaur
                scaled_mino_img = pygame.transform.scale(brown_mino_idle_1, (100 * 2.2, 80 * 2.2))
                mino_rect = pygame.Rect(230, 170, 110, 140)
                # pygame.draw.rect(screen, (255, 0, 0), mino_rect)
                screen.blit(scaled_mino_img, (170, 150))

                # Golem
                scaled_golem_img = pygame.transform.scale(fire_golem_idle_1, (120 * 2.2, 100 * 2.2))
                golem_rect = pygame.Rect(425, 190, 105, 120)
                # pygame.draw.rect(screen, (255, 0, 0), golem_rect)
                screen.blit(scaled_golem_img, (350, 130))

                # Satyr
                scaled_satyr_img = pygame.transform.scale(gold_satyr_idle_1, (120 * 2.2, 95 * 2.2))
                satyr_rect = pygame.Rect(625, 195, 115, 115)
                # pygame.draw.rect(screen, (255, 0, 0), satyr_rect)
                screen.blit(scaled_satyr_img, (550, 150))

                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        sys.exit()
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        if mino_rect.collidepoint(event.pos):
                            two_mino_picked = True
                            player_two_category = False
                        if golem_rect.collidepoint(event.pos):
                            two_golem_picked = True
                            player_two_category = False
                        if satyr_rect.collidepoint(event.pos):
                            two_satyr_picked = True
                            player_two_category = False

            # Minotaur Picked
            if two_mino_picked == True:
                draw_text("Player Two", round_font, (255, 255, 0), 330, 40)
                draw_text("Choose a Minotaur", round_font, (255, 255, 0), 200, 100)

                scaled_brown_mino_img = pygame.transform.scale(brown_mino_idle_1, (100 * 2.2, 80 * 2.2))
                brown_mino_rect = pygame.Rect(230, 170, 110, 140)
                screen.blit(scaled_brown_mino_img, (170, 150))

                scaled_blue_mino_img = pygame.transform.scale(blue_mino_idle_1, (100 * 2.2, 80 * 2.2))
                blue_mino_rect = pygame.Rect(440, 170, 110, 140)
                screen.blit(scaled_blue_mino_img, (380, 150))

                scaled_dark_mino_img = pygame.transform.scale(dark_mino_idle_1, (100 * 2.2, 80 * 2.2))
                dark_mino_rect = pygame.Rect(640, 170, 110, 140)
                screen.blit(scaled_dark_mino_img, (580, 150))

                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        sys.exit()
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        if brown_mino_rect.collidepoint(event.pos):
                            fighter_two = Fighter(2, 700, 310, True, brown_mino_idle_list, brown_mino_running_list, brown_mino_attacking_list, brown_mino_hurt_list, brown_mino_dying_list, heart_list, slash_fx, "Mino")
                            game_display = True
                            character_selection_display = False
                            two_mino_picked = False
                            two_brown_mino_picked = True
                        if blue_mino_rect.collidepoint(event.pos):
                            fighter_two = Fighter(2, 700, 310, True, blue_mino_idle_list, blue_mino_running_list, blue_mino_attacking_list, blue_mino_hurt_list, blue_mino_dying_list, heart_list, slash_fx, "Mino")
                            game_display = True
                            character_selection_display = False
                            two_mino_picked = False
                            two_blue_mino_picked = True
                        if dark_mino_rect.collidepoint(event.pos):
                            fighter_two = Fighter(2, 700, 310, True, dark_mino_idle_list, dark_mino_running_list, dark_mino_attacking_list, dark_mino_hurt_list, dark_mino_dying_list, heart_list, slash_fx, "Mino")
                            game_display = True
                            character_selection_display = False
                            two_mino_picked = False
                            two_dark_mino_picked = True
            # Golem picked
            elif two_golem_picked == True:
                draw_text("Player Two", round_font, (255, 255, 0), 330, 40)
                draw_text("Choose a Golem", round_font, (255, 255, 0), 240, 100)

                # Fire
                scaled_fire_golem_img = pygame.transform.scale(fire_golem_idle_1, (115 * 2.2, 100 * 2.2))
                fire_golem_rect = pygame.Rect(240, 190, 110, 120)
                screen.blit(scaled_fire_golem_img , (170, 130))

                # Ice
                scaled_ice_golem_img = pygame.transform.scale(ice_golem_idle_1, (115 * 2.2, 100 * 2.2))
                ice_golem_rect = pygame.Rect(435, 190, 110, 120)
                screen.blit(scaled_ice_golem_img, (370, 130))

                # Nature
                scaled_nature_golem_img = pygame.transform.scale(nature_golem_idle_1, (115 * 2.2, 100 * 2.2))
                nature_golem_rect = pygame.Rect(645, 190, 110, 120)
                screen.blit(scaled_nature_golem_img, (580, 130))

                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        sys.exit()
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        if fire_golem_rect.collidepoint(event.pos):
                            fighter_two = Fighter(2, 700, 310, True, fire_golem_idle_list, fire_golem_running_list, fire_golem_attacking_list, fire_golem_hurt_list, fire_golem_dead_list, heart_list, slash_fx, "Golem")
                            game_display = True
                            character_selection_display = False
                            two_golem_picked = False
                            two_fire_golem_picked = True

                        if ice_golem_rect.collidepoint(event.pos):
                            fighter_two = Fighter(2, 700, 310, True, ice_golem_idle_list, ice_golem_running_list, ice_golem_attacking_list, ice_golem_hurt_list, ice_golem_dead_list, heart_list, slash_fx, "Golem")
                            game_display = True
                            character_selection_display = False
                            two_golem_picked = False
                            two_ice_golem_picked = True                        
                        if nature_golem_rect.collidepoint(event.pos):
                            fighter_two = Fighter(2, 700, 310, True, nature_golem_idle_list, nature_golem_running_list, nature_golem_attacking_list, nature_golem_hurt_list, nature_golem_dead_list, heart_list, slash_fx, "Golem")
                            game_display = True
                            character_selection_display = False
                            two_golem_picked = False  
                            two_nature_golem_picked = True                      

            # Satyr picked
            elif two_satyr_picked == True:
                draw_text("Player Two", round_font, (255, 255, 0), 330, 40)
                draw_text("Choose a Satyr", round_font, (255, 255, 0), 250, 100)

                scaled_brown_satyr_img = pygame.transform.scale(brown_satyr_idle_1, (100 * 2.2, 80 * 2.2))
                brown_satyr_rect = pygame.Rect(230, 170, 110, 115)
                screen.blit(scaled_brown_satyr_img, (170, 150))

                scaled_human_satyr_img = pygame.transform.scale(human_satyr_idle_1, (100 * 2.2, 80 * 2.2))
                human_satyr_rect = pygame.Rect(440, 170, 110, 115)
                screen.blit(scaled_human_satyr_img, (380, 150))

                scaled_gold_satyr_img = pygame.transform.scale(gold_satyr_idle_1, (100 * 2.2, 80 * 2.2))
                gold_satyr_rect = pygame.Rect(625, 170, 110, 115)
                screen.blit(scaled_gold_satyr_img, (570, 150))

                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        sys.exit()
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        if brown_satyr_rect.collidepoint(event.pos):
                            fighter_two = Fighter(2, 700, 310, True, brown_satyr_idle_list, brown_satyr_running_list, brown_satyr_attacking_list, brown_satyr_hurt_list, brown_satyr_dying_list, heart_list, slash_fx, "Satyr")
                            game_display = True
                            character_selection_display = False
                            two_satyr_picked = False
                            two_brown_satyr_picked = True
                        if human_satyr_rect.collidepoint(event.pos):
                            fighter_two = Fighter(2, 700, 310, True, human_satyr_idle_list, human_satyr_running_list, human_satyr_attacking_list, human_satyr_hurt_list, human_satyr_dying_list, heart_list, slash_fx, "Satyr")
                            game_display = True
                            character_selection_display = False
                            two_satyr_picked = False
                            two_human_satyr_picked = True                   
                        if gold_satyr_rect.collidepoint(event.pos):
                            fighter_two = Fighter(2, 700, 310, True, gold_satyr_idle_list, gold_satyr_running_list, gold_satyr_attacking_list, gold_satyr_hurt_list, gold_satyr_dying_list, heart_list, slash_fx, "Satyr")
                            game_display = True
                            character_selection_display = False
                            two_satyr_picked = False  
                            two_gold_satyr_picked = True

        # Event handler
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_isRunning = False

        pygame.display.update()
    elif main_menu_display:
        main_menu()
    elif game_display:
        play()
    elif credits_display:
        credits()

    if not game_isRunning:
        break

# Exit Pygame
pygame.quit() 
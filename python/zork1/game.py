"""Zork I: The Great Underground Empire -- Python translation.

GENERATED FILE - do not edit by hand.  Produced by python/tools/zil2py.py
from the original Infocom ZIL source:

    zork1.zil, gmacros.zil, gsyntax.zil, 1dungeon.zil, gglobals.zil,
    gclock.zil, gmain.zil, gparser.zil, gverbs.zil, 1actions.zil

Routine, variable and object names follow the ZIL source so the two can
be read side by side.
"""

from . import runtime as z

# fmt: off
# flake8: noqa

# ---------------------------------------------------------------- flags
LIGHTBIT = 1
ACTORBIT = 2
WEAPONBIT = 3
TOOLBIT = 4
VEHBIT = 5
BURNBIT = 6
FLAMEBIT = 7
RMUNGBIT = 8
CLIMBBIT = 9
DOORBIT = 10
DRINKBIT = 11
FOODBIT = 12
ONBIT = 13
CONTBIT = 14
TAKEBIT = 15
READBIT = 16
TURNBIT = 17
NDESCBIT = 18
TRYTAKEBIT = 19
TRANSBIT = 20
OPENBIT = 21
SURFACEBIT = 22
SACREDBIT = 23
SEARCHBIT = 24
INVISIBLE = 25
RLANDBIT = 26
MAZEBIT = 27
NONLANDBIT = 28
TOUCHBIT = 29
FIGHTBIT = 30
STAGGERED = 31
WEARBIT = 32

# ----------------------------------------------------------- properties
P_NORTH = 31
P_EAST = 30
P_WEST = 29
P_SOUTH = 28
P_NE = 27
P_NW = 26
P_SE = 25
P_SW = 24
P_UP = 23
P_DOWN = 22
P_IN = 21
P_OUT = 20
P_LAND = 19
P_SYNONYM = 18
P_ACTION = 17
P_ADJECTIVE = 16
P_SIZE = 15
P_FDESC = 14
P_VALUE = 13
P_TVALUE = 12
P_LDESC = 11
P_CAPACITY = 10
P_DESCFCN = 9
P_TEXT = 8
P_STRENGTH = 7
P_VTYPE = 6
P_GLOBAL = 5
P_PSEUDO = 4
P_ADVFCN = 3
P_CONTFCN = 2

# --------------------------------------------------------------- objects
BOARD = 1
TEETH = 2
WALL = 3
GRANITE_WALL = 4
SONGBIRD = 5
WHITE_HOUSE = 6
FOREST = 7
TREE = 8
MOUNTAIN_RANGE = 9
GLOBAL_WATER = 10
WATER = 11
KITCHEN_WINDOW = 12
CHIMNEY = 13
GHOSTS = 14
SKULL = 15
LOWERED_BASKET = 16
RAISED_BASKET = 17
LUNCH = 18
BAT = 19
BELL = 20
HOT_BELL = 21
AXE = 22
BOLT = 23
BUBBLE = 24
ALTAR = 25
BOOK = 26
BROKEN_LAMP = 27
SCEPTRE = 28
TIMBERS = 29
SLIDE = 30
KITCHEN_TABLE = 31
ATTIC_TABLE = 32
SANDWICH_BAG = 33
TOOL_CHEST = 34
YELLOW_BUTTON = 35
BROWN_BUTTON = 36
RED_BUTTON = 37
BLUE_BUTTON = 38
TROPHY_CASE = 39
RUG = 40
CHALICE = 41
GARLIC = 42
TRIDENT = 43
CYCLOPS = 44
DAM = 45
TRAP_DOOR = 46
BOARDED_WINDOW = 47
FRONT_DOOR = 48
BARROW_DOOR = 49
BARROW = 50
BOTTLE = 51
CRACK = 52
COFFIN = 53
GRATE = 54
PUMP = 55
DIAMOND = 56
JADE = 57
KNIFE = 58
BONES = 59
BURNED_OUT_LANTERN = 60
BAG_OF_COINS = 61
LAMP = 62
EMERALD = 63
ADVERTISEMENT = 64
LEAK = 65
MACHINE = 66
INFLATED_BOAT = 67
MAILBOX = 68
MATCH = 69
MIRROR_2 = 70
MIRROR_1 = 71
PAINTING = 72
CANDLES = 73
GUNK = 74
BODIES = 75
LEAVES = 76
PUNCTURED_BOAT = 77
INFLATABLE_BOAT = 78
BAR = 79
POT_OF_GOLD = 80
PRAYER = 81
RAILING = 82
RAINBOW = 83
RIVER = 84
BUOY = 85
ROPE = 86
RUSTY_KNIFE = 87
SAND = 88
BRACELET = 89
SCREWDRIVER = 90
KEYS = 91
SHOVEL = 92
COAL = 93
LADDER = 94
SCARAB = 95
LARGE_BAG = 96
STILETTO = 97
MACHINE_SWITCH = 98
WOODEN_DOOR = 99
SWORD = 100
MAP = 101
BOAT_LABEL = 102
THIEF = 103
PEDESTAL = 104
TORCH = 105
GUIDE = 106
TROLL = 107
TRUNK = 108
TUBE = 109
PUTTY = 110
ENGRAVINGS = 111
OWNERS_MANUAL = 112
CLIMBABLE_CLIFF = 113
WHITE_CLIFF = 114
WRENCH = 115
CONTROL_PANEL = 116
NEST = 117
EGG = 118
BROKEN_EGG = 119
BAUBLE = 120
CANARY = 121
BROKEN_CANARY = 122
WEST_OF_HOUSE = 123
STONE_BARROW = 124
NORTH_OF_HOUSE = 125
SOUTH_OF_HOUSE = 126
EAST_OF_HOUSE = 127
FOREST_1 = 128
FOREST_2 = 129
MOUNTAINS = 130
FOREST_3 = 131
PATH = 132
UP_A_TREE = 133
GRATING_CLEARING = 134
CLEARING = 135
KITCHEN = 136
ATTIC = 137
LIVING_ROOM = 138
CELLAR = 139
TROLL_ROOM = 140
EAST_OF_CHASM = 141
GALLERY = 142
STUDIO = 143
MAZE_1 = 144
MAZE_2 = 145
MAZE_3 = 146
MAZE_4 = 147
DEAD_END_1 = 148
MAZE_5 = 149
DEAD_END_2 = 150
MAZE_6 = 151
MAZE_7 = 152
MAZE_8 = 153
DEAD_END_3 = 154
MAZE_9 = 155
MAZE_10 = 156
MAZE_11 = 157
GRATING_ROOM = 158
MAZE_12 = 159
DEAD_END_4 = 160
MAZE_13 = 161
MAZE_14 = 162
MAZE_15 = 163
CYCLOPS_ROOM = 164
STRANGE_PASSAGE = 165
TREASURE_ROOM = 166
RESERVOIR_SOUTH = 167
RESERVOIR = 168
RESERVOIR_NORTH = 169
STREAM_VIEW = 170
IN_STREAM = 171
MIRROR_ROOM_1 = 172
MIRROR_ROOM_2 = 173
SMALL_CAVE = 174
TINY_CAVE = 175
COLD_PASSAGE = 176
NARROW_PASSAGE = 177
WINDING_PASSAGE = 178
TWISTING_PASSAGE = 179
ATLANTIS_ROOM = 180
EW_PASSAGE = 181
ROUND_ROOM = 182
DEEP_CANYON = 183
DAMP_CAVE = 184
LOUD_ROOM = 185
NS_PASSAGE = 186
CHASM_ROOM = 187
ENTRANCE_TO_HADES = 188
LAND_OF_LIVING_DEAD = 189
ENGRAVINGS_CAVE = 190
EGYPT_ROOM = 191
DOME_ROOM = 192
TORCH_ROOM = 193
NORTH_TEMPLE = 194
SOUTH_TEMPLE = 195
DAM_ROOM = 196
DAM_LOBBY = 197
MAINTENANCE_ROOM = 198
DAM_BASE = 199
RIVER_1 = 200
RIVER_2 = 201
RIVER_3 = 202
WHITE_CLIFFS_NORTH = 203
WHITE_CLIFFS_SOUTH = 204
RIVER_4 = 205
RIVER_5 = 206
SHORE = 207
SANDY_BEACH = 208
SANDY_CAVE = 209
ARAGAIN_FALLS = 210
ON_RAINBOW = 211
END_OF_RAINBOW = 212
CANYON_BOTTOM = 213
CLIFF_MIDDLE = 214
CANYON_VIEW = 215
MINE_ENTRANCE = 216
SQUEEKY_ROOM = 217
BAT_ROOM = 218
SHAFT_ROOM = 219
SMELLY_ROOM = 220
GAS_ROOM = 221
LADDER_TOP = 222
LADDER_BOTTOM = 223
DEAD_END_5 = 224
TIMBER_ROOM = 225
LOWER_SHAFT = 226
MACHINE_ROOM = 227
MINE_1 = 228
MINE_2 = 229
MINE_3 = 230
MINE_4 = 231
SLIDE_ROOM = 232
GLOBAL_OBJECTS = 233
LOCAL_GLOBALS = 234
ROOMS = 235
INTNUM = 236
PSEUDO_OBJECT = 237
IT = 238
NOT_HERE_OBJECT = 239
BLESSINGS = 240
STAIRS = 241
SAILOR = 242
GROUND = 243
GRUE = 244
LUNGS = 245
ME = 246
ADVENTURER = 247
PATHOBJ = 248
ZORKMID = 249
HANDS = 250

# ------------------------------------------------- actions and verbs
V_VERBOSE = 1
V_BRIEF = 2
V_SUPER_BRIEF = 3
V_DIAGNOSE = 4
V_INVENTORY = 5
V_QUIT = 6
V_RESTART = 7
V_RESTORE = 8
V_SAVE = 9
V_SCORE = 10
V_SCRIPT = 11
V_UNSCRIPT = 12
V_VERSION = 13
V_VERIFY = 14
V_RANDOM = 15
V_COMMAND_FILE = 16
V_RECORD = 17
V_UNRECORD = 18
V_LAMP_ON = 19
V_ANSWER = 20
V_REPLY = 21
V_PUT = 22
V_ATTACK = 23
V_BACK = 24
V_BLAST = 25
V_LAMP_OFF = 26
V_INFLATE = 27
V_BREATHE = 28
V_BOARD = 29
V_BRUSH = 30
V_BUG = 31
V_BURN = 32
V_CHOMP = 33
V_CLIMB_UP = 34
V_CLIMB_DOWN = 35
V_CLIMB_FOO = 36
V_CLIMB_ON = 37
V_THROUGH = 38
V_CLOSE = 39
V_COMMAND = 40
V_COUNT = 41
V_CROSS = 42
V_CUT = 43
V_CURSES = 44
V_DEFLATE = 45
V_MUNG = 46
V_OPEN = 47
V_DIG = 48
V_DISEMBARK = 49
V_DISENCHANT = 50
V_DRINK = 51
V_DRINK_FROM = 52
V_DROP = 53
V_PUT_ON = 54
V_EAT = 55
V_ECHO = 56
V_ENCHANT = 57
V_ENTER = 58
V_EXIT = 59
V_EXAMINE = 60
V_LOOK_INSIDE = 61
V_EXORCISE = 62
V_FILL = 63
V_FIND = 64
V_FOLLOW = 65
V_FROBOZZ = 66
V_GIVE = 67
V_SGIVE = 68
V_HATCH = 69
V_HELLO = 70
V_INCANT = 71
V_LEAP = 72
V_KICK = 73
V_STAB = 74
V_KISS = 75
V_KNOCK = 76
V_LAUNCH = 77
V_LEAN_ON = 78
V_LEAVE = 79
V_LISTEN = 80
V_LOCK = 81
V_LOOK = 82
V_LOOK_ON = 83
V_LOOK_UNDER = 84
V_LOOK_BEHIND = 85
V_READ = 86
V_LOWER = 87
V_OIL = 88
V_MAKE = 89
V_MELT = 90
V_MOVE = 91
V_PUSH_TO = 92
V_TURN = 93
V_MUMBLE = 94
V_ODYSSEUS = 95
V_PICK = 96
V_TAKE = 97
V_PLAY = 98
V_PLUG = 99
V_ADVENT = 100
V_POUR_ON = 101
V_PRAY = 102
V_PUMP = 103
V_PUSH = 104
V_PUT_UNDER = 105
V_WEAR = 106
V_PUT_BEHIND = 107
V_RAISE = 108
V_RAPE = 109
V_READ_PAGE = 110
V_REPENT = 111
V_RING = 112
V_RUB = 113
V_TELL = 114
V_SAY = 115
V_SEARCH = 116
V_SEND = 117
V_SHAKE = 118
V_SKIP = 119
V_SMELL = 120
V_SPIN = 121
V_SPRAY = 122
V_SSPRAY = 123
V_SQUEEZE = 124
V_STAND = 125
V_STAY = 126
V_STRIKE = 127
V_SWIM = 128
V_SWING = 129
V_THROW = 130
V_OVERBOARD = 131
V_THROW_OFF = 132
V_TIE = 133
V_TIE_UP = 134
V_TREASURE = 135
V_UNLOCK = 136
V_UNTIE = 137
V_WAIT = 138
V_ALARM = 139
V_WALK_AROUND = 140
V_WALK = 141
V_WALK_TO = 142
V_WAVE = 143
V_WIN = 144
V_WIND = 145
V_WISH = 146
V_YELL = 147
V_ZORK = 148
ACT_VERBOSE = 255
ACT_BRIEF = 254
ACT_SUPER = 253
ACT_DIAGNOSE = 252
ACT_INVENTORY = 251
ACT_QUIT = 250
ACT_RESTART = 249
ACT_RESTORE = 248
ACT_SAVE = 247
ACT_SCORE = 246
ACT_SCRIPT = 245
ACT_UNSCRIPT = 244
ACT_VERSION = 243
ACT_S_VERIFY = 242
ACT_H_RANDOM = 241
ACT_H_COMMAND = 240
ACT_H_RECORD = 239
ACT_H_UNRECORD = 238
ACT_ACTIVATE = 237
ACT_ANSWER = 236
ACT_APPLY = 235
ACT_ATTACK = 234
ACT_BACK = 233
ACT_BLAST = 232
ACT_BLOW = 231
ACT_BOARD = 230
ACT_BRUSH = 229
ACT_BUG = 228
ACT_BURN = 227
ACT_CHOMP = 226
ACT_CLIMB = 225
ACT_CLOSE = 224
ACT_COMMAND = 223
ACT_COUNT = 222
ACT_CROSS = 221
ACT_CUT = 220
ACT_CURSE = 219
ACT_DEFLATE = 218
ACT_DESTROY = 217
ACT_DIG = 216
ACT_DISEMBARK = 215
ACT_DISENCHANT = 214
ACT_DRINK = 213
ACT_DROP = 212
ACT_EAT = 211
ACT_ECHO = 210
ACT_ENCHANT = 209
ACT_ENTER = 208
ACT_EXIT = 207
ACT_EXAMINE = 206
ACT_EXORCISE = 205
ACT_EXTINGUISH = 204
ACT_FILL = 203
ACT_FIND = 202
ACT_FOLLOW = 201
ACT_FROBOZZ = 200
ACT_GIVE = 199
ACT_HATCH = 198
ACT_HELLO = 197
ACT_INCANT = 196
ACT_INFLAT = 195
ACT_JUMP = 194
ACT_KICK = 193
ACT_KILL = 192
ACT_STAB = 191
ACT_KISS = 190
ACT_KNOCK = 189
ACT_LAUNCH = 188
ACT_LEAN = 187
ACT_LEAVE = 186
ACT_LIGHT = 185
ACT_LISTEN = 184
ACT_LOCK = 183
ACT_LOOK = 182
ACT_LOWER = 181
ACT_LUBRICATE = 180
ACT_MAKE = 179
ACT_MELT = 178
ACT_MOVE = 177
ACT_ROLL = 176
ACT_MUMBLE = 175
ACT_ODYSSEUS = 174
ACT_OPEN = 173
ACT_PICK = 172
ACT_PLAY = 171
ACT_PLUG = 170
ACT_PLUGH = 169
ACT_POKE = 168
ACT_PUNCTURE = 167
ACT_POUR = 166
ACT_PRAY = 165
ACT_PULL = 164
ACT_PUMP = 163
ACT_PUSH = 162
ACT_PUT = 161
ACT_RAISE = 160
ACT_RAPE = 159
ACT_READ = 158
ACT_REPENT = 157
ACT_RING = 156
ACT_RUB = 155
ACT_TALK = 154
ACT_SAY = 153
ACT_SEARCH = 152
ACT_SEND = 151
ACT_SHAKE = 150
ACT_SKIP = 149
ACT_SLIDE = 148
ACT_SMELL = 147
ACT_SPIN = 146
ACT_SPRAY = 145
ACT_SQUEEZE = 144
ACT_STAND = 143
ACT_STAY = 142
ACT_STRIKE = 141
ACT_SWIM = 140
ACT_SWING = 139
ACT_TAKE = 138
ACT_TELL = 137
ACT_THROW = 136
ACT_TIE = 135
ACT_TREASURE = 134
ACT_TURN = 133
ACT_UNLOCK = 132
ACT_UNTIE = 131
ACT_WAIT = 130
ACT_WAKE = 129
ACT_WALK = 128
ACT_WAVE = 127
ACT_WEAR = 126
ACT_WIN = 125
ACT_WIND = 124
ACT_WISH = 123
ACT_YELL = 122
ACT_ZORK = 121
PR_TO = 255
PR_WITH = 254
PR_OUT = 253
PR_UP = 252
PR_IN = 251
PR_DOWN = 250
PR_ON = 249
PR_FROM = 248
PR_AWAY = 247
PR_OVER = 246
PR_ACROSS = 245
PR_OFF = 244
PR_AT = 243
PR_FOR = 242
PR_AROUND = 241
PR_UNDER = 240
PR_BEHIND = 239
PR_ABOUT = 238

# ------------------------------------------------- parts of speech
PS_OBJECT = 128
PS_VERB = 64
PS_ADJECTIVE = 32
PS_DIRECTION = 16
PS_PREPOSITION = 8
PS_BUZZ_WORD = 4
P1_OBJECT = 0
P1_VERB = 1
P1_ADJECTIVE = 2
P1_DIRECTION = 3

# ----------------------------------------------- compile-time settings
ZORK_NUMBER = 1
C_ENABLED = 1
C_DISABLED = 0
DEBUG = False

# ------------------------------------------------- numeric constants
C_TABLELEN = 180
C_INTLEN = 6
C_ENABLED_P = 0
C_TICK = 1
C_RTN = 2
SERIAL = 0
M_FATAL = 2
M_HANDLED = 1
M_NOT_HANDLED = False
M_OBJECT = False
M_BEG = 1
M_END = 6
M_ENTER = 2
M_LOOK = 3
M_FLASH = 4
M_OBJDESC = 5
CC_SBPTR = 0
CC_SEPTR = 1
CC_DBPTR = 2
CC_DEPTR = 3
O_PTR = 0
O_START = 1
O_LENGTH = 2
O_END = 3
P_LEXWORDS = 1
P_LEXSTART = 1
P_LEXELEN = 2
P_WORDLEN = 4
P_PSOFF = 4
P_P1OFF = 5
P_P1BITS = 3
P_ITBLLEN = 9
P_VERB = 0
P_VERBN = 1
P_PREP1 = 2
P_PREP1N = 3
P_PREP2 = 4
P_PREP2N = 5
P_NC1 = 6
P_NC1L = 7
P_NC2 = 8
P_NC2L = 9
P_SYNLEN = 8
P_SBITS = 0
P_SPREP1 = 1
P_SPREP2 = 2
P_SFWIM1 = 3
P_SFWIM2 = 4
P_SLOC1 = 5
P_SLOC2 = 6
P_SACTION = 7
P_SONUMS = 3
P_ALL = 1
P_ONE = 2
P_INHIBIT = 4
SH = 128
SC = 64
SIR = 32
SOG = 16
STAKE = 8
SMANY = 4
SHAVE = 2
P_SRCBOT = 2
P_SRCTOP = 0
P_SRCALL = 1
REXIT = 0
UEXIT = 1
NEXIT = 2
FEXIT = 3
CEXIT = 4
DEXIT = 5
NEXITSTR = 0
FEXITFCN = 0
CEXITFLAG = 1
CEXITSTR = 1
DEXITOBJ = 1
DEXITSTR = 1
F_BUSY_P = 1
F_DEAD = 2
F_UNCONSCIOUS = 3
F_CONSCIOUS = 4
F_FIRST_P = 5
MISSED = 1
UNCONSCIOUS = 2
KILLED = 3
LIGHT_WOUND = 4
SERIOUS_WOUND = 5
STAGGER = 6
LOSE_WEAPON = 7
HESITATE = 8
SITTING_DUCK = 9
STRENGTH_MAX = 7
STRENGTH_MIN = 2
CURE_WAIT = 30
F_WEP = 0
F_DEF = 1
V_VILLAIN = 0
V_BEST = 1
V_BEST_ADV = 2
V_PROB = 3
V_MSGS = 4
LOW_DIRECTION = 19

# ===================================================================
# Routines
# ===================================================================

def zprob(base=0):
    if LUCKY:
        return base > z.random(100)
    else:
        return base > z.random(300)
    return False


def random_element(frob=0):
    return z.get(frob, z.random(z.get(frob, 0)))


def pick_one(frob=0):
    l = z.get(frob, 0)
    cnt = z.get(frob, 1)
    rnd = 0
    msg = 0
    rfrob = 0
    l = l - 1
    frob = frob + 2
    rfrob = frob + (cnt * 2)
    rnd = z.random((l - cnt))
    msg = z.get(rfrob, rnd)
    z.put(rfrob, rnd, z.get(rfrob, 1))
    z.put(rfrob, 1, msg)
    cnt = cnt + 1
    if cnt == l:
        cnt = 0
    z.put(frob, 0, cnt)
    return msg


def treasure_inside():
    if PRSA == V_OPEN:
        score_obj(EMERALD)
        return False
    return False


def grating_exit():
    if GRATE_REVEALED:
        if z.fset_p(GRATE, OPENBIT):
            return GRATING_ROOM
        else:
            z.tell('The grating is closed!\n')
            this_is_it(GRATE)
            return False
    else:
        z.tell("You can't go that way.\n")
        return False
    return False


def canyon_view_f(rarg=0):
    if (rarg == M_BEG) and (PRSA == V_LEAP) and (not PRSO):
        jigs_up('Nice view, lousy place to jump.')
        return True
    return False


def go():
    global HERE, LIT, PLAYER, WINNER
    while True:
        z.put(queue(z.rtn(i_fight), -1), C_ENABLED_P, 1)
        queue(z.rtn(i_sword), -1)
        z.put(queue(z.rtn(i_thief), -1), C_ENABLED_P, 1)
        queue(z.rtn(i_candles), 40)
        queue(z.rtn(i_lantern), 200)
        z.putp(INFLATED_BOAT, P_VTYPE, NONLANDBIT)
        z.put(DEF1_RES, 1, (DEF1 + 2))
        z.put(DEF1_RES, 2, (DEF1 + 4))
        z.put(DEF2_RES, 2, (DEF2B + 2))
        z.put(DEF2_RES, 3, (DEF2B + 4))
        z.put(DEF3_RES, 1, (DEF3A + 2))
        z.put(DEF3_RES, 3, (DEF3B + 2))
        HERE = WEST_OF_HOUSE
        this_is_it(MAILBOX)
        if not z.fset_p(HERE, TOUCHBIT):
            v_version()
            z.crlf()
        LIT = True
        WINNER = ADVENTURER
        PLAYER = WINNER
        z.move(WINNER, HERE)
        v_look()
        main_loop()
        continue
        break
    return False


def not_here_object_f():
    global P_CONT, QUOTE_FLAG
    tbl = 0
    prso_p = True
    obj = 0
    if (PRSO == NOT_HERE_OBJECT) and (PRSI == NOT_HERE_OBJECT):
        z.tell("Those things aren't here!\n")
        return True
    elif PRSO == NOT_HERE_OBJECT:
        tbl = P_PRSO
    else:
        tbl = P_PRSI
        prso_p = False
    P_CONT = False
    QUOTE_FLAG = False
    if WINNER == PLAYER:
        z.tell("You can't see any ")
        not_here_print(prso_p)
        z.tell(' here!\n')
    else:
        z.tell('The ', z.D(WINNER), ' seems confused. "I don\'t see any ')
        not_here_print(prso_p)
        z.tell(' here!"\n')
    return True


def not_here_print(prso_p=0):
    if P_OFLAG:
        if P_XADJ:
            z.printb(P_XADJN)
        if P_XNAM:
            return z.printb(P_XNAM)
    elif prso_p:
        return buffer_print(z.get(P_ITBL, P_NC1), z.get(P_ITBL, P_NC1L), False)
    else:
        return buffer_print(z.get(P_ITBL, P_NC2), z.get(P_ITBL, P_NC2L), False)
    return False


def null_f(a1=0, a2=0):
    return False


def stairs_f():
    if PRSA == V_THROUGH:
        z.tell('You should say whether you want to go up or down.\n')
        return True
    return False


def sailor_fcn():
    global HS, P_CONT, QUOTE_FLAG
    if PRSA == V_TELL:
        P_CONT = False
        QUOTE_FLAG = False
        z.tell("You can't talk to the sailor that way.\n")
        return True
    elif PRSA == V_EXAMINE:
        z.tell('There is no sailor to be seen.\n')
        return True
    elif PRSA == V_HELLO:
        HS = HS + 1
        if z.mod(HS, 20) == 0:
            z.tell('You seem to be repeating yourself.\n')
            return True
        elif z.mod(HS, 10) == 0:
            z.tell('I think that phrase is getting a bit worn out.\n')
            return True
        else:
            z.tell('Nothing happens here.\n')
            return True
    return False


def ground_function():
    if (PRSA in (V_PUT, V_PUT_ON)) and (PRSI == GROUND):
        perform(V_DROP, PRSO)
        return True
    elif HERE == SANDY_CAVE:
        return sand_function()
    elif PRSA == V_DIG:
        z.tell('The ground is too hard for digging here.\n')
        return True
    return False


def grue_function():
    if PRSA == V_EXAMINE:
        z.tell('The grue is a sinister, lurking presence in the dark places of the earth. Its favorite diet is adventurers, but its insatiable appetite is tempered by its fear of light. No grue has ever been seen by the light of day, and few have survived its fearsome jaws to tell the tale.\n')
        return True
    elif PRSA == V_FIND:
        z.tell("There is no grue here, but I'm sure there is at least one lurking in the darkness nearby. I wouldn't let my light go out if I were you!\n")
        return True
    elif PRSA == V_LISTEN:
        z.tell('It makes no sound but is always lurking in the darkness nearby.\n')
        return True
    return False


def cretin_fcn():
    global P_CONT, QUOTE_FLAG
    if PRSA == V_TELL:
        P_CONT = False
        QUOTE_FLAG = False
        z.tell('Talking to yourself is said to be a sign of impending mental collapse.\n')
        return True
    elif (PRSA == V_GIVE) and (PRSI == ME):
        perform(V_TAKE, PRSO)
        return True
    elif PRSA == V_MAKE:
        z.tell('Only you can do that.\n')
        return True
    elif PRSA == V_DISEMBARK:
        z.tell("You'll have to do that on your own.\n")
        return True
    elif PRSA == V_EAT:
        z.tell('Auto-cannibalism is not the answer.\n')
        return True
    elif PRSA in (V_ATTACK, V_MUNG):
        if PRSI and z.fset_p(PRSI, WEAPONBIT):
            return jigs_up("If you insist.... Poof, you're dead!")
        else:
            z.tell('Suicide is not the answer.\n')
            return True
    elif PRSA == V_THROW:
        if PRSO == ME:
            z.tell("Why don't you just walk like normal people?\n")
            return True
    elif PRSA == V_TAKE:
        z.tell('How romantic!\n')
        return True
    elif PRSA == V_EXAMINE:
        if HERE in (z.loc(MIRROR_1), z.loc(MIRROR_2)):
            z.tell('Your image in the mirror looks tired.\n')
            return True
        else:
            z.tell("That's difficult unless your eyes are prehensile.\n")
            return True
    return False


def path_object():
    if PRSA in (V_TAKE, V_FOLLOW):
        z.tell('You must specify a direction to go.\n')
        return True
    elif PRSA == V_FIND:
        z.tell("I can't help you there....\n")
        return True
    elif PRSA == V_DIG:
        z.tell('Not a chance.\n')
        return True
    return False


def zorkmid_function():
    if PRSA == V_EXAMINE:
        z.tell('The zorkmid is the unit of currency of the Great Underground Empire.\n')
        return True
    elif PRSA == V_FIND:
        z.tell('The best way to find zorkmids is to go out and look for them.\n')
        return True
    return False


def queue(rtn=0, tick=0):
    cint = 0
    z.put((cint := int_(rtn)), C_TICK, tick)
    return cint


def int_(rtn=0, demon=False, e=0, c=0, int__=0):
    global C_DEMONS, C_INTS
    e = C_TABLE + C_TABLELEN
    c = C_TABLE + C_INTS
    while True:
        if c == e:
            C_INTS = C_INTS - C_INTLEN
            if demon:
                C_DEMONS = C_DEMONS - C_INTLEN
            int__ = C_TABLE + C_INTS
            z.put(int__, C_RTN, rtn)
            return int__
        elif z.get(c, C_RTN) == rtn:
            return c
        c = c + C_INTLEN
    return False


def clocker():
    global CLOCK_WAIT, MOVES
    c = 0
    e = 0
    tick = 0
    flg = False
    if CLOCK_WAIT:
        CLOCK_WAIT = False
        return False
    if P_WON:
        _t1 = C_INTS
    else:
        _t1 = C_DEMONS
    c = C_TABLE + _t1
    e = C_TABLE + C_TABLELEN
    while True:
        if c == e:
            MOVES = MOVES + 1
            return flg
        elif not (z.get(c, C_ENABLED_P) == 0):
            tick = z.get(c, C_TICK)
            if tick == 0:
                pass
            else:
                z.put(c, C_TICK, (tick - 1))
                if (not (tick > 1)) and z.apply(z.get(c, C_RTN)):
                    flg = True
        c = c + C_INTLEN
    return False


def main_loop():
    trash = 0
    while True:
        trash = main_loop_1()
    return False


def main_loop_1():
    global PRSI, PRSO, P_CONT, P_MULT, P_NOT_HERE, P_WON
    icnt = 0
    ocnt = 0
    num = 0
    cnt = 0
    obj = 0
    tbl = 0
    v = 0
    ptbl = 0
    obj1 = 0
    tmp = 0
    o = 0
    i = 0
    cnt = 0
    obj = False
    ptbl = True
    if (P_WON := parser()):
        icnt = z.get(P_PRSI, P_MATCHLEN)
        ocnt = z.get(P_PRSO, P_MATCHLEN)
        if P_IT_OBJECT and accessible_p(P_IT_OBJECT):
            tmp = False
            while True:
                if (cnt := (cnt + 1)) > icnt:
                    break
                else:
                    if z.get(P_PRSI, cnt) == IT:
                        z.put(P_PRSI, cnt, P_IT_OBJECT)
                        tmp = True
                        break
            if not tmp:
                cnt = 0
                while True:
                    if (cnt := (cnt + 1)) > ocnt:
                        break
                    else:
                        if z.get(P_PRSO, cnt) == IT:
                            z.put(P_PRSO, cnt, P_IT_OBJECT)
                            break
            cnt = 0
        if ocnt == 0:
            num = ocnt
        elif ocnt > 1:
            tbl = P_PRSO
            if icnt == 0:
                obj = False
            else:
                obj = z.get(P_PRSI, 1)
            num = ocnt
        elif icnt > 1:
            ptbl = False
            tbl = P_PRSI
            obj = z.get(P_PRSO, 1)
            num = icnt
        else:
            num = 1
        if (not obj) and (icnt == 1):
            obj = z.get(P_PRSI, 1)
        if (PRSA == V_WALK) and (not (P_WALK_DIR == 0)):
            v = perform(PRSA, PRSO)
        elif num == 0:
            if (z.getb(P_SYNTAX, P_SBITS) & P_SONUMS) == 0:
                v = perform(PRSA)
                PRSO = False
            elif not LIT:
                z.tell("It's too dark to see.\n")
            else:
                z.tell("It's not clear what you're referring to.\n")
                v = False
        else:
            P_NOT_HERE = 0
            P_MULT = False
            if num > 1:
                P_MULT = True
            tmp = False
            while True:
                if (cnt := (cnt + 1)) > num:
                    if P_NOT_HERE > 0:
                        z.tell('The ')
                        if P_NOT_HERE != num:
                            z.tell('other ')
                        z.tell('object')
                        if P_NOT_HERE != 1:
                            z.tell('s')
                        z.tell(' that you mentioned ')
                        if P_NOT_HERE != 1:
                            z.tell('are')
                        else:
                            z.tell('is')
                        z.tell("n't here.\n")
                    elif not tmp:
                        z.tell("There's nothing here you can take.\n")
                    break
                else:
                    if ptbl:
                        obj1 = z.get(P_PRSO, cnt)
                    else:
                        obj1 = z.get(P_PRSI, cnt)
                    if ptbl:
                        o = obj1
                    else:
                        o = obj
                    if ptbl:
                        i = obj
                    else:
                        i = obj1
                    if (num > 1) or (z.get(z.get(P_ITBL, P_NC1), 0) == W_ALL):
                        v = z.loc(WINNER)
                        if o == NOT_HERE_OBJECT:
                            P_NOT_HERE = P_NOT_HERE + 1
                            continue
                        elif (PRSA == V_TAKE) and i and (z.get(z.get(P_ITBL, P_NC1), 0) == W_ALL) and (not z.in_p(o, i)):
                            continue
                        elif (P_GETFLAGS == P_ALL) and (PRSA == V_TAKE) and (((not (z.loc(o) in (WINNER, HERE, v))) and (z.loc(o) != i) and (not z.fset_p(z.loc(o), SURFACEBIT))) or (not (z.fset_p(o, TAKEBIT) or z.fset_p(o, TRYTAKEBIT)))):
                            continue
                        else:
                            if obj1 == IT:
                                z.printd(P_IT_OBJECT)
                            else:
                                z.printd(obj1)
                            z.tell(': ')
                    PRSO = o
                    PRSI = i
                    tmp = True
                    v = perform(PRSA, PRSO, PRSI)
                    if v == M_FATAL:
                        break
        if v != M_FATAL:
            v = z.apply(z.getp(z.loc(WINNER), P_ACTION), M_END)
        if v == M_FATAL:
            P_CONT = False
    else:
        P_CONT = False
    null_f()
    if P_WON:
        if PRSA in (V_TELL, V_BRIEF, V_SUPER_BRIEF, V_VERBOSE, V_SAVE, V_VERSION, V_QUIT, V_RESTART, V_SCORE, V_SCRIPT, V_UNSCRIPT, V_RESTORE):
            return True
        else:
            v = clocker()
            return v
    return False


def perform(a=0, o=False, i=False):
    global PRSA, PRSI, PRSO, P_IT_OBJECT
    v = 0
    oa = 0
    oo = 0
    oi = 0
    oa = PRSA
    oo = PRSO
    oi = PRSI
    if (IT in (i, o)) and (not accessible_p(P_IT_OBJECT)):
        z.tell("I don't see what you are referring to.\n")
        return 2
    if o == IT:
        o = P_IT_OBJECT
    if i == IT:
        i = P_IT_OBJECT
    PRSA = a
    PRSO = o
    if PRSO and (not (PRSA == V_WALK)):
        P_IT_OBJECT = PRSO
    PRSI = i
    if (NOT_HERE_OBJECT in (PRSO, PRSI)) and (v := d_apply('Not Here', z.rtn(not_here_object_f))):
        pass
    else:
        o = PRSO
        i = PRSI
        if (v := dd_apply('Actor', WINNER, z.getp(WINNER, P_ACTION))):
            pass
        elif (v := d_apply('Room (M-BEG)', z.getp(z.loc(WINNER), P_ACTION), M_BEG)):
            pass
        elif (v := d_apply('Preaction', z.get(PREACTIONS, a))):
            pass
        elif i and (v := d_apply('PRSI', z.getp(i, P_ACTION))):
            pass
        elif o and (a != V_WALK) and z.loc(o) and z.getp(z.loc(o), P_CONTFCN) and (v := dd_apply('Container', z.loc(o), z.getp(z.loc(o), P_CONTFCN))):
            pass
        elif o and (a != V_WALK) and (v := d_apply('PRSO', z.getp(o, P_ACTION))):
            pass
        elif (v := d_apply(False, z.get(ACTIONS, a))):
            pass
    PRSA = oa
    PRSO = oo
    PRSI = oi
    return v


def d_apply(str_=0, fcn=0, foo=z.NOARG):
    res = 0
    if not fcn:
        return False
    else:
        if foo is not z.NOARG:
            res = z.apply(fcn, foo)
        else:
            res = z.apply(fcn)
        if False and str_:
            if res == 2:
                z.tell('Fatal\n')
            elif not res:
                z.tell('Not handled')
            else:
                z.tell('Handled\n')
        return res
    return False


def dd_apply(str_=0, obj=0, fcn=0, foo=False):
    return d_apply(str_, fcn, foo)


def parser():
    global AGAIN_DIR, HERE, LIT, PRSA, PRSO, P_ACT, P_ADVERB, P_CONT, P_DIR
    global P_END_ON_PREP, P_GETFLAGS, P_LEN, P_MERGED, P_NCN, P_NUMBER, P_OFLAG
    global P_WALK_DIR, QUOTE_FLAG, RESERVE_PTR, WINNER
    ptr = P_LEXSTART
    wrd = 0
    val = 0
    verb = False
    of_flag = False
    owinner = 0
    omerged = 0
    len_ = 0
    dir = False
    nw = 0
    lw = 0
    cnt = -1
    while True:
        if (cnt := (cnt + 1)) > P_ITBLLEN:
            break
        else:
            if not P_OFLAG:
                z.put(P_OTBL, cnt, z.get(P_ITBL, cnt))
            z.put(P_ITBL, cnt, 0)
    owinner = WINNER
    omerged = P_MERGED
    P_ADVERB = False
    P_MERGED = False
    P_END_ON_PREP = False
    z.put(P_PRSO, P_MATCHLEN, 0)
    z.put(P_PRSI, P_MATCHLEN, 0)
    z.put(P_BUTS, P_MATCHLEN, 0)
    if (not QUOTE_FLAG) and (WINNER != PLAYER):
        WINNER = PLAYER
        HERE = meta_loc(PLAYER)
        LIT = lit_p(HERE)
    if RESERVE_PTR:
        ptr = RESERVE_PTR
        stuff(RESERVE_LEXV, P_LEXV)
        if (not SUPER_BRIEF) and (PLAYER == WINNER):
            z.crlf()
        RESERVE_PTR = False
        P_CONT = False
    elif P_CONT:
        ptr = P_CONT
        if (not SUPER_BRIEF) and (PLAYER == WINNER) and (not (PRSA == V_SAY)):
            z.crlf()
        P_CONT = False
    else:
        WINNER = PLAYER
        QUOTE_FLAG = False
        if not z.fset_p(z.loc(WINNER), VEHBIT):
            HERE = z.loc(WINNER)
        LIT = lit_p(HERE)
        if not SUPER_BRIEF:
            z.crlf()
        z.tell('>')
        z.read(P_INBUF, P_LEXV)
    P_LEN = z.getb(P_LEXV, P_LEXWORDS)
    if P_LEN == 0:
        z.tell('I beg your pardon?\n')
        return False
    if (wrd := z.get(P_LEXV, ptr)) == W_OOPS:
        if z.get(P_LEXV, (ptr + P_LEXELEN)) in (W_PERIOD, W_COMMA):
            ptr = ptr + P_LEXELEN
            P_LEN = P_LEN - 1
        if not (P_LEN > 1):
            z.tell("I can't help your clumsiness.\n")
            return False
        elif z.get(OOPS_TABLE, O_PTR):
            if (P_LEN > 2) and (z.get(P_LEXV, (ptr + P_LEXELEN)) == W_QUOTE):
                z.tell("Sorry, you can't correct mistakes in quoted text.\n")
                return False
            elif P_LEN > 2:
                z.tell('Warning: only the first word after OOPS is used.\n')
            z.put(AGAIN_LEXV, z.get(OOPS_TABLE, O_PTR), z.get(P_LEXV, (ptr + P_LEXELEN)))
            WINNER = owinner
            inbuf_add(z.getb(P_LEXV, ((ptr * P_LEXELEN) + 6)), z.getb(P_LEXV, ((ptr * P_LEXELEN) + 7)), ((z.get(OOPS_TABLE, O_PTR) * P_LEXELEN) + 3))
            stuff(AGAIN_LEXV, P_LEXV)
            P_LEN = z.getb(P_LEXV, P_LEXWORDS)
            ptr = z.get(OOPS_TABLE, O_START)
            inbuf_stuff(OOPS_INBUF, P_INBUF)
        else:
            z.put(OOPS_TABLE, O_END, False)
            z.tell('There was no word to replace!\n')
            return False
    else:
        if not (wrd in (W_AGAIN, W_G)):
            P_NUMBER = 0
        z.put(OOPS_TABLE, O_END, False)
    if z.get(P_LEXV, ptr) in (W_AGAIN, W_G):
        if z.getb(OOPS_INBUF, 1) == 0:
            z.tell('Beg pardon?\n')
            return False
        elif P_OFLAG:
            z.tell("It's difficult to repeat fragments.\n")
            return False
        elif not P_WON:
            z.tell('That would just repeat a mistake.\n')
            return False
        elif P_LEN > 1:
            if (z.get(P_LEXV, (ptr + P_LEXELEN)) in (W_PERIOD, W_COMMA, W_THEN)) or (z.get(P_LEXV, (ptr + P_LEXELEN)) == W_AND):
                ptr = ptr + (2 * P_LEXELEN)
                z.putb(P_LEXV, P_LEXWORDS, (z.getb(P_LEXV, P_LEXWORDS) - 2))
            else:
                z.tell("I couldn't understand that sentence.\n")
                return False
        else:
            ptr = ptr + P_LEXELEN
            z.putb(P_LEXV, P_LEXWORDS, (z.getb(P_LEXV, P_LEXWORDS) - 1))
        if z.getb(P_LEXV, P_LEXWORDS) > 0:
            stuff(P_LEXV, RESERVE_LEXV)
            RESERVE_PTR = ptr
        else:
            RESERVE_PTR = False
        WINNER = owinner
        P_MERGED = omerged
        inbuf_stuff(OOPS_INBUF, P_INBUF)
        stuff(AGAIN_LEXV, P_LEXV)
        cnt = -1
        dir = AGAIN_DIR
        while True:
            if (cnt := cnt + 1) > P_ITBLLEN:
                break
            else:
                z.put(P_ITBL, cnt, z.get(P_OTBL, cnt))
    else:
        stuff(P_LEXV, AGAIN_LEXV)
        inbuf_stuff(P_INBUF, OOPS_INBUF)
        z.put(OOPS_TABLE, O_START, ptr)
        z.put(OOPS_TABLE, O_LENGTH, (4 * P_LEN))
        len_ = 2 * (ptr + (P_LEXELEN * z.getb(P_LEXV, P_LEXWORDS)))
        z.put(OOPS_TABLE, O_END, (z.getb(P_LEXV, (len_ - 1)) + z.getb(P_LEXV, (len_ - 2))))
        RESERVE_PTR = False
        len_ = P_LEN
        P_DIR = False
        P_NCN = 0
        P_GETFLAGS = 0
        while True:
            if (P_LEN := (P_LEN - 1)) < 0:
                QUOTE_FLAG = False
                break
            elif (wrd := z.get(P_LEXV, ptr)) or (wrd := number_p(ptr)):
                if P_LEN == 0:
                    nw = 0
                else:
                    nw = z.get(P_LEXV, (ptr + P_LEXELEN))
                if (wrd == W_TO) and (verb == ACT_TELL):
                    wrd = W_QUOTE
                elif (wrd == W_THEN) and (P_LEN > 0) and (not verb) and (not QUOTE_FLAG):
                    if lw in (0, W_PERIOD):
                        wrd = W_THE
                    else:
                        z.put(P_ITBL, P_VERB, ACT_TELL)
                        z.put(P_ITBL, P_VERBN, 0)
                        wrd = W_QUOTE
                if wrd in (W_THEN, W_PERIOD, W_QUOTE):
                    if wrd == W_QUOTE:
                        if QUOTE_FLAG:
                            QUOTE_FLAG = False
                        else:
                            QUOTE_FLAG = True
                    if not ((P_LEN == 0)):
                        P_CONT = ptr + P_LEXELEN
                    z.putb(P_LEXV, P_LEXWORDS, P_LEN)
                    break
                elif (val := wt_p(wrd, PS_DIRECTION, P1_DIRECTION)) and (verb in (False, ACT_WALK)) and ((len_ == 1) or ((len_ == 2) and (verb == ACT_WALK)) or ((nw in (W_THEN, W_PERIOD, W_QUOTE)) and (not (len_ < 2))) or (QUOTE_FLAG and (len_ == 2) and (nw == W_QUOTE)) or ((len_ > 2) and (nw in (W_COMMA, W_AND)))):
                    dir = val
                    if nw in (W_COMMA, W_AND):
                        z.put(P_LEXV, (ptr + P_LEXELEN), W_THEN)
                    if not (len_ > 2):
                        QUOTE_FLAG = False
                        break
                elif (val := wt_p(wrd, PS_VERB, P1_VERB)) and (not verb):
                    verb = val
                    z.put(P_ITBL, P_VERB, val)
                    z.put(P_ITBL, P_VERBN, P_VTBL)
                    z.put(P_VTBL, 0, wrd)
                    z.putb(P_VTBL, 2, z.getb(P_LEXV, (cnt := ((ptr * 2) + 2))))
                    z.putb(P_VTBL, 3, z.getb(P_LEXV, (cnt + 1)))
                elif (val := wt_p(wrd, PS_PREPOSITION, 0)) or (wrd in (W_ALL, W_ONE)) or wt_p(wrd, PS_ADJECTIVE) or wt_p(wrd, PS_OBJECT):
                    if (P_LEN > 1) and (nw == W_OF) and (val == 0) and (not (wrd in (W_ALL, W_ONE, W_A))):
                        of_flag = True
                    elif (not (val == 0)) and ((P_LEN == 0) or (nw in (W_THEN, W_PERIOD))):
                        P_END_ON_PREP = True
                        if P_NCN < 2:
                            z.put(P_ITBL, P_PREP1, val)
                            z.put(P_ITBL, P_PREP1N, wrd)
                    elif P_NCN == 2:
                        z.tell('There were too many nouns in that sentence.\n')
                        return False
                    else:
                        P_NCN = P_NCN + 1
                        P_ACT = verb
                        if not ((ptr := clause(ptr, val, wrd))):
                            return False
                        if ptr < 0:
                            QUOTE_FLAG = False
                            break
                elif wrd == W_OF:
                    if (not of_flag) or (nw in (W_PERIOD, W_THEN)):
                        cant_use(ptr)
                        return False
                    else:
                        of_flag = False
                elif wt_p(wrd, PS_BUZZ_WORD):
                    pass
                elif (verb == ACT_TELL) and wt_p(wrd, PS_VERB, P1_VERB) and (WINNER == PLAYER):
                    z.tell('Please consult your manual for the correct way to talk to other people or creatures.\n')
                    return False
                else:
                    cant_use(ptr)
                    return False
            else:
                unknown_word(ptr)
                return False
            lw = wrd
            ptr = ptr + P_LEXELEN
    z.put(OOPS_TABLE, O_PTR, False)
    if dir:
        PRSA = V_WALK
        PRSO = dir
        P_OFLAG = False
        P_WALK_DIR = dir
        AGAIN_DIR = dir
        return AGAIN_DIR
    else:
        if P_OFLAG:
            orphan_merge()
        P_WALK_DIR = False
        AGAIN_DIR = False
        if syntax_check() and snarf_objects() and many_check() and take_check():
            return True
    return False


def stuff(src=0, dest=0, max_=29):
    ptr = P_LEXSTART
    ctr = 1
    bptr = 0
    z.putb(dest, 0, z.getb(src, 0))
    z.putb(dest, 1, z.getb(src, 1))
    while True:
        z.put(dest, ptr, z.get(src, ptr))
        bptr = (ptr * 2) + 2
        z.putb(dest, bptr, z.getb(src, bptr))
        bptr = (ptr * 2) + 3
        z.putb(dest, bptr, z.getb(src, bptr))
        ptr = ptr + P_LEXELEN
        if (ctr := ctr + 1) > max_:
            return True
    return False


def inbuf_stuff(src=0, dest=0):
    cnt = 0
    cnt = z.getb(src, 0) - 1
    while True:
        z.putb(dest, cnt, z.getb(src, cnt))
        if (cnt := cnt - 1) < 0:
            return True
    return False


def inbuf_add(len_=0, beg=0, slot=0):
    dbeg = 0
    ctr = 0
    tmp = 0
    if (tmp := z.get(OOPS_TABLE, O_END)):
        dbeg = tmp
    else:
        dbeg = z.getb(AGAIN_LEXV, (tmp := z.get(OOPS_TABLE, O_LENGTH))) + z.getb(AGAIN_LEXV, (tmp + 1))
    z.put(OOPS_TABLE, O_END, (dbeg + len_))
    while True:
        z.putb(OOPS_INBUF, (dbeg + ctr), z.getb(P_INBUF, (beg + ctr)))
        ctr = ctr + 1
        if ctr == len_:
            break
    z.putb(AGAIN_LEXV, slot, dbeg)
    return z.putb(AGAIN_LEXV, (slot - 1), len_)


def wt_p(ptr=0, bit=0, b1=5):
    offs = P_P1OFF
    typ = 0
    if z.btst((typ := z.getb(ptr, P_PSOFF)), bit):
        if b1 > 4:
            return True
        else:
            typ = typ & P_P1BITS
            if typ != b1:
                offs = offs + 1
            return z.getb(ptr, offs)
    return False


def clause(ptr=0, val=0, wrd=0):
    global P_LEN, P_NCN
    off = 0
    num = 0
    andflg = False
    first_p_p = True
    nw = 0
    lw = 0
    off = (P_NCN - 1) * 2
    if val != 0:
        z.put(P_ITBL, (num := (P_PREP1 + off)), val)
        z.put(P_ITBL, (num + 1), wrd)
        ptr = ptr + P_LEXELEN
    else:
        P_LEN = P_LEN + 1
    if P_LEN == 0:
        P_NCN = P_NCN - 1
        return -1
    z.put(P_ITBL, (num := (P_NC1 + off)), (P_LEXV + (ptr * 2)))
    if z.get(P_LEXV, ptr) in (W_THE, W_A, W_AN):
        z.put(P_ITBL, num, (z.get(P_ITBL, num) + 4))
    while True:
        if (P_LEN := (P_LEN - 1)) < 0:
            z.put(P_ITBL, (num + 1), (P_LEXV + (ptr * 2)))
            return -1
        if (wrd := z.get(P_LEXV, ptr)) or (wrd := number_p(ptr)):
            if P_LEN == 0:
                nw = 0
            else:
                nw = z.get(P_LEXV, (ptr + P_LEXELEN))
            if wrd in (W_AND, W_COMMA):
                andflg = True
            elif wrd in (W_ALL, W_ONE):
                if nw == W_OF:
                    P_LEN = P_LEN - 1
                    ptr = ptr + P_LEXELEN
            elif (wrd in (W_THEN, W_PERIOD)) or (wt_p(wrd, PS_PREPOSITION) and z.get(P_ITBL, P_VERB) and (not first_p_p)):
                P_LEN = P_LEN + 1
                z.put(P_ITBL, (num + 1), (P_LEXV + (ptr * 2)))
                return ptr - P_LEXELEN
            elif wt_p(wrd, PS_OBJECT):
                if (P_LEN > 0) and (nw == W_OF) and (not (wrd in (W_ALL, W_ONE))):
                    pass
                elif wt_p(wrd, PS_ADJECTIVE, P1_ADJECTIVE) and (nw != 0) and wt_p(nw, PS_OBJECT):
                    pass
                elif (not andflg) and (not (nw in (W_BUT, W_EXCEPT))) and (not (nw in (W_AND, W_COMMA))):
                    z.put(P_ITBL, (num + 1), (P_LEXV + ((ptr + 2) * 2)))
                    return ptr
                else:
                    andflg = False
            elif (P_MERGED or P_OFLAG or (z.get(P_ITBL, P_VERB) != 0)) and (wt_p(wrd, PS_ADJECTIVE) or wt_p(wrd, PS_BUZZ_WORD)):
                pass
            elif andflg and (wt_p(wrd, PS_DIRECTION) or wt_p(wrd, PS_VERB)):
                ptr = ptr - 4
                z.put(P_LEXV, (ptr + 2), W_THEN)
                P_LEN = P_LEN + 2
            elif wt_p(wrd, PS_PREPOSITION):
                pass
            else:
                cant_use(ptr)
                return False
        else:
            unknown_word(ptr)
            return False
        lw = wrd
        first_p_p = False
        ptr = ptr + P_LEXELEN
    return False


def number_p(ptr=0):
    global P_NUMBER
    cnt = 0
    bptr = 0
    chr_ = 0
    sum_ = 0
    tim = False
    cnt = z.getb((P_LEXV + (ptr * 2)), 2)
    bptr = z.getb((P_LEXV + (ptr * 2)), 3)
    while True:
        if (cnt := (cnt - 1)) < 0:
            break
        else:
            chr_ = z.getb(P_INBUF, bptr)
            if chr_ == 58:
                tim = sum_
                sum_ = 0
            elif sum_ > 10000:
                return False
            elif (chr_ < 58) and (chr_ > 47):
                sum_ = (sum_ * 10) + (chr_ - 48)
            else:
                return False
            bptr = bptr + 1
    z.put(P_LEXV, ptr, W_INTNUM)
    if sum_ > 1000:
        return False
    elif tim:
        if tim < 8:
            tim = tim + 12
        elif tim > 23:
            return False
        sum_ = sum_ + (tim * 60)
    P_NUMBER = sum_
    return W_INTNUM


def orphan_merge():
    global P_ACLAUSE, P_MERGED, P_NCN, P_OFLAG
    cnt = -1
    temp = 0
    verb = 0
    beg = 0
    end = 0
    adj = False
    wrd = 0
    P_OFLAG = False
    if (wt_p((wrd := z.get(z.get(P_ITBL, P_VERBN), 0)), PS_VERB, P1_VERB) == z.get(P_OTBL, P_VERB)) or (not (wt_p(wrd, PS_ADJECTIVE) == 0)):
        adj = True
    elif (not (wt_p(wrd, PS_OBJECT, P1_OBJECT) == 0)) and (P_NCN == 0):
        z.put(P_ITBL, P_VERB, 0)
        z.put(P_ITBL, P_VERBN, 0)
        z.put(P_ITBL, P_NC1, (P_LEXV + 2))
        z.put(P_ITBL, P_NC1L, (P_LEXV + 6))
        P_NCN = 1
    if (not ((verb := z.get(P_ITBL, P_VERB)) == 0)) and (not adj) and (verb != z.get(P_OTBL, P_VERB)):
        return False
    elif P_NCN == 2:
        return False
    elif z.get(P_OTBL, P_NC1) == 1:
        if ((temp := z.get(P_ITBL, P_PREP1)) == z.get(P_OTBL, P_PREP1)) or (temp == 0):
            if adj:
                z.put(P_OTBL, P_NC1, (P_LEXV + 2))
                if z.get(P_ITBL, P_NC1L) == 0:
                    z.put(P_ITBL, P_NC1L, (P_LEXV + 6))
                if P_NCN == 0:
                    P_NCN = 1
            else:
                z.put(P_OTBL, P_NC1, z.get(P_ITBL, P_NC1))
            z.put(P_OTBL, P_NC1L, z.get(P_ITBL, P_NC1L))
        else:
            return False
    elif z.get(P_OTBL, P_NC2) == 1:
        if ((temp := z.get(P_ITBL, P_PREP1)) == z.get(P_OTBL, P_PREP2)) or (temp == 0):
            if adj:
                z.put(P_ITBL, P_NC1, (P_LEXV + 2))
                if z.get(P_ITBL, P_NC1L) == 0:
                    z.put(P_ITBL, P_NC1L, (P_LEXV + 6))
            z.put(P_OTBL, P_NC2, z.get(P_ITBL, P_NC1))
            z.put(P_OTBL, P_NC2L, z.get(P_ITBL, P_NC1L))
            P_NCN = 2
        else:
            return False
    elif not (P_ACLAUSE == 0):
        if (P_NCN != 1) and (not adj):
            P_ACLAUSE = False
            return False
        else:
            beg = z.get(P_ITBL, P_NC1)
            if adj:
                beg = P_LEXV + 2
                adj = False
            end = z.get(P_ITBL, P_NC1L)
            while True:
                wrd = z.get(beg, 0)
                if beg == end:
                    if adj:
                        aclause_win(adj)
                        break
                    else:
                        P_ACLAUSE = False
                        return False
                elif (not adj) and (z.btst(z.getb(wrd, P_PSOFF), PS_ADJECTIVE) or (wrd in (W_ALL, W_ONE))):
                    adj = wrd
                elif wrd == W_ONE:
                    aclause_win(adj)
                    break
                elif z.btst(z.getb(wrd, P_PSOFF), PS_OBJECT):
                    if wrd == P_ANAM:
                        aclause_win(adj)
                    else:
                        nclause_win()
                    break
                beg = beg + P_WORDLEN
                if end == 0:
                    end = beg
                    P_NCN = 1
                    z.put(P_ITBL, P_NC1, (beg - 4))
                    z.put(P_ITBL, P_NC1L, beg)
    z.put(P_VTBL, 0, z.get(P_OVTBL, 0))
    z.putb(P_VTBL, 2, z.getb(P_OVTBL, 2))
    z.putb(P_VTBL, 3, z.getb(P_OVTBL, 3))
    z.put(P_OTBL, P_VERBN, P_VTBL)
    z.putb(P_VTBL, 2, 0)
    while True:
        if (cnt := (cnt + 1)) > P_ITBLLEN:
            P_MERGED = True
            return True
        else:
            z.put(P_ITBL, cnt, z.get(P_OTBL, cnt))
    return True


def aclause_win(adj=0):
    global P_ACLAUSE, P_NCN
    z.put(P_ITBL, P_VERB, z.get(P_OTBL, P_VERB))
    z.put(P_CCTBL, CC_SBPTR, P_ACLAUSE)
    z.put(P_CCTBL, CC_SEPTR, (P_ACLAUSE + 1))
    z.put(P_CCTBL, CC_DBPTR, P_ACLAUSE)
    z.put(P_CCTBL, CC_DEPTR, (P_ACLAUSE + 1))
    clause_copy(P_OTBL, P_OTBL, adj)
    if z.get(P_OTBL, P_NC2) != 0:
        P_NCN = 2
    P_ACLAUSE = False
    return True


def nclause_win():
    global P_ACLAUSE, P_NCN
    z.put(P_CCTBL, CC_SBPTR, P_NC1)
    z.put(P_CCTBL, CC_SEPTR, P_NC1L)
    z.put(P_CCTBL, CC_DBPTR, P_ACLAUSE)
    z.put(P_CCTBL, CC_DEPTR, (P_ACLAUSE + 1))
    clause_copy(P_ITBL, P_OTBL)
    if z.get(P_OTBL, P_NC2) != 0:
        P_NCN = 2
    P_ACLAUSE = False
    return True


def word_print(cnt=0, buf=0):
    while True:
        if (cnt := cnt - 1) < 0:
            return True
        else:
            z.printc(z.getb(P_INBUF, buf))
            buf = buf + 1
    return False


def unknown_word(ptr=0):
    global P_OFLAG, QUOTE_FLAG
    buf = 0
    z.put(OOPS_TABLE, O_PTR, ptr)
    if PRSA == V_SAY:
        z.tell('Nothing happens.\n')
        return False
    z.tell('I don\'t know the word "')
    word_print(z.getb((P_LEXV + (buf := (ptr * 2))), 2), z.getb((P_LEXV + buf), 3))
    z.tell('".\n')
    QUOTE_FLAG = False
    P_OFLAG = False
    return P_OFLAG


def cant_use(ptr=0):
    global P_OFLAG, QUOTE_FLAG
    buf = 0
    if PRSA == V_SAY:
        z.tell('Nothing happens.\n')
        return False
    z.tell('You used the word "')
    word_print(z.getb((P_LEXV + (buf := (ptr * 2))), 2), z.getb((P_LEXV + buf), 3))
    z.tell('" in a way that I don\'t understand.\n')
    QUOTE_FLAG = False
    P_OFLAG = False
    return P_OFLAG


def syntax_check():
    global P_OFLAG
    syn = 0
    len_ = 0
    num = 0
    obj = 0
    drive1 = False
    drive2 = False
    prep = 0
    verb = 0
    tmp = 0
    if (verb := z.get(P_ITBL, P_VERB)) == 0:
        z.tell('There was no verb in that sentence!\n')
        return False
    syn = z.get(VERBS, (255 - verb))
    len_ = z.getb(syn, 0)
    syn = syn + 1
    while True:
        num = z.getb(syn, P_SBITS) & P_SONUMS
        if P_NCN > num:
            pass
        elif (not (num < 1)) and (P_NCN == 0) and (((prep := z.get(P_ITBL, P_PREP1)) == 0) or (prep == z.getb(syn, P_SPREP1))):
            drive1 = syn
        elif z.getb(syn, P_SPREP1) == z.get(P_ITBL, P_PREP1):
            if (num == 2) and (P_NCN == 1):
                drive2 = syn
            elif z.getb(syn, P_SPREP2) == z.get(P_ITBL, P_PREP2):
                syntax_found(syn)
                return True
        if (len_ := len_ - 1) < 1:
            if drive1 or drive2:
                break
            else:
                z.tell("That sentence isn't one I recognize.\n")
                return False
        else:
            syn = syn + P_SYNLEN
    if drive1 and (obj := gwim(z.getb(drive1, P_SFWIM1), z.getb(drive1, P_SLOC1), z.getb(drive1, P_SPREP1))):
        z.put(P_PRSO, P_MATCHLEN, 1)
        z.put(P_PRSO, 1, obj)
        return syntax_found(drive1)
    elif drive2 and (obj := gwim(z.getb(drive2, P_SFWIM2), z.getb(drive2, P_SLOC2), z.getb(drive2, P_SPREP2))):
        z.put(P_PRSI, P_MATCHLEN, 1)
        z.put(P_PRSI, 1, obj)
        return syntax_found(drive2)
    elif verb == ACT_FIND:
        z.tell("That question can't be answered.\n")
        return False
    elif WINNER != PLAYER:
        return cant_orphan()
    else:
        orphan(drive1, drive2)
        z.tell('What do you want to ')
        tmp = z.get(P_OTBL, P_VERBN)
        if tmp == 0:
            z.tell('tell')
        elif z.getb(P_VTBL, 2) == 0:
            z.printb(z.get(tmp, 0))
        else:
            word_print(z.getb(tmp, 2), z.getb(tmp, 3))
            z.putb(P_VTBL, 2, 0)
        if drive2:
            z.tell(' ')
            thing_print(True, True)
        P_OFLAG = True
        if drive1:
            _t1 = z.getb(drive1, P_SPREP1)
        else:
            _t1 = z.getb(drive2, P_SPREP2)
        prep_print(_t1)
        z.tell('?\n')
        return False
    return False


def cant_orphan():
    z.tell('"I don\'t understand! What are you referring to?"\n')
    return False


def orphan(d1=0, d2=0):
    cnt = -1
    if not P_MERGED:
        z.put(P_OCLAUSE, P_MATCHLEN, 0)
    z.put(P_OVTBL, 0, z.get(P_VTBL, 0))
    z.putb(P_OVTBL, 2, z.getb(P_VTBL, 2))
    z.putb(P_OVTBL, 3, z.getb(P_VTBL, 3))
    while True:
        if (cnt := cnt + 1) > P_ITBLLEN:
            break
        else:
            z.put(P_OTBL, cnt, z.get(P_ITBL, cnt))
    if P_NCN == 2:
        z.put(P_CCTBL, CC_SBPTR, P_NC2)
        z.put(P_CCTBL, CC_SEPTR, P_NC2L)
        z.put(P_CCTBL, CC_DBPTR, P_NC2)
        z.put(P_CCTBL, CC_DEPTR, P_NC2L)
        clause_copy(P_ITBL, P_OTBL)
    if not (P_NCN < 1):
        z.put(P_CCTBL, CC_SBPTR, P_NC1)
        z.put(P_CCTBL, CC_SEPTR, P_NC1L)
        z.put(P_CCTBL, CC_DBPTR, P_NC1)
        z.put(P_CCTBL, CC_DEPTR, P_NC1L)
        clause_copy(P_ITBL, P_OTBL)
    if d1:
        z.put(P_OTBL, P_PREP1, z.getb(d1, P_SPREP1))
        return z.put(P_OTBL, P_NC1, 1)
    elif d2:
        z.put(P_OTBL, P_PREP2, z.getb(d2, P_SPREP2))
        return z.put(P_OTBL, P_NC2, 1)
    return False


def thing_print(prso_p=0, the_p=False):
    beg = 0
    end = 0
    if prso_p:
        beg = z.get(P_ITBL, P_NC1)
        end = z.get(P_ITBL, P_NC1L)
    else:
        beg = z.get(P_ITBL, P_NC2)
        end = z.get(P_ITBL, P_NC2L)
    return buffer_print(beg, end, the_p)


def buffer_print(beg=0, end=0, cp=0):
    nosp = True
    wrd = 0
    first_p_p = True
    pn = False
    q_p = False
    while True:
        if beg == end:
            return True
        else:
            wrd = z.get(beg, 0)
            if wrd == W_COMMA:
                z.tell(', ')
            elif nosp:
                nosp = False
            else:
                z.tell(' ')
            if wrd in (W_PERIOD, W_COMMA):
                nosp = True
            elif wrd == W_ME:
                z.printd(ME)
                pn = True
            elif wrd == W_INTNUM:
                z.printn(P_NUMBER)
                pn = True
            else:
                if first_p_p and (not pn) and cp:
                    z.tell('the ')
                if P_OFLAG or P_MERGED:
                    z.printb(wrd)
                elif (wrd == W_IT) and accessible_p(P_IT_OBJECT):
                    z.printd(P_IT_OBJECT)
                else:
                    word_print(z.getb(beg, 2), z.getb(beg, 3))
                first_p_p = False
        beg = beg + P_WORDLEN
    return False


def prep_print(prep=0):
    wrd = 0
    if not (prep == 0):
        z.tell(' ')
        wrd = prep_find(prep)
        return z.printb(wrd)
    return False


def clause_copy(src=0, dest=0, insrt=False):
    beg = 0
    end = 0
    beg = z.get(src, z.get(P_CCTBL, CC_SBPTR))
    end = z.get(src, z.get(P_CCTBL, CC_SEPTR))
    z.put(dest, z.get(P_CCTBL, CC_DBPTR), (P_OCLAUSE + ((z.get(P_OCLAUSE, P_MATCHLEN) * P_LEXELEN) + 2)))
    while True:
        if beg == end:
            z.put(dest, z.get(P_CCTBL, CC_DEPTR), (P_OCLAUSE + ((z.get(P_OCLAUSE, P_MATCHLEN) * P_LEXELEN) + 2)))
            return True
        else:
            if insrt and (P_ANAM == z.get(beg, 0)):
                clause_add(insrt)
            clause_add(z.get(beg, 0))
        beg = beg + P_WORDLEN
    return False


def clause_add(wrd=0):
    ptr = 0
    ptr = z.get(P_OCLAUSE, P_MATCHLEN) + 2
    z.put(P_OCLAUSE, (ptr - 1), wrd)
    z.put(P_OCLAUSE, ptr, 0)
    return z.put(P_OCLAUSE, P_MATCHLEN, ptr)


def prep_find(prep=0):
    cnt = 0
    size = 0
    size = z.get(PREPOSITIONS, 0) * 2
    while True:
        if (cnt := cnt + 1) > size:
            return False
        elif z.get(PREPOSITIONS, cnt) == prep:
            return z.get(PREPOSITIONS, (cnt - 1))
    return False


def syntax_found(syn=0):
    global PRSA, P_SYNTAX
    P_SYNTAX = syn
    PRSA = z.getb(syn, P_SACTION)
    return PRSA


def gwim(gbit=0, lbit=0, prep=0):
    global P_GWIMBIT, P_SLOCBITS
    obj = 0
    if gbit == RMUNGBIT:
        return ROOMS
    P_GWIMBIT = gbit
    P_SLOCBITS = lbit
    z.put(P_MERGE, P_MATCHLEN, 0)
    if get_object(P_MERGE, False):
        P_GWIMBIT = 0
        if z.get(P_MERGE, P_MATCHLEN) == 1:
            obj = z.get(P_MERGE, 1)
            z.tell('(')
            if (not (prep == 0)) and (not P_END_ON_PREP):
                z.printb((prep := prep_find(prep)))
                if prep == W_OUT:
                    z.tell(' of')
                z.tell(' ')
                if obj == HANDS:
                    z.tell('your hands')
                else:
                    z.tell('the ', z.D(obj))
                z.tell(')\n')
            else:
                z.tell(z.D(obj), ')\n')
            return obj
    else:
        P_GWIMBIT = 0
        return False
    return False


def snarf_objects():
    global P_PRSI, P_PRSO, P_SLOCBITS
    optr = 0
    iptr = 0
    l = 0
    z.put(P_BUTS, P_MATCHLEN, 0)
    if (iptr := z.get(P_ITBL, P_NC2)) != 0:
        P_SLOCBITS = z.getb(P_SYNTAX, P_SLOC2)
        if not (snarfem(iptr, z.get(P_ITBL, P_NC2L), P_PRSI)):
            return False
    if (optr := z.get(P_ITBL, P_NC1)) != 0:
        P_SLOCBITS = z.getb(P_SYNTAX, P_SLOC1)
        if not (snarfem(optr, z.get(P_ITBL, P_NC1L), P_PRSO)):
            return False
    if not (z.get(P_BUTS, P_MATCHLEN) == 0):
        l = z.get(P_PRSO, P_MATCHLEN)
        if optr:
            P_PRSO = but_merge(P_PRSO)
        if iptr and ((not optr) or (l == z.get(P_PRSO, P_MATCHLEN))):
            P_PRSI = but_merge(P_PRSI)
    return True


def but_merge(tbl=0):
    global P_MERGE
    len_ = 0
    butlen = 0
    cnt = 1
    matches = 0
    obj = 0
    ntbl = 0
    len_ = z.get(tbl, P_MATCHLEN)
    z.put(P_MERGE, P_MATCHLEN, 0)
    while True:
        if (len_ := len_ - 1) < 0:
            break
        elif zmemq((obj := z.get(tbl, cnt)), P_BUTS):
            pass
        else:
            z.put(P_MERGE, (matches + 1), obj)
            matches = matches + 1
        cnt = cnt + 1
    z.put(P_MERGE, P_MATCHLEN, matches)
    ntbl = P_MERGE
    P_MERGE = tbl
    return ntbl


def snarfem(ptr=0, eptr=0, tbl=0):
    global P_ADJ, P_ADJN, P_AND, P_GETFLAGS, P_NAM, P_ONEOBJ
    but = False
    len_ = 0
    wv = 0
    wrd = 0
    nw = 0
    was_all = False
    P_AND = False
    if P_GETFLAGS == P_ALL:
        was_all = True
    P_GETFLAGS = 0
    z.put(tbl, P_MATCHLEN, 0)
    wrd = z.get(ptr, 0)
    while True:
        if ptr == eptr:
            wv = get_object((but or tbl))
            if was_all:
                P_GETFLAGS = P_ALL
            return wv
        else:
            if eptr == (ptr + P_WORDLEN):
                nw = 0
            else:
                nw = z.get(ptr, P_LEXELEN)
            if wrd == W_ALL:
                P_GETFLAGS = P_ALL
                if nw == W_OF:
                    ptr = ptr + P_WORDLEN
            elif wrd in (W_BUT, W_EXCEPT):
                if not (get_object((but or tbl))):
                    return False
                but = P_BUTS
                z.put(but, P_MATCHLEN, 0)
            elif wrd in (W_A, W_ONE):
                if not P_ADJ:
                    P_GETFLAGS = P_ONE
                    if nw == W_OF:
                        ptr = ptr + P_WORDLEN
                else:
                    P_NAM = P_ONEOBJ
                    if not (get_object((but or tbl))):
                        return False
                    if nw == 0:
                        return True
            elif (wrd in (W_AND, W_COMMA)) and (not (nw in (W_AND, W_COMMA))):
                P_AND = True
                if not (get_object((but or tbl))):
                    return False
            elif wt_p(wrd, PS_BUZZ_WORD):
                pass
            elif wrd in (W_AND, W_COMMA):
                pass
            elif wrd == W_OF:
                if P_GETFLAGS == 0:
                    P_GETFLAGS = P_INHIBIT
            elif (wv := wt_p(wrd, PS_ADJECTIVE, P1_ADJECTIVE)) and (not P_ADJ):
                P_ADJ = wv
                P_ADJN = wrd
            elif wt_p(wrd, PS_OBJECT, P1_OBJECT):
                P_NAM = wrd
                P_ONEOBJ = wrd
        if ptr != eptr:
            ptr = ptr + P_WORDLEN
            wrd = nw
    return False


def get_object(tbl=0, vrb=True):
    global P_AADJ, P_ACLAUSE, P_ADJ, P_ADJN, P_ANAM, P_NAM, P_OFLAG, P_SLOCBITS
    global P_TABLE, P_XADJ, P_XADJN, P_XNAM
    bits = 0
    len_ = 0
    xbits = 0
    tlen = 0
    gcheck = False
    olen = 0
    obj = 0
    xbits = P_SLOCBITS
    tlen = z.get(tbl, P_MATCHLEN)
    if z.btst(P_GETFLAGS, P_INHIBIT):
        return True
    if (not P_NAM) and P_ADJ:
        if wt_p(P_ADJN, PS_OBJECT, P1_OBJECT):
            P_NAM = P_ADJN
            P_ADJ = False
        elif null_f():
            pass
    if (not P_NAM) and (not P_ADJ) and (P_GETFLAGS != P_ALL) and (P_GWIMBIT == 0):
        if vrb:
            z.tell('There seems to be a noun missing in that sentence!\n')
        return False
    if (P_GETFLAGS != P_ALL) or (P_SLOCBITS == 0):
        P_SLOCBITS = -1
    P_TABLE = tbl
    while True:
        if gcheck:
            global_check(tbl)
        else:
            if LIT:
                z.fclear(PLAYER, TRANSBIT)
                do_sl(HERE, SOG, SIR)
                z.fset(PLAYER, TRANSBIT)
            do_sl(PLAYER, SH, SC)
        len_ = z.get(tbl, P_MATCHLEN) - tlen
        if z.btst(P_GETFLAGS, P_ALL):
            pass
        elif z.btst(P_GETFLAGS, P_ONE) and (not (len_ == 0)):
            if len_ != 1:
                z.put(tbl, 1, z.get(tbl, z.random(len_)))
                z.tell('(How about the ')
                z.printd(z.get(tbl, 1))
                z.tell('?)\n')
            z.put(tbl, P_MATCHLEN, 1)
        elif (len_ > 1) or ((len_ == 0) and (P_SLOCBITS != -1)):
            if P_SLOCBITS == -1:
                P_SLOCBITS = xbits
                olen = len_
                z.put(tbl, P_MATCHLEN, (z.get(tbl, P_MATCHLEN) - len_))
                continue
            else:
                if len_ == 0:
                    len_ = olen
                if WINNER != PLAYER:
                    cant_orphan()
                    return False
                elif vrb and P_NAM:
                    which_print(tlen, len_, tbl)
                    if tbl == P_PRSO:
                        P_ACLAUSE = P_NC1
                    else:
                        P_ACLAUSE = P_NC2
                    P_AADJ = P_ADJ
                    P_ANAM = P_NAM
                    orphan(False, False)
                    P_OFLAG = True
                elif vrb:
                    z.tell('There seems to be a noun missing in that sentence!\n')
                P_NAM = False
                P_ADJ = False
                return False
        if (len_ == 0) and gcheck:
            if vrb:
                P_SLOCBITS = xbits
                if LIT or (PRSA == V_TELL):
                    obj_found(NOT_HERE_OBJECT, tbl)
                    P_XNAM = P_NAM
                    P_XADJ = P_ADJ
                    P_XADJN = P_ADJN
                    P_NAM = False
                    P_ADJ = False
                    P_ADJN = False
                    return True
                else:
                    z.tell("It's too dark to see!\n")
            P_NAM = False
            P_ADJ = False
            return False
        elif len_ == 0:
            gcheck = True
            continue
        P_SLOCBITS = xbits
        P_NAM = False
        P_ADJ = False
        return True
    return False


def which_print(tlen=0, len_=0, tbl=0):
    obj = 0
    rlen = 0
    rlen = len_
    z.tell('Which ')
    if P_OFLAG or P_MERGED or P_AND:
        if P_NAM:
            _t1 = P_NAM
        elif P_ADJ:
            _t1 = P_ADJN
        else:
            _t1 = W_ONE
        z.printb(_t1)
    else:
        thing_print((tbl == P_PRSO))
    z.tell(' do you mean, ')
    while True:
        tlen = tlen + 1
        obj = z.get(tbl, tlen)
        z.tell('the ', z.D(obj))
        if len_ == 2:
            if rlen != 2:
                z.tell(',')
            z.tell(' or ')
        elif len_ > 2:
            z.tell(', ')
        if (len_ := (len_ - 1)) < 1:
            z.tell('?\n')
            return True
    return False


def global_check(tbl=0):
    global P_SLOCBITS, P_TABLE
    len_ = 0
    rmg = 0
    rmgl = 0
    cnt = 0
    obj = 0
    obits = 0
    foo = 0
    len_ = z.get(tbl, P_MATCHLEN)
    obits = P_SLOCBITS
    if (rmg := z.getpt(HERE, P_GLOBAL)):
        rmgl = z.ptsize(rmg) - 1
        while True:
            if this_it_p((obj := z.getb(rmg, cnt)), tbl):
                obj_found(obj, tbl)
            if (cnt := cnt + 1) > rmgl:
                break
    if (rmg := z.getpt(HERE, P_PSEUDO)):
        rmgl = z.div(z.ptsize(rmg), 4) - 1
        cnt = 0
        while True:
            if P_NAM == z.get(rmg, (cnt * 2)):
                z.putp(PSEUDO_OBJECT, P_ACTION, z.get(rmg, ((cnt * 2) + 1)))
                foo = z.getpt(PSEUDO_OBJECT, P_ACTION) - 5
                z.put(foo, 0, z.get(P_NAM, 0))
                z.put(foo, 1, z.get(P_NAM, 1))
                obj_found(PSEUDO_OBJECT, tbl)
                break
            elif (cnt := cnt + 1) > rmgl:
                break
    if z.get(tbl, P_MATCHLEN) == len_:
        P_SLOCBITS = -1
        P_TABLE = tbl
        do_sl(GLOBAL_OBJECTS, 1, 1)
        P_SLOCBITS = obits
        if (z.get(tbl, P_MATCHLEN) == 0) and (PRSA in (V_LOOK_INSIDE, V_SEARCH, V_EXAMINE)):
            return do_sl(ROOMS, 1, 1)
    return False


def do_sl(obj=0, bit1=0, bit2=0):
    bts = 0
    if z.btst(P_SLOCBITS, (bit1 + bit2)):
        return search_list(obj, P_TABLE, P_SRCALL)
    else:
        if z.btst(P_SLOCBITS, bit1):
            return search_list(obj, P_TABLE, P_SRCTOP)
        elif z.btst(P_SLOCBITS, bit2):
            return search_list(obj, P_TABLE, P_SRCBOT)
        else:
            return True
    return False


def search_list(obj=0, tbl=0, lvl=0):
    fls = 0
    nobj = 0
    if (obj := z.first_p(obj)):
        while True:
            if (lvl != P_SRCBOT) and z.getpt(obj, P_SYNONYM) and this_it_p(obj, tbl):
                obj_found(obj, tbl)
            if ((lvl != P_SRCTOP) or z.fset_p(obj, SEARCHBIT) or z.fset_p(obj, SURFACEBIT)) and (nobj := z.first_p(obj)) and (z.fset_p(obj, OPENBIT) or z.fset_p(obj, TRANSBIT)):
                if z.fset_p(obj, SURFACEBIT):
                    _t1 = P_SRCALL
                elif z.fset_p(obj, SEARCHBIT):
                    _t1 = P_SRCALL
                else:
                    _t1 = P_SRCTOP
                fls = search_list(obj, tbl, _t1)
            if (obj := z.next_p(obj)):
                pass
            else:
                return True
    return False


def obj_found(obj=0, tbl=0):
    ptr = 0
    ptr = z.get(tbl, P_MATCHLEN)
    z.put(tbl, (ptr + 1), obj)
    return z.put(tbl, P_MATCHLEN, (ptr + 1))


def take_check():
    return itake_check(P_PRSO, z.getb(P_SYNTAX, P_SLOC1)) and itake_check(P_PRSI, z.getb(P_SYNTAX, P_SLOC2))


def itake_check(tbl=0, ibits=0):
    global PRSO
    ptr = 0
    obj = 0
    taken = 0
    if (ptr := z.get(tbl, P_MATCHLEN)) and (z.btst(ibits, SHAVE) or z.btst(ibits, STAKE)):
        while True:
            if (ptr := (ptr - 1)) < 0:
                return True
            else:
                obj = z.get(tbl, (ptr + 1))
                if obj == IT:
                    if not accessible_p(P_IT_OBJECT):
                        z.tell("I don't see what you're referring to.\n")
                        return False
                    else:
                        obj = P_IT_OBJECT
                if (not held_p(obj)) and (not (obj in (HANDS, ME))):
                    PRSO = obj
                    if z.fset_p(obj, TRYTAKEBIT):
                        taken = True
                    elif WINNER != ADVENTURER:
                        taken = False
                    elif z.btst(ibits, STAKE) and (itake(False) == True):
                        taken = False
                    else:
                        taken = True
                    if taken and z.btst(ibits, SHAVE) and (WINNER == ADVENTURER):
                        if obj == NOT_HERE_OBJECT:
                            z.tell("You don't have that!\n")
                            return False
                        z.tell("You don't have the ")
                        z.printd(obj)
                        z.tell('.\n')
                        return False
                    elif (not taken) and (WINNER == ADVENTURER):
                        z.tell('(Taken)\n')
    else:
        return True
    return False


def many_check():
    loss = False
    tmp = 0
    if (z.get(P_PRSO, P_MATCHLEN) > 1) and (not z.btst(z.getb(P_SYNTAX, P_SLOC1), SMANY)):
        loss = 1
    elif (z.get(P_PRSI, P_MATCHLEN) > 1) and (not z.btst(z.getb(P_SYNTAX, P_SLOC2), SMANY)):
        loss = 2
    if loss:
        z.tell("You can't use multiple ")
        if loss == 2:
            z.tell('in')
        z.tell('direct objects with "')
        tmp = z.get(P_ITBL, P_VERBN)
        if tmp == 0:
            z.tell('tell')
        elif P_OFLAG or P_MERGED:
            z.printb(z.get(tmp, 0))
        else:
            word_print(z.getb(tmp, 2), z.getb(tmp, 3))
        z.tell('".\n')
        return False
    else:
        return True
    return False


def zmemq(itm=0, tbl=0, size=-1):
    cnt = 1
    if not tbl:
        return False
    if not (size < 0):
        cnt = 0
    else:
        size = z.get(tbl, 0)
    while True:
        if itm == z.get(tbl, cnt):
            return tbl + (cnt * 2)
        elif (cnt := cnt + 1) > size:
            return False
    return False


def zmemqb(itm=0, tbl=0, size=0):
    cnt = 0
    while True:
        if itm == z.getb(tbl, cnt):
            return True
        elif (cnt := cnt + 1) > size:
            return False
    return False


def lit_p(rm=0, rmbit=True):
    global HERE, P_GWIMBIT, P_SLOCBITS, P_TABLE
    ohere = 0
    lit = False
    if ALWAYS_LIT and (WINNER == PLAYER):
        return True
    P_GWIMBIT = ONBIT
    ohere = HERE
    HERE = rm
    if rmbit and z.fset_p(rm, ONBIT):
        lit = True
    else:
        z.put(P_MERGE, P_MATCHLEN, 0)
        P_TABLE = P_MERGE
        P_SLOCBITS = -1
        if ohere == rm:
            do_sl(WINNER, 1, 1)
            if (WINNER != PLAYER) and z.in_p(PLAYER, rm):
                do_sl(PLAYER, 1, 1)
        do_sl(rm, 1, 1)
        if z.get(P_TABLE, P_MATCHLEN) > 0:
            lit = True
    HERE = ohere
    P_GWIMBIT = 0
    return lit


def this_it_p(obj=0, tbl=0):
    syns = 0
    if z.fset_p(obj, INVISIBLE):
        return False
    elif P_NAM and (not zmemq(P_NAM, (syns := z.getpt(obj, P_SYNONYM)), (z.div(z.ptsize(syns), 2) - 1))):
        return False
    elif P_ADJ and ((not (syns := z.getpt(obj, P_ADJECTIVE))) or (not zmemqb(P_ADJ, syns, (z.ptsize(syns) - 1)))):
        return False
    elif (not (P_GWIMBIT == 0)) and (not z.fset_p(obj, P_GWIMBIT)):
        return False
    return True


def accessible_p(obj=0):
    l = z.loc(obj)
    if z.fset_p(obj, INVISIBLE):
        return False
    elif not l:
        return False
    elif l == GLOBAL_OBJECTS:
        return True
    elif (l == LOCAL_GLOBALS) and global_in_p(obj, HERE):
        return True
    elif not (meta_loc(obj) in (HERE, z.loc(WINNER))):
        return False
    elif l in (WINNER, HERE, z.loc(WINNER)):
        return True
    elif z.fset_p(l, OPENBIT) and accessible_p(l):
        return True
    else:
        return False
    return False


def meta_loc(obj=0):
    while True:
        if not obj:
            return False
        elif z.in_p(obj, GLOBAL_OBJECTS):
            return GLOBAL_OBJECTS
        if z.in_p(obj, ROOMS):
            return obj
        else:
            obj = z.loc(obj)
    return False


def v_verbose():
    global SUPER_BRIEF, VERBOSE
    VERBOSE = True
    SUPER_BRIEF = False
    z.tell('Maximum verbosity.\n')
    return True


def v_brief():
    global SUPER_BRIEF, VERBOSE
    VERBOSE = False
    SUPER_BRIEF = False
    z.tell('Brief descriptions.\n')
    return True


def v_super_brief():
    global SUPER_BRIEF
    SUPER_BRIEF = True
    z.tell('Superbrief descriptions.\n')
    return True


def v_inventory():
    if z.first_p(WINNER):
        return print_cont(WINNER)
    else:
        z.tell('You are empty-handed.\n')
        return True
    return False


def finish():
    wrd = 0
    v_score()
    while True:
        z.crlf()
        z.tell('Would you like to restart the game from the beginning, restore a saved game position, or end this session of the game?\n(Type RESTART, RESTORE, or QUIT):\n>')
        z.read(P_INBUF, P_LEXV)
        wrd = z.get(P_LEXV, 1)
        if wrd == W_RESTART:
            z.restart()
            z.tell('Failed.\n')
        elif wrd == W_RESTORE:
            if z.restore():
                z.tell('Ok.\n')
            else:
                z.tell('Failed.\n')
        elif wrd in (W_QUIT, W_Q):
            z.quit()
    return False


def v_quit():
    scor = 0
    v_score()
    z.tell('Do you wish to leave the game? (Y is affirmative): ')
    if yes_p():
        return z.quit()
    else:
        z.tell('Ok.\n')
        return True
    return False


def v_restart():
    v_score(True)
    z.tell('Do you wish to restart? (Y is affirmative): ')
    if yes_p():
        z.tell('Restarting.\n')
        z.restart()
        z.tell('Failed.\n')
        return True
    return False


def v_restore():
    if z.restore():
        z.tell('Ok.\n')
        return v_first_look()
    else:
        z.tell('Failed.\n')
        return True
    return False


def v_save():
    if z.save():
        z.tell('Ok.\n')
        return True
    else:
        z.tell('Failed.\n')
        return True
    return False


def v_script():
    z.put(0, 8, (z.get(0, 8) | 1))
    z.tell('Here begins a transcript of interaction with\n')
    v_version()
    return True


def v_unscript():
    z.tell('Here ends a transcript of interaction with\n')
    v_version()
    z.put(0, 8, (z.get(0, 8) & -2))
    return True


def v_version():
    cnt = 17
    z.tell('ZORK I: The Great Underground Empire\nInfocom interactive fiction - a fantasy story\nCopyright (c) 1981, 1982, 1983, 1984, 1985, 1986')
    z.tell(' Infocom, Inc. All rights reserved.\n')
    z.tell('ZORK is a registered trademark of Infocom, Inc.\nRelease ')
    z.printn((z.get(0, 1) & 2047))
    z.tell(' / Serial number ')
    while True:
        if (cnt := (cnt + 1)) > 23:
            break
        else:
            z.printc(z.getb(0, cnt))
    return z.crlf()


def v_verify():
    z.tell('Verifying disk...\n')
    if z.verify():
        z.tell('The disk is correct.\n')
        return True
    else:
        z.tell('\n** Disk Failure **\n')
        return True
    return False


def v_command_file():
    z.dirin(1)
    return True


def v_random():
    if PRSO != INTNUM:
        z.tell('Illegal call to #RND.\n')
        return True
    else:
        z.random((0 - P_NUMBER))
        return True
    return False


def v_record():
    z.dirout(4)
    return True


def v_unrecord():
    z.dirout(-4)
    return True


def v_advent():
    z.tell('A hollow voice says "Fool."\n')
    return True


def v_alarm():
    if z.fset_p(PRSO, ACTORBIT):
        if z.getp(PRSO, P_STRENGTH) < 0:
            z.tell('The ', z.D(PRSO), ' is rudely awakened.\n')
            return awaken(PRSO)
        else:
            z.tell("He's wide awake, or haven't you noticed...\n")
            return True
    else:
        z.tell('The ', z.D(PRSO), " isn't sleeping.\n")
        return True
    return False


def v_answer():
    global P_CONT, QUOTE_FLAG
    z.tell('Nobody seems to be awaiting your answer.\n')
    P_CONT = False
    QUOTE_FLAG = False
    return True


def v_attack():
    if not z.fset_p(PRSO, ACTORBIT):
        z.tell("I've known strange people, but fighting a ", z.D(PRSO), '?\n')
        return True
    elif (not PRSI) or (PRSI == HANDS):
        z.tell('Trying to attack a ', z.D(PRSO), ' with your bare hands is suicidal.\n')
        return True
    elif not z.in_p(PRSI, WINNER):
        z.tell("You aren't even holding the ", z.D(PRSI), '.\n')
        return True
    elif not z.fset_p(PRSI, WEAPONBIT):
        z.tell('Trying to attack the ', z.D(PRSO), ' with a ', z.D(PRSI), ' is suicidal.\n')
        return True
    else:
        return hero_blow()
    return False


def v_back():
    z.tell('Sorry, my memory is poor. Please give a direction.\n')
    return True


def v_blast():
    z.tell("You can't blast anything by using words.\n")
    return True


def pre_board():
    av = 0
    av = z.loc(WINNER)
    if null_f():
        return True
    elif z.fset_p(PRSO, VEHBIT):
        if not z.in_p(PRSO, HERE):
            z.tell('The ', z.D(PRSO), ' must be on the ground to be boarded.\n')
        elif z.fset_p(av, VEHBIT):
            z.tell('You are already in the ', z.D(av), '!\n')
        else:
            return False
    elif PRSO in (WATER, GLOBAL_WATER):
        perform(V_SWIM, PRSO)
        return True
    else:
        z.tell('You have a theory on how to board a ', z.D(PRSO), ', perhaps?\n')
    return 2


def v_board():
    av = 0
    z.tell('You are now in the ', z.D(PRSO), '.\n')
    z.move(WINNER, PRSO)
    z.apply(z.getp(PRSO, P_ACTION), M_ENTER)
    return True


def v_breathe():
    return perform(V_INFLATE, PRSO, LUNGS)


def v_brush():
    z.tell('If you wish, but heaven only knows why.\n')
    return True


def v_bug():
    z.tell('Bug? Not in a flawless program like this! (Cough, cough).\n')
    return True


def tell_no_prsi():
    z.tell("You didn't say with what!\n")
    return True


def pre_burn():
    if not PRSI:
        return tell_no_prsi()
    elif z.fset_p(PRSI, FLAMEBIT) and z.fset_p(PRSI, ONBIT):
        return False
    else:
        z.tell('With a ', z.D(PRSI), '??!?\n')
        return True
    return False


def v_burn():
    if null_f():
        return False
    elif z.fset_p(PRSO, BURNBIT):
        if z.in_p(PRSO, WINNER) or z.in_p(WINNER, PRSO):
            remove_carefully(PRSO)
            z.tell('The ', z.D(PRSO))
            z.tell(' catches fire. Unfortunately, you were ')
            if z.in_p(WINNER, PRSO):
                z.tell('in')
            else:
                z.tell('holding')
            return jigs_up(' it at the time.')
        else:
            remove_carefully(PRSO)
            z.tell('The ', z.D(PRSO), ' catches fire and is consumed.\n')
            return True
    else:
        z.tell("You can't burn a ", z.D(PRSO), '.\n')
        return True
    return False


def v_chomp():
    z.tell('Preposterous!\n')
    return True


def v_climb_down():
    return v_climb_up(P_DOWN, PRSO)


def v_climb_foo():
    return v_climb_up(P_UP, PRSO)


def v_climb_on():
    if z.fset_p(PRSO, VEHBIT):
        perform(V_BOARD, PRSO)
        return True
    else:
        z.tell("You can't climb onto the ", z.D(PRSO), '.\n')
        return True
    return False


def v_climb_up(dir=z.NOARG, obj=False):
    if dir is z.NOARG:
        dir = P_UP
    x = 0
    tx = 0
    if obj and (PRSO != ROOMS):
        obj = PRSO
    if (tx := z.getpt(HERE, dir)):
        if obj:
            x = z.ptsize(tx)
            if (x == NEXIT) or ((x in (CEXIT, DEXIT, UEXIT)) and (not global_in_p(PRSO, z.getb(tx, 0)))):
                z.tell('The ', z.D(obj), ' do')
                if obj != STAIRS:
                    z.tell('es')
                z.tell("n't lead ")
                if dir == P_UP:
                    z.tell('up')
                else:
                    z.tell('down')
                z.tell('ward.\n')
                return True
        do_walk(dir)
        return True
    elif obj and zmemq(W_WALL, (x := z.getpt(PRSO, P_SYNONYM)), z.ptsize(x)):
        z.tell('Climbing the walls is to no avail.\n')
        return True
    elif (HERE != PATH) and (obj in (False, TREE)) and global_in_p(TREE, HERE):
        z.tell('There are no climbable trees here.\n')
        return True
    elif obj in (False, ROOMS):
        z.tell("You can't go that way.\n")
        return True
    else:
        z.tell("You can't do that!\n")
        return True
    return False


def v_close():
    global LIT
    if (not z.fset_p(PRSO, CONTBIT)) and (not z.fset_p(PRSO, DOORBIT)):
        z.tell('You must tell me how to do that to a ', z.D(PRSO), '.\n')
        return True
    elif (not z.fset_p(PRSO, SURFACEBIT)) and (z.getp(PRSO, P_CAPACITY) != 0):
        if z.fset_p(PRSO, OPENBIT):
            z.fclear(PRSO, OPENBIT)
            z.tell('Closed.\n')
            if LIT and (not (LIT := lit_p(HERE))):
                z.tell('It is now pitch black.\n')
            return True
        else:
            z.tell('It is already closed.\n')
            return True
    elif z.fset_p(PRSO, DOORBIT):
        if z.fset_p(PRSO, OPENBIT):
            z.fclear(PRSO, OPENBIT)
            z.tell('The ', z.D(PRSO), ' is now closed.\n')
            return True
        else:
            z.tell('It is already closed.\n')
            return True
    else:
        z.tell('You cannot close that.\n')
        return True
    return False


def v_command():
    if z.fset_p(PRSO, ACTORBIT):
        z.tell('The ', z.D(PRSO), ' pays no attention.\n')
        return True
    else:
        z.tell('You cannot talk to that!\n')
        return True
    return False


def v_count():
    if PRSO == BLESSINGS:
        z.tell('Well, for one, you are playing Zork...\n')
        return True
    else:
        z.tell('You have lost your mind.\n')
        return True
    return False


def v_cross():
    z.tell("You can't cross that!\n")
    return True


def v_curses():
    if PRSO:
        if z.fset_p(PRSO, ACTORBIT):
            z.tell("Insults of this nature won't help you.\n")
            return True
        else:
            z.tell('What a loony!\n')
            return True
    else:
        z.tell('Such language in a high-class establishment like this!\n')
        return True
    return False


def v_cut():
    if z.fset_p(PRSO, ACTORBIT):
        return perform(V_ATTACK, PRSO, PRSI)
    elif z.fset_p(PRSO, BURNBIT) and z.fset_p(PRSI, WEAPONBIT):
        if z.in_p(WINNER, PRSO):
            z.tell("Not a bright idea, especially since you're in it.\n")
            return True
        remove_carefully(PRSO)
        z.tell('Your skillful ', z.D(PRSI), 'smanship slices the ', z.D(PRSO), ' into innumerable slivers which blow away.\n')
        return True
    elif not z.fset_p(PRSI, WEAPONBIT):
        z.tell('The "cutting edge" of a ', z.D(PRSI), ' is hardly adequate.\n')
        return True
    else:
        z.tell('Strange concept, cutting the ', z.D(PRSO), '....\n')
        return True
    return False


def v_deflate():
    z.tell('Come on, now!\n')
    return True


def v_dig():
    global PRSI
    if not PRSI:
        PRSI = HANDS
    if PRSI == SHOVEL:
        z.tell("There's no reason to be digging here.\n")
        return True
    if z.fset_p(PRSI, TOOLBIT):
        z.tell('Digging with the ', z.D(PRSI), ' is slow and tedious.\n')
        return True
    else:
        z.tell('Digging with a ', z.D(PRSI), ' is silly.\n')
        return True
    return False


def v_disembark():
    if (PRSO == ROOMS) and z.fset_p(z.loc(WINNER), VEHBIT):
        perform(V_DISEMBARK, z.loc(WINNER))
        return True
    elif z.loc(WINNER) != PRSO:
        z.tell("You're not in that!\n")
        return 2
    elif z.fset_p(HERE, RLANDBIT):
        z.tell('You are on your own feet again.\n')
        return z.move(WINNER, HERE)
    else:
        z.tell('You realize that getting out here would be fatal.\n')
        return 2
    return False


def v_disenchant():
    z.tell('Nothing happens.\n')
    return True


def v_drink():
    return v_eat()


def v_drink_from():
    z.tell('How peculiar!\n')
    return True


def pre_drop():
    if PRSO == z.loc(WINNER):
        perform(V_DISEMBARK, PRSO)
        return True
    return False


def v_drop():
    if idrop():
        z.tell('Dropped.\n')
        return True
    return False


def v_eat():
    eat_p = False
    drink_p = False
    nobj = False
    if (eat_p := z.fset_p(PRSO, FOODBIT)):
        if (not z.in_p(PRSO, WINNER)) and (not z.in_p(z.loc(PRSO), WINNER)):
            z.tell("You're not holding that.\n")
        elif PRSA == V_DRINK:
            z.tell('How can you drink that?')
        else:
            z.tell('Thank you very much. It really hit the spot.')
            remove_carefully(PRSO)
        return z.crlf()
    elif z.fset_p(PRSO, DRINKBIT):
        drink_p = True
        nobj = z.loc(PRSO)
        if z.in_p(PRSO, GLOBAL_OBJECTS) or global_in_p(GLOBAL_WATER, HERE) or (PRSO == PSEUDO_OBJECT):
            return hit_spot()
        elif (not nobj) or (not accessible_p(nobj)):
            z.tell("There isn't any water here.\n")
            return True
        elif accessible_p(nobj) and (not z.in_p(nobj, WINNER)):
            z.tell('You have to be holding the ', z.D(nobj), ' first.\n')
            return True
        elif not z.fset_p(nobj, OPENBIT):
            z.tell("You'll have to open the ", z.D(nobj), ' first.\n')
            return True
        else:
            return hit_spot()
    elif not (eat_p or drink_p):
        z.tell("I don't think that the ", z.D(PRSO), ' would agree with you.\n')
        return True
    return False


def hit_spot():
    if (PRSO == WATER) and (not global_in_p(GLOBAL_WATER, HERE)):
        remove_carefully(PRSO)
    z.tell('Thank you very much. I was rather thirsty (from all this talking, probably).\n')
    return True


def v_echo():
    lst = 0
    max_ = 0
    ech = 0
    cnt = 0
    if z.getb(P_LEXV, P_LEXWORDS) > 0:
        lst = P_LEXV + (z.getb(P_LEXV, P_LEXWORDS) * P_WORDLEN)
        max_ = (z.getb(lst, 0) + z.getb(lst, 1)) - 1
        while True:
            if (ech := (ech + 1)) > 2:
                z.tell('...\n')
                return True
            else:
                cnt = z.getb(lst, 1) - 1
                while True:
                    if (cnt := (cnt + 1)) > max_:
                        break
                    else:
                        z.printc(z.getb(P_INBUF, cnt))
                z.tell(' ')
    else:
        z.tell('echo echo ...\n')
        return True
    return False


def v_enchant():
    null_f()
    return v_disenchant()


def remove_carefully(obj=0):
    global LIT, P_IT_OBJECT
    olit = 0
    if obj == P_IT_OBJECT:
        P_IT_OBJECT = False
    olit = LIT
    z.remove(obj)
    LIT = lit_p(HERE)
    if olit and (olit != LIT):
        z.tell('You are left in the dark...\n')
    return True


def v_enter():
    return do_walk(P_IN)


def v_examine():
    if z.getp(PRSO, P_TEXT):
        z.tell(z.S(z.getp(PRSO, P_TEXT)), '\n')
        return True
    elif z.fset_p(PRSO, CONTBIT) or z.fset_p(PRSO, DOORBIT):
        return v_look_inside()
    else:
        z.tell("There's nothing special about the ", z.D(PRSO), '.\n')
        return True
    return False


def v_exit():
    if (PRSO in (False, ROOMS)) and z.fset_p(z.loc(WINNER), VEHBIT):
        perform(V_DISEMBARK, z.loc(WINNER))
        return True
    elif PRSO and z.in_p(WINNER, PRSO):
        perform(V_DISEMBARK, PRSO)
        return True
    else:
        return do_walk(P_OUT)
    return False


def v_exorcise():
    z.tell('What a bizarre concept!\n')
    return True


def pre_fill():
    tx = 0
    if not PRSI:
        tx = z.getpt(HERE, P_GLOBAL)
        if tx and zmemqb(GLOBAL_WATER, tx, (z.ptsize(tx) - 1)):
            perform(V_FILL, PRSO, GLOBAL_WATER)
            return True
        elif z.in_p(WATER, z.loc(WINNER)):
            perform(V_FILL, PRSO, WATER)
            return True
        else:
            z.tell('There is nothing to fill it with.\n')
            return True
    if PRSI == WATER:
        return False
    elif PRSI != GLOBAL_WATER:
        perform(V_PUT, PRSI, PRSO)
        return True
    return False


def v_fill():
    if not PRSI:
        if global_in_p(GLOBAL_WATER, HERE):
            perform(V_FILL, PRSO, GLOBAL_WATER)
            return True
        elif z.in_p(WATER, z.loc(WINNER)):
            perform(V_FILL, PRSO, WATER)
            return True
        else:
            z.tell("There's nothing to fill it with.\n")
            return True
    else:
        z.tell("You may know how to do that, but I don't.\n")
        return True
    return False


def v_find():
    l = z.loc(PRSO)
    if PRSO in (HANDS, LUNGS):
        z.tell("Within six feet of your head, assuming you haven't left that somewhere.\n")
        return True
    elif PRSO == ME:
        z.tell("You're around here somewhere...\n")
        return True
    elif l == GLOBAL_OBJECTS:
        z.tell('You find it.\n')
        return True
    elif z.in_p(PRSO, WINNER):
        z.tell('You have it.\n')
        return True
    elif z.in_p(PRSO, HERE) or global_in_p(PRSO, HERE) or (PRSO == PSEUDO_OBJECT):
        z.tell("It's right here.\n")
        return True
    elif z.fset_p(l, ACTORBIT):
        z.tell('The ', z.D(l), ' has it.\n')
        return True
    elif z.fset_p(l, SURFACEBIT):
        z.tell("It's on the ", z.D(l), '.\n')
        return True
    elif z.fset_p(l, CONTBIT):
        z.tell("It's in the ", z.D(l), '.\n')
        return True
    else:
        z.tell('Beats me.\n')
        return True
    return False


def v_follow():
    z.tell("You're nuts!\n")
    return True


def v_frobozz():
    z.tell('The FROBOZZ Corporation created, owns, and operates this dungeon.\n')
    return True


def pre_give():
    if not held_p(PRSO):
        z.tell("That's easy for you to say since you don't even have the ", z.D(PRSO), '.\n')
        return True
    return False


def v_give():
    if not z.fset_p(PRSI, ACTORBIT):
        z.tell("You can't give a ", z.D(PRSO), ' to a ', z.D(PRSI), '!\n')
        return True
    else:
        z.tell('The ', z.D(PRSI), ' refuses it politely.\n')
        return True
    return False


def v_hatch():
    z.tell('Bizarre!\n')
    return True


def v_hello():
    if PRSO:
        if z.fset_p(PRSO, ACTORBIT):
            z.tell('The ', z.D(PRSO), ' bows his head to you in greeting.\n')
            return True
        else:
            z.tell('It\'s a well known fact that only schizophrenics say "Hello" to a ', z.D(PRSO), '.\n')
            return True
    else:
        _t1 = z.S(pick_one(HELLOS))
        z.tell(_t1, '\n')
        return True
    return False


def v_incant():
    global P_CONT, QUOTE_FLAG
    z.tell('The incantation echoes back faintly, but nothing else happens.\n')
    QUOTE_FLAG = False
    P_CONT = False
    return True


def v_inflate():
    z.tell('How can you inflate that?\n')
    return True


def v_kick():
    return hack_hack('Kicking the ')


def v_kiss():
    z.tell("I'd sooner kiss a pig.\n")
    return True


def v_knock():
    if z.fset_p(PRSO, DOORBIT):
        z.tell("Nobody's home.\n")
        return True
    else:
        z.tell('Why knock on a ', z.D(PRSO), '?\n')
        return True
    return False


def v_lamp_off():
    global LIT
    if z.fset_p(PRSO, LIGHTBIT):
        if not z.fset_p(PRSO, ONBIT):
            z.tell('It is already off.\n')
        else:
            z.fclear(PRSO, ONBIT)
            if LIT:
                LIT = lit_p(HERE)
            z.tell('The ', z.D(PRSO), ' is now off.\n')
            if not LIT:
                z.tell('It is now pitch black.\n')
    else:
        z.tell("You can't turn that off.\n")
    return True


def v_lamp_on():
    global LIT
    if z.fset_p(PRSO, LIGHTBIT):
        if z.fset_p(PRSO, ONBIT):
            z.tell('It is already on.\n')
        else:
            z.fset(PRSO, ONBIT)
            z.tell('The ', z.D(PRSO), ' is now on.\n')
            if not LIT:
                LIT = lit_p(HERE)
                z.crlf()
                v_look()
    elif z.fset_p(PRSO, BURNBIT):
        z.tell('If you wish to burn the ', z.D(PRSO), ', you should say so.\n')
    else:
        z.tell("You can't turn that on.\n")
    return True


def v_launch():
    if z.fset_p(PRSO, VEHBIT):
        z.tell('You can\'t launch that by saying "launch"!\n')
        return True
    else:
        z.tell("That's pretty weird.\n")
        return True
    return False


def v_lean_on():
    z.tell('Getting tired?\n')
    return True


def v_leap():
    tx = 0
    s = 0
    if PRSO:
        if z.in_p(PRSO, HERE):
            if z.fset_p(PRSO, ACTORBIT):
                z.tell('The ', z.D(PRSO), ' is too big to jump over.\n')
                return True
            else:
                return v_skip()
        else:
            z.tell('That would be a good trick.\n')
            return True
    elif (tx := z.getpt(HERE, P_DOWN)):
        s = z.ptsize(tx)
        if (s == 2) or ((s == 4) and (not z.value(z.getb(tx, 1)))):
            z.tell('This was not a very safe place to try jumping.\n')
            return jigs_up(pick_one(JUMPLOSS))
        elif HERE == UP_A_TREE:
            z.tell('In a feat of unaccustomed daring, you manage to land on your feet without killing yourself.\n\n')
            do_walk(P_DOWN)
            return True
        else:
            return v_skip()
    else:
        return v_skip()
    return False


def v_leave():
    return do_walk(P_OUT)


def v_listen():
    z.tell('The ', z.D(PRSO), ' makes no sound.\n')
    return True


def v_lock():
    z.tell("It doesn't seem to work.\n")
    return True


def v_look():
    if describe_room(True):
        return describe_objects(True)
    return False


def v_look_behind():
    z.tell('There is nothing behind the ', z.D(PRSO), '.\n')
    return True


def v_look_inside():
    if z.fset_p(PRSO, DOORBIT):
        if z.fset_p(PRSO, OPENBIT):
            z.tell('The ', z.D(PRSO), " is open, but I can't tell what's beyond it.")
        else:
            z.tell('The ', z.D(PRSO), ' is closed.')
        return z.crlf()
    elif z.fset_p(PRSO, CONTBIT):
        if z.fset_p(PRSO, ACTORBIT):
            z.tell('There is nothing special to be seen.\n')
            return True
        elif see_inside_p(PRSO):
            if z.first_p(PRSO) and print_cont(PRSO):
                return True
            elif null_f():
                return True
            else:
                z.tell('The ', z.D(PRSO), ' is empty.\n')
                return True
        else:
            z.tell('The ', z.D(PRSO), ' is closed.\n')
            return True
    else:
        z.tell("You can't look inside a ", z.D(PRSO), '.\n')
        return True
    return False


def v_look_on():
    if z.fset_p(PRSO, SURFACEBIT):
        perform(V_LOOK_INSIDE, PRSO)
        return True
    else:
        z.tell('Look on a ', z.D(PRSO), '???\n')
        return True
    return False


def v_look_under():
    z.tell('There is nothing but dust there.\n')
    return True


def v_lower():
    return hack_hack('Playing in this way with the ')


def v_make():
    z.tell("You can't do that.\n")
    return True


def v_melt():
    z.tell("It's not clear that a ", z.D(PRSO), ' can be melted.\n')
    return True


def pre_move():
    if held_p(PRSO):
        z.tell("You aren't an accomplished enough juggler.\n")
        return True
    return False


def v_move():
    if z.fset_p(PRSO, TAKEBIT):
        z.tell('Moving the ', z.D(PRSO), ' reveals nothing.\n')
        return True
    else:
        z.tell("You can't move the ", z.D(PRSO), '.\n')
        return True
    return False


def v_mumble():
    z.tell("You'll have to speak up if you expect me to hear you!\n")
    return True


def pre_mung():
    if null_f():
        return True
    elif (not PRSI) or (not z.fset_p(PRSI, WEAPONBIT)):
        z.tell('Trying to destroy the ', z.D(PRSO), ' with ')
        if not PRSI:
            z.tell('your bare hands')
        else:
            z.tell('a ', z.D(PRSI))
        z.tell(' is futile.\n')
        return True
    return False


def v_mung():
    if z.fset_p(PRSO, ACTORBIT):
        perform(V_ATTACK, PRSO)
        return True
    else:
        z.tell('Nice try.\n')
        return True
    return False


def v_odysseus():
    global CYCLOPS_FLAG, MAGIC_FLAG
    if (HERE == CYCLOPS_ROOM) and z.in_p(CYCLOPS, HERE) and (not CYCLOPS_FLAG):
        z.put(int_(z.rtn(i_cyclops)), C_ENABLED_P, 0)
        CYCLOPS_FLAG = True
        z.tell("The cyclops, hearing the name of his father's deadly nemesis, flees the room by knocking down the wall on the east of the room.\n")
        MAGIC_FLAG = True
        z.fclear(CYCLOPS, FIGHTBIT)
        return remove_carefully(CYCLOPS)
    else:
        z.tell("Wasn't he a sailor?\n")
        return True
    return False


def v_oil():
    z.tell('You probably put spinach in your gas tank, too.\n')
    return True


def v_open():
    f = 0
    str_ = 0
    if z.fset_p(PRSO, CONTBIT) and (z.getp(PRSO, P_CAPACITY) != 0):
        if z.fset_p(PRSO, OPENBIT):
            z.tell('It is already open.\n')
            return True
        else:
            z.fset(PRSO, OPENBIT)
            z.fset(PRSO, TOUCHBIT)
            if (not z.first_p(PRSO)) or z.fset_p(PRSO, TRANSBIT):
                z.tell('Opened.\n')
                return True
            elif (f := z.first_p(PRSO)) and (not z.next_p(f)) and (not z.fset_p(f, TOUCHBIT)) and (str_ := z.getp(f, P_FDESC)):
                z.tell('The ', z.D(PRSO), ' opens.\n')
                z.tell(z.S(str_), '\n')
                return True
            else:
                z.tell('Opening the ', z.D(PRSO), ' reveals ')
                print_contents(PRSO)
                z.tell('.\n')
                return True
    elif z.fset_p(PRSO, DOORBIT):
        if z.fset_p(PRSO, OPENBIT):
            z.tell('It is already open.\n')
            return True
        else:
            z.tell('The ', z.D(PRSO), ' opens.\n')
            return z.fset(PRSO, OPENBIT)
    else:
        z.tell('You must tell me how to do that to a ', z.D(PRSO), '.\n')
        return True
    return False


def v_overboard():
    locn = 0
    if PRSI == TEETH:
        if z.fset_p((locn := z.loc(WINNER)), VEHBIT):
            z.move(PRSO, z.loc(locn))
            z.tell('Ahoy -- ', z.D(PRSO), ' overboard!\n')
            return True
        else:
            z.tell("You're not in anything!\n")
            return True
    elif z.fset_p(z.loc(WINNER), VEHBIT):
        perform(V_THROW, PRSO)
        return True
    else:
        z.tell('Huh?\n')
        return True
    return False


def v_pick():
    z.tell("You can't pick that.\n")
    return True


def v_play():
    if z.fset_p(PRSO, ACTORBIT):
        z.tell('You become so engrossed in the role of the ', z.D(PRSO), ' that you kill yourself, just as he might have done!\n')
        return jigs_up('')
    else:
        z.tell("That's silly!\n")
        return True
    return False


def v_plug():
    z.tell('This has no effect.\n')
    return True


def v_pour_on():
    if PRSO == WATER:
        remove_carefully(PRSO)
        if z.fset_p(PRSI, FLAMEBIT) and z.fset_p(PRSI, ONBIT):
            z.tell('The ', z.D(PRSI), ' is extinguished.\n')
            null_f()
            z.fclear(PRSI, ONBIT)
            return z.fclear(PRSI, FLAMEBIT)
        else:
            z.tell('The water spills over the ', z.D(PRSI), ', to the floor, and evaporates.\n')
            return True
    elif PRSO == PUTTY:
        return perform(V_PUT, PUTTY, PRSI)
    else:
        z.tell("You can't pour that.\n")
        return True
    return False


def v_pray():
    if HERE == SOUTH_TEMPLE:
        return goto(FOREST_1)
    else:
        z.tell('If you pray enough, your prayers may be answered.\n')
        return True
    return False


def v_pump():
    if PRSI and (PRSI != PUMP):
        z.tell('Pump it up with a ', z.D(PRSI), '?\n')
        return True
    elif z.in_p(PUMP, WINNER):
        return perform(V_INFLATE, PRSO, PUMP)
    else:
        z.tell("It's really not clear how.\n")
        return True
    return False


def v_push():
    return hack_hack('Pushing the ')


def v_push_to():
    z.tell("You can't push things to that.\n")
    return True


def pre_put():
    if null_f():
        return False
    else:
        return pre_give()
    return False


def v_put():
    if z.fset_p(PRSI, OPENBIT) or (z.fset_p(PRSI, DOORBIT) or z.fset_p(PRSI, CONTBIT)) or z.fset_p(PRSI, VEHBIT):
        pass
    else:
        z.tell("You can't do that.\n")
        return True
    if not z.fset_p(PRSI, OPENBIT):
        z.tell('The ', z.D(PRSI), " isn't open.\n")
        return this_is_it(PRSI)
    elif PRSI == PRSO:
        z.tell('How can you do that?\n')
        return True
    elif z.in_p(PRSO, PRSI):
        z.tell('The ', z.D(PRSO), ' is already in the ', z.D(PRSI), '.\n')
        return True
    elif ((weight(PRSI) + weight(PRSO)) - z.getp(PRSI, P_SIZE)) > z.getp(PRSI, P_CAPACITY):
        z.tell("There's no room.\n")
        return True
    elif (not held_p(PRSO)) and z.fset_p(PRSO, TRYTAKEBIT):
        z.tell("You don't have the ", z.D(PRSO), '.\n')
        return True
    elif (not held_p(PRSO)) and (not itake()):
        return True
    else:
        z.move(PRSO, PRSI)
        z.fset(PRSO, TOUCHBIT)
        score_obj(PRSO)
        z.tell('Done.\n')
        return True
    return False


def v_put_behind():
    z.tell('That hiding place is too obvious.\n')
    return True


def v_put_on():
    if PRSI == GROUND:
        perform(V_DROP, PRSO)
        return True
    elif z.fset_p(PRSI, SURFACEBIT):
        return v_put()
    else:
        z.tell("There's no good surface on the ", z.D(PRSI), '.\n')
        return True
    return False


def v_put_under():
    z.tell("You can't do that.\n")
    return True


def v_raise():
    return v_lower()


def v_rape():
    z.tell('What a (ahem!) strange idea.\n')
    return True


def pre_read():
    if not LIT:
        z.tell('It is impossible to read in the dark.\n')
        return True
    elif PRSI and (not z.fset_p(PRSI, TRANSBIT)):
        z.tell('How does one look through a ', z.D(PRSI), '?\n')
        return True
    return False


def v_read():
    if not z.fset_p(PRSO, READBIT):
        z.tell('How does one read a ', z.D(PRSO), '?\n')
        return True
    else:
        z.tell(z.S(z.getp(PRSO, P_TEXT)), '\n')
        return True
    return False


def v_read_page():
    perform(V_READ, PRSO)
    return True


def v_repent():
    z.tell('It could very well be too late!\n')
    return True


def v_reply():
    global P_CONT, QUOTE_FLAG
    z.tell('It is hardly likely that the ', z.D(PRSO), ' is interested.\n')
    P_CONT = False
    QUOTE_FLAG = False
    return True


def v_ring():
    z.tell('How, exactly, can you ring that?\n')
    return True


def v_rub():
    return hack_hack('Fiddling with the ')


def v_say():
    global P_CONT, QUOTE_FLAG
    v = 0
    if not P_CONT:
        z.tell('Say what?\n')
        return True
    QUOTE_FLAG = False
    if (v := find_in(HERE, ACTORBIT)):
        z.tell('You must address the ', z.D(v), ' directly.\n')
        P_CONT = False
    elif z.get(P_LEXV, P_CONT) != W_HELLO:
        P_CONT = False
        z.tell('Talking to yourself is a sign of impending mental collapse.\n')
    return True


def v_search():
    z.tell('You find nothing unusual.\n')
    return True


def v_send():
    if z.fset_p(PRSO, ACTORBIT):
        z.tell('Why would you send for the ', z.D(PRSO), '?\n')
        return True
    else:
        z.tell("That doesn't make sends.\n")
        return True
    return False


def pre_sgive():
    perform(V_GIVE, PRSI, PRSO)
    return True


def v_sgive():
    z.tell('Foo!\n')
    return True


def v_shake():
    if z.fset_p(PRSO, ACTORBIT):
        z.tell('This seems to have no effect.\n')
        return True
    elif not z.fset_p(PRSO, TAKEBIT):
        z.tell("You can't take it; thus, you can't shake it!\n")
        return True
    elif z.fset_p(PRSO, CONTBIT):
        if z.fset_p(PRSO, OPENBIT):
            if z.first_p(PRSO):
                shake_loop()
                z.tell('The contents of the ', z.D(PRSO), ' spill ')
                if not z.fset_p(HERE, RLANDBIT):
                    z.tell('out and disappears')
                else:
                    z.tell('to the ground')
                z.tell('.\n')
                return True
            else:
                z.tell('Shaken.\n')
                return True
        else:
            if z.first_p(PRSO):
                z.tell('It sounds like there is something inside the ', z.D(PRSO), '.\n')
                return True
            else:
                z.tell('The ', z.D(PRSO), ' sounds empty.\n')
                return True
    else:
        z.tell('Shaken.\n')
        return True
    return False


def shake_loop():
    x = 0
    while True:
        if (x := z.first_p(PRSO)):
            z.fset(x, TOUCHBIT)
            if HERE == UP_A_TREE:
                _t1 = PATH
            elif not z.fset_p(HERE, RLANDBIT):
                _t1 = PSEUDO_OBJECT
            else:
                _t1 = HERE
            z.move(x, _t1)
        else:
            return True
    return False


def v_skip():
    _t1 = z.S(pick_one(WHEEEEE))
    z.tell(_t1, '\n')
    return True


def v_smell():
    z.tell('It smells like a ', z.D(PRSO), '.\n')
    return True


def v_spin():
    z.tell("You can't spin that!\n")
    return True


def v_spray():
    return v_squeeze()


def v_squeeze():
    if z.fset_p(PRSO, ACTORBIT):
        z.tell('The ', z.D(PRSO), ' does not understand this.')
    else:
        z.tell('How singularly useless.')
    return z.crlf()


def v_sspray():
    return perform(V_SPRAY, PRSI, PRSO)


def v_stab():
    w = 0
    if (w := find_weapon(WINNER)):
        perform(V_ATTACK, PRSO, w)
        return True
    else:
        z.tell('No doubt you propose to stab the ', z.D(PRSO), ' with your pinky?\n')
        return True
    return False


def v_stand():
    if z.fset_p(z.loc(WINNER), VEHBIT):
        perform(V_DISEMBARK, z.loc(WINNER))
        return True
    else:
        z.tell('You are already standing, I think.\n')
        return True
    return False


def v_stay():
    z.tell('You will be lost without me!\n')
    return True


def v_strike():
    if z.fset_p(PRSO, ACTORBIT):
        z.tell("Since you aren't versed in hand-to-hand combat, you'd better attack the ", z.D(PRSO), ' with a weapon.\n')
        return True
    else:
        perform(V_LAMP_ON, PRSO)
        return True
    return False


def v_swim():
    if global_in_p(GLOBAL_WATER, HERE):
        z.tell("Swimming isn't usually allowed in the ")
        if not (PRSO in (WATER, GLOBAL_WATER)):
            z.tell(z.D(PRSO), '.')
        else:
            z.tell('dungeon.')
        return z.crlf()
    elif null_f():
        return False
    else:
        z.tell('Go jump in a lake!\n')
        return True
    return False


def v_swing():
    if not PRSI:
        z.tell('Whoosh!\n')
        return True
    else:
        return perform(V_ATTACK, PRSI, PRSO)
    return False


def pre_take():
    global PRSI
    if z.in_p(PRSO, WINNER):
        if z.fset_p(PRSO, WEARBIT):
            z.tell('You are already wearing it.\n')
            return True
        else:
            z.tell('You already have that!\n')
            return True
    elif z.fset_p(z.loc(PRSO), CONTBIT) and (not z.fset_p(z.loc(PRSO), OPENBIT)):
        z.tell("You can't reach something that's inside a closed container.\n")
        return True
    elif PRSI:
        if PRSI == GROUND:
            PRSI = False
            return False
        null_f()
        if PRSI != z.loc(PRSO):
            z.tell('The ', z.D(PRSO), " isn't in the ", z.D(PRSI), '.\n')
            return True
        else:
            PRSI = False
            return False
    elif PRSO == z.loc(WINNER):
        z.tell("You're inside of it!\n")
        return True
    return False


def v_take():
    if itake() == True:
        if z.fset_p(PRSO, WEARBIT):
            z.tell('You are now wearing the ', z.D(PRSO), '.\n')
            return True
        else:
            z.tell('Taken.\n')
            return True
    return False


def v_tell():
    global HERE, P_CONT, QUOTE_FLAG, WINNER
    if z.fset_p(PRSO, ACTORBIT):
        if P_CONT:
            WINNER = PRSO
            HERE = z.loc(WINNER)
            return HERE
        else:
            z.tell('The ', z.D(PRSO), ' pauses for a moment, perhaps thinking that you should reread the manual.\n')
            return True
    else:
        z.tell("You can't talk to the ", z.D(PRSO), '!\n')
        QUOTE_FLAG = False
        P_CONT = False
        return 2
    return False


def v_through(obj=False):
    m = 0
    if z.fset_p(PRSO, DOORBIT) and (m := other_side(PRSO)):
        do_walk(m)
        return True
    elif (not obj) and z.fset_p(PRSO, VEHBIT):
        perform(V_BOARD, PRSO)
        return True
    elif obj or (not z.fset_p(PRSO, TAKEBIT)):
        null_f()
        z.tell('You hit your head against the ', z.D(PRSO), ' as you attempt this feat.\n')
        return True
    elif z.in_p(PRSO, WINNER):
        z.tell('That would involve quite a contortion!\n')
        return True
    else:
        _t1 = z.S(pick_one(YUKS))
        z.tell(_t1, '\n')
        return True
    return False


def v_throw():
    global WINNER
    if idrop():
        if PRSI == ME:
            z.tell('A terrific throw! The ', z.D(PRSO))
            WINNER = PLAYER
            return jigs_up(" hits you squarely in the head. Normally, this wouldn't do much damage, but by incredible mischance, you fall over backwards trying to duck, and break your neck, justice being swift and merciful in the Great Underground Empire.")
        elif PRSI and z.fset_p(PRSI, ACTORBIT):
            z.tell('The ', z.D(PRSI), ' ducks as the ', z.D(PRSO), ' flies by and crashes to the ground.\n')
            return True
        else:
            z.tell('Thrown.\n')
            return True
    else:
        z.tell('Huh?\n')
        return True
    return False


def v_throw_off():
    z.tell("You can't throw anything off of that!\n")
    return True


def v_tie():
    if PRSI == WINNER:
        z.tell("You can't tie anything to yourself.\n")
        return True
    else:
        z.tell("You can't tie the ", z.D(PRSO), ' to that.\n')
        return True
    return False


def v_tie_up():
    z.tell('You could certainly never tie it with that!\n')
    return True


def v_treasure():
    if HERE == NORTH_TEMPLE:
        return goto(TREASURE_ROOM)
    elif HERE == TREASURE_ROOM:
        return goto(NORTH_TEMPLE)
    else:
        z.tell('Nothing happens.\n')
        return True
    return False


def pre_turn():
    if (PRSI in (False, ROOMS)) and (PRSO != BOOK):
        z.tell("Your bare hands don't appear to be enough.\n")
        return True
    elif not z.fset_p(PRSO, TURNBIT):
        z.tell("You can't turn that!\n")
        return True
    return False


def v_turn():
    z.tell('This has no effect.\n')
    return True


def v_unlock():
    return v_lock()


def v_untie():
    z.tell('This cannot be tied, so it cannot be untied!\n')
    return True


def v_wait(num=3):
    global CLOCK_WAIT
    z.tell('Time passes...\n')
    while True:
        if (num := (num - 1)) < 0:
            break
        elif clocker():
            break
    CLOCK_WAIT = True
    return CLOCK_WAIT


def v_walk():
    pt = 0
    pts = 0
    str_ = 0
    obj = 0
    rm = 0
    if not P_WALK_DIR:
        perform(V_WALK_TO, PRSO)
        return True
    elif (pt := z.getpt(HERE, PRSO)):
        if (pts := z.ptsize(pt)) == UEXIT:
            return goto(z.getb(pt, REXIT))
        elif pts == NEXIT:
            z.tell(z.S(z.get(pt, NEXITSTR)), '\n')
            return 2
        elif pts == FEXIT:
            if (rm := z.apply(z.get(pt, FEXITFCN))):
                return goto(rm)
            elif null_f():
                return False
            else:
                return 2
        elif pts == CEXIT:
            if z.value(z.getb(pt, CEXITFLAG)):
                return goto(z.getb(pt, REXIT))
            elif (str_ := z.get(pt, CEXITSTR)):
                z.tell(z.S(str_), '\n')
                return 2
            else:
                z.tell("You can't go that way.\n")
                return 2
        elif pts == DEXIT:
            if z.fset_p((obj := z.getb(pt, DEXITOBJ)), OPENBIT):
                return goto(z.getb(pt, REXIT))
            elif (str_ := z.get(pt, DEXITSTR)):
                z.tell(z.S(str_), '\n')
                return 2
            else:
                z.tell('The ', z.D(obj), ' is closed.\n')
                this_is_it(obj)
                return 2
    elif (not LIT) and (80 > z.random(100)) and (WINNER == ADVENTURER) and (not z.fset_p(HERE, NONLANDBIT)):
        if SPRAYED_P:
            z.tell('There are odd noises in the darkness, and there is no exit in that direction.\n')
            return 2
        elif null_f():
            return False
        else:
            return jigs_up('Oh, no! You have walked into the slavering fangs of a lurking grue!')
    else:
        z.tell("You can't go that way.\n")
        return 2
    return False


def v_walk_around():
    z.tell('Use compass directions for movement.\n')
    return True


def v_walk_to():
    if PRSO and (z.in_p(PRSO, HERE) or global_in_p(PRSO, HERE)):
        z.tell("It's here!\n")
        return True
    else:
        z.tell('You should supply a direction!\n')
        return True
    return False


def v_wave():
    return hack_hack('Waving the ')


def v_wear():
    if not z.fset_p(PRSO, WEARBIT):
        z.tell("You can't wear the ", z.D(PRSO), '.\n')
        return True
    else:
        perform(V_TAKE, PRSO)
        return True
    return False


def v_win():
    z.tell('Naturally!\n')
    return True


def v_wind():
    z.tell('You cannot wind up a ', z.D(PRSO), '.\n')
    return True


def v_wish():
    z.tell('With luck, your wish will come true.\n')
    return True


def v_yell():
    z.tell('Aaaarrrrgggghhhh!\n')
    return True


def v_zork():
    z.tell('At your service!\n')
    return True


def v_first_look():
    if describe_room():
        if not SUPER_BRIEF:
            return describe_objects()
    return False


def describe_room(look_p=False):
    v_p = 0
    str_ = 0
    av = 0
    v_p = look_p or VERBOSE
    if not LIT:
        z.tell('It is pitch black.')
        if not SPRAYED_P:
            z.tell(' You are likely to be eaten by a grue.')
        z.crlf()
        null_f()
        return False
    if not z.fset_p(HERE, TOUCHBIT):
        z.fset(HERE, TOUCHBIT)
        v_p = True
    if z.fset_p(HERE, MAZEBIT):
        z.fclear(HERE, TOUCHBIT)
    if z.in_p(HERE, ROOMS):
        z.tell(z.D(HERE))
        if z.fset_p((av := z.loc(WINNER)), VEHBIT):
            z.tell(', in the ', z.D(av))
        z.crlf()
    if look_p or (not SUPER_BRIEF):
        av = z.loc(WINNER)
        if v_p and z.apply(z.getp(HERE, P_ACTION), M_LOOK):
            return True
        elif v_p and (str_ := z.getp(HERE, P_LDESC)):
            z.tell(z.S(str_), '\n')
        else:
            z.apply(z.getp(HERE, P_ACTION), M_FLASH)
        if (HERE != av) and z.fset_p(av, VEHBIT):
            z.apply(z.getp(av, P_ACTION), M_LOOK)
    return True


def describe_objects(v_p=False):
    if LIT:
        if z.first_p(HERE):
            return print_cont(HERE, (v_p := (v_p or VERBOSE)), -1)
    else:
        z.tell("Only bats can see in the dark. And you're not one.\n")
        return True
    return False


def describe_object(obj=0, v_p=0, level=0):
    global DESC_OBJECT
    str_ = False
    av = 0
    DESC_OBJECT = obj
    if (level == 0) and z.apply(z.getp(obj, P_DESCFCN), M_OBJDESC):
        return True
    elif (level == 0) and (((not z.fset_p(obj, TOUCHBIT)) and (str_ := z.getp(obj, P_FDESC))) or (str_ := z.getp(obj, P_LDESC))):
        z.tell(z.S(str_))
    elif level == 0:
        z.tell('There is a ', z.D(obj), ' here')
        if z.fset_p(obj, ONBIT):
            z.tell(' (providing light)')
        z.tell('.')
    else:
        z.tell(z.S(z.get(INDENTS, level)))
        z.tell('A ', z.D(obj))
        if z.fset_p(obj, ONBIT):
            z.tell(' (providing light)')
        elif z.fset_p(obj, WEARBIT) and z.in_p(obj, WINNER):
            z.tell(' (being worn)')
    null_f()
    if (level == 0) and (av := z.loc(WINNER)) and z.fset_p(av, VEHBIT):
        z.tell(' (outside the ', z.D(av), ')')
    z.crlf()
    if see_inside_p(obj) and z.first_p(obj):
        return print_cont(obj, v_p, level)
    return False


def print_contents(obj=0):
    f = 0
    n = 0
    n1st_p = True
    it_p = False
    two_p = False
    if (f := z.first_p(obj)):
        while True:
            n = z.next_p(f)
            if n1st_p:
                n1st_p = False
            else:
                z.tell(', ')
                if not n:
                    z.tell('and ')
            z.tell('a ', z.D(f))
            if (not it_p) and (not two_p):
                it_p = f
            else:
                two_p = True
                it_p = False
            f = n
            if not f:
                if it_p and (not two_p):
                    this_is_it(it_p)
                return True
    return False


def print_cont(obj=0, v_p=False, level=0):
    y = 0
    n1st_p = 0
    shit = 0
    av = 0
    str_ = 0
    pv_p = False
    inv_p = False
    if not (y := z.first_p(obj)):
        return True
    if (av := z.loc(WINNER)) and z.fset_p(av, VEHBIT):
        pass
    else:
        av = False
    n1st_p = True
    shit = True
    if WINNER in (obj, z.loc(obj)):
        inv_p = True
    else:
        while True:
            if not y:
                break
            elif y == av:
                pv_p = True
            elif y == WINNER:
                pass
            elif (not z.fset_p(y, INVISIBLE)) and (not z.fset_p(y, TOUCHBIT)) and (str_ := z.getp(y, P_FDESC)):
                if not z.fset_p(y, NDESCBIT):
                    z.tell(z.S(str_), '\n')
                    shit = False
                if see_inside_p(y) and (not z.getp(z.loc(y), P_DESCFCN)) and z.first_p(y):
                    if print_cont(y, v_p, 0):
                        n1st_p = False
            y = z.next_p(y)
    y = z.first_p(obj)
    while True:
        if not y:
            if pv_p and av and z.first_p(av):
                level = level + 1
                print_cont(av, v_p, level)
            break
        elif y in (av, ADVENTURER):
            pass
        elif (not z.fset_p(y, INVISIBLE)) and (inv_p or z.fset_p(y, TOUCHBIT) or (not z.getp(y, P_FDESC))):
            if not z.fset_p(y, NDESCBIT):
                if n1st_p:
                    if firster(obj, level):
                        if level < 0:
                            level = 0
                    level = 1 + level
                    n1st_p = False
                if level < 0:
                    level = 0
                describe_object(y, v_p, level)
            elif z.first_p(y) and see_inside_p(y):
                level = level + 1
                print_cont(y, v_p, level)
                level = level - 1
        y = z.next_p(y)
    if n1st_p and shit:
        return False
    else:
        return True
    return False


def firster(obj=0, level=0):
    if obj == TROPHY_CASE:
        z.tell('Your collection of treasures consists of:\n')
        return True
    elif obj == WINNER:
        z.tell('You are carrying:\n')
        return True
    elif not z.in_p(obj, ROOMS):
        if level > 0:
            z.tell(z.S(z.get(INDENTS, level)))
        if z.fset_p(obj, SURFACEBIT):
            z.tell('Sitting on the ', z.D(obj), ' is: \n')
            return True
        elif z.fset_p(obj, ACTORBIT):
            z.tell('The ', z.D(obj), ' is holding: \n')
            return True
        else:
            z.tell('The ', z.D(obj), ' contains:\n')
            return True
    return False


def see_inside_p(obj=0):
    return (not z.fset_p(obj, INVISIBLE)) and (z.fset_p(obj, TRANSBIT) or z.fset_p(obj, OPENBIT))


def score_upd(num=0):
    global BASE_SCORE, SCORE, WON_FLAG
    BASE_SCORE = BASE_SCORE + num
    SCORE = SCORE + num
    if (SCORE == 350) and (not WON_FLAG):
        WON_FLAG = True
        z.fclear(MAP, INVISIBLE)
        z.fclear(WEST_OF_HOUSE, TOUCHBIT)
        z.tell('An almost inaudible voice whispers in your ear, "Look to your treasures for the final secret."\n')
    return True


def score_obj(obj=0):
    temp = 0
    if (temp := z.getp(obj, P_VALUE)) > 0:
        score_upd(temp)
        return z.putp(obj, P_VALUE, 0)
    return False


def yes_p():
    z.print_('>')
    z.read(P_INBUF, P_LEXV)
    if z.get(P_LEXV, 1) in (W_YES, W_Y):
        return True
    else:
        return False
    return False


def itake(vb=True):
    cnt = 0
    obj = 0
    if DEAD:
        if vb:
            z.tell('Your hand passes through its object.\n')
        return False
    elif not z.fset_p(PRSO, TAKEBIT):
        if vb:
            _t1 = z.S(pick_one(YUKS))
            z.tell(_t1, '\n')
        return False
    elif null_f():
        return False
    elif z.fset_p(z.loc(PRSO), CONTBIT) and (not z.fset_p(z.loc(PRSO), OPENBIT)):
        return False
    elif (not z.in_p(z.loc(PRSO), WINNER)) and ((weight(PRSO) + weight(WINNER)) > LOAD_ALLOWED):
        if vb:
            z.tell('Your load is too heavy')
            if LOAD_ALLOWED < LOAD_MAX:
                z.tell(', especially in light of your condition.')
            else:
                z.tell('.')
            z.crlf()
        return 2
    elif (PRSA == V_TAKE) and ((cnt := ccount(WINNER)) > FUMBLE_NUMBER) and ((cnt * FUMBLE_PROB) > z.random(100)):
        z.tell("You're holding too many things already!\n")
        return False
    else:
        z.move(PRSO, WINNER)
        z.fclear(PRSO, NDESCBIT)
        z.fset(PRSO, TOUCHBIT)
        null_f()
        score_obj(PRSO)
        return True
    return False


def idrop():
    if (not z.in_p(PRSO, WINNER)) and (not z.in_p(z.loc(PRSO), WINNER)):
        z.tell("You're not carrying the ", z.D(PRSO), '.\n')
        return False
    elif (not z.in_p(PRSO, WINNER)) and (not z.fset_p(z.loc(PRSO), OPENBIT)):
        z.tell('The ', z.D(PRSO), ' is closed.\n')
        return False
    else:
        z.move(PRSO, z.loc(WINNER))
        return True
    return False


def ccount(obj=0):
    cnt = 0
    x = 0
    if (x := z.first_p(obj)):
        while True:
            if not z.fset_p(x, WEARBIT):
                cnt = cnt + 1
            if not (x := z.next_p(x)):
                break
    return cnt


def weight(obj=0):
    cont = 0
    wt = 0
    if (cont := z.first_p(obj)):
        while True:
            if (obj == PLAYER) and z.fset_p(cont, WEARBIT):
                wt = wt + 1
            else:
                wt = wt + weight(cont)
            if not (cont := z.next_p(cont)):
                break
    return wt + z.getp(obj, P_SIZE)


def hack_hack(str_=0):
    if z.in_p(PRSO, GLOBAL_OBJECTS) and (PRSA in (V_WAVE, V_RAISE, V_LOWER)):
        z.tell('The ', z.D(PRSO), " isn't here!\n")
        return True
    else:
        z.tell(z.S(str_), z.D(PRSO))
        _t1 = z.S(pick_one(HO_HUM))
        z.tell(_t1, '\n')
        return True
    return False


def no_go_tell(av=0, wloc=0):
    if av:
        z.tell("You can't go there in a ", z.D(wloc), '.')
    else:
        z.tell("You can't go there without a vehicle.")
    return z.crlf()


def goto(rm=0, v_p=True):
    global HERE, LIT, P_CONT
    lb = z.fset_p(rm, RLANDBIT)
    wloc = z.loc(WINNER)
    av = False
    olit = 0
    ohere = 0
    olit = LIT
    ohere = HERE
    if z.fset_p(wloc, VEHBIT):
        av = z.getp(wloc, P_VTYPE)
    if (not lb) and (not av):
        no_go_tell(av, wloc)
        return False
    elif (not lb) and (not z.fset_p(rm, av)):
        no_go_tell(av, wloc)
        return False
    elif z.fset_p(HERE, RLANDBIT) and lb and av and (av != RLANDBIT) and (not z.fset_p(rm, av)):
        no_go_tell(av, wloc)
        return False
    elif z.fset_p(rm, RMUNGBIT):
        z.tell(z.S(z.getp(rm, P_LDESC)), '\n')
        return False
    else:
        if lb and (not z.fset_p(HERE, RLANDBIT)) and (not DEAD) and z.fset_p(wloc, VEHBIT):
            z.tell('The ', z.D(wloc), ' comes to a rest on the shore.\n\n')
        if av:
            z.move(wloc, rm)
        else:
            z.move(WINNER, rm)
        HERE = rm
        LIT = lit_p(HERE)
        if (not olit) and (not LIT) and (80 > z.random(100)):
            if SPRAYED_P:
                z.tell('There are sinister gurgling noises in the darkness all around you!\n')
            elif null_f():
                return False
            else:
                z.tell('Oh, no! A lurking grue slithered into the ')
                if z.fset_p(z.loc(WINNER), VEHBIT):
                    z.tell(z.D(z.loc(WINNER)))
                else:
                    z.tell('room')
                jigs_up(' and devoured you!')
                return True
        if (not LIT) and (WINNER == ADVENTURER):
            z.tell('You have moved into a dark place.\n')
            P_CONT = False
        z.apply(z.getp(HERE, P_ACTION), M_ENTER)
        score_obj(rm)
        if HERE != rm:
            return True
        elif (ADVENTURER != WINNER) and z.in_p(ADVENTURER, ohere):
            z.tell('The ', z.D(WINNER), ' leaves the room.\n')
        elif (HERE == ohere) and (HERE == ENTRANCE_TO_HADES):
            return True
        elif v_p and (WINNER == ADVENTURER):
            v_first_look()
        return True
    return False


def lkp(itm=0, tbl=0):
    cnt = 0
    len_ = z.get(tbl, 0)
    while True:
        if (cnt := (cnt + 1)) > len_:
            return False
        elif z.get(tbl, cnt) == itm:
            if cnt == len_:
                return False
            else:
                return z.get(tbl, (cnt + 1))
    return False


def do_walk(dir=0):
    global P_WALK_DIR
    P_WALK_DIR = dir
    return perform(V_WALK, dir)


def global_in_p(obj1=0, obj2=0):
    tx = 0
    if (tx := z.getpt(obj2, P_GLOBAL)):
        return zmemqb(obj1, tx, (z.ptsize(tx) - 1))
    return False


def find_in(where=0, what=0):
    w = 0
    w = z.first_p(where)
    if not w:
        return False
    while True:
        if z.fset_p(w, what) and (w != ADVENTURER):
            return w
        elif not (w := z.next_p(w)):
            return False
    return False


def held_p(can=0):
    while True:
        can = z.loc(can)
        if not can:
            return False
        elif can == WINNER:
            return True
    return False


def other_side(dobj=0):
    p = 0
    tx = 0
    while True:
        if (p := z.nextp(HERE, p)) < LOW_DIRECTION:
            return False
        else:
            tx = z.getpt(HERE, p)
            if (z.ptsize(tx) == DEXIT) and (z.getb(tx, DEXITOBJ) == dobj):
                return p
    return False


def mung_room(rm=0, str_=0):
    z.fset(rm, RMUNGBIT)
    return z.putp(rm, P_LDESC, str_)


def this_is_it(obj=0):
    global P_IT_OBJECT
    P_IT_OBJECT = obj
    return P_IT_OBJECT


def west_house(rarg=0):
    if rarg == M_LOOK:
        z.tell('You are standing in an open field west of a white house, with a boarded front door.')
        if WON_FLAG:
            z.tell(' A secret path leads southwest into the forest.')
        return z.crlf()
    return False


def east_house(rarg=0):
    if rarg == M_LOOK:
        z.tell('You are behind the white house. A path leads into the forest to the east. In one corner of the house there is a small window which is ')
        if z.fset_p(KITCHEN_WINDOW, OPENBIT):
            z.tell('open.')
        else:
            z.tell('slightly ajar.')
        return z.crlf()
    return False


def open_close(obj=0, stropn=0, strcls=0):
    if PRSA == V_OPEN:
        if z.fset_p(obj, OPENBIT):
            _t1 = z.S(pick_one(DUMMY))
            z.tell(_t1)
        else:
            z.tell(z.S(stropn))
            z.fset(obj, OPENBIT)
        return z.crlf()
    elif PRSA == V_CLOSE:
        if z.fset_p(obj, OPENBIT):
            z.tell(z.S(strcls))
            z.fclear(obj, OPENBIT)
        else:
            _t2 = z.S(pick_one(DUMMY))
            z.tell(_t2)
        return z.crlf()
    return False


def board_f():
    if PRSA in (V_TAKE, V_EXAMINE):
        z.tell('The boards are securely fastened.\n')
        return True
    return False


def teeth_f():
    if (PRSA == V_BRUSH) and (PRSO == TEETH):
        if (PRSI == PUTTY) and z.in_p(PRSI, WINNER):
            return jigs_up('Well, you seem to have been brushing your teeth with some sort of glue. As a result, your mouth gets glued together (with your nose) and you die of respiratory failure.')
        elif not PRSI:
            z.tell("Dental hygiene is highly recommended, but I'm not sure what you want to brush them with.\n")
            return True
        else:
            z.tell('A nice idea, but with a ', z.D(PRSI), '?\n')
            return True
    return False


def granite_wall_f():
    if HERE == NORTH_TEMPLE:
        if PRSA == V_FIND:
            z.tell('The west wall is solid granite here.\n')
            return True
        elif PRSA in (V_TAKE, V_RAISE, V_LOWER):
            z.tell("It's solid granite.\n")
            return True
    elif HERE == TREASURE_ROOM:
        if PRSA == V_FIND:
            z.tell('The east wall is solid granite here.\n')
            return True
        elif PRSA in (V_TAKE, V_RAISE, V_LOWER):
            z.tell("It's solid granite.\n")
            return True
    elif HERE == SLIDE_ROOM:
        if PRSA in (V_FIND, V_READ):
            z.tell('It only SAYS "Granite Wall".\n')
            return True
        else:
            z.tell("The wall isn't granite.\n")
            return True
    else:
        z.tell('There is no granite wall here.\n')
        return True
    return False


def songbird_f():
    if PRSA in (V_FIND, V_TAKE):
        z.tell('The songbird is not here but is probably nearby.\n')
        return True
    elif PRSA == V_LISTEN:
        z.tell("You can't hear the songbird now.\n")
        return True
    elif PRSA == V_FOLLOW:
        z.tell("It can't be followed.\n")
        return True
    else:
        z.tell("You can't see any songbird here.\n")
        return True
    return False


def white_house_f():
    if HERE in (KITCHEN, LIVING_ROOM, ATTIC):
        if PRSA == V_FIND:
            z.tell('Why not find your brains?\n')
            return True
        elif PRSA == V_WALK_AROUND:
            go_next(IN_HOUSE_AROUND)
            return True
    elif not ((HERE in (EAST_OF_HOUSE, WEST_OF_HOUSE)) or (HERE in (NORTH_OF_HOUSE, SOUTH_OF_HOUSE))):
        if PRSA == V_FIND:
            if HERE == CLEARING:
                z.tell('It seems to be to the west.\n')
                return True
            else:
                z.tell('It was here just a minute ago....\n')
                return True
        else:
            z.tell("You're not at the house.\n")
            return True
    elif PRSA == V_FIND:
        z.tell("It's right here! Are you blind or something?\n")
        return True
    elif PRSA == V_WALK_AROUND:
        go_next(HOUSE_AROUND)
        return True
    elif PRSA == V_EXAMINE:
        z.tell('The house is a beautiful colonial house which is painted white. It is clear that the owners must have been extremely wealthy.\n')
        return True
    elif PRSA in (V_THROUGH, V_OPEN):
        if HERE == EAST_OF_HOUSE:
            if z.fset_p(KITCHEN_WINDOW, OPENBIT):
                return goto(KITCHEN)
            else:
                z.tell('The window is closed.\n')
                return this_is_it(KITCHEN_WINDOW)
        else:
            z.tell("I can't see how to get in from here.\n")
            return True
    elif PRSA == V_BURN:
        z.tell('You must be joking.\n')
        return True
    return False


def go_next(tbl=0):
    val = 0
    if (val := lkp(HERE, tbl)):
        if not goto(val):
            return 2
        else:
            return 1
    return False


def forest_f():
    if PRSA == V_WALK_AROUND:
        if (HERE in (WEST_OF_HOUSE, NORTH_OF_HOUSE, SOUTH_OF_HOUSE)) or (HERE == EAST_OF_HOUSE):
            z.tell("You aren't even in the forest.\n")
        return go_next(FOREST_AROUND)
    elif PRSA == V_DISEMBARK:
        z.tell('You will have to specify a direction.\n')
        return True
    elif PRSA == V_FIND:
        z.tell('You cannot see the forest for the trees.\n')
        return True
    elif PRSA == V_LISTEN:
        z.tell('The pines and the hemlocks seem to be murmuring.\n')
        return True
    return False


def mountain_range_f():
    if PRSA in (V_CLIMB_UP, V_CLIMB_DOWN, V_CLIMB_FOO):
        z.tell("Don't you believe me? The mountains are impassable!\n")
        return True
    return False


def water_f():
    global PRSA, PRSI, PRSO
    av = 0
    w = 0
    pi_p = 0
    if PRSA == V_SGIVE:
        return False
    elif PRSA in (V_THROUGH, V_BOARD):
        _t1 = z.S(pick_one(SWIMYUKS))
        z.tell(_t1, '\n')
        return True
    elif PRSA == V_FILL:
        w = PRSI
        PRSA = V_PUT
        PRSI = PRSO
        PRSO = w
        pi_p = False
    elif (PRSO == GLOBAL_WATER) or (PRSO == WATER):
        w = PRSO
        pi_p = False
    else:
        w = PRSI
        if w:
            pi_p = True
    if w == GLOBAL_WATER:
        w = WATER
        if PRSA in (V_TAKE, V_PUT):
            remove_carefully(w)
    if pi_p:
        PRSI = w
    else:
        PRSO = w
    av = z.loc(WINNER)
    if not z.fset_p(av, VEHBIT):
        av = False
    if (PRSA in (V_TAKE, V_PUT)) and (not pi_p):
        if av and ((av == PRSI) or ((not PRSI) and (not z.in_p(w, av)))):
            z.tell('There is now a puddle in the bottom of the ', z.D(av), '.\n')
            remove_carefully(PRSO)
            return z.move(PRSO, av)
        elif PRSI and (PRSI != BOTTLE):
            z.tell('The water leaks out of the ', z.D(PRSI), ' and evaporates immediately.\n')
            return remove_carefully(w)
        elif z.in_p(BOTTLE, WINNER):
            if not z.fset_p(BOTTLE, OPENBIT):
                z.tell('The bottle is closed.\n')
                return this_is_it(BOTTLE)
            elif not z.first_p(BOTTLE):
                z.move(WATER, BOTTLE)
                z.tell('The bottle is now full of water.\n')
                return True
            else:
                z.tell('The water slips through your fingers.\n')
                return True
        elif z.in_p(PRSO, BOTTLE) and (PRSA == V_TAKE) and (not PRSI):
            z.tell("It's in the bottle. Perhaps you should take that instead.\n")
            return True
        else:
            z.tell('The water slips through your fingers.\n')
            return True
    elif pi_p:
        if (PRSA == V_PUT) and global_in_p(RIVER, HERE):
            perform(V_PUT, PRSO, RIVER)
        else:
            z.tell('Nice try.\n')
        return True
    elif PRSA in (V_DROP, V_GIVE):
        if (PRSA == V_DROP) and z.in_p(WATER, BOTTLE) and (not z.fset_p(BOTTLE, OPENBIT)):
            z.tell('The bottle is closed.\n')
            return True
        remove_carefully(WATER)
        if av:
            z.tell('There is now a puddle in the bottom of the ', z.D(av), '.\n')
            return z.move(WATER, av)
        else:
            z.tell('The water spills to the floor and evaporates immediately.\n')
            return remove_carefully(WATER)
    elif PRSA == V_THROW:
        z.tell('The water splashes on the walls and evaporates immediately.\n')
        return remove_carefully(WATER)
    return False


def kitchen_window_f():
    global KITCHEN_WINDOW_FLAG
    if PRSA in (V_OPEN, V_CLOSE):
        KITCHEN_WINDOW_FLAG = True
        return open_close(KITCHEN_WINDOW, 'With great effort, you open the window far enough to allow entry.', 'The window closes (more easily than it opened).')
    elif (PRSA == V_EXAMINE) and (not KITCHEN_WINDOW_FLAG):
        z.tell('The window is slightly ajar, but not enough to allow entry.\n')
        return True
    elif PRSA in (V_WALK, V_BOARD, V_THROUGH):
        if HERE == KITCHEN:
            do_walk(P_EAST)
        else:
            do_walk(P_WEST)
        return True
    elif PRSA == V_LOOK_INSIDE:
        z.tell('You can see ')
        if HERE == KITCHEN:
            z.tell('a clear area leading towards a forest.\n')
            return True
        else:
            z.tell('what appears to be a kitchen.\n')
            return True
    return False


def ghosts_f():
    global P_CONT
    if PRSA == V_TELL:
        z.tell('The spirits jeer loudly and ignore you.\n')
        P_CONT = False
        return P_CONT
    elif PRSA == V_EXORCISE:
        z.tell('Only the ceremony itself has any effect.\n')
        return True
    elif (PRSA in (V_ATTACK, V_MUNG)) and (PRSO == GHOSTS):
        z.tell('How can you attack a spirit with material objects?\n')
        return True
    else:
        z.tell('You seem unable to interact with these spirits.\n')
        return True
    return False


def basket_f():
    global CAGE_TOP, LIT
    if PRSA == V_RAISE:
        if CAGE_TOP:
            _t1 = z.S(pick_one(DUMMY))
            z.tell(_t1, '\n')
            return True
        else:
            z.move(RAISED_BASKET, SHAFT_ROOM)
            z.move(LOWERED_BASKET, LOWER_SHAFT)
            CAGE_TOP = True
            this_is_it(RAISED_BASKET)
            z.tell('The basket is raised to the top of the shaft.\n')
            return True
    elif PRSA == V_LOWER:
        if not CAGE_TOP:
            _t2 = z.S(pick_one(DUMMY))
            z.tell(_t2, '\n')
            return True
        else:
            z.move(RAISED_BASKET, LOWER_SHAFT)
            z.move(LOWERED_BASKET, SHAFT_ROOM)
            this_is_it(LOWERED_BASKET)
            z.tell('The basket is lowered to the bottom of the shaft.\n')
            CAGE_TOP = False
            if LIT and (not (LIT := lit_p(HERE))):
                z.tell('It is now pitch black.\n')
            return True
    elif (PRSO == LOWERED_BASKET) or (PRSI == LOWERED_BASKET):
        z.tell('The basket is at the other end of the chain.\n')
        return True
    elif (PRSA == V_TAKE) and (PRSO in (RAISED_BASKET, LOWERED_BASKET)):
        z.tell('The cage is securely fastened to the iron chain.\n')
        return True
    return False


def bat_f():
    global P_CONT
    if PRSA == V_TELL:
        fweep(6)
        P_CONT = False
        return P_CONT
    elif PRSA in (V_TAKE, V_ATTACK, V_MUNG):
        if z.loc(GARLIC) in (WINNER, HERE):
            z.tell("You can't reach him; he's on the ceiling.\n")
            return True
        else:
            return fly_me()
    return False


def fly_me():
    fweep(4)
    z.tell('The bat grabs you by the scruff of your neck and lifts you away....\n\n')
    goto(pick_one(BAT_DROPS), False)
    if HERE != ENTRANCE_TO_HADES:
        v_first_look()
    return True


def fweep(n=0):
    while True:
        if (n := (n - 1)) < 1:
            break
        else:
            z.tell('    Fweep!\n')
    return z.crlf()


def bell_f():
    if PRSA == V_RING:
        if (HERE == z.rtn(lld_room)) and (not LLD_FLAG):
            return False
        else:
            z.tell('Ding, dong.\n')
            return True
    return False


def hot_bell_f():
    if PRSA == V_TAKE:
        z.tell('The bell is very hot and cannot be taken.\n')
        return True
    elif (PRSA == V_RUB) or ((PRSA == V_RING) and PRSI):
        if z.fset_p(PRSI, BURNBIT):
            z.tell('The ', z.D(PRSI), ' burns and is consumed.\n')
            return remove_carefully(PRSI)
        elif PRSI == HANDS:
            z.tell('The bell is too hot to touch.\n')
            return True
        else:
            z.tell('The heat from the bell is too intense.\n')
            return True
    elif PRSA == V_POUR_ON:
        remove_carefully(PRSO)
        z.tell('The water cools the bell and is evaporated.\n')
        queue(z.rtn(i_xbh), 0)
        return i_xbh()
    elif PRSA == V_RING:
        z.tell('The bell is too hot to reach.\n')
        return True
    return False


def boarded_window_fcn():
    if PRSA == V_OPEN:
        z.tell("The windows are boarded and can't be opened.\n")
        return True
    elif PRSA == V_MUNG:
        z.tell("You can't break the windows open.\n")
        return True
    return False


def nails_pseudo():
    if PRSA == V_TAKE:
        z.tell('The nails, deeply imbedded in the door, cannot be removed.\n')
        return True
    return False


def crack_fcn():
    if PRSA == V_THROUGH:
        z.tell("You can't fit through the crack.\n")
        return True
    return False


def kitchen_fcn(rarg=0):
    if rarg == M_LOOK:
        z.tell('You are in the kitchen of the white house. A table seems to have been used recently for the preparation of food. A passage leads to the west and a dark staircase can be seen leading upward. A dark chimney leads down and to the east is a small window which is ')
        if z.fset_p(KITCHEN_WINDOW, OPENBIT):
            z.tell('open.\n')
            return True
        else:
            z.tell('slightly ajar.\n')
            return True
    elif rarg == M_BEG:
        if (PRSA == V_CLIMB_UP) and (PRSO == STAIRS):
            return do_walk(P_UP)
        elif (PRSA == V_CLIMB_UP) and (PRSO == STAIRS):
            z.tell('There are no stairs leading down.\n')
            return True
    return False


def stone_barrow_fcn(rarg=0):
    if (rarg == M_BEG) and ((PRSA == V_ENTER) or ((PRSA == V_WALK) and (PRSO in (P_WEST, P_IN))) or ((PRSA == V_THROUGH) and (PRSO == BARROW))):
        z.tell('Inside the Barrow\nAs you enter the barrow, the door closes inexorably behind you. Around you it is dark, but ahead is an enormous cavern, brightly lit. Through its center runs a wide stream. Spanning the stream is a small wooden footbridge, and beyond a path leads into a dark tunnel. Above the bridge, floating in the air, is a large sign. It reads:  All ye who stand before this bridge have completed a great and perilous adventure which has tested your wit and courage. You have mastered')
        if (z.getb(0, 1) & 8) == 0:
            z.tell(' the first part of the ZORK trilogy. Those who pass over this bridge must be prepared to undertake an even greater adventure that will severely test your skill and bravery!\n\nThe ZORK trilogy continues with "ZORK II: The Wizard of Frobozz" and is completed in "ZORK III: The Dungeon Master."\n')
        else:
            z.tell(' ZORK: The Great Underground Empire.\n\n')
        return finish()
    return False


def barrow_door_fcn():
    if PRSA in (V_OPEN, V_CLOSE):
        z.tell('The door is too heavy.\n')
        return True
    return False


def barrow_fcn():
    if PRSA == V_THROUGH:
        return do_walk(P_WEST)
    return False


def trophy_case_fcn():
    if (PRSA == V_TAKE) and (PRSO == TROPHY_CASE):
        z.tell('The trophy case is securely fastened to the wall.\n')
        return True
    return False


def living_room_fcn(rarg=0):
    global SCORE
    rug_p = 0
    tc = 0
    if rarg == M_LOOK:
        z.tell('You are in the living room. There is a doorway to the east')
        if MAGIC_FLAG:
            z.tell('. To the west is a cyclops-shaped opening in an old wooden door, above which is some strange gothic lettering, ')
        else:
            z.tell(', a wooden door with strange gothic lettering to the west, which appears to be nailed shut, ')
        z.tell('a trophy case, ')
        rug_p = RUG_MOVED
        if rug_p and z.fset_p(TRAP_DOOR, OPENBIT):
            z.tell('and a rug lying beside an open trap door.')
        elif rug_p:
            z.tell('and a closed trap door at your feet.')
        elif z.fset_p(TRAP_DOOR, OPENBIT):
            z.tell('and an open trap door at your feet.')
        else:
            z.tell('and a large oriental rug in the center of the room.')
        z.crlf()
        return True
    elif rarg == M_END:
        if (PRSA == V_TAKE) or ((PRSA == V_PUT) and (PRSI == TROPHY_CASE)):
            if z.in_p(PRSO, TROPHY_CASE):
                touch_all(PRSO)
            SCORE = BASE_SCORE + otval_frob()
            score_upd(0)
            return False
    return False


def touch_all(obj=0):
    f = 0
    f = z.first_p(obj)
    while True:
        if not f:
            return True
        else:
            z.fset(f, TOUCHBIT)
            if z.first_p(f):
                touch_all(f)
        f = z.next_p(f)
    return False


def otval_frob(o=z.NOARG):
    if o is z.NOARG:
        o = TROPHY_CASE
    f = 0
    score = 0
    f = z.first_p(o)
    while True:
        if not f:
            return score
        score = score + z.getp(f, P_TVALUE)
        if z.first_p(f):
            otval_frob(f)
        f = z.next_p(f)
    return False


def trap_door_fcn():
    if PRSA == V_RAISE:
        perform(V_OPEN, TRAP_DOOR)
        return True
    elif (PRSA in (V_OPEN, V_CLOSE)) and (HERE == LIVING_ROOM):
        return open_close(PRSO, 'The door reluctantly opens to reveal a rickety staircase descending into darkness.', 'The door swings shut and closes.')
    elif (PRSA == V_LOOK_UNDER) and (HERE == LIVING_ROOM):
        if z.fset_p(TRAP_DOOR, OPENBIT):
            z.tell('You see a rickety staircase descending into darkness.\n')
            return True
        else:
            z.tell("It's closed.\n")
            return True
    elif HERE == CELLAR:
        if (PRSA in (V_OPEN, V_UNLOCK)) and (not z.fset_p(TRAP_DOOR, OPENBIT)):
            z.tell('The door is locked from above.\n')
            return True
        elif (PRSA == V_CLOSE) and (not z.fset_p(TRAP_DOOR, OPENBIT)):
            z.fclear(TRAP_DOOR, TOUCHBIT)
            z.fclear(TRAP_DOOR, OPENBIT)
            z.tell('The door closes and locks.\n')
            return True
        elif PRSA in (V_OPEN, V_CLOSE):
            _t1 = z.S(pick_one(DUMMY))
            z.tell(_t1, '\n')
            return True
    return False


def cellar_fcn(rarg=0):
    if rarg == M_LOOK:
        z.tell('You are in a dark and damp cellar with a narrow passageway leading north, and a crawlway to the south. On the west is the bottom of a steep metal ramp which is unclimbable.\n')
        return True
    elif rarg == M_ENTER:
        if z.fset_p(TRAP_DOOR, OPENBIT) and (not z.fset_p(TRAP_DOOR, TOUCHBIT)):
            z.fclear(TRAP_DOOR, OPENBIT)
            z.fset(TRAP_DOOR, TOUCHBIT)
            z.tell('The trap door crashes shut, and you hear someone barring it.\n\n')
            return True
    return False


def chimney_f():
    if PRSA == V_EXAMINE:
        z.tell('The chimney leads ')
        if HERE == KITCHEN:
            z.tell('down')
        else:
            z.tell('up')
        z.tell('ward, and looks climbable.\n')
        return True
    return False


def up_chimney_function():
    f = 0
    if not (f := z.first_p(WINNER)):
        z.tell('Going up empty-handed is a bad idea.\n')
        return False
    elif ((not (f := z.next_p(f))) or (not z.next_p(f))) and z.in_p(LAMP, WINNER):
        if not z.fset_p(TRAP_DOOR, OPENBIT):
            z.fclear(TRAP_DOOR, TOUCHBIT)
        return KITCHEN
    else:
        z.tell("You can't get up there with what you're carrying.\n")
        return False
    return False


def trap_door_exit():
    if RUG_MOVED:
        if z.fset_p(TRAP_DOOR, OPENBIT):
            return CELLAR
        else:
            z.tell('The trap door is closed.\n')
            this_is_it(TRAP_DOOR)
            return False
    else:
        z.tell("You can't go that way.\n")
        return False
    return False


def rug_fcn():
    global RUG_MOVED
    if PRSA == V_RAISE:
        z.tell('The rug is too heavy to lift')
        if RUG_MOVED:
            z.tell('.\n')
            return True
        else:
            z.tell(', but in trying to take it you have noticed an irregularity beneath it.\n')
            return True
    elif PRSA in (V_MOVE, V_PUSH):
        if RUG_MOVED:
            z.tell('Having moved the carpet previously, you find it impossible to move it again.\n')
            return True
        else:
            z.tell('With a great effort, the rug is moved to one side of the room, revealing the dusty cover of a closed trap door.\n')
            z.fclear(TRAP_DOOR, INVISIBLE)
            this_is_it(TRAP_DOOR)
            RUG_MOVED = True
            return RUG_MOVED
    elif PRSA == V_TAKE:
        z.tell('The rug is extremely heavy and cannot be carried.\n')
        return True
    elif (PRSA == V_LOOK_UNDER) and (not RUG_MOVED) and (not z.fset_p(TRAP_DOOR, OPENBIT)):
        z.tell('Underneath the rug is a closed trap door. As you drop the corner of the rug, the trap door is once again concealed from view.\n')
        return True
    elif PRSA == V_CLIMB_ON:
        if (not RUG_MOVED) and (not z.fset_p(TRAP_DOOR, OPENBIT)):
            z.tell('As you sit, you notice an irregularity underneath it. Rather than be uncomfortable, you stand up again.\n')
            return True
        else:
            z.tell("I suppose you think it's a magic carpet?\n")
            return True
    return False


def axe_f():
    if TROLL_FLAG:
        return False
    else:
        return weapon_function(AXE, TROLL)
    return False


def stiletto_function():
    return weapon_function(STILETTO, THIEF)


def weapon_function(w=0, v=0):
    if not z.in_p(v, HERE):
        return False
    elif PRSA == V_TAKE:
        if z.in_p(w, v):
            z.tell('The ', z.D(v), ' swings it out of your reach.\n')
        else:
            z.tell('The ', z.D(w), " seems white-hot. You can't hold on to it.\n")
        return True
    return False


def troll_fcn(mode=False):
    global P_CONT, TROLL_FLAG
    if PRSA == V_TELL:
        P_CONT = False
        z.tell("The troll isn't much of a conversationalist.\n")
        return True
    elif mode == F_BUSY_P:
        if z.in_p(AXE, TROLL):
            return False
        elif z.in_p(AXE, HERE) and zprob(75):
            z.fset(AXE, NDESCBIT)
            z.fclear(AXE, WEAPONBIT)
            z.move(AXE, TROLL)
            z.putp(TROLL, P_LDESC, 'A nasty-looking troll, brandishing a bloody axe, blocks all passages out of the room.')
            if z.in_p(TROLL, HERE):
                z.tell('The troll, angered and humiliated, recovers his weapon. He appears to have an axe to grind with you.\n')
            return True
        elif z.in_p(TROLL, HERE):
            z.putp(TROLL, P_LDESC, 'A pathetically babbling troll is here.')
            z.tell('The troll, disarmed, cowers in terror, pleading for his life in the guttural tongue of the trolls.\n')
            return True
    elif mode == F_DEAD:
        if z.in_p(AXE, TROLL):
            z.move(AXE, HERE)
            z.fclear(AXE, NDESCBIT)
            z.fset(AXE, WEAPONBIT)
        TROLL_FLAG = True
        return TROLL_FLAG
    elif mode == F_UNCONSCIOUS:
        z.fclear(TROLL, FIGHTBIT)
        if z.in_p(AXE, TROLL):
            z.move(AXE, HERE)
            z.fclear(AXE, NDESCBIT)
            z.fset(AXE, WEAPONBIT)
        z.putp(TROLL, P_LDESC, 'An unconscious troll is sprawled on the floor. All passages out of the room are open.')
        TROLL_FLAG = True
        return TROLL_FLAG
    elif mode == F_CONSCIOUS:
        if z.in_p(TROLL, HERE):
            z.fset(TROLL, FIGHTBIT)
            z.tell('The troll stirs, quickly resuming a fighting stance.\n')
        if z.in_p(AXE, TROLL):
            z.putp(TROLL, P_LDESC, 'A nasty-looking troll, brandishing a bloody axe, blocks all passages out of the room.')
        elif z.in_p(AXE, TROLL_ROOM):
            z.fset(AXE, NDESCBIT)
            z.fclear(AXE, WEAPONBIT)
            z.move(AXE, TROLL)
            z.putp(TROLL, P_LDESC, 'A nasty-looking troll, brandishing a bloody axe, blocks all passages out of the room.')
        else:
            z.putp(TROLL, P_LDESC, 'A troll is here.')
        TROLL_FLAG = False
        return TROLL_FLAG
    elif mode == F_FIRST_P:
        if 33 > z.random(100):
            z.fset(TROLL, FIGHTBIT)
            P_CONT = False
            return True
    elif not mode:
        if PRSA == V_EXAMINE:
            z.tell(z.S(z.getp(TROLL, P_LDESC)), '\n')
            return True
        elif ((PRSA in (V_THROW, V_GIVE)) and PRSO and (PRSI == TROLL)) or (PRSA in (V_TAKE, V_MOVE, V_MUNG)):
            awaken(TROLL)
            if PRSA in (V_THROW, V_GIVE):
                if (PRSO == AXE) and z.in_p(AXE, WINNER):
                    z.tell('The troll scratches his head in confusion, then takes the axe.\n')
                    z.fset(TROLL, FIGHTBIT)
                    z.move(AXE, TROLL)
                    return True
                elif PRSO in (TROLL, AXE):
                    z.tell('You would have to get the ', z.D(PRSO), ' first, and that seems unlikely.\n')
                    return True
                if PRSA == V_THROW:
                    z.tell('The troll, who is remarkably coordinated, catches the ', z.D(PRSO))
                else:
                    z.tell('The troll, who is not overly proud, graciously accepts the gift')
                if (20 > z.random(100)) and (PRSO in (KNIFE, SWORD, AXE)):
                    remove_carefully(PRSO)
                    z.tell(' and eats it hungrily. Poor troll, he dies from an internal hemorrhage and his carcass disappears in a sinister black fog.\n')
                    remove_carefully(TROLL)
                    z.apply(z.getp(TROLL, P_ACTION), F_DEAD)
                    TROLL_FLAG = True
                    return TROLL_FLAG
                elif PRSO in (KNIFE, SWORD, AXE):
                    z.move(PRSO, HERE)
                    z.tell(' and, being for the moment sated, throws it back. Fortunately, the troll has poor control, and the ', z.D(PRSO), ' falls to the floor. He does not look pleased.\n')
                    return z.fset(TROLL, FIGHTBIT)
                else:
                    z.tell(' and not having the most discriminating tastes, gleefully eats it.\n')
                    return remove_carefully(PRSO)
            elif PRSA in (V_TAKE, V_MOVE):
                z.tell('The troll spits in your face, grunting "Better luck next time" in a rather barbarous accent.\n')
                return True
            elif PRSA == V_MUNG:
                z.tell('The troll laughs at your puny gesture.\n')
                return True
        elif PRSA == V_LISTEN:
            z.tell('Every so often the troll says something, probably uncomplimentary, in his guttural tongue.\n')
            return True
        elif TROLL_FLAG and (PRSA == V_HELLO):
            z.tell("Unfortunately, the troll can't hear you.\n")
            return True
    return False


def leaves_appear():
    global GRATE_REVEALED
    if (not z.fset_p(GRATE, OPENBIT)) and (not GRATE_REVEALED):
        if PRSA in (V_MOVE, V_TAKE):
            z.tell('In disturbing the pile of leaves, a grating is revealed.\n')
        else:
            z.tell('With the leaves moved, a grating is revealed.\n')
        z.fclear(GRATE, INVISIBLE)
        GRATE_REVEALED = True
    return False


def leaf_pile():
    if PRSA == V_COUNT:
        z.tell('There are 69,105 leaves here.\n')
        return True
    elif PRSA == V_BURN:
        leaves_appear()
        remove_carefully(PRSO)
        if z.in_p(PRSO, HERE):
            z.tell('The leaves burn.\n')
            return True
        else:
            return jigs_up('The leaves burn, and so do you.')
    elif PRSA == V_CUT:
        z.tell('You rustle the leaves around, making quite a mess.\n')
        leaves_appear()
        return True
    elif PRSA in (V_MOVE, V_TAKE):
        if PRSA == V_MOVE:
            z.tell('Done.\n')
        if GRATE_REVEALED:
            return False
        leaves_appear()
        if PRSA == V_TAKE:
            return False
        else:
            return True
    elif (PRSA == V_LOOK_UNDER) and (not GRATE_REVEALED):
        z.tell('Underneath the pile of leaves is a grating. As you release the leaves, the grating is once again concealed from view.\n')
        return True
    return False


def clearing_fcn(rarg=0):
    if rarg == M_ENTER:
        if not GRATE_REVEALED:
            return z.fset(GRATE, INVISIBLE)
    elif rarg == M_LOOK:
        z.tell('You are in a clearing, with a forest surrounding you on all sides. A path leads south.')
        if z.fset_p(GRATE, OPENBIT):
            z.crlf()
            z.tell('There is an open grating, descending into darkness.')
        elif GRATE_REVEALED:
            z.crlf()
            z.tell('There is a grating securely fastened into the ground.')
        return z.crlf()
    return False


def maze_11_fcn(rarg=0):
    if rarg == M_ENTER:
        return z.fclear(GRATE, INVISIBLE)
    elif rarg == M_LOOK:
        z.tell('You are in a small room near the maze. There are twisty passages in the immediate vicinity.\n')
        if z.fset_p(GRATE, OPENBIT):
            z.tell('Above you is an open grating with sunlight pouring in.')
        elif GRUNLOCK:
            z.tell('Above you is a grating.')
        else:
            z.tell('Above you is a grating locked with a skull-and-crossbones lock.')
        return z.crlf()
    return False


def grate_function():
    global GRATE_REVEALED, GRUNLOCK
    if (PRSA == V_OPEN) and (PRSI == KEYS):
        perform(V_UNLOCK, GRATE, KEYS)
        return True
    elif PRSA == V_LOCK:
        if HERE == GRATING_ROOM:
            GRUNLOCK = False
            z.tell('The grate is locked.\n')
            return True
        elif HERE == GRATING_CLEARING:
            z.tell("You can't lock it from this side.\n")
            return True
    elif (PRSA == V_UNLOCK) and (PRSO == GRATE):
        if (HERE == GRATING_ROOM) and (PRSI == KEYS):
            GRUNLOCK = True
            z.tell('The grate is unlocked.\n')
            return True
        elif (HERE == GRATING_CLEARING) and (PRSI == KEYS):
            z.tell("You can't reach the lock from here.\n")
            return True
        else:
            z.tell('Can you unlock a grating with a ', z.D(PRSI), '?\n')
            return True
    elif PRSA == V_PICK:
        z.tell("You can't pick the lock.\n")
        return True
    elif PRSA in (V_OPEN, V_CLOSE):
        if GRUNLOCK:
            if HERE == CLEARING:
                _t1 = 'The grating opens.'
            else:
                _t1 = 'The grating opens to reveal trees above you.'
            open_close(GRATE, _t1, 'The grating is closed.')
            if z.fset_p(GRATE, OPENBIT):
                if (HERE != CLEARING) and (not GRATE_REVEALED):
                    z.tell('A pile of leaves falls onto your head and to the ground.\n')
                    GRATE_REVEALED = True
                    z.move(LEAVES, HERE)
                return z.fset(GRATING_ROOM, ONBIT)
            else:
                return z.fclear(GRATING_ROOM, ONBIT)
        else:
            z.tell('The grating is locked.\n')
            return True
    elif (PRSA == V_PUT) and (PRSI == GRATE):
        if z.getp(PRSO, P_SIZE) > 20:
            z.tell("It won't fit through the grating.\n")
            return True
        else:
            z.move(PRSO, GRATING_ROOM)
            z.tell('The ', z.D(PRSO), ' goes through the grating into the darkness below.\n')
            return True
    return False


def maze_diodes():
    z.tell("You won't be able to get back up to the tunnel you are going through when it gets to the next room.\n\n")
    if HERE == MAZE_2:
        return MAZE_4
    elif HERE == MAZE_7:
        return DEAD_END_1
    elif HERE == MAZE_9:
        return MAZE_11
    elif HERE == MAZE_12:
        return MAZE_5
    return False


def rusty_knife_fcn():
    if PRSA == V_TAKE:
        if z.in_p(SWORD, WINNER):
            z.tell('As you touch the rusty knife, your sword gives a single pulse of blinding blue light.\n')
        return False
    elif ((PRSI == RUSTY_KNIFE) and (PRSA == V_ATTACK)) or ((PRSA == V_SWING) and (PRSO == RUSTY_KNIFE) and PRSI):
        remove_carefully(RUSTY_KNIFE)
        return jigs_up('As the knife approaches its victim, your mind is submerged by an overmastering will. Slowly, your hand turns, until the rusty blade is an inch from your neck. The knife seems to sing as it savagely slits your throat.')
    return False


def knife_f():
    if PRSA == V_TAKE:
        z.fclear(ATTIC_TABLE, NDESCBIT)
        return False
    return False


def skeleton():
    if PRSA in (V_TAKE, V_RUB, V_MOVE, V_PUSH, V_RAISE, V_LOWER, V_ATTACK, V_KICK, V_KISS):
        z.tell('A ghost appears in the room and is appalled at your desecration of the remains of a fellow adventurer. He casts a curse on your valuables and banishes them to the Land of the Living Dead. The ghost leaves, muttering obscenities.\n')
        rob(HERE, LAND_OF_LIVING_DEAD, 100)
        rob(ADVENTURER, LAND_OF_LIVING_DEAD)
        return True
    return False


def torch_object():
    if PRSA == V_EXAMINE:
        z.tell('The torch is burning.\n')
        return True
    elif (PRSA == V_POUR_ON) and (PRSI == TORCH):
        z.tell('The water evaporates before it gets close.\n')
        return True
    elif (PRSA == V_LAMP_OFF) and z.fset_p(PRSO, ONBIT):
        z.tell('You nearly burn your hand trying to extinguish the flame.\n')
        return True
    return False


def mirror_room(rarg=0):
    if rarg == M_LOOK:
        z.tell('You are in a large square room with tall ceilings. On the south wall is an enormous mirror which fills the entire wall. There are exits on the other three sides of the room.\n')
        if MIRROR_MUNG:
            z.tell('Unfortunately, the mirror has been destroyed by your recklessness.\n')
            return True
    return False


def mirror_mirror():
    global LUCKY, MIRROR_MUNG
    rm2 = MIRROR_ROOM_2
    l1 = 0
    l2 = 0
    n = 0
    if (not MIRROR_MUNG) and (PRSA == V_RUB):
        if PRSI and (PRSI != HANDS):
            z.tell('You feel a faint tingling transmitted through the ', z.D(PRSI), '.\n')
            return True
        if HERE == rm2:
            rm2 = MIRROR_ROOM_1
        l1 = z.first_p(HERE)
        l2 = z.first_p(rm2)
        while True:
            if not l1:
                break
            n = z.next_p(l1)
            z.move(l1, rm2)
            l1 = n
        while True:
            if not l2:
                break
            n = z.next_p(l2)
            z.move(l2, HERE)
            l2 = n
        goto(rm2, False)
        z.tell('There is a rumble from deep within the earth and the room shakes.\n')
        return True
    elif PRSA in (V_LOOK_INSIDE, V_EXAMINE):
        if MIRROR_MUNG:
            z.tell('The mirror is broken into many pieces.')
        else:
            z.tell('There is an ugly person staring back at you.')
        return z.crlf()
    elif PRSA == V_TAKE:
        z.tell('The mirror is many times your size. Give up.\n')
        return True
    elif PRSA in (V_MUNG, V_THROW, V_ATTACK):
        if MIRROR_MUNG:
            z.tell("Haven't you done enough damage already?\n")
            return True
        else:
            MIRROR_MUNG = True
            LUCKY = False
            z.tell("You have broken the mirror. I hope you have a seven years' supply of good luck handy.\n")
            return True
    return False


def torch_room_fcn(rarg=0):
    if rarg == M_LOOK:
        z.tell('This is a large room with a prominent doorway leading to a down staircase. Above you is a large dome. Up around the edge of the dome (20 feet up) is a wooden railing. In the center of the room sits a white marble pedestal.\n')
        if DOME_FLAG:
            z.tell('A piece of rope descends from the railing above, ending some five feet above your head.\n')
            return True
    return False


def dome_room_fcn(rarg=0):
    global HERE
    if rarg == M_LOOK:
        z.tell('You are at the periphery of a large dome, which forms the ceiling of another room below. Protecting you from a precipitous drop is a wooden railing which circles the dome.\n')
        if DOME_FLAG:
            z.tell('Hanging down from the railing is a rope which ends about ten feet from the floor below.\n')
            return True
    elif rarg == M_ENTER:
        if DEAD:
            z.tell('As you enter the dome you feel a strong pull as if from a wind drawing you over the railing and down.\n')
            z.move(WINNER, TORCH_ROOM)
            HERE = TORCH_ROOM
            return True
        elif PRSA == V_LEAP:
            return jigs_up("I'm afraid that the leap you attempted has done you in.")
    return False


def lld_room(rarg=0):
    global LLD_FLAG, XB, XC
    if rarg == M_LOOK:
        z.tell('You are outside a large gateway, on which is inscribed\n\n  Abandon every hope all ye who enter here!\n\nThe gate is open; through it you can see a desolation, with a pile of mangled bodies in one corner. Thousands of voices, lamenting some hideous fate, can be heard.\n')
        if (not LLD_FLAG) and (not DEAD):
            z.tell('The way through the gate is barred by evil spirits, who jeer at your attempts to pass.\n')
            return True
    elif rarg == M_BEG:
        if PRSA == V_EXORCISE:
            if not LLD_FLAG:
                if z.in_p(BELL, WINNER) and z.in_p(BOOK, WINNER) and z.in_p(CANDLES, WINNER):
                    z.tell('You must perform the ceremony.\n')
                    return True
                else:
                    z.tell("You aren't equipped for an exorcism.\n")
                    return True
        elif (not LLD_FLAG) and (PRSA == V_RING) and (PRSO == BELL):
            XB = True
            remove_carefully(BELL)
            this_is_it(HOT_BELL)
            z.move(HOT_BELL, HERE)
            z.tell('The bell suddenly becomes red hot and falls to the ground. The wraiths, as if paralyzed, stop their jeering and slowly turn to face you. On their ashen faces, the expression of a long-forgotten terror takes shape.\n')
            if z.in_p(CANDLES, WINNER):
                z.tell('In your confusion, the candles drop to the ground (and they are out).\n')
                z.move(CANDLES, HERE)
                z.fclear(CANDLES, ONBIT)
                z.put(int_(z.rtn(i_candles)), C_ENABLED_P, 0)
            z.put(queue(z.rtn(i_xb), 6), C_ENABLED_P, 1)
            return z.put(queue(z.rtn(i_xbh), 20), C_ENABLED_P, 1)
        elif XC and (PRSA == V_READ) and (PRSO == BOOK) and (not LLD_FLAG):
            z.tell('Each word of the prayer reverberates through the hall in a deafening confusion. As the last word fades, a voice, loud and commanding, speaks: "Begone, fiends!" A heart-stopping scream fills the cavern, and the spirits, sensing a greater power, flee through the walls.\n')
            remove_carefully(GHOSTS)
            LLD_FLAG = True
            return z.put(int_(z.rtn(i_xc)), C_ENABLED_P, 0)
    elif rarg == M_END:
        if XB and z.in_p(CANDLES, WINNER) and z.fset_p(CANDLES, ONBIT) and (not XC):
            XC = True
            z.tell('The flames flicker wildly and appear to dance. The earth beneath your feet trembles, and your legs nearly buckle beneath you. The spirits cower at your unearthly power.\n')
            z.put(int_(z.rtn(i_xb)), C_ENABLED_P, 0)
            return z.put(queue(z.rtn(i_xc), 3), C_ENABLED_P, 1)
    return False


def i_xb():
    global XB
    if not (XC):
        if HERE == ENTRANCE_TO_HADES:
            z.tell('The tension of this ceremony is broken, and the wraiths, amused but shaken at your clumsy attempt, resume their hideous jeering.\n')
    XB = False
    return XB


def i_xc():
    global XC
    XC = False
    return i_xb()


def i_xbh():
    remove_carefully(HOT_BELL)
    z.move(BELL, ENTRANCE_TO_HADES)
    if HERE == ENTRANCE_TO_HADES:
        z.tell('The bell appears to have cooled down.\n')
        return True
    return False


def dam_room_fcn(rarg=0):
    if rarg == M_LOOK:
        z.tell('You are standing on the top of the Flood Control Dam #3, which was quite a tourist attraction in times far distant. There are paths to the north, south, and west, and a scramble down.\n')
        if LOW_TIDE and GATES_OPEN:
            z.tell('The water level behind the dam is low: The sluice gates have been opened. Water rushes through the dam and downstream.\n')
        elif GATES_OPEN:
            z.tell('The sluice gates are open, and water rushes through the dam. The water level behind the dam is still high.\n')
        elif LOW_TIDE:
            z.tell('The sluice gates are closed. The water level in the reservoir is quite low, but the level is rising quickly.\n')
        else:
            z.tell('The sluice gates on the dam are closed. Behind the dam, there can be seen a wide reservoir. Water is pouring over the top of the now abandoned dam.\n')
        z.tell('There is a control panel here, on which a large metal bolt is mounted. Directly above the bolt is a small green plastic bubble')
        if GATE_FLAG:
            z.tell(' which is glowing serenely')
        z.tell('.\n')
        return True
    return False


def bolt_f():
    global GATES_OPEN
    if PRSA == V_TURN:
        if PRSI == WRENCH:
            if GATE_FLAG:
                z.fclear(RESERVOIR_SOUTH, TOUCHBIT)
                if GATES_OPEN:
                    GATES_OPEN = False
                    z.fclear(LOUD_ROOM, TOUCHBIT)
                    z.tell('The sluice gates close and water starts to collect behind the dam.\n')
                    z.put(queue(z.rtn(i_rfill), 8), C_ENABLED_P, 1)
                    queue(z.rtn(i_rempty), 0)
                    return True
                else:
                    GATES_OPEN = True
                    z.tell('The sluice gates open and water pours through the dam.\n')
                    z.put(queue(z.rtn(i_rempty), 8), C_ENABLED_P, 1)
                    queue(z.rtn(i_rfill), 0)
                    return True
            else:
                z.tell("The bolt won't turn with your best effort.\n")
                return True
        else:
            z.tell("The bolt won't turn using the ", z.D(PRSI), '.\n')
            return True
    elif PRSA == V_TAKE:
        return integral_part()
    elif PRSA == V_OIL:
        z.tell("Hmm. It appears the tube contained glue, not oil. Turning the bolt won't get any easier....\n")
        return True
    return False


def bubble_f():
    if PRSA == V_TAKE:
        return integral_part()
    return False


def integral_part():
    z.tell('It is an integral part of the control panel.\n')
    return True


def i_rfill():
    global LOW_TIDE
    z.fset(RESERVOIR, NONLANDBIT)
    z.fclear(RESERVOIR, RLANDBIT)
    z.fclear(DEEP_CANYON, TOUCHBIT)
    z.fclear(LOUD_ROOM, TOUCHBIT)
    if z.in_p(TRUNK, RESERVOIR):
        z.fset(TRUNK, INVISIBLE)
    LOW_TIDE = False
    if HERE == RESERVOIR:
        if z.fset_p(z.loc(WINNER), VEHBIT):
            z.tell('The boat lifts gently out of the mud and is now floating on the reservoir.\n')
        else:
            jigs_up('You are lifted up by the rising river! You try to swim, but the currents are too strong. You come closer, closer to the awesome structure of Flood Control Dam #3. The dam beckons to you. The roar of the water nearly deafens you, but you remain conscious as you tumble over the dam toward your certain doom among the rocks at its base.')
    elif HERE == DEEP_CANYON:
        z.tell('A sound, like that of flowing water, starts to come from below.\n')
    elif HERE == LOUD_ROOM:
        z.tell('All of a sudden, an alarmingly loud roaring sound fills the room. Filled with fear, you scramble away.\n')
        goto(pick_one(LOUD_RUNS))
    elif HERE in (RESERVOIR_NORTH, RESERVOIR_SOUTH):
        z.tell('You notice that the water level has risen to the point that it is impossible to cross.\n')
    return True


def i_rempty():
    global LOW_TIDE
    z.fset(RESERVOIR, RLANDBIT)
    z.fclear(RESERVOIR, NONLANDBIT)
    z.fclear(DEEP_CANYON, TOUCHBIT)
    z.fclear(LOUD_ROOM, TOUCHBIT)
    z.fclear(TRUNK, INVISIBLE)
    LOW_TIDE = True
    if (HERE == RESERVOIR) and z.fset_p(z.loc(WINNER), VEHBIT):
        z.tell('The water level has dropped to the point at which the boat can no longer stay afloat. It sinks into the mud.\n')
    elif HERE == DEEP_CANYON:
        z.tell('The roar of rushing water is quieter now.\n')
    elif HERE in (RESERVOIR_NORTH, RESERVOIR_SOUTH):
        z.tell('The water level is now quite low here and you could easily cross over to the other side.\n')
    return True


def button_f():
    global GATE_FLAG, WATER_LEVEL
    if PRSA == V_READ:
        z.tell("They're greek to you.\n")
        return True
    elif PRSA == V_PUSH:
        if PRSO == BLUE_BUTTON:
            if WATER_LEVEL == 0:
                z.fclear(LEAK, INVISIBLE)
                z.tell('There is a rumbling sound and a stream of water appears to burst from the east wall of the room (apparently, a leak has occurred in a pipe).\n')
                WATER_LEVEL = 1
                z.put(queue(z.rtn(i_maint_room), -1), C_ENABLED_P, 1)
                return True
            else:
                z.tell('The blue button appears to be jammed.\n')
                return True
        elif PRSO == RED_BUTTON:
            z.tell('The lights within the room ')
            if z.fset_p(HERE, ONBIT):
                z.fclear(HERE, ONBIT)
                z.tell('shut off.\n')
                return True
            else:
                z.fset(HERE, ONBIT)
                z.tell('come on.\n')
                return True
        elif PRSO == BROWN_BUTTON:
            z.fclear(DAM_ROOM, TOUCHBIT)
            GATE_FLAG = False
            z.tell('Click.\n')
            return True
        elif PRSO == YELLOW_BUTTON:
            z.fclear(DAM_ROOM, TOUCHBIT)
            GATE_FLAG = True
            z.tell('Click.\n')
            return True
    return False


def tool_chest_fcn():
    if PRSA == V_EXAMINE:
        z.tell('The chests are all empty.\n')
        return True
    elif PRSA in (V_TAKE, V_OPEN, V_PUT):
        remove_carefully(TOOL_CHEST)
        z.tell('The chests are so rusty and corroded that they crumble when you touch them.\n')
        return True
    elif PRSA == V_OPEN:
        z.tell('The chests are already open.\n')
        return True
    return False


def i_maint_room():
    global WATER_LEVEL
    here_p = 0
    here_p = HERE == MAINTENANCE_ROOM
    if here_p:
        z.tell('The water level here is now ')
        z.tell(z.S(z.get(DROWNINGS, z.div(WATER_LEVEL, 2))))
        z.crlf()
    WATER_LEVEL = 1 + WATER_LEVEL
    if not (WATER_LEVEL < 14):
        mung_room(MAINTENANCE_ROOM, 'The room is full of water and cannot be entered.')
        queue(z.rtn(i_maint_room), 0)
        if here_p:
            jigs_up("I'm afraid you have done drowned yourself.")
    elif z.in_p(WINNER, INFLATED_BOAT) and (HERE in (MAINTENANCE_ROOM, DAM_ROOM, DAM_LOBBY)):
        jigs_up('The rising water carries the boat over the dam, down the river, and over the falls. Tsk, tsk.')
    return True


def leak_function():
    if WATER_LEVEL > 0:
        if (PRSA in (V_PUT, V_PUT_ON)) and (PRSO == PUTTY):
            return fix_maint_leak()
        elif PRSA == V_PLUG:
            if PRSI == PUTTY:
                return fix_maint_leak()
            else:
                return with_tell(PRSI)
    return False


def fix_maint_leak():
    global WATER_LEVEL
    WATER_LEVEL = -1
    queue(z.rtn(i_maint_room), 0)
    z.tell('By some miracle of Zorkian technology, you have managed to stop the leak in the dam.\n')
    return True


def putty_fcn():
    if ((PRSA == V_OIL) and (PRSI == PUTTY)) or ((PRSA == V_PUT) and (PRSO == PUTTY)):
        z.tell("The all-purpose gunk isn't a lubricant.\n")
        return True
    return False


def tube_function():
    if (PRSA == V_PUT) and (PRSI == TUBE):
        z.tell('The tube refuses to accept anything.\n')
        return True
    elif PRSA == V_SQUEEZE:
        if z.fset_p(PRSO, OPENBIT) and z.in_p(PUTTY, PRSO):
            z.move(PUTTY, WINNER)
            z.tell('The viscous material oozes into your hand.\n')
            return True
        elif z.fset_p(PRSO, OPENBIT):
            z.tell('The tube is apparently empty.\n')
            return True
        else:
            z.tell('The tube is closed.\n')
            return True
    return False


def dam_function():
    if PRSA in (V_OPEN, V_CLOSE):
        z.tell("Sounds reasonable, but this isn't how.\n")
        return True
    elif PRSA == V_PLUG:
        if PRSI == HANDS:
            z.tell('Are you the little Dutch boy, then? Sorry, this is a big dam.\n')
            return True
        else:
            z.tell('With a ', z.D(PRSI), '? Do you know how big this dam is? You could only stop a tiny leak with that.\n')
            return True
    return False


def with_tell(obj=0):
    z.tell('With a ', z.D(obj), '?\n')
    return True


def reservoir_south_fcn(rarg=0):
    if rarg == M_LOOK:
        if LOW_TIDE and GATES_OPEN:
            z.tell('You are in a long room, to the north of which was formerly a lake. However, with the water level lowered, there is merely a wide stream running through the center of the room.')
        elif GATES_OPEN:
            z.tell('You are in a long room. To the north is a large lake, too deep to cross. You notice, however, that the water level appears to be dropping at a rapid rate. Before long, it might be possible to cross to the other side from here.')
        elif LOW_TIDE:
            z.tell('You are in a long room, to the north of which is a wide area which was formerly a reservoir, but now is merely a stream. You notice, however, that the level of the stream is rising quickly and that before long it will be impossible to cross here.')
        else:
            z.tell('You are in a long room on the south shore of a large lake, far too deep and wide for crossing.')
        z.crlf()
        z.tell('There is a path along the stream to the east or west, a steep pathway climbing southwest along the edge of a chasm, and a path leading into a canyon to the southeast.\n')
        return True
    return False


def reservoir_fcn(rarg=0):
    if (rarg == M_END) and (not z.fset_p(z.loc(WINNER), VEHBIT)) and (not GATES_OPEN) and LOW_TIDE:
        z.tell('You notice that the water level here is rising rapidly. The currents are also becoming stronger. Staying here seems quite perilous!\n')
        return True
    elif rarg == M_LOOK:
        if LOW_TIDE:
            z.tell('You are on what used to be a large lake, but which is now a large mud pile. There are "shores" to the north and south.')
        else:
            z.tell('You are on the lake. Beaches can be seen north and south. Upstream a small stream enters the lake through a narrow cleft in the rocks. The dam can be seen downstream.')
        return z.crlf()
    return False


def reservoir_north_fcn(rarg=0):
    if rarg == M_LOOK:
        if LOW_TIDE and GATES_OPEN:
            z.tell('You are in a large cavernous room, the south of which was formerly a lake. However, with the water level lowered, there is merely a wide stream running through there.')
        elif GATES_OPEN:
            z.tell('You are in a large cavernous area. To the south is a wide lake, whose water level appears to be falling rapidly.')
        elif LOW_TIDE:
            z.tell('You are in a cavernous area, to the south of which is a very wide stream. The level of the stream is rising rapidly, and it appears that before long it will be impossible to cross to the other side.')
        else:
            z.tell('You are in a large cavernous room, north of a large lake.')
        z.crlf()
        z.tell('There is a slimy stairway leaving the room to the north.\n')
        return True
    return False


def bottle_function():
    e_p = False
    if (PRSA == V_THROW) and (PRSO == BOTTLE):
        remove_carefully(PRSO)
        e_p = True
        z.tell('The bottle hits the far wall and shatters.\n')
    elif PRSA == V_MUNG:
        e_p = True
        remove_carefully(PRSO)
        z.tell('A brilliant maneuver destroys the bottle.\n')
    elif PRSA == V_SHAKE:
        if z.fset_p(PRSO, OPENBIT) and z.in_p(WATER, PRSO):
            e_p = True
    if e_p and z.in_p(WATER, PRSO):
        z.tell('The water spills to the floor and evaporates.\n')
        remove_carefully(WATER)
        return True
    elif e_p:
        return True
    return False


def cyclops_fcn():
    global CYCLOPS_FLAG, CYCLOWRATH, WINNER
    count = 0
    count = CYCLOWRATH
    if WINNER == CYCLOPS:
        if CYCLOPS_FLAG:
            z.tell("No use talking to him. He's fast asleep.\n")
            return True
        elif PRSA == V_ODYSSEUS:
            WINNER = ADVENTURER
            perform(V_ODYSSEUS)
            return True
        else:
            z.tell('The cyclops prefers eating to making conversation.\n')
            return True
    elif CYCLOPS_FLAG:
        if PRSA == V_EXAMINE:
            z.tell('The cyclops is sleeping like a baby, albeit a very ugly one.\n')
            return True
        elif PRSA in (V_ALARM, V_KICK, V_ATTACK, V_BURN, V_MUNG):
            z.tell('The cyclops yawns and stares at the thing that woke him up.\n')
            CYCLOPS_FLAG = False
            z.fset(CYCLOPS, FIGHTBIT)
            if count < 0:
                CYCLOWRATH = -count
                return CYCLOWRATH
            else:
                CYCLOWRATH = count
                return CYCLOWRATH
    elif PRSA == V_EXAMINE:
        z.tell('A hungry cyclops is standing at the foot of the stairs.\n')
        return True
    elif (PRSA == V_GIVE) and (PRSI == CYCLOPS):
        if PRSO == LUNCH:
            if not (count < 0):
                remove_carefully(LUNCH)
                z.tell('The cyclops says "Mmm Mmm. I love hot peppers! But oh, could I use a drink. Perhaps I could drink the blood of that thing."  From the gleam in his eye, it could be surmised that you are "that thing".\n')
                CYCLOWRATH = min(-1, (-count))
            return z.put(queue(z.rtn(i_cyclops), -1), C_ENABLED_P, 1)
        elif (PRSO == WATER) or ((PRSO == BOTTLE) and z.in_p(WATER, BOTTLE)):
            if count < 0:
                remove_carefully(WATER)
                z.move(BOTTLE, HERE)
                z.fset(BOTTLE, OPENBIT)
                z.fclear(CYCLOPS, FIGHTBIT)
                z.tell("The cyclops takes the bottle, checks that it's open, and drinks the water. A moment later, he lets out a yawn that nearly blows you over, and then falls fast asleep (what did you put in that drink, anyway?).\n")
                CYCLOPS_FLAG = True
                return CYCLOPS_FLAG
            else:
                z.tell('The cyclops apparently is not thirsty and refuses your generous offer.\n')
                return True
        elif PRSO == GARLIC:
            z.tell('The cyclops may be hungry, but there is a limit.\n')
            return True
        else:
            z.tell('The cyclops is not so stupid as to eat THAT!\n')
            return True
    elif PRSA in (V_THROW, V_ATTACK, V_MUNG):
        z.put(queue(z.rtn(i_cyclops), -1), C_ENABLED_P, 1)
        if PRSA == V_MUNG:
            z.tell('"Do you think I\'m as stupid as my father was?", he says, dodging.\n')
            return True
        else:
            z.tell('The cyclops shrugs but otherwise ignores your pitiful attempt.\n')
            if PRSA == V_THROW:
                z.move(PRSO, HERE)
            return True
    elif PRSA == V_TAKE:
        z.tell("The cyclops doesn't take kindly to being grabbed.\n")
        return True
    elif PRSA == V_TIE:
        z.tell('You cannot tie the cyclops, though he is fit to be tied.\n')
        return True
    elif PRSA == V_LISTEN:
        z.tell('You can hear his stomach rumbling.\n')
        return True
    return False


def i_cyclops():
    global CYCLOWRATH
    if CYCLOPS_FLAG or DEAD:
        return True
    elif HERE != CYCLOPS_ROOM:
        return z.put(int_(z.rtn(i_cyclops)), C_ENABLED_P, 0)
    else:
        if abs(CYCLOWRATH) > 5:
            z.put(int_(z.rtn(i_cyclops)), C_ENABLED_P, 0)
            return jigs_up('The cyclops, tired of all of your games and trickery, grabs you firmly. As he licks his chops, he says "Mmm. Just like Mom used to make \'em." It\'s nice to be appreciated.')
        else:
            if CYCLOWRATH < 0:
                CYCLOWRATH = CYCLOWRATH - 1
            else:
                CYCLOWRATH = CYCLOWRATH + 1
            if not CYCLOPS_FLAG:
                z.tell(z.S(z.get(CYCLOMAD, (abs(CYCLOWRATH) - 1))), '\n')
                return True
    return False


def cyclops_room_fcn(rarg=0):
    if rarg == M_LOOK:
        z.tell('This room has an exit on the northwest, and a staircase leading up.\n')
        if CYCLOPS_FLAG and (not MAGIC_FLAG):
            z.tell('The cyclops is sleeping blissfully at the foot of the stairs.\n')
            return True
        elif MAGIC_FLAG:
            z.tell('The east wall, previously solid, now has a cyclops-sized opening in it.\n')
            return True
        elif CYCLOWRATH == 0:
            z.tell('A cyclops, who looks prepared to eat horses (much less mere adventurers), blocks the staircase. From his state of health, and the bloodstains on the walls, you gather that he is not very friendly, though he likes people.\n')
            return True
        elif CYCLOWRATH > 0:
            z.tell("The cyclops is standing in the corner, eyeing you closely. I don't think he likes you very much. He looks extremely hungry, even for a cyclops.\n")
            return True
        elif CYCLOWRATH < 0:
            z.tell('The cyclops, having eaten the hot peppers, appears to be gasping. His enflamed tongue protrudes from his man-sized mouth.\n')
            return True
    elif rarg == M_ENTER:
        return (CYCLOWRATH == 0) or z.put(int_(z.rtn(i_cyclops)), C_ENABLED_P, 1)
    return False


def loud_room_fcn(rarg=0):
    global LOUD_FLAG, P_CONT
    wrd = 0
    if rarg == M_LOOK:
        z.tell('This is a large room with a ceiling which cannot be detected from the ground. There is a narrow passage from east to west and a stone stairway leading upward.')
        if LOUD_FLAG or ((not GATES_OPEN) and LOW_TIDE):
            z.tell(' The room is eerie in its quietness.')
        else:
            z.tell(' The room is deafeningly loud with an undetermined rushing sound. The sound seems to reverberate from all of the walls, making it difficult even to think.')
        return z.crlf()
    elif (rarg == M_END) and GATES_OPEN and (not LOW_TIDE):
        z.tell("It is unbearably loud here, with an ear-splitting roar seeming to come from all around you. There is a pounding in your head which won't stop. With a tremendous effort, you scramble out of the room.\n\n")
        goto(pick_one(LOUD_RUNS))
        return False
    elif rarg == M_ENTER:
        if LOUD_FLAG or ((not GATES_OPEN) and LOW_TIDE):
            return False
        elif GATES_OPEN and (not LOW_TIDE):
            return False
        else:
            v_first_look()
            if P_CONT:
                z.tell('The rest of your commands have been lost in the noise.\n')
                P_CONT = False
            while True:
                if not SUPER_BRIEF:
                    z.crlf()
                z.tell('>')
                z.read(P_INBUF, P_LEXV)
                if z.getb(P_LEXV, P_LEXWORDS) == 0:
                    z.tell('I beg your pardon?\n')
                    continue
                wrd = z.get(P_LEXV, 1)
                if wrd in (W_GO, W_WALK, W_RUN):
                    wrd = z.get(P_LEXV, 3)
                elif wrd == W_SAY:
                    wrd = z.get(P_LEXV, 5)
                if wrd == W_SAVE:
                    v_save()
                elif wrd == W_RESTORE:
                    v_restore()
                elif wrd in (W_Q, W_QUIT):
                    v_quit()
                elif wrd in (W_W, W_WEST):
                    return goto(ROUND_ROOM)
                elif wrd in (W_E, W_EAST):
                    return goto(DAMP_CAVE)
                elif wrd in (W_U, W_UP):
                    return goto(DEEP_CANYON)
                elif wrd == W_BUG:
                    z.tell("That's only your opinion.\n")
                elif wrd == W_ECHO:
                    LOUD_FLAG = True
                    z.fclear(BAR, SACREDBIT)
                    z.tell('The acoustics of the room change subtly.\n')
                    if not SUPER_BRIEF:
                        z.crlf()
                    return True
                else:
                    v_echo()
    return False


def deep_canyon_f(rarg=0):
    if rarg == M_LOOK:
        z.tell('You are on the south edge of a deep canyon. Passages lead off to the east, northwest and southwest. A stairway leads down.')
        if GATES_OPEN and (not LOW_TIDE):
            z.tell(' You can hear a loud roaring sound, like that of rushing water, from below.')
        elif (not GATES_OPEN) and LOW_TIDE:
            z.crlf()
            return True
        else:
            z.tell(' You can hear the sound of flowing water from below.')
        return z.crlf()
    return False


def thief_vs_adventurer(here_p=0):
    global THIEF_HERE
    robbed_p = 0
    winner_robbed_p = False
    if (not DEAD) and (HERE == TREASURE_ROOM):
        pass
    elif not THIEF_HERE:
        if (not DEAD) and (not here_p) and (30 > z.random(100)):
            if z.in_p(STILETTO, THIEF):
                z.fclear(THIEF, INVISIBLE)
                z.tell('Someone carrying a large bag is casually leaning against one of the walls here. He does not speak, but it is clear from his aspect that the bag will be taken only over his dead body.\n')
                THIEF_HERE = True
                return True
        elif here_p and z.fset_p(THIEF, FIGHTBIT) and (not winning_p(THIEF)):
            z.tell('Your opponent, determining discretion to be the better part of valor, decides to terminate this little contretemps. With a rueful nod of his head, he steps backward into the gloom and disappears.\n')
            z.fset(THIEF, INVISIBLE)
            z.fclear(THIEF, FIGHTBIT)
            recover_stiletto()
            return True
        elif here_p and z.fset_p(THIEF, FIGHTBIT) and (90 > z.random(100)):
            return False
        elif here_p and (30 > z.random(100)):
            z.tell('The holder of the large bag just left, looking disgusted. Fortunately, he took nothing.\n')
            z.fset(THIEF, INVISIBLE)
            recover_stiletto()
            return True
        elif 70 > z.random(100):
            return False
        elif not DEAD:
            if rob(HERE, THIEF, 100):
                robbed_p = HERE
            elif rob(WINNER, THIEF):
                robbed_p = PLAYER
            THIEF_HERE = True
            if robbed_p and (not here_p):
                z.tell('A seedy-looking individual with a large bag just wandered through the room. On the way through, he quietly abstracted some valuables from ')
                if robbed_p == HERE:
                    z.tell('the room')
                else:
                    z.tell('your possession')
                z.tell(', mumbling something about "Doing unto others before..."\n')
                stole_light_p()
            elif here_p:
                recover_stiletto()
                if robbed_p:
                    z.tell('The thief just left, still carrying his large bag. You may not have noticed that he ')
                    if robbed_p == PLAYER:
                        z.tell('robbed you blind first.')
                    else:
                        z.tell('appropriated the valuables in the room.')
                    z.crlf()
                    stole_light_p()
                else:
                    z.tell('The thief, finding nothing of value, left disgusted.\n')
                z.fset(THIEF, INVISIBLE)
                here_p = False
                return True
            else:
                z.tell('A "lean and hungry" gentleman just wandered through, carrying a large bag. Finding nothing of value, he left disgruntled.\n')
                return True
    else:
        if here_p:
            if 30 > z.random(100):
                if rob(HERE, THIEF, 100):
                    robbed_p = HERE
                elif rob(WINNER, THIEF):
                    robbed_p = PLAYER
                if robbed_p:
                    z.tell('The thief just left, still carrying his large bag. You may not have noticed that he ')
                    if robbed_p == PLAYER:
                        z.tell('robbed you blind first.')
                    else:
                        z.tell('appropriated the valuables in the room.')
                    z.crlf()
                    stole_light_p()
                else:
                    z.tell('The thief, finding nothing of value, left disgusted.\n')
                z.fset(THIEF, INVISIBLE)
                here_p = False
                recover_stiletto()
    return False


def stole_light_p():
    global LIT
    old_lit = 0
    old_lit = LIT
    LIT = lit_p(HERE)
    if (not LIT) and old_lit:
        z.tell('The thief seems to have left you in the dark.\n')
    return True


def hack_treasures():
    x = 0
    recover_stiletto()
    z.fset(THIEF, INVISIBLE)
    x = z.first_p(TREASURE_ROOM)
    while True:
        if not x:
            return True
        else:
            z.fclear(x, INVISIBLE)
        x = z.next_p(x)
    return False


def deposit_booty(rm=0):
    global EGG_SOLVE
    x = 0
    n = 0
    flg = False
    x = z.first_p(THIEF)
    while True:
        if not x:
            return flg
        n = z.next_p(x)
        if x in (STILETTO, LARGE_BAG):
            pass
        elif z.getp(x, P_TVALUE) > 0:
            z.move(x, rm)
            flg = True
            if x == EGG:
                EGG_SOLVE = True
                z.fset(EGG, OPENBIT)
        x = n
    return False


def rob_maze(rm=0):
    x = 0
    n = 0
    x = z.first_p(rm)
    while True:
        if not x:
            return False
        n = z.next_p(x)
        if z.fset_p(x, TAKEBIT) and (not z.fset_p(x, INVISIBLE)) and (40 > z.random(100)):
            z.tell('You hear, off in the distance, someone saying "My, I wonder what this fine ', z.D(x), ' is doing here."\n')
            if zprob(60):
                z.move(x, THIEF)
                z.fset(x, TOUCHBIT)
                z.fset(x, INVISIBLE)
            return True
        x = n
    return False


def robber_function(mode=False):
    global P_CONT, THIEF_ENGROSSED
    flg = False
    x = 0
    n = 0
    if PRSA == V_TELL:
        z.tell('The thief is a strong, silent type.\n')
        P_CONT = False
        return P_CONT
    elif not mode:
        if (PRSA == V_HELLO) and (z.getp(THIEF, P_LDESC) == ROBBER_U_DESC):
            z.tell('The thief, being temporarily incapacitated, is unable to acknowledge your greeting with his usual graciousness.\n')
            return True
        elif (PRSO == KNIFE) and (PRSA == V_THROW) and (not z.fset_p(THIEF, FIGHTBIT)):
            z.move(PRSO, HERE)
            if zprob(10):
                z.tell("You evidently frightened the robber, though you didn't hit him. He flees")
                z.remove(LARGE_BAG)
                x = False
                if z.in_p(STILETTO, THIEF):
                    z.remove(STILETTO)
                    x = True
                if z.first_p(THIEF):
                    move_all(THIEF, HERE)
                    z.tell(', but the contents of his bag fall on the floor.')
                else:
                    z.tell('.')
                z.move(LARGE_BAG, THIEF)
                if x:
                    z.move(STILETTO, THIEF)
                z.crlf()
                return z.fset(THIEF, INVISIBLE)
            else:
                z.tell('You missed. The thief makes no attempt to take the knife, though it would be a fine addition to the collection in his bag. He does seem angered by your attempt.\n')
                return z.fset(THIEF, FIGHTBIT)
        elif (PRSA in (V_THROW, V_GIVE)) and PRSO and (PRSO != THIEF) and (PRSI == THIEF):
            if z.getp(THIEF, P_STRENGTH) < 0:
                z.putp(THIEF, P_STRENGTH, (-z.getp(THIEF, P_STRENGTH)))
                z.put(int_(z.rtn(i_thief)), C_ENABLED_P, 1)
                recover_stiletto()
                z.putp(THIEF, P_LDESC, ROBBER_C_DESC)
                z.tell('Your proposed victim suddenly recovers consciousness.\n')
            z.move(PRSO, THIEF)
            if z.getp(PRSO, P_TVALUE) > 0:
                THIEF_ENGROSSED = True
                z.tell('The thief is taken aback by your unexpected generosity, but accepts the ', z.D(PRSO), ' and stops to admire its beauty.\n')
                return True
            else:
                z.tell('The thief places the ', z.D(PRSO), ' in his bag and thanks you politely.\n')
                return True
        elif PRSA == V_TAKE:
            z.tell('Once you got him, what would you do with him?\n')
            return True
        elif PRSA in (V_EXAMINE, V_LOOK_INSIDE):
            z.tell("The thief is a slippery character with beady eyes that flit back and forth. He carries, along with an unmistakable arrogance, a large bag over his shoulder and a vicious stiletto, whose blade is aimed menacingly in your direction. I'd watch out if I were you.\n")
            return True
        elif PRSA == V_LISTEN:
            z.tell('The thief says nothing, as you have not been formally introduced.\n')
            return True
    elif mode == F_BUSY_P:
        if z.in_p(STILETTO, THIEF):
            return False
        elif z.in_p(STILETTO, z.loc(THIEF)):
            z.move(STILETTO, THIEF)
            z.fset(STILETTO, NDESCBIT)
            if z.in_p(THIEF, HERE):
                z.tell('The robber, somewhat surprised at this turn of events, nimbly retrieves his stiletto.\n')
            return True
    elif mode == F_DEAD:
        z.move(STILETTO, HERE)
        z.fclear(STILETTO, NDESCBIT)
        x = deposit_booty(HERE)
        if HERE == TREASURE_ROOM:
            x = z.first_p(HERE)
            while True:
                if not x:
                    z.tell('The chalice is now safe to take.\n')
                    break
                elif not (x in (CHALICE, THIEF, ADVENTURER)):
                    z.fclear(x, INVISIBLE)
                    if not flg:
                        flg = True
                        z.tell('As the thief dies, the power of his magic decreases, and his treasures reappear:\n')
                    z.tell('  A ', z.D(x))
                    if z.first_p(x) and see_inside_p(x):
                        z.tell(', with ')
                        print_contents(x)
                    z.crlf()
                x = z.next_p(x)
        elif x:
            z.tell('His booty remains.\n')
        return z.put(int_(z.rtn(i_thief)), C_ENABLED_P, 0)
    elif mode == F_FIRST_P:
        if THIEF_HERE and (not z.fset_p(THIEF, INVISIBLE)) and (20 > z.random(100)):
            z.fset(THIEF, FIGHTBIT)
            P_CONT = False
            return True
    elif mode == F_UNCONSCIOUS:
        z.put(int_(z.rtn(i_thief)), C_ENABLED_P, 0)
        z.fclear(THIEF, FIGHTBIT)
        z.move(STILETTO, HERE)
        z.fclear(STILETTO, NDESCBIT)
        return z.putp(THIEF, P_LDESC, ROBBER_U_DESC)
    elif mode == F_CONSCIOUS:
        if z.loc(THIEF) == HERE:
            z.fset(THIEF, FIGHTBIT)
            z.tell('The robber revives, briefly feigning continued unconsciousness, and, when he sees his moment, scrambles away from you.\n')
        z.put(int_(z.rtn(i_thief)), C_ENABLED_P, 1)
        z.putp(THIEF, P_LDESC, ROBBER_C_DESC)
        return recover_stiletto()
    return False


def large_bag_f():
    if PRSA == V_TAKE:
        if z.getp(THIEF, P_LDESC) == ROBBER_U_DESC:
            z.tell('Sadly for you, the robber collapsed on top of the bag. Trying to take it would wake him.\n')
            return True
        else:
            z.tell('The bag will be taken over his dead body.\n')
            return True
    elif (PRSA == V_PUT) and (PRSI == LARGE_BAG):
        z.tell('It would be a good trick.\n')
        return True
    elif PRSA in (V_OPEN, V_CLOSE):
        z.tell('Getting close enough would be a good trick.\n')
        return True
    elif PRSA in (V_EXAMINE, V_LOOK_INSIDE):
        z.tell("The bag is underneath the thief, so one can't say what, if anything, is inside.\n")
        return True
    return False


def move_all(from_=0, to=0):
    x = 0
    n = 0
    if (x := z.first_p(from_)):
        while True:
            if not x:
                return True
            n = z.next_p(x)
            z.fclear(x, INVISIBLE)
            z.move(x, to)
            x = n
    return False


def chalice_fcn():
    if PRSA == V_TAKE:
        if z.in_p(PRSO, TREASURE_ROOM) and z.in_p(THIEF, TREASURE_ROOM) and z.fset_p(THIEF, FIGHTBIT) and (not z.fset_p(THIEF, INVISIBLE)) and (z.getp(THIEF, P_LDESC) != ROBBER_U_DESC):
            z.tell("You'd be stabbed in the back first.\n")
            return True
    elif (PRSA == V_PUT) and (PRSI == CHALICE):
        z.tell("You can't. It's not a very good chalice, is it?\n")
        return True
    else:
        return dumb_container()
    return False


def treasure_room_fcn(rarg=0):
    tl = 0
    if (rarg == M_ENTER) and (z.get(int_(z.rtn(i_thief)), C_ENABLED_P) == 1) and (not DEAD):
        if not z.in_p(THIEF, HERE):
            z.tell("You hear a scream of anguish as you violate the robber's hideaway. Using passages unknown to you, he rushes to its defense.\n")
            z.move(THIEF, HERE)
        z.fset(THIEF, FIGHTBIT)
        z.fclear(THIEF, INVISIBLE)
        return thief_in_treasure()
    return False


def thief_in_treasure():
    f = 0
    n = 0
    f = z.first_p(HERE)
    if f and z.next_p(f):
        z.tell('The thief gestures mysteriously, and the treasures in the room suddenly vanish.\n\n')
    while True:
        if not f:
            return True
        elif not (f in (CHALICE, THIEF)):
            z.fset(f, INVISIBLE)
        f = z.next_p(f)
    return False


def front_door_fcn():
    if PRSA == V_OPEN:
        z.tell('The door cannot be opened.\n')
        return True
    elif PRSA == V_BURN:
        z.tell('You cannot burn this door.\n')
        return True
    elif PRSA == V_MUNG:
        z.tell("You can't seem to damage the door.\n")
        return True
    elif PRSA == V_LOOK_BEHIND:
        z.tell("It won't open.\n")
        return True
    return False


def body_function():
    if PRSA == V_TAKE:
        z.tell('A force keeps you from taking the bodies.\n')
        return True
    elif PRSA in (V_MUNG, V_BURN):
        return jigs_up('The voice of the guardian of the dungeon booms out from the darkness, "Your disrespect costs you your life!" and places your head on a sharp pole.')
    return False


def black_book():
    if PRSA == V_OPEN:
        z.tell('The book is already open to page 569.\n')
        return True
    elif PRSA == V_CLOSE:
        z.tell('As hard as you try, the book cannot be closed.\n')
        return True
    elif (PRSA == V_TURN) or ((PRSA == V_READ_PAGE) and (PRSI == INTNUM) and (P_NUMBER != 569)):
        z.tell('Beside page 569, there is only one other page with any legible printing on it. Most of it is unreadable, but the subject seems to be the banishment of evil. Apparently, certain noises, lights, and prayers are efficacious in this regard.\n')
        return True
    elif PRSA == V_BURN:
        remove_carefully(PRSO)
        return jigs_up('A booming voice says "Wrong, cretin!" and you notice that you have turned into a pile of dust. How, I can\'t imagine.')
    return False


def painting_fcn():
    if PRSA == V_MUNG:
        z.putp(PRSO, P_TVALUE, 0)
        z.putp(PRSO, P_LDESC, 'There is a worthless piece of canvas here.')
        z.tell("Congratulations! Unlike the other vandals, who merely stole the artist's masterpieces, you have destroyed one.\n")
        return True
    return False


def lantern():
    if PRSA == V_THROW:
        z.tell('The lamp has smashed into the floor, and the light has gone out.\n')
        z.put(int_(z.rtn(i_lantern)), C_ENABLED_P, 0)
        remove_carefully(LAMP)
        return z.move(BROKEN_LAMP, HERE)
    elif PRSA == V_LAMP_ON:
        if z.fset_p(LAMP, RMUNGBIT):
            z.tell("A burned-out lamp won't light.\n")
            return True
        else:
            z.put(int_(z.rtn(i_lantern)), C_ENABLED_P, 1)
            return False
    elif PRSA == V_LAMP_OFF:
        if z.fset_p(LAMP, RMUNGBIT):
            z.tell('The lamp has already burned out.\n')
            return True
        else:
            z.put(int_(z.rtn(i_lantern)), C_ENABLED_P, 0)
            return False
    elif PRSA == V_EXAMINE:
        z.tell('The lamp ')
        if z.fset_p(LAMP, RMUNGBIT):
            z.tell('has burned out.')
        elif z.fset_p(LAMP, ONBIT):
            z.tell('is on.')
        else:
            z.tell('is turned off.')
        return z.crlf()
    return False


def mailbox_f():
    if (PRSA == V_TAKE) and (PRSO == MAILBOX):
        z.tell('It is securely anchored.\n')
        return True
    return False


def match_function():
    global LIT, MATCH_COUNT
    cnt = 0
    if (PRSA in (V_LAMP_ON, V_BURN)) and (PRSO == MATCH):
        if MATCH_COUNT > 0:
            MATCH_COUNT = MATCH_COUNT - 1
        if not (MATCH_COUNT > 0):
            z.tell("I'm afraid that you have run out of matches.\n")
            return True
        elif HERE in (LOWER_SHAFT, TIMBER_ROOM):
            z.tell('This room is drafty, and the match goes out instantly.\n')
            return True
        else:
            z.fset(MATCH, FLAMEBIT)
            z.fset(MATCH, ONBIT)
            z.put(queue(z.rtn(i_match), 2), C_ENABLED_P, 1)
            z.tell('One of the matches starts to burn.\n')
            if not LIT:
                LIT = True
                v_look()
            return True
    elif (PRSA == V_LAMP_OFF) and z.fset_p(MATCH, FLAMEBIT):
        z.tell('The match is out.\n')
        z.fclear(MATCH, FLAMEBIT)
        z.fclear(MATCH, ONBIT)
        LIT = lit_p(HERE)
        if not LIT:
            z.tell("It's pitch black in here!\n")
        queue(z.rtn(i_match), 0)
        return True
    elif PRSA in (V_COUNT, V_OPEN):
        z.tell('You have ')
        cnt = MATCH_COUNT - 1
        if not (cnt > 0):
            z.tell('no')
        else:
            z.tell(z.N(cnt))
        z.tell(' match')
        if not (cnt == 1):
            z.tell('es.')
        else:
            z.tell('.')
        return z.crlf()
    elif PRSA == V_EXAMINE:
        if z.fset_p(MATCH, ONBIT):
            z.tell('The match is burning.')
        else:
            z.tell("The matchbook isn't very interesting, except for what's written on it.")
        return z.crlf()
    return False


def i_match():
    global LIT
    z.tell('The match has gone out.\n')
    z.fclear(MATCH, FLAMEBIT)
    z.fclear(MATCH, ONBIT)
    LIT = lit_p(HERE)
    return True


def i_lantern():
    global LAMP_TABLE
    tick = 0
    tbl = LAMP_TABLE
    z.put(queue(z.rtn(i_lantern), (tick := z.get(tbl, 0))), C_ENABLED_P, 1)
    light_int(LAMP, tbl, tick)
    if not (tick == 0):
        LAMP_TABLE = tbl + 4
        return LAMP_TABLE
    return False


def i_candles():
    global CANDLE_TABLE
    tick = 0
    tbl = CANDLE_TABLE
    z.fset(CANDLES, TOUCHBIT)
    z.put(queue(z.rtn(i_candles), (tick := z.get(tbl, 0))), C_ENABLED_P, 1)
    light_int(CANDLES, tbl, tick)
    if not (tick == 0):
        CANDLE_TABLE = tbl + 4
        return CANDLE_TABLE
    return False


def light_int(obj=0, tbl=0, tick=0):
    if tick == 0:
        z.fclear(obj, ONBIT)
        z.fset(obj, RMUNGBIT)
    if held_p(obj) or z.in_p(obj, HERE):
        if tick == 0:
            z.tell("You'd better have more light than from the ", z.D(obj), '.\n')
            return True
        else:
            z.tell(z.S(z.get(tbl, 1)), '\n')
            return True
    return False


def min_(n1=0, n2=0):
    if n1 < n2:
        return n1
    else:
        return n2
    return False


def candles_fcn():
    global LIT
    if not z.fset_p(CANDLES, TOUCHBIT):
        z.put(int_(z.rtn(i_candles)), C_ENABLED_P, 1)
    if CANDLES == PRSI:
        return False
    else:
        if PRSA in (V_LAMP_ON, V_BURN):
            if z.fset_p(CANDLES, RMUNGBIT):
                z.tell("Alas, there's not much left of the candles. Certainly not enough to burn.\n")
                return True
            elif not PRSI:
                if z.fset_p(MATCH, FLAMEBIT):
                    z.tell('(with the match)\n')
                    perform(V_LAMP_ON, CANDLES, MATCH)
                    return True
                else:
                    z.tell('You should say what to light them with.\n')
                    return 2
            elif (PRSI == MATCH) and z.fset_p(MATCH, ONBIT):
                z.tell('The candles are ')
                if z.fset_p(CANDLES, ONBIT):
                    z.tell('already lit.\n')
                    return True
                else:
                    z.fset(CANDLES, ONBIT)
                    z.tell('lit.\n')
                    return z.put(int_(z.rtn(i_candles)), C_ENABLED_P, 1)
            elif PRSI == TORCH:
                if z.fset_p(CANDLES, ONBIT):
                    z.tell('You realize, just in time, that the candles are already lighted.\n')
                    return True
                else:
                    z.tell('The heat from the torch is so intense that the candles are vaporized.\n')
                    return remove_carefully(CANDLES)
            else:
                z.tell("You have to light them with something that's burning, you know.\n")
                return True
        elif PRSA == V_COUNT:
            z.tell("Let's see, how many objects in a pair? Don't tell me, I'll get it.\n")
            return True
        elif PRSA == V_LAMP_OFF:
            z.put(int_(z.rtn(i_candles)), C_ENABLED_P, 0)
            if z.fset_p(CANDLES, ONBIT):
                z.tell('The flame is extinguished.')
                z.fclear(CANDLES, ONBIT)
                z.fset(CANDLES, TOUCHBIT)
                LIT = lit_p(HERE)
                if not LIT:
                    z.tell(" It's really dark in here....")
                z.crlf()
                return True
            else:
                z.tell('The candles are not lighted.\n')
                return True
        elif (PRSA == V_PUT) and z.fset_p(PRSI, BURNBIT):
            z.tell("That wouldn't be smart.\n")
            return True
        elif PRSA == V_EXAMINE:
            z.tell('The candles are ')
            if z.fset_p(CANDLES, ONBIT):
                z.tell('burning.')
            else:
                z.tell('out.')
            return z.crlf()
    return False


def cave2_room(rarg=0):
    global LIT
    if rarg == M_END:
        if z.in_p(CANDLES, WINNER) and zprob(50) and z.fset_p(CANDLES, ONBIT):
            z.put(int_(z.rtn(i_candles)), C_ENABLED_P, 0)
            z.fclear(CANDLES, ONBIT)
            z.tell('A gust of wind blows out your candles!\n')
            if not (LIT := lit_p(HERE)):
                z.tell('It is now completely dark.\n')
                return True
    return False


def sword_fcn():
    g = 0
    if (PRSA == V_TAKE) and (WINNER == ADVENTURER):
        z.put(queue(z.rtn(i_sword), -1), C_ENABLED_P, 1)
        return False
    elif PRSA == V_EXAMINE:
        if (g := z.getp(SWORD, P_TVALUE)) == 1:
            z.tell('Your sword is glowing with a faint blue glow.\n')
            return True
        elif g == 2:
            z.tell('Your sword is glowing very brightly.\n')
            return True
    return False


def boom_room(rarg=0):
    dummy_p = False
    flame = 0
    if rarg == M_END:
        if (rarg == M_END) and (PRSA in (V_LAMP_ON, V_BURN)) and (PRSO in (CANDLES, TORCH, MATCH)):
            dummy_p = True
        if (held_p(CANDLES) and z.fset_p(CANDLES, ONBIT)) or (held_p(TORCH) and z.fset_p(TORCH, ONBIT)) or (held_p(MATCH) and z.fset_p(MATCH, ONBIT)):
            if dummy_p:
                z.tell('How sad for an aspiring adventurer to light a ', z.D(PRSO), ' in a room which reeks of gas. Fortunately, there is justice in the world.\n')
            else:
                z.tell('Oh dear. It appears that the smell coming from this room was coal gas. I would have thought twice about carrying flaming objects in here.\n')
            return jigs_up('\n      ** BOOOOOOOOOOOM **')
    return False


def bat_d(foo=0):
    if z.loc(GARLIC) in (WINNER, HERE):
        z.tell('In the corner of the room on the ceiling is a large vampire bat who is obviously deranged and holding his nose.\n')
        return True
    else:
        z.tell('A large vampire bat, hanging from the ceiling, swoops down at you!\n')
        return True
    return False


def bats_room(rarg=0):
    if rarg == M_LOOK:
        z.tell('You are in a small room which has doors only to the east and south.\n')
        return True
    elif (rarg == M_ENTER) and (not DEAD):
        if not (z.loc(GARLIC) in (WINNER, HERE)):
            v_look()
            z.crlf()
            return fly_me()
    return False


def machine_room_fcn(rarg=0):
    if rarg == M_LOOK:
        z.tell('This is a large, cold room whose sole exit is to the north. In one corner there is a machine which is reminiscent of a clothes dryer. On its face is a switch which is labelled "START". The switch does not appear to be manipulable by any human hand (unless the fingers are about 1/16 by 1/4 inch). On the front of the machine is a large lid, which is ')
        if z.fset_p(MACHINE, OPENBIT):
            z.tell('open.')
        else:
            z.tell('closed.')
        return z.crlf()
    return False


def machine_f():
    if (PRSA == V_TAKE) and (PRSO == MACHINE):
        z.tell('It is far too large to carry.\n')
        return True
    elif PRSA == V_OPEN:
        if z.fset_p(MACHINE, OPENBIT):
            _t1 = z.S(pick_one(DUMMY))
            z.tell(_t1, '\n')
            return True
        elif z.first_p(MACHINE):
            z.tell('The lid opens, revealing ')
            print_contents(MACHINE)
            z.tell('.\n')
            return z.fset(MACHINE, OPENBIT)
        else:
            z.tell('The lid opens.\n')
            return z.fset(MACHINE, OPENBIT)
    elif PRSA == V_CLOSE:
        if z.fset_p(MACHINE, OPENBIT):
            z.tell('The lid closes.\n')
            z.fclear(MACHINE, OPENBIT)
            return True
        else:
            _t2 = z.S(pick_one(DUMMY))
            z.tell(_t2, '\n')
            return True
    elif PRSA == V_LAMP_ON:
        if not PRSI:
            z.tell("It's not clear how to turn it on with your bare hands.\n")
            return True
        else:
            perform(V_TURN, MACHINE_SWITCH, PRSI)
            return True
    return False


def mswitch_function():
    o = 0
    if PRSA == V_TURN:
        if PRSI == SCREWDRIVER:
            if z.fset_p(MACHINE, OPENBIT):
                z.tell("The machine doesn't seem to want to do anything.\n")
                return True
            else:
                z.tell('The machine comes to life (figuratively) with a dazzling display of colored lights and bizarre noises. After a few moments, the excitement abates.\n')
                if z.in_p(COAL, MACHINE):
                    remove_carefully(COAL)
                    return z.move(DIAMOND, MACHINE)
                else:
                    while True:
                        if (o := z.first_p(MACHINE)):
                            remove_carefully(o)
                        else:
                            break
                    return z.move(GUNK, MACHINE)
        else:
            z.tell('It seems that a ', z.D(PRSI), " won't do.\n")
            return True
    return False


def gunk_function():
    remove_carefully(GUNK)
    z.tell('The slag was rather insubstantial, and crumbles into dust at your touch.\n')
    return True


def no_objs(rarg=0):
    global EMPTY_HANDED, LIGHT_SHAFT
    f = 0
    if rarg == M_BEG:
        f = z.first_p(WINNER)
        EMPTY_HANDED = True
        while True:
            if not f:
                break
            elif weight(f) > 4:
                EMPTY_HANDED = False
                break
            f = z.next_p(f)
        if (HERE == LOWER_SHAFT) and LIT:
            score_upd(LIGHT_SHAFT)
            LIGHT_SHAFT = 0
        return False
    return False


def south_temple_fcn(rarg=0):
    global COFFIN_CURE
    if rarg == M_BEG:
        COFFIN_CURE = not z.in_p(COFFIN, WINNER)
        return False
    return False


def white_cliffs_function(rarg=0):
    global DEFLATE
    if rarg == M_END:
        if z.in_p(INFLATED_BOAT, WINNER):
            DEFLATE = False
            return DEFLATE
        else:
            DEFLATE = True
            return DEFLATE
    return False


def sceptre_function():
    global RAINBOW_FLAG
    if PRSA in (V_WAVE, V_RAISE):
        if (HERE == ARAGAIN_FALLS) or (HERE == END_OF_RAINBOW):
            if not RAINBOW_FLAG:
                z.fclear(POT_OF_GOLD, INVISIBLE)
                z.tell('Suddenly, the rainbow appears to become solid and, I venture, walkable (I think the giveaway was the stairs and bannister).\n')
                if (HERE == END_OF_RAINBOW) and z.in_p(POT_OF_GOLD, END_OF_RAINBOW):
                    z.tell('A shimmering pot of gold appears at the end of the rainbow.\n')
                RAINBOW_FLAG = True
                return RAINBOW_FLAG
            else:
                rob(ON_RAINBOW, WALL)
                z.tell('The rainbow seems to have become somewhat run-of-the-mill.\n')
                RAINBOW_FLAG = False
                return True
        elif HERE == ON_RAINBOW:
            RAINBOW_FLAG = False
            return jigs_up('The structural integrity of the rainbow is severely compromised, leaving you hanging in midair, supported only by water vapor. Bye.')
        else:
            z.tell('A dazzling display of color briefly emanates from the sceptre.\n')
            return True
    return False


def falls_room(rarg=0):
    if rarg == M_LOOK:
        z.tell('You are at the top of Aragain Falls, an enormous waterfall with a drop of about 450 feet. The only path here is on the north end.\n')
        if RAINBOW_FLAG:
            z.tell('A solid rainbow spans the falls.')
        else:
            z.tell('A beautiful rainbow can be seen over the falls and to the west.')
        return z.crlf()
    return False


def rainbow_fcn():
    if PRSA in (V_CROSS, V_THROUGH):
        if HERE == CANYON_VIEW:
            z.tell('From here?!?\n')
            return True
        if RAINBOW_FLAG:
            if HERE == ARAGAIN_FALLS:
                return goto(END_OF_RAINBOW)
            elif HERE == END_OF_RAINBOW:
                return goto(ARAGAIN_FALLS)
            else:
                z.tell("You'll have to say which way...\n")
                return True
        else:
            z.tell('Can you walk on water vapor?\n')
            return True
    elif PRSA == V_LOOK_UNDER:
        z.tell('The Frigid River flows under the rainbow.\n')
        return True
    return False


def dboat_function():
    if (PRSA in (V_PUT, V_PUT_ON)) and (PRSO == PUTTY):
        return fix_boat()
    elif PRSA in (V_INFLATE, V_FILL):
        z.tell('No chance. Some moron punctured it.\n')
        return True
    elif PRSA == V_PLUG:
        if PRSI == PUTTY:
            return fix_boat()
        else:
            return with_tell(PRSI)
    return False


def fix_boat():
    z.tell('Well done. The boat is repaired.\n')
    z.move(INFLATABLE_BOAT, z.loc(PUNCTURED_BOAT))
    return remove_carefully(PUNCTURED_BOAT)


def river_function():
    if PRSA == V_PUT:
        if PRSI == RIVER:
            if PRSO == ME:
                return jigs_up('You splash around for a while, fighting the current, then you drown.')
            elif PRSO == INFLATED_BOAT:
                z.tell('You should get in the boat then launch it.\n')
                return True
            elif z.fset_p(PRSO, BURNBIT):
                remove_carefully(PRSO)
                z.tell('The ', z.D(PRSO), ' floats for a moment, then sinks.\n')
                return True
            else:
                remove_carefully(PRSO)
                z.tell('The ', z.D(PRSO), ' splashes into the water and is gone forever.\n')
                return True
    elif PRSA in (V_LEAP, V_THROUGH):
        z.tell('A look before leaping reveals that the river is wide and dangerous, with swift currents and large, half-hidden rocks. You decide to forgo your swim.\n')
        return True
    return False


def i_river():
    rm = 0
    if (not (HERE in (RIVER_1, RIVER_2, RIVER_3))) and (not (HERE in (RIVER_4, RIVER_5))):
        return z.put(int_(z.rtn(i_river)), C_ENABLED_P, 0)
    elif (rm := lkp(HERE, RIVER_NEXT)):
        z.tell('The flow of the river carries you downstream.\n\n')
        goto(rm)
        return z.put(queue(z.rtn(i_river), lkp(HERE, RIVER_SPEEDS)), C_ENABLED_P, 1)
    else:
        return jigs_up("Unfortunately, the magic boat doesn't provide protection from the rocks and boulders one meets at the bottom of waterfalls. Including this one.")
    return False


def rboat_function(rarg=False):
    global DEFLATE
    tmp = 0
    if rarg in (M_ENTER, M_END, M_LOOK):
        return False
    elif rarg == M_BEG:
        if PRSA == V_WALK:
            if PRSO in (P_LAND, P_EAST, P_WEST):
                return False
            elif (HERE == RESERVOIR) and (PRSO in (P_NORTH, P_SOUTH)):
                return False
            elif (HERE == IN_STREAM) and (PRSO == P_SOUTH):
                return False
            else:
                z.tell("Read the label for the boat's instructions.\n")
                return True
        elif PRSA == V_LAUNCH:
            if (HERE in (RIVER_1, RIVER_2, RIVER_3)) or (HERE in (RIVER_4, RESERVOIR, IN_STREAM)):
                z.tell('You are on the ')
                if HERE == RESERVOIR:
                    z.tell('reservoir')
                elif HERE == IN_STREAM:
                    z.tell('stream')
                else:
                    z.tell('river')
                z.tell(', or have you forgotten?\n')
                return True
            elif (tmp := go_next(RIVER_LAUNCH)) == 1:
                z.put(queue(z.rtn(i_river), lkp(HERE, RIVER_SPEEDS)), C_ENABLED_P, 1)
                return True
            elif tmp != 2:
                z.tell("You can't launch it here.\n")
                return True
            else:
                return True
        elif ((PRSA == V_DROP) and z.fset_p(PRSO, WEAPONBIT)) or ((PRSA == V_PUT) and z.fset_p(PRSO, WEAPONBIT) and (PRSI == INFLATED_BOAT)) or ((PRSA in (V_ATTACK, V_MUNG)) and z.fset_p(PRSI, WEAPONBIT)):
            remove_carefully(INFLATED_BOAT)
            z.move(PUNCTURED_BOAT, HERE)
            rob(INFLATED_BOAT, HERE)
            z.move(WINNER, HERE)
            z.tell('It seems that the ')
            if PRSA in (V_DROP, V_PUT):
                z.tell(z.D(PRSO))
            else:
                z.tell(z.D(PRSI))
            z.tell(" didn't agree with the boat, as evidenced by the loud hissing noise issuing therefrom. With a pathetic sputter, the boat deflates, leaving you without.\n")
            if z.fset_p(HERE, NONLANDBIT):
                z.crlf()
                if HERE in (RESERVOIR, IN_STREAM):
                    jigs_up('Another pathetic sputter, this time from you, heralds your drowning.')
                else:
                    jigs_up('In other words, fighting the fierce currents of the Frigid River. You manage to hold your own for a bit, but then you are carried over a waterfall and into some nasty rocks. Ouch!')
            return True
        elif PRSA == V_LAUNCH:
            z.tell("You're not in the boat!\n")
            return True
    elif PRSA == V_BOARD:
        if z.in_p(SCEPTRE, WINNER) or z.in_p(KNIFE, WINNER) or z.in_p(SWORD, WINNER) or z.in_p(RUSTY_KNIFE, WINNER) or z.in_p(AXE, WINNER) or z.in_p(STILETTO, WINNER):
            z.tell('Oops! Something sharp seems to have slipped and punctured the boat. The boat deflates to the sounds of hissing, sputtering, and cursing.\n')
            remove_carefully(INFLATED_BOAT)
            z.move(PUNCTURED_BOAT, HERE)
            this_is_it(PUNCTURED_BOAT)
            return True
    elif PRSA in (V_INFLATE, V_FILL):
        z.tell('Inflating it further would probably burst it.\n')
        return True
    elif PRSA == V_DEFLATE:
        if z.loc(WINNER) == INFLATED_BOAT:
            z.tell("You can't deflate the boat while you're in it.\n")
            return True
        elif not z.in_p(INFLATED_BOAT, HERE):
            z.tell('The boat must be on the ground to be deflated.\n')
            return True
        else:
            z.tell('The boat deflates.\n')
            DEFLATE = True
            remove_carefully(INFLATED_BOAT)
            z.move(INFLATABLE_BOAT, HERE)
            return this_is_it(INFLATABLE_BOAT)
    return False


def breathe():
    return perform(V_INFLATE, PRSO, LUNGS)


def iboat_function():
    global DEFLATE
    if PRSA in (V_INFLATE, V_FILL):
        if not z.in_p(INFLATABLE_BOAT, HERE):
            z.tell('The boat must be on the ground to be inflated.\n')
            return True
        elif PRSI == PUMP:
            z.tell('The boat inflates and appears seaworthy.\n')
            if not z.fset_p(BOAT_LABEL, TOUCHBIT):
                z.tell('A tan label is lying inside the boat.\n')
            DEFLATE = False
            remove_carefully(INFLATABLE_BOAT)
            z.move(INFLATED_BOAT, HERE)
            return this_is_it(INFLATED_BOAT)
        elif PRSI == LUNGS:
            z.tell("You don't have enough lung power to inflate it.\n")
            return True
        else:
            z.tell('With a ', z.D(PRSI), '? Surely you jest!\n')
            return True
    return False


def rivr4_room(rarg=0):
    global BUOY_FLAG
    if rarg == M_END:
        if z.in_p(BUOY, WINNER) and BUOY_FLAG:
            z.tell('You notice something funny about the feel of the buoy.\n')
            BUOY_FLAG = False
            return BUOY_FLAG
    return False


def sand_function():
    global BEACH_DIG
    if (PRSA == V_DIG) and (PRSI == SHOVEL):
        BEACH_DIG = 1 + BEACH_DIG
        if BEACH_DIG > 3:
            BEACH_DIG = -1
            if z.in_p(SCARAB, HERE):
                z.fset(SCARAB, INVISIBLE)
            return jigs_up('The hole collapses, smothering you.')
        elif BEACH_DIG == 3:
            if z.fset_p(SCARAB, INVISIBLE):
                z.tell('You can see a scarab here in the sand.\n')
                this_is_it(SCARAB)
                return z.fclear(SCARAB, INVISIBLE)
        else:
            z.tell(z.S(z.get(BDIGS, BEACH_DIG)), '\n')
            return True
    return False


def tree_room(rarg=0):
    f = 0
    if rarg == M_LOOK:
        z.tell('You are about 10 feet above the ground nestled among some large branches. The nearest branch above you is above your reach.\n')
        if (f := z.first_p(PATH)) and z.next_p(f):
            z.tell('On the ground below you can see:  ')
            print_contents(PATH)
            z.tell('.\n')
            return True
    elif rarg == M_BEG:
        if (PRSA == V_CLIMB_DOWN) and (PRSO in (TREE, ROOMS)):
            return do_walk(P_DOWN)
        elif (PRSA in (V_CLIMB_UP, V_CLIMB_FOO)) and (PRSO == TREE):
            return do_walk(P_UP)
        elif PRSA == V_DROP:
            if not idrop():
                return True
            elif (PRSO == NEST) and z.in_p(EGG, NEST):
                z.tell('The nest falls to the ground, and the egg spills out of it, seriously damaged.\n')
                remove_carefully(EGG)
                return z.move(BROKEN_EGG, PATH)
            elif PRSO == EGG:
                z.tell('The egg falls to the ground and springs open, seriously damaged.')
                z.move(EGG, PATH)
                bad_egg()
                return z.crlf()
            elif not (PRSO in (WINNER, TREE)):
                z.move(PRSO, PATH)
                z.tell('The ', z.D(PRSO), ' falls to the ground.\n')
                return True
            elif PRSA == V_LEAP:
                return jigs_up('That was just a bit too far down.')
    elif rarg == M_ENTER:
        return z.put(queue(z.rtn(i_forest_room), -1), C_ENABLED_P, 1)
    return False


def egg_object():
    if (PRSA in (V_OPEN, V_MUNG)) and (PRSO == EGG):
        if z.fset_p(PRSO, OPENBIT):
            z.tell('The egg is already open.\n')
            return True
        elif not PRSI:
            z.tell('You have neither the tools nor the expertise.\n')
            return True
        elif PRSI == HANDS:
            z.tell('I doubt you could do that without damaging it.\n')
            return True
        elif z.fset_p(PRSI, WEAPONBIT) or z.fset_p(PRSI, TOOLBIT) or (PRSA == V_MUNG):
            z.tell('The egg is now open, but the clumsiness of your attempt has seriously compromised its esthetic appeal.')
            bad_egg()
            return z.crlf()
        elif z.fset_p(PRSO, FIGHTBIT):
            z.tell('Not to say that using the ', z.D(PRSI), " isn't original too...\n")
            return True
        else:
            z.tell('The concept of using a ', z.D(PRSI), ' is certainly original.\n')
            return z.fset(PRSO, FIGHTBIT)
    elif PRSA in (V_CLIMB_ON, V_HATCH):
        z.tell('There is a noticeable crunch from beneath you, and inspection reveals that the egg is lying open, badly damaged.')
        bad_egg()
        return z.crlf()
    elif PRSA in (V_OPEN, V_MUNG, V_THROW):
        if PRSA == V_THROW:
            z.move(PRSO, HERE)
        z.tell('Your rather indelicate handling of the egg has caused it some damage, although you have succeeded in opening it.')
        bad_egg()
        return z.crlf()
    return False


def bad_egg():
    l = 0
    if z.in_p(CANARY, EGG):
        z.tell(' ', z.S(z.getp(BROKEN_CANARY, P_FDESC)))
    else:
        remove_carefully(BROKEN_CANARY)
    z.move(BROKEN_EGG, z.loc(EGG))
    remove_carefully(EGG)
    return True


def canary_object():
    global SING_SONG
    if PRSA == V_WIND:
        if PRSO == CANARY:
            if (not SING_SONG) and forest_room_p():
                z.tell('The canary chirps, slightly off-key, an aria from a forgotten opera. From out of the greenery flies a lovely songbird. It perches on a limb just over your head and opens its beak to sing. As it does so a beautiful brass bauble drops from its mouth, bounces off the top of your head, and lands glimmering in the grass. As the canary winds down, the songbird flies away.\n')
                SING_SONG = True
                if HERE == UP_A_TREE:
                    _t1 = PATH
                else:
                    _t1 = HERE
                return z.move(BAUBLE, _t1)
            else:
                z.tell('The canary chirps blithely, if somewhat tinnily, for a short time.\n')
                return True
        else:
            z.tell('There is an unpleasant grinding noise from inside the canary.\n')
            return True
    return False


def forest_room_p():
    return (HERE in (FOREST_1, FOREST_2, FOREST_3)) or (HERE in (PATH, UP_A_TREE))


def i_forest_room():
    if not forest_room_p():
        z.put(int_(z.rtn(i_forest_room)), C_ENABLED_P, 0)
        return False
    elif 15 > z.random(100):
        z.tell('You hear in the distance the chirping of a song bird.\n')
        return True
    return False


def forest_room(rarg=0):
    if rarg == M_ENTER:
        return z.put(queue(z.rtn(i_forest_room), -1), C_ENABLED_P, 1)
    elif rarg == M_BEG:
        if (PRSA in (V_CLIMB_FOO, V_CLIMB_UP)) and (PRSO == TREE):
            return do_walk(P_UP)
    return False


def wclif_object():
    if PRSA in (V_CLIMB_UP, V_CLIMB_DOWN, V_CLIMB_FOO):
        z.tell('The cliff is too steep for climbing.\n')
        return True
    return False


def cliff_object():
    if (PRSA == V_LEAP) or ((PRSA == V_PUT) and (PRSO == ME)):
        z.tell('That would be very unwise. Perhaps even fatal.\n')
        return True
    elif PRSI == CLIMBABLE_CLIFF:
        if PRSA in (V_PUT, V_THROW_OFF):
            z.tell('The ', z.D(PRSO), ' tumbles into the river and is seen no more.\n')
            return remove_carefully(PRSO)
    return False


def rope_function():
    global DOME_FLAG
    rloc = 0
    if HERE != DOME_ROOM:
        DOME_FLAG = False
        if PRSA == V_TIE:
            z.tell("You can't tie the rope to that.\n")
            return True
    elif PRSA == V_TIE:
        if PRSI == RAILING:
            if DOME_FLAG:
                z.tell('The rope is already tied to it.\n')
                return True
            else:
                z.tell('The rope drops over the side and comes within ten feet of the floor.\n')
                DOME_FLAG = True
                z.fset(ROPE, NDESCBIT)
                rloc = z.loc(ROPE)
                if (not rloc) or (not z.in_p(rloc, ROOMS)):
                    z.move(ROPE, HERE)
                return True
    elif (PRSA == V_CLIMB_DOWN) and (PRSO in (ROPE, ROOMS)) and DOME_FLAG:
        return do_walk(P_DOWN)
    elif (PRSA == V_TIE_UP) and (ROPE == PRSI):
        if z.fset_p(PRSO, ACTORBIT):
            if z.getp(PRSO, P_STRENGTH) < 0:
                z.tell('Your attempt to tie up the ', z.D(PRSO), ' awakens him.')
                return awaken(PRSO)
            else:
                z.tell('The ', z.D(PRSO), ' struggles and you cannot tie him up.\n')
                return True
        else:
            z.tell('Why would you tie up a ', z.D(PRSO), '?\n')
            return True
    elif PRSA == V_UNTIE:
        if DOME_FLAG:
            DOME_FLAG = False
            z.fclear(ROPE, NDESCBIT)
            z.tell('The rope is now untied.\n')
            return True
        else:
            z.tell('It is not tied to anything.\n')
            return True
    elif (PRSA == V_DROP) and (HERE == DOME_ROOM) and (not DOME_FLAG):
        z.move(ROPE, TORCH_ROOM)
        z.tell('The rope drops gently to the floor below.\n')
        return True
    elif PRSA == V_TAKE:
        if DOME_FLAG:
            z.tell('The rope is tied to the railing.\n')
            return True
    return False


def untie_from():
    if (PRSO == ROPE) and (DOME_FLAG and (PRSI == RAILING)):
        return perform(V_UNTIE, PRSO)
    else:
        z.tell("It's not attached to that!\n")
        return True
    return False


def slide_function():
    if (PRSA in (V_THROUGH, V_CLIMB_UP, V_CLIMB_DOWN, V_CLIMB_FOO)) or ((PRSA == V_PUT) and (PRSO == ME)):
        if HERE == CELLAR:
            do_walk(P_WEST)
            return True
        else:
            z.tell('You tumble down the slide....\n')
            return goto(CELLAR)
    elif PRSA == V_PUT:
        return slider(PRSO)
    return False


def slider(obj=0):
    if z.fset_p(obj, TAKEBIT):
        z.tell('The ', z.D(obj), ' falls into the slide and is gone.\n')
        if obj == WATER:
            return remove_carefully(obj)
        else:
            return z.move(obj, CELLAR)
    else:
        _t1 = z.S(pick_one(YUKS))
        z.tell(_t1, '\n')
        return True
    return False


def sandwich_bag_fcn():
    if (PRSA == V_SMELL) and z.in_p(LUNCH, PRSO):
        z.tell('It smells of hot peppers.\n')
        return True
    return False


def dead_function(foo=False):
    global ALWAYS_LIT, DEAD, P_CONT, TROLL_FLAG
    m = 0
    if PRSA == V_WALK:
        if (HERE == TIMBER_ROOM) and (PRSO == P_WEST):
            z.tell('You cannot enter in your condition.\n')
            return True
    elif PRSA in (V_BRIEF, V_VERBOSE, V_SUPER_BRIEF, V_VERSION, V_SAVE, V_RESTORE, V_QUIT, V_RESTART):
        return False
    elif PRSA in (V_ATTACK, V_MUNG, V_ALARM, V_SWING):
        z.tell('All such attacks are vain in your condition.\n')
        return True
    elif PRSA in (V_OPEN, V_CLOSE, V_EAT, V_DRINK, V_INFLATE, V_DEFLATE, V_TURN, V_BURN, V_TIE, V_UNTIE, V_RUB):
        z.tell('Even such an action is beyond your capabilities.\n')
        return True
    elif PRSA == V_WAIT:
        z.tell("Might as well. You've got an eternity.\n")
        return True
    elif PRSA == V_LAMP_ON:
        z.tell('You need no light to guide you.\n')
        return True
    elif PRSA == V_SCORE:
        z.tell("You're dead! How can you think of your score?\n")
        return True
    elif PRSA in (V_TAKE, V_RUB):
        z.tell('Your hand passes through its object.\n')
        return True
    elif PRSA in (V_DROP, V_THROW, V_INVENTORY):
        z.tell('You have no possessions.\n')
        return True
    elif PRSA == V_DIAGNOSE:
        z.tell('You are dead.\n')
        return True
    elif PRSA == V_LOOK:
        z.tell('The room looks strange and unearthly')
        if not z.first_p(HERE):
            z.tell('.')
        else:
            z.tell(' and objects appear indistinct.')
        z.crlf()
        if not z.fset_p(HERE, ONBIT):
            z.tell('Although there is no light, the room seems dimly illuminated.\n')
        z.crlf()
        return False
    elif PRSA == V_PRAY:
        if HERE == SOUTH_TEMPLE:
            z.fclear(LAMP, INVISIBLE)
            z.putp(WINNER, P_ACTION, 0)
            ALWAYS_LIT = False
            DEAD = False
            if z.in_p(TROLL, TROLL_ROOM):
                TROLL_FLAG = False
            z.tell('From the distance the sound of a lone trumpet is heard. The room becomes very bright and you feel disembodied. In a moment, the brightness fades and you find yourself rising as if from a long sleep, deep in the woods. In the distance you can faintly hear a songbird and the sounds of the forest.\n\n')
            return goto(FOREST_1)
        else:
            z.tell('Your prayers are not heard.\n')
            return True
    else:
        z.tell("You can't even do that.\n")
        P_CONT = False
        return 2
    return False


def lake_pseudo():
    if LOW_TIDE:
        z.tell("There's not much lake left....\n")
        return True
    elif PRSA == V_CROSS:
        z.tell("It's too wide to cross.\n")
        return True
    elif PRSA == V_THROUGH:
        z.tell("You can't swim in this lake.\n")
        return True
    return False


def stream_pseudo():
    if PRSA in (V_SWIM, V_THROUGH):
        z.tell("You can't swim in the stream.\n")
        return True
    elif PRSA == V_CROSS:
        z.tell('The other side is a sheer rock cliff.\n')
        return True
    return False


def chasm_pseudo():
    if (PRSA == V_LEAP) or ((PRSA == V_PUT) and (PRSO == ME)):
        z.tell('You look before leaping, and realize that you would never survive.\n')
        return True
    elif PRSA == V_CROSS:
        z.tell("It's too far to jump, and there's no bridge.\n")
        return True
    elif (PRSA in (V_PUT, V_THROW_OFF)) and (PRSI == PSEUDO_OBJECT):
        z.tell('The ', z.D(PRSO), ' drops out of sight into the chasm.\n')
        return remove_carefully(PRSO)
    return False


def dome_pseudo():
    if PRSA == V_KISS:
        z.tell('No.\n')
        return True
    return False


def gate_pseudo():
    if PRSA == V_THROUGH:
        do_walk(P_IN)
        return True
    else:
        z.tell('The gate is protected by an invisible force. It makes your teeth ache to touch it.\n')
        return True
    return False


def door_pseudo():
    if PRSA in (V_OPEN, V_CLOSE):
        z.tell("The door won't budge.\n")
        return True
    elif PRSA == V_THROUGH:
        return do_walk(P_SOUTH)
    return False


def paint_pseudo():
    if PRSA == V_MUNG:
        z.tell('Some paint chips away, revealing more paint.\n')
        return True
    return False


def gas_pseudo():
    if PRSA == V_BREATHE:
        z.tell('There is too much gas to blow away.\n')
        return True
    elif PRSA == V_SMELL:
        z.tell('It smells like coal gas in here.\n')
        return True
    return False


def do_fight(len_=0):
    cnt = 0
    res = 0
    o = 0
    oo = 0
    out = False
    while True:
        cnt = 0
        while True:
            cnt = cnt + 1
            if cnt == len_:
                res = True
                return True
            oo = z.get(VILLAINS, cnt)
            o = z.get(oo, V_VILLAIN)
            if not z.fset_p(o, FIGHTBIT):
                pass
            elif z.apply(z.getp(o, P_ACTION), F_BUSY_P):
                pass
            elif not (res := villain_blow(oo, out)):
                res = False
                break
            elif res == UNCONSCIOUS:
                out = 1 + z.random(3)
        if res:
            if not out:
                return True
            else:
                out = out - 1
                if out == 0:
                    return True
        else:
            return True
    return False


def remark(remark_=0, d=0, w=0):
    len_ = z.get(remark_, 0)
    cnt = 0
    str_ = 0
    while True:
        if (cnt := (cnt + 1)) > len_:
            break
        str_ = z.get(remark_, cnt)
        if str_ == F_WEP:
            z.printd(w)
        elif str_ == F_DEF:
            z.printd(d)
        else:
            z.print_(str_)
    return z.crlf()


def fight_strength(adjust_p=True):
    s = 0
    s = STRENGTH_MIN + z.div(SCORE, z.div(SCORE_MAX, (STRENGTH_MAX - STRENGTH_MIN)))
    if adjust_p:
        return s + z.getp(WINNER, P_STRENGTH)
    else:
        return s
    return False


def villain_strength(oo=0):
    global THIEF_ENGROSSED
    villain = z.get(oo, V_VILLAIN)
    od = 0
    tmp = 0
    od = z.getp(villain, P_STRENGTH)
    if not (od < 0):
        if (villain == THIEF) and THIEF_ENGROSSED:
            if od > 2:
                od = 2
            THIEF_ENGROSSED = False
        if PRSI and z.fset_p(PRSI, WEAPONBIT) and (z.get(oo, V_BEST) == PRSI):
            tmp = od - z.get(oo, V_BEST_ADV)
            if tmp < 1:
                tmp = 1
            od = tmp
    return od


def find_weapon(o=0):
    w = 0
    w = z.first_p(o)
    if not w:
        return False
    while True:
        if (w in (STILETTO, AXE, SWORD)) or (w in (KNIFE, RUSTY_KNIFE)):
            return w
        elif not (w := z.next_p(w)):
            return False
    return False


def villain_blow(oo=0, out_p=0):
    global LOAD_ALLOWED
    villain = z.get(oo, V_VILLAIN)
    remarks = z.get(oo, V_MSGS)
    dweapon = 0
    att = 0
    def_ = 0
    oa = 0
    od = 0
    tbl = 0
    res = 0
    nweapon = 0
    z.fclear(WINNER, STAGGERED)
    if z.fset_p(villain, STAGGERED):
        z.tell('The ', z.D(villain), ' slowly regains his feet.\n')
        z.fclear(villain, STAGGERED)
        return True
    att = villain_strength(oo)
    oa = att
    if not ((def_ := fight_strength()) > 0):
        return True
    od = fight_strength(False)
    dweapon = find_weapon(WINNER)
    if def_ < 0:
        res = KILLED
    else:
        if def_ == 1:
            if att > 2:
                att = 3
            tbl = z.get(DEF1_RES, (att - 1))
        elif def_ == 2:
            if att > 3:
                att = 4
            tbl = z.get(DEF2_RES, (att - 1))
        elif def_ > 2:
            att = att - def_
            if att < -1:
                att = -2
            elif att > 1:
                att = 2
            tbl = z.get(DEF3_RES, (att + 2))
        res = z.get(tbl, (z.random(9) - 1))
        if out_p:
            if res == STAGGER:
                res = HESITATE
            else:
                res = SITTING_DUCK
        if (res == STAGGER) and dweapon and zprob(25):
            res = LOSE_WEAPON
        remark(random_element(z.get(remarks, (res - 1))), WINNER, dweapon)
    if (res == MISSED) or (res == HESITATE):
        pass
    elif res == UNCONSCIOUS:
        pass
    elif (res == KILLED) or (res == SITTING_DUCK):
        def_ = 0
    elif res == LIGHT_WOUND:
        def_ = def_ - 1
        if def_ < 0:
            def_ = 0
        if LOAD_ALLOWED > 50:
            LOAD_ALLOWED = LOAD_ALLOWED - 10
    elif res == SERIOUS_WOUND:
        def_ = def_ - 2
        if def_ < 0:
            def_ = 0
        if LOAD_ALLOWED > 50:
            LOAD_ALLOWED = LOAD_ALLOWED - 20
    elif res == STAGGER:
        z.fset(WINNER, STAGGERED)
    else:
        z.move(dweapon, HERE)
        if (nweapon := find_weapon(WINNER)):
            z.tell('Fortunately, you still have a ', z.D(nweapon), '.\n')
    return winner_result(def_, res, od)


def hero_blow():
    oo = 0
    villain = 0
    out_p = False
    dweapon = 0
    att = 0
    def_ = 0
    cnt = 0
    oa = 0
    od = 0
    tbl = 0
    res = 0
    nweapon = 0
    len_ = z.get(VILLAINS, 0)
    while True:
        cnt = cnt + 1
        if cnt == len_:
            break
        oo = z.get(VILLAINS, cnt)
        if z.get(oo, V_VILLAIN) == PRSO:
            break
    z.fset(PRSO, FIGHTBIT)
    if z.fset_p(WINNER, STAGGERED):
        z.tell('You are still recovering from that last blow, so your attack is ineffective.\n')
        z.fclear(WINNER, STAGGERED)
        return True
    att = fight_strength()
    if att < 1:
        att = 1
    oa = att
    villain = z.get(oo, V_VILLAIN)
    if (od := (def_ := villain_strength(oo))) == 0:
        if PRSO == WINNER:
            return jigs_up('Well, you really did it that time. Is suicide painless?')
        z.tell('Attacking the ', z.D(villain), ' is pointless.\n')
        return True
    dweapon = find_weapon(villain)
    if (not dweapon) or (def_ < 0):
        z.tell('The ')
        if def_ < 0:
            z.tell('unconscious')
        else:
            z.tell('unarmed')
        z.tell(' ', z.D(villain), ' cannot defend himself: He dies.\n')
        res = KILLED
    else:
        if def_ == 1:
            if att > 2:
                att = 3
            tbl = z.get(DEF1_RES, (att - 1))
        elif def_ == 2:
            if att > 3:
                att = 4
            tbl = z.get(DEF2_RES, (att - 1))
        elif def_ > 2:
            att = att - def_
            if att < -1:
                att = -2
            elif att > 1:
                att = 2
            tbl = z.get(DEF3_RES, (att + 2))
        res = z.get(tbl, (z.random(9) - 1))
        if out_p:
            if res == STAGGER:
                res = HESITATE
            else:
                res = SITTING_DUCK
        if (res == STAGGER) and dweapon and (25 > z.random(100)):
            res = LOSE_WEAPON
        remark(random_element(z.get(HERO_MELEE, (res - 1))), PRSO, PRSI)
    if (res == MISSED) or (res == HESITATE):
        pass
    elif res == UNCONSCIOUS:
        def_ = -def_
    elif (res == KILLED) or (res == SITTING_DUCK):
        def_ = 0
    elif res == LIGHT_WOUND:
        def_ = def_ - 1
        if def_ < 0:
            def_ = 0
    elif res == SERIOUS_WOUND:
        def_ = def_ - 2
        if def_ < 0:
            def_ = 0
    elif res == STAGGER:
        z.fset(PRSO, STAGGERED)
    else:
        z.fclear(dweapon, NDESCBIT)
        z.fset(dweapon, WEAPONBIT)
        z.move(dweapon, HERE)
        this_is_it(dweapon)
    return villain_result(PRSO, def_, res)


def winner_result(def_=0, res=0, od=0):
    if def_ == 0:
        _t1 = -10000
    else:
        _t1 = def_ - od
    z.putp(WINNER, P_STRENGTH, _t1)
    if (def_ - od) < 0:
        z.put(queue(z.rtn(i_cure), CURE_WAIT), C_ENABLED_P, 1)
    if not (fight_strength() > 0):
        z.putp(WINNER, P_STRENGTH, (1 + (-fight_strength(False))))
        jigs_up("It appears that that last blow was too much for you. I'm afraid you are dead.")
        return False
    else:
        return res
    return False


def villain_result(villain=0, def_=0, res=0):
    z.putp(villain, P_STRENGTH, def_)
    if def_ == 0:
        z.fclear(villain, FIGHTBIT)
        z.tell('Almost as soon as the ', z.D(villain), ' breathes his last breath, a cloud of sinister black fog envelops him, and when the fog lifts, the carcass has disappeared.\n')
        remove_carefully(villain)
        z.apply(z.getp(villain, P_ACTION), F_DEAD)
        return res
    elif res == UNCONSCIOUS:
        z.apply(z.getp(villain, P_ACTION), F_UNCONSCIOUS)
        return res
    else:
        return res
    return False


def winning_p(v=0):
    vs = 0
    ps = 0
    vs = z.getp(v, P_STRENGTH)
    ps = vs - fight_strength()
    if ps > 3:
        return 90 > z.random(100)
    elif ps > 0:
        return 75 > z.random(100)
    elif ps == 0:
        return 50 > z.random(100)
    elif vs > 1:
        return 25 > z.random(100)
    else:
        return 10 > z.random(100)
    return False


def i_cure():
    global LOAD_ALLOWED
    s = z.getp(WINNER, P_STRENGTH)
    if s > 0:
        s = 0
        z.putp(WINNER, P_STRENGTH, s)
    elif s < 0:
        s = s + 1
        z.putp(WINNER, P_STRENGTH, s)
    if s < 0:
        if LOAD_ALLOWED < LOAD_MAX:
            LOAD_ALLOWED = LOAD_ALLOWED + 10
        return z.put(queue(z.rtn(i_cure), CURE_WAIT), C_ENABLED_P, 1)
    else:
        LOAD_ALLOWED = LOAD_MAX
        return z.put(int_(z.rtn(i_cure)), C_ENABLED_P, 0)
    return False


def i_fight():
    global THIEF_ENGROSSED
    fight_p = False
    len_ = z.get(VILLAINS, 0)
    cnt = 0
    oo = 0
    o = 0
    p = 0
    if DEAD:
        return False
    cnt = 0
    while True:
        cnt = cnt + 1
        if cnt == len_:
            break
        oo = z.get(VILLAINS, cnt)
        if z.in_p((o := z.get(oo, V_VILLAIN)), HERE) and (not z.fset_p(o, INVISIBLE)):
            if (o == THIEF) and THIEF_ENGROSSED:
                THIEF_ENGROSSED = False
            elif z.getp(o, P_STRENGTH) < 0:
                p = z.get(oo, V_PROB)
                if (not (p == 0)) and (p > z.random(100)):
                    z.put(oo, V_PROB, 0)
                    awaken(o)
                else:
                    z.put(oo, V_PROB, (p + 25))
            elif z.fset_p(o, FIGHTBIT) or z.apply(z.getp(o, P_ACTION), F_FIRST_P):
                fight_p = True
        else:
            if z.fset_p(o, FIGHTBIT):
                z.apply(z.getp(o, P_ACTION), F_BUSY_P)
            if o == THIEF:
                THIEF_ENGROSSED = False
            z.fclear(WINNER, STAGGERED)
            z.fclear(o, STAGGERED)
            z.fclear(o, FIGHTBIT)
            awaken(o)
    if not fight_p:
        return False
    return do_fight(len_)


def awaken(o=0):
    s = z.getp(o, P_STRENGTH)
    if s < 0:
        z.putp(o, P_STRENGTH, (0 - s))
        z.apply(z.getp(o, P_ACTION), F_CONSCIOUS)
    return True


def i_sword():
    dem = int_(z.rtn(i_sword))
    g = z.getp(SWORD, P_TVALUE)
    ng = 0
    p = 0
    t = 0
    l = 0
    if z.in_p(SWORD, ADVENTURER):
        if infested_p(HERE):
            ng = 2
        else:
            p = 0
            while True:
                if (p := z.nextp(HERE, p)) == 0:
                    break
                elif not (p < LOW_DIRECTION):
                    t = z.getpt(HERE, p)
                    l = z.ptsize(t)
                    if l in (UEXIT, CEXIT, DEXIT):
                        if infested_p(z.getb(t, 0)):
                            ng = 1
                            break
        if ng == g:
            return False
        elif ng == 2:
            z.tell('Your sword has begun to glow very brightly.\n')
        elif ng == 1:
            z.tell('Your sword is glowing with a faint blue glow.\n')
        elif ng == 0:
            z.tell('Your sword is no longer glowing.\n')
        z.putp(SWORD, P_TVALUE, ng)
        return True
    else:
        z.put(dem, C_ENABLED_P, 0)
        return False
    return False


def infested_p(r=0):
    f = z.first_p(r)
    while True:
        if not f:
            return False
        elif z.fset_p(f, ACTORBIT) and (not z.fset_p(f, INVISIBLE)):
            return True
        elif not (f := z.next_p(f)):
            return False
    return False


def i_thief():
    global THIEF_HERE
    rm = z.loc(THIEF)
    robj = 0
    here_p = 0
    once = False
    flg = False
    while True:
        if (here_p := (not z.fset_p(THIEF, INVISIBLE))):
            rm = z.loc(THIEF)
        if (rm == TREASURE_ROOM) and (rm != HERE):
            if here_p:
                hack_treasures()
                here_p = False
            deposit_booty(TREASURE_ROOM)
        elif (rm == HERE) and (not z.fset_p(rm, ONBIT)) and (not z.in_p(TROLL, HERE)):
            if thief_vs_adventurer(here_p):
                return True
            if z.fset_p(THIEF, INVISIBLE):
                here_p = False
        else:
            if z.in_p(THIEF, rm) and (not z.fset_p(THIEF, INVISIBLE)):
                z.fset(THIEF, INVISIBLE)
                here_p = False
            if z.fset_p(rm, TOUCHBIT):
                rob(rm, THIEF, 75)
                if z.fset_p(rm, MAZEBIT) and z.fset_p(HERE, MAZEBIT):
                    flg = rob_maze(rm)
                else:
                    flg = steal_junk(rm)
        if (once := (not once)) and (not here_p):
            recover_stiletto()
            while True:
                if rm and (rm := z.next_p(rm)):
                    pass
                else:
                    rm = z.first_p(ROOMS)
                if (not z.fset_p(rm, SACREDBIT)) and z.fset_p(rm, RLANDBIT):
                    z.move(THIEF, rm)
                    z.fclear(THIEF, FIGHTBIT)
                    z.fset(THIEF, INVISIBLE)
                    THIEF_HERE = False
                    break
            continue
        break
    if rm != TREASURE_ROOM:
        drop_junk(rm)
    return flg


def drop_junk(rm=0):
    x = 0
    n = 0
    flg = False
    x = z.first_p(THIEF)
    while True:
        if not x:
            return flg
        n = z.next_p(x)
        if x in (STILETTO, LARGE_BAG):
            pass
        elif (z.getp(x, P_TVALUE) == 0) and zprob(30):
            z.fclear(x, INVISIBLE)
            z.move(x, rm)
            if (not flg) and (rm == HERE):
                z.tell('The robber, rummaging through his bag, dropped a few items he found valueless.\n')
                flg = True
        x = n
    return False


def recover_stiletto():
    if z.in_p(STILETTO, z.loc(THIEF)):
        z.fset(STILETTO, NDESCBIT)
        return z.move(STILETTO, THIEF)
    return False


def steal_junk(rm=0):
    global DOME_FLAG
    x = 0
    n = 0
    x = z.first_p(rm)
    while True:
        if not x:
            return False
        n = z.next_p(x)
        if (z.getp(x, P_TVALUE) == 0) and z.fset_p(x, TAKEBIT) and (not z.fset_p(x, SACREDBIT)) and (not z.fset_p(x, INVISIBLE)) and ((x == STILETTO) or zprob(10)):
            z.move(x, THIEF)
            z.fset(x, TOUCHBIT)
            z.fset(x, INVISIBLE)
            if x == ROPE:
                DOME_FLAG = False
            if rm == HERE:
                z.tell('You suddenly notice that the ', z.D(x), ' vanished.\n')
                return True
            else:
                return False
        x = n
    return False


def rob(what=0, where=0, prob=False):
    n = 0
    x = 0
    robbed_p = False
    x = z.first_p(what)
    while True:
        if not x:
            return robbed_p
        n = z.next_p(x)
        if (not z.fset_p(x, INVISIBLE)) and (not z.fset_p(x, SACREDBIT)) and (z.getp(x, P_TVALUE) > 0) and ((not prob) or (prob > z.random(100))):
            z.move(x, where)
            z.fset(x, TOUCHBIT)
            if where == THIEF:
                z.fset(x, INVISIBLE)
            robbed_p = True
        x = n
    return False


def v_diagnose():
    ms = fight_strength(False)
    wd = z.getp(WINNER, P_STRENGTH)
    rs = ms + wd
    if z.get(int_(z.rtn(i_cure)), C_ENABLED_P) == 0:
        wd = 0
    else:
        wd = -wd
    if wd == 0:
        z.tell('You are in perfect health.')
    else:
        z.tell('You have ')
        if wd == 1:
            z.tell('a light wound,')
        elif wd == 2:
            z.tell('a serious wound,')
        elif wd == 3:
            z.tell('several wounds,')
        elif wd > 3:
            z.tell('serious wounds,')
    if not (wd == 0):
        z.tell(' which will be cured after ')
        z.printn(((CURE_WAIT * (wd - 1)) + z.get(int_(z.rtn(i_cure)), C_TICK)))
        z.tell(' moves.')
    z.crlf()
    z.tell('You can ')
    if rs == 0:
        z.tell('expect death soon')
    elif rs == 1:
        z.tell('be killed by one more light wound')
    elif rs == 2:
        z.tell('be killed by a serious wound')
    elif rs == 3:
        z.tell('survive one serious wound')
    elif rs > 3:
        z.tell('survive several wounds')
    z.tell('.\n')
    if not (DEATHS == 0):
        z.tell('You have been killed ')
        if DEATHS == 1:
            z.tell('once')
        else:
            z.tell('twice')
        z.tell('.\n')
        return True
    return False


def v_score(ask_p=True):
    z.tell('Your score is ')
    z.tell(z.N(SCORE))
    z.tell(' (total of 350 points), in ')
    z.tell(z.N(MOVES))
    if MOVES == 1:
        z.tell(' move.')
    else:
        z.tell(' moves.')
    z.crlf()
    z.tell('This gives you the rank of ')
    if SCORE == 350:
        z.tell('Master Adventurer')
    elif SCORE > 330:
        z.tell('Wizard')
    elif SCORE > 300:
        z.tell('Master')
    elif SCORE > 200:
        z.tell('Adventurer')
    elif SCORE > 100:
        z.tell('Junior Adventurer')
    elif SCORE > 50:
        z.tell('Novice Adventurer')
    elif SCORE > 25:
        z.tell('Amateur Adventurer')
    else:
        z.tell('Beginner')
    z.tell('.\n')
    return SCORE


def jigs_up(desc=0, player_p=False):
    global ALWAYS_LIT, DEAD, DEATHS, P_CONT, TROLL_FLAG, WINNER
    WINNER = ADVENTURER
    if DEAD:
        z.tell('\nIt takes a talented person to be killed while already dead. YOU are such a talent. Unfortunately, it takes a talented person to deal with it. I am not such a talent. Sorry.\n')
        finish()
    z.tell(z.S(desc), '\n')
    if not LUCKY:
        z.tell('Bad luck, huh?\n')
    score_upd(-10)
    z.tell(' \n    ****  You have died  **** \n\n')
    if z.fset_p(z.loc(WINNER), VEHBIT):
        z.move(WINNER, HERE)
    if not (DEATHS < 2):
        z.tell("You clearly are a suicidal maniac. We don't allow psychotics in the cave, since they may harm other adventurers. Your remains will be installed in the Land of the Living Dead, where your fellow adventurers may gloat over them.\n")
        return finish()
    else:
        DEATHS = DEATHS + 1
        z.move(WINNER, HERE)
        if z.fset_p(SOUTH_TEMPLE, TOUCHBIT):
            z.tell('As you take your last breath, you feel relieved of your burdens. The feeling passes as you find yourself before the gates of Hell, where the spirits jeer at you and deny you entry. Your senses are disturbed. The objects in the dungeon appear indistinct, bleached of color, even unreal.\n\n')
            DEAD = True
            TROLL_FLAG = True
            ALWAYS_LIT = True
            z.putp(WINNER, P_ACTION, z.rtn(dead_function))
            goto(ENTRANCE_TO_HADES)
        else:
            z.tell("Now, let's take a look here... Well, you probably deserve another chance. I can't quite fix you up completely, but you can't have everything.\n\n")
            goto(FOREST_1)
        z.fclear(TRAP_DOOR, TOUCHBIT)
        P_CONT = False
        randomize_objects()
        kill_interrupts()
        return 2
    return False


def randomize_objects():
    r = False
    f = 0
    n = 0
    l = 0
    if z.in_p(LAMP, WINNER):
        z.move(LAMP, LIVING_ROOM)
    if z.in_p(COFFIN, WINNER):
        z.move(COFFIN, EGYPT_ROOM)
    z.putp(SWORD, P_TVALUE, 0)
    n = z.first_p(WINNER)
    l = z.get(ABOVE_GROUND, 0)
    while True:
        f = n
        if not f:
            return True
        n = z.next_p(f)
        if z.getp(f, P_TVALUE) > 0:
            while True:
                if not r:
                    r = z.first_p(ROOMS)
                if z.fset_p(r, RLANDBIT) and (not z.fset_p(r, ONBIT)) and (50 > z.random(100)):
                    z.move(f, r)
                    break
                else:
                    r = z.next_p(r)
        else:
            z.move(f, z.get(ABOVE_GROUND, z.random(l)))
    return False


def kill_interrupts():
    z.put(int_(z.rtn(i_xb)), C_ENABLED_P, 0)
    z.put(int_(z.rtn(i_xc)), C_ENABLED_P, 0)
    z.put(int_(z.rtn(i_cyclops)), C_ENABLED_P, 0)
    z.put(int_(z.rtn(i_lantern)), C_ENABLED_P, 0)
    z.put(int_(z.rtn(i_candles)), C_ENABLED_P, 0)
    z.put(int_(z.rtn(i_sword)), C_ENABLED_P, 0)
    z.put(int_(z.rtn(i_forest_room)), C_ENABLED_P, 0)
    z.put(int_(z.rtn(i_match)), C_ENABLED_P, 0)
    z.fclear(MATCH, ONBIT)
    return True


def bag_of_coins_f():
    return stupid_container(BAG_OF_COINS, 'coins')


def trunk_f():
    return stupid_container(TRUNK, 'jewels')


def stupid_container(obj=0, str_=0):
    if PRSA in (V_OPEN, V_CLOSE):
        z.tell('The ', z.S(str_), " are safely inside; there's no need to do that.\n")
        return True
    elif PRSA in (V_LOOK_INSIDE, V_EXAMINE):
        z.tell('There are lots of ', z.S(str_), ' in there.\n')
        return True
    elif (PRSA == V_PUT) and (PRSI == obj):
        z.tell("Don't be silly. It wouldn't be a ", z.D(obj), ' anymore.\n')
        return True
    return False


def dumb_container():
    if PRSA in (V_OPEN, V_CLOSE, V_LOOK_INSIDE):
        z.tell("You can't do that.\n")
        return True
    elif PRSA == V_EXAMINE:
        z.tell('It looks pretty much like a ', z.D(PRSO), '.\n')
        return True
    return False


def garlic_f():
    if PRSA == V_EAT:
        remove_carefully(PRSO)
        z.tell("What the heck! You won't make friends this way, but nobody around here is too friendly anyhow. Gulp!\n")
        return True
    return False


def chain_pseudo():
    if PRSA in (V_TAKE, V_MOVE):
        z.tell('The chain is secure.\n')
        return True
    elif PRSA in (V_RAISE, V_LOWER):
        z.tell('Perhaps you should do that to the basket.\n')
        return True
    elif PRSA == V_EXAMINE:
        z.tell('The chain secures a basket within the shaft.\n')
        return True
    return False


def troll_room_f(rarg=0):
    if (rarg == M_ENTER) and z.in_p(TROLL, HERE):
        return this_is_it(TROLL)
    return False


# ===================================================================
# Data: vocabulary, objects, tables and globals
# ===================================================================

z.begin_build(globals())

# Vocabulary: (word, parts-of-speech byte, value 1, value 2)
_W = z.vocabulary([
    ('"', 0x04, 239, 0),
    ('#command', 0x41, 240, 0),
    ('#random', 0x41, 241, 0),
    ('#record', 0x41, 239, 0),
    ('#unrecord', 0x41, 238, 0),
    ('$verify', 0x41, 242, 0),
    (',', 0x04, 240, 0),
    ('.', 0x04, 241, 0),
    ('a', 0x04, 252, 0),
    ('about', 0x08, 238, 0),
    ('across', 0x08, 245, 0),
    ('activate', 0x41, 237, 0),
    ('adventurer', 0x80, 1, 0),
    ('advertisement', 0x80, 1, 0),
    ('again', 0x04, 255, 0),
    ('air', 0x80, 1, 0),
    ('air-pump', 0x80, 1, 0),
    ('all', 0x04, 245, 0),
    ('altar', 0x80, 1, 0),
    ('an', 0x04, 251, 0),
    ('ancient', 0x22, 223, 0),
    ('and', 0x04, 248, 0),
    ('answer', 0x41, 236, 0),
    ('antique', 0x22, 159, 0),
    ('apply', 0x41, 235, 0),
    ('around', 0x08, 241, 0),
    ('art', 0x80, 1, 0),
    ('ask', 0x41, 137, 0),
    ('at', 0x08, 243, 0),
    ('attach', 0x41, 135, 0),
    ('attack', 0x41, 234, 0),
    ('aviator', 0x80, 1, 0),
    ('awake', 0x41, 129, 0),
    ('away', 0x08, 247, 0),
    ('ax', 0x80, 1, 0),
    ('axe', 0x80, 1, 0),
    ('back', 0x41, 233, 0),
    ('bag', 0x80, 1, 0),
    ('banish', 0x41, 205, 0),
    ('bar', 0x80, 1, 0),
    ('bare', 0x22, 130, 0),
    ('barf', 0x41, 226, 0),
    ('barrow', 0x80, 1, 0),
    ('basket', 0x80, 1, 0),
    ('bat', 0x80, 1, 0),
    ('bathe', 0x41, 140, 0),
    ('bauble', 0x80, 1, 0),
    ('beauti', 0x22, 251, 0),
    ('beetle', 0x80, 1, 0),
    ('begone', 0x41, 205, 0),
    ('behind', 0x08, 239, 0),
    ('bell', 0x80, 1, 0),
    ('below', 0x08, 240, 0),
    ('beneath', 0x08, 240, 0),
    ('bird', 0x80, 1, 0),
    ('birds', 0x22, 142, 0),
    ('bite', 0x41, 211, 0),
    ('black', 0x22, 227, 0),
    ('blade', 0x80, 1, 0),
    ('blast', 0x41, 232, 0),
    ('blessings', 0x80, 1, 0),
    ('block', 0x41, 217, 0),
    ('bloody', 0x22, 231, 0),
    ('blow', 0x41, 231, 0),
    ('blue', 0x22, 213, 0),
    ('board', 0xc0, 1, 230),
    ('boarded', 0x22, 202, 0),
    ('boards', 0x80, 1, 0),
    ('boat', 0x80, 1, 0),
    ('bodies', 0x80, 1, 0),
    ('body', 0x80, 1, 0),
    ('bolt', 0x80, 1, 0),
    ('bones', 0x80, 1, 0),
    ('book', 0x80, 1, 0),
    ('booklet', 0x80, 1, 0),
    ('books', 0x80, 1, 0),
    ('bottle', 0x80, 1, 0),
    ('box', 0x80, 1, 0),
    ('bracelet', 0x80, 1, 0),
    ('branch', 0x80, 1, 0),
    ('brandish', 0x41, 127, 0),
    ('brass', 0x22, 233, 0),
    ('break', 0x41, 217, 0),
    ('breath', 0x80, 1, 0),
    ('brief', 0x41, 254, 0),
    ('broken', 0x22, 226, 0),
    ('brown', 0x22, 218, 0),
    ('brush', 0x41, 229, 0),
    ('bubble', 0x80, 1, 0),
    ('bug', 0xc0, 1, 228),
    ('buoy', 0x80, 1, 0),
    ('burn', 0x41, 227, 0),
    ('burned', 0x22, 186, 0),
    ('burning', 0x22, 177, 0),
    ('but', 0x04, 243, 0),
    ('button', 0x80, 1, 0),
    ('cage', 0x80, 1, 0),
    ('canary', 0x80, 1, 0),
    ('candles', 0x80, 1, 0),
    ('canvas', 0x80, 1, 0),
    ('carpet', 0x80, 1, 0),
    ('carry', 0x41, 138, 0),
    ('carved', 0x22, 167, 0),
    ('case', 0x80, 1, 0),
    ('casket', 0x80, 1, 0),
    ('cast', 0x41, 205, 0),
    ('catch', 0x41, 138, 0),
    ('chain', 0x80, 1, 0),
    ('chalice', 0x80, 1, 0),
    ('chant', 0x41, 196, 0),
    ('chase', 0x41, 201, 0),
    ('chasm', 0x80, 1, 0),
    ('chest', 0x80, 1, 0),
    ('chests', 0x80, 1, 0),
    ('chimney', 0x80, 1, 0),
    ('chomp', 0x41, 226, 0),
    ('chuck', 0x41, 136, 0),
    ('chute', 0x80, 1, 0),
    ('clean', 0x41, 229, 0),
    ('clear', 0x22, 197, 0),
    ('cliff', 0x80, 1, 0),
    ('cliffs', 0x80, 1, 0),
    ('climb', 0x41, 225, 0),
    ('clockwork', 0x22, 139, 0),
    ('close', 0x41, 224, 0),
    ('clove', 0x80, 1, 0),
    ('coal', 0x80, 1, 0),
    ('coffin', 0x80, 1, 0),
    ('coil', 0x80, 1, 0),
    ('coins', 0x80, 1, 0),
    ('coloni', 0x22, 250, 0),
    ('come', 0x41, 201, 0),
    ('command', 0x41, 223, 0),
    ('consume', 0x41, 211, 0),
    ('container', 0x80, 1, 0),
    ('control', 0x22, 143, 0),
    ('count', 0x41, 222, 0),
    ('cover', 0x80, 1, 0),
    ('crack', 0x80, 1, 0),
    ('cretin', 0x80, 1, 0),
    ('cross', 0x41, 221, 0),
    ('crystal', 0x22, 239, 0),
    ('cup', 0x80, 1, 0),
    ('curse', 0x41, 219, 0),
    ('cut', 0x41, 220, 0),
    ('cyclops', 0x80, 1, 0),
    ('d', 0x18, 250, 22),
    ('dam', 0x80, 1, 0),
    ('damage', 0x41, 217, 0),
    ('damn', 0x41, 219, 0),
    ('dark', 0x22, 243, 0),
    ('dead', 0x22, 185, 0),
    ('deflate', 0x41, 218, 0),
    ('deranged', 0x22, 234, 0),
    ('describe', 0x41, 206, 0),
    ('destroy', 0x41, 217, 0),
    ('diagnose', 0x41, 252, 0),
    ('diamond', 0x80, 1, 0),
    ('dig', 0x41, 216, 0),
    ('dinner', 0x80, 1, 0),
    ('dirt', 0x80, 1, 0),
    ('disembark', 0x41, 215, 0),
    ('disenchant', 0x41, 214, 0),
    ('dispatch', 0x41, 192, 0),
    ('dive', 0x41, 194, 0),
    ('dome', 0x80, 1, 0),
    ('donate', 0x41, 199, 0),
    ('door', 0x80, 1, 0),
    ('douse', 0x41, 204, 0),
    ('down', 0x18, 250, 22),
    ('drink', 0x41, 213, 0),
    ('drip', 0x80, 1, 0),
    ('drive', 0x41, 205, 0),
    ('driver', 0x80, 1, 0),
    ('drop', 0x41, 212, 0),
    ('dryer', 0x80, 1, 0),
    ('dumbwaiter', 0x80, 1, 0),
    ('dusty', 0x22, 203, 0),
    ('e', 0x13, 30, 0),
    ('east', 0x13, 30, 0),
    ('eat', 0x41, 211, 0),
    ('echo', 0x41, 210, 0),
    ('egg', 0x80, 1, 0),
    ('egyptian', 0x22, 224, 0),
    ('elongated', 0x22, 217, 0),
    ('elvish', 0x22, 160, 0),
    ('emerald', 0x80, 1, 0),
    ('enameled', 0x22, 222, 0),
    ('enchant', 0x41, 209, 0),
    ('encrusted', 0x22, 141, 0),
    ('engravings', 0xa2, 209, 1),
    ('enormous', 0xa2, 192, 1),
    ('enter', 0x41, 208, 0),
    ('evil', 0x22, 240, 0),
    ('examine', 0x41, 206, 0),
    ('except', 0x04, 242, 0),
    ('exit', 0x41, 207, 0),
    ('exorcise', 0x41, 205, 0),
    ('exquisite', 0x22, 191, 0),
    ('extinguish', 0x41, 204, 0),
    ('eye', 0x80, 1, 0),
    ('fasten', 0x41, 135, 0),
    ('fcd#3', 0x80, 1, 0),
    ('feed', 0x41, 199, 0),
    ('feel', 0x41, 155, 0),
    ('fiends', 0x80, 1, 0),
    ('fight', 0x41, 234, 0),
    ('figurine', 0x80, 1, 0),
    ('fill', 0x41, 203, 0),
    ('find', 0x41, 202, 0),
    ('fine', 0x22, 157, 0),
    ('fineprint', 0x80, 1, 0),
    ('fix', 0x41, 170, 0),
    ('flaming', 0x22, 152, 0),
    ('flathead', 0x22, 246, 0),
    ('flip', 0x41, 133, 0),
    ('floor', 0x80, 1, 0),
    ('follow', 0x41, 201, 0),
    ('foobar', 0x80, 1, 0),
    ('food', 0x80, 1, 0),
    ('footpad', 0x80, 1, 0),
    ('for', 0x08, 242, 0),
    ('forbidding', 0x22, 137, 0),
    ('force', 0x80, 1, 0),
    ('ford', 0x41, 221, 0),
    ('forest', 0xa0, 1, 133),
    ('fork', 0x80, 1, 0),
    ('free', 0x41, 131, 0),
    ('frigid', 0x22, 172, 0),
    ('frobozz', 0x41, 200, 0),
    ('from', 0x08, 248, 0),
    ('front', 0x22, 201, 0),
    ('fuck', 0x41, 219, 0),
    ('g', 0x04, 254, 0),
    ('garlic', 0x80, 1, 0),
    ('gas', 0x80, 1, 0),
    ('gate', 0x80, 1, 0),
    ('gates', 0x80, 1, 0),
    ('gaze', 0x41, 182, 0),
    ('get', 0x41, 138, 0),
    ('ghosts', 0x80, 1, 0),
    ('giant', 0x22, 205, 0),
    ('give', 0x41, 199, 0),
    ('glamdring', 0x80, 1, 0),
    ('glass', 0x22, 196, 0),
    ('glue', 0x41, 170, 0),
    ('go', 0x41, 128, 0),
    ('gold', 0xa2, 194, 1),
    ('golden', 0x22, 138, 0),
    ('gothic', 0x22, 163, 0),
    ('grab', 0x41, 138, 0),
    ('graces', 0x80, 1, 0),
    ('granite', 0x22, 254, 0),
    ('grate', 0x80, 1, 0),
    ('grating', 0x80, 1, 0),
    ('grease', 0x41, 180, 0),
    ('green', 0x22, 229, 0),
    ('ground', 0x80, 1, 0),
    ('group', 0x80, 1, 0),
    ('grue', 0x80, 1, 0),
    ('guide', 0xa0, 1, 149),
    ('guidebooks', 0x80, 1, 0),
    ('gunk', 0x80, 1, 0),
    ('h2o', 0x80, 1, 0),
    ('hand', 0xc0, 1, 199),
    ('hand-held', 0x22, 193, 0),
    ('hands', 0x80, 1, 0),
    ('hatch', 0x41, 198, 0),
    ('head', 0x80, 1, 0),
    ('heap', 0x80, 1, 0),
    ('hello', 0x41, 197, 0),
    ('hemlocks', 0x80, 1, 0),
    ('hemp', 0x80, 1, 0),
    ('her', 0x80, 1, 0),
    ('here', 0x04, 235, 0),
    ('hi', 0x41, 197, 0),
    ('hide', 0x41, 161, 0),
    ('him', 0x80, 1, 0),
    ('hit', 0x41, 234, 0),
    ('hold', 0x41, 138, 0),
    ('hop', 0x41, 149, 0),
    ('hot', 0x22, 237, 0),
    ('house', 0x80, 1, 0),
    ('huge', 0x22, 200, 0),
    ('hungry', 0x22, 206, 0),
    ('hurl', 0x41, 136, 0),
    ('hurt', 0x41, 234, 0),
    ('i', 0x41, 251, 0),
    ('ignite', 0x41, 227, 0),
    ('imbibe', 0x41, 213, 0),
    ('impassable', 0x22, 247, 0),
    ('in', 0x18, 251, 21),
    ('incant', 0x41, 196, 0),
    ('incinerate', 0x41, 227, 0),
    ('inflat', 0x62, 181, 195),
    ('injure', 0x41, 234, 0),
    ('inscription', 0x80, 1, 0),
    ('insert', 0x41, 161, 0),
    ('inside', 0x18, 251, 21),
    ('intnum', 0x80, 1, 0),
    ('into', 0x18, 251, 21),
    ('inventory', 0x41, 251, 0),
    ('invisible', 0x22, 241, 0),
    ('is', 0x04, 249, 0),
    ('it', 0x80, 1, 0),
    ('ivory', 0xa0, 1, 151),
    ('jade', 0x22, 190, 0),
    ('jewel', 0xa0, 1, 140),
    ('jeweled', 0x22, 166, 0),
    ('jewels', 0x80, 1, 0),
    ('jump', 0x41, 194, 0),
    ('key', 0x80, 1, 0),
    ('kick', 0x41, 193, 0),
    ('kill', 0x41, 192, 0),
    ('kiss', 0x41, 190, 0),
    ('kitchen', 0x22, 245, 0),
    ('knife', 0x80, 1, 0),
    ('knives', 0x80, 1, 0),
    ('knock', 0x41, 189, 0),
    ('l', 0x41, 182, 0),
    ('label', 0x80, 1, 0),
    ('ladder', 0x80, 1, 0),
    ('lake', 0x80, 1, 0),
    ('lamp', 0x80, 1, 0),
    ('land', 0x13, 19, 0),
    ('lantern', 0x80, 1, 0),
    ('large', 0x22, 249, 0),
    ('launch', 0x41, 188, 0),
    ('leaf', 0x80, 1, 0),
    ('leaflet', 0x80, 1, 0),
    ('leak', 0x80, 1, 0),
    ('lean', 0x41, 187, 0),
    ('leap', 0x41, 194, 0),
    ('leather', 0x22, 182, 0),
    ('leave', 0x41, 186, 0),
    ('leaves', 0x80, 1, 0),
    ('ledge', 0x80, 1, 0),
    ('lettering', 0x80, 1, 0),
    ('lid', 0x80, 1, 0),
    ('lift', 0x41, 160, 0),
    ('light', 0xc0, 1, 185),
    ('liquid', 0x80, 1, 0),
    ('liquify', 0x41, 178, 0),
    ('listen', 0x41, 184, 0),
    ('lock', 0x41, 183, 0),
    ('long', 0x22, 132, 0),
    ('look', 0x41, 182, 0),
    ('lose', 0x41, 226, 0),
    ('lower', 0x41, 181, 0),
    ('lowered', 0x22, 238, 0),
    ('lubricate', 0x41, 180, 0),
    ('lunch', 0x80, 1, 0),
    ('lungs', 0x80, 1, 0),
    ('lurking', 0x22, 136, 0),
    ('machine', 0x80, 1, 0),
    ('magic', 0x22, 180, 0),
    ('mail', 0x80, 1, 0),
    ('mailbox', 0x80, 1, 0),
    ('make', 0x41, 179, 0),
    ('man', 0x80, 1, 0),
    ('mangled', 0x22, 175, 0),
    ('manual', 0x80, 1, 0),
    ('map', 0x80, 1, 0),
    ('marble', 0x22, 153, 0),
    ('massive', 0x22, 198, 0),
    ('match', 0xa0, 1, 178),
    ('matchbook', 0x80, 1, 0),
    ('matches', 0x80, 1, 0),
    ('material', 0x80, 1, 0),
    ('me', 0x80, 1, 0),
    ('melt', 0x41, 178, 0),
    ('metal', 0x22, 230, 0),
    ('mirror', 0x80, 1, 0),
    ('molest', 0x41, 159, 0),
    ('monster', 0x80, 1, 0),
    ('mountain', 0x80, 1, 0),
    ('mouth', 0x80, 1, 0),
    ('move', 0x41, 177, 0),
    ('mumble', 0x41, 175, 0),
    ('murder', 0x41, 192, 0),
    ('myself', 0x80, 1, 0),
    ('n', 0x13, 31, 0),
    ('nail', 0x80, 1, 0),
    ('nails', 0x80, 1, 0),
    ('narrow', 0x22, 242, 0),
    ('nasty', 0x22, 189, 0),
    ('ne', 0x13, 27, 0),
    ('nest', 0x80, 1, 0),
    ('no', 0x04, 237, 0),
    ('north', 0x13, 31, 0),
    ('northe', 0x13, 27, 0),
    ('northwest', 0x13, 26, 0),
    ('nut', 0x80, 1, 0),
    ('nw', 0x13, 26, 0),
    ('odor', 0x80, 1, 0),
    ('odysseus', 0x41, 174, 0),
    ('of', 0x04, 247, 0),
    ('off', 0x08, 244, 0),
    ('offer', 0x41, 199, 0),
    ('oil', 0x41, 180, 0),
    ('old', 0x22, 183, 0),
    ('on', 0x08, 249, 0),
    ('one', 0x04, 244, 0),
    ('onto', 0x08, 249, 0),
    ('oops', 0x04, 253, 0),
    ('open', 0x41, 173, 0),
    ('orcrist', 0x80, 1, 0),
    ('oriental', 0x22, 211, 0),
    ('out', 0x18, 253, 20),
    ('over', 0x08, 246, 0),
    ('overboard', 0x80, 1, 0),
    ('own', 0x22, 207, 0),
    ('owners', 0x22, 146, 0),
    ('page', 0x80, 1, 0),
    ('paint', 0x80, 1, 0),
    ('painting', 0x80, 1, 0),
    ('pair', 0x80, 1, 0),
    ('panel', 0x80, 1, 0),
    ('paper', 0x80, 1, 0),
    ('parchment', 0x80, 1, 0),
    ('paste', 0x80, 1, 0),
    ('pat', 0x41, 155, 0),
    ('patch', 0x41, 170, 0),
    ('path', 0x80, 1, 0),
    ('pdp10', 0x80, 1, 0),
    ('peal', 0x41, 156, 0),
    ('pedestal', 0x80, 1, 0),
    ('pepper', 0x22, 236, 0),
    ('person', 0x80, 1, 0),
    ('pet', 0x41, 155, 0),
    ('pick', 0x41, 172, 0),
    ('piece', 0x80, 1, 0),
    ('pierce', 0x41, 220, 0),
    ('pile', 0x80, 1, 0),
    ('pines', 0x80, 1, 0),
    ('pipe', 0x80, 1, 0),
    ('place', 0x41, 161, 0),
    ('plastic', 0xa2, 228, 1),
    ('platinum', 0xa0, 1, 173),
    ('play', 0x41, 171, 0),
    ('plug', 0x41, 170, 0),
    ('plugh', 0x41, 169, 0),
    ('poke', 0x41, 168, 0),
    ('poseidon', 0x22, 208, 0),
    ('pot', 0x80, 1, 0),
    ('pour', 0x41, 166, 0),
    ('pray', 0x41, 165, 0),
    ('prayer', 0x80, 1, 0),
    ('press', 0x41, 162, 0),
    ('print', 0x80, 1, 0),
    ('proceed', 0x41, 128, 0),
    ('pull', 0x41, 164, 0),
    ('pump', 0xc0, 1, 163),
    ('puncture', 0x62, 174, 167),
    ('pursue', 0x41, 201, 0),
    ('push', 0x41, 162, 0),
    ('put', 0x41, 161, 0),
    ('q', 0x41, 250, 0),
    ('quantity', 0x80, 1, 0),
    ('quit', 0x41, 250, 0),
    ('raft', 0x80, 1, 0),
    ('rail', 0x80, 1, 0),
    ('railing', 0x80, 1, 0),
    ('rainbow', 0x80, 1, 0),
    ('raise', 0x41, 160, 0),
    ('ramp', 0x80, 1, 0),
    ('range', 0x80, 1, 0),
    ('rap', 0x41, 189, 0),
    ('rape', 0x41, 159, 0),
    ('read', 0x41, 158, 0),
    ('red', 0x22, 232, 0),
    ('reflection', 0x80, 1, 0),
    ('release', 0x41, 131, 0),
    ('remains', 0x80, 1, 0),
    ('remove', 0x41, 138, 0),
    ('repair', 0x41, 170, 0),
    ('repent', 0x41, 157, 0),
    ('reply', 0x41, 236, 0),
    ('restart', 0x41, 249, 0),
    ('restore', 0x41, 248, 0),
    ('rickety', 0x22, 168, 0),
    ('ring', 0x41, 156, 0),
    ('river', 0x80, 1, 0),
    ('robber', 0x80, 1, 0),
    ('rocky', 0x22, 145, 0),
    ('roll', 0x41, 176, 0),
    ('rope', 0x80, 1, 0),
    ('rub', 0x41, 155, 0),
    ('rug', 0x80, 1, 0),
    ('run', 0x41, 128, 0),
    ('rusty', 0x22, 187, 0),
    ('s', 0x13, 28, 0),
    ('sack', 0x80, 1, 0),
    ('sailor', 0x80, 1, 0),
    ('sand', 0x80, 1, 0),
    ('sandwich', 0x80, 1, 0),
    ('sapphire', 0xa0, 1, 171),
    ('save', 0x41, 247, 0),
    ('say', 0x41, 153, 0),
    ('scarab', 0x80, 1, 0),
    ('scepter', 0x80, 1, 0),
    ('sceptre', 0x80, 1, 0),
    ('score', 0x41, 246, 0),
    ('scream', 0x41, 122, 0),
    ('screw', 0x22, 170, 0),
    ('screwdriver', 0x80, 1, 0),
    ('script', 0x41, 245, 0),
    ('se', 0x13, 25, 0),
    ('search', 0x41, 152, 0),
    ('seaworthy', 0x22, 179, 0),
    ('secure', 0x41, 135, 0),
    ('see', 0x41, 202, 0),
    ('seedy', 0x22, 154, 0),
    ('seek', 0x41, 202, 0),
    ('self', 0x80, 1, 0),
    ('send', 0x41, 151, 0),
    ('set', 0x41, 133, 0),
    ('shady', 0x22, 156, 0),
    ('shake', 0x41, 150, 0),
    ('sharp', 0x22, 225, 0),
    ('sheer', 0x22, 144, 0),
    ('shit', 0x41, 219, 0),
    ('shout', 0x41, 122, 0),
    ('shovel', 0x80, 1, 0),
    ('shut', 0x41, 133, 0),
    ('sigh', 0x41, 175, 0),
    ('silent', 0x22, 134, 0),
    ('silver', 0xa0, 1, 210),
    ('sinister', 0x22, 135, 0),
    ('sit', 0x41, 225, 0),
    ('skeleton', 0xa0, 1, 169),
    ('skim', 0x41, 158, 0),
    ('skip', 0x41, 149, 0),
    ('skull', 0x80, 1, 0),
    ('slag', 0x80, 1, 0),
    ('slay', 0x41, 192, 0),
    ('slice', 0x41, 220, 0),
    ('slide', 0xc0, 1, 148),
    ('small', 0x22, 244, 0),
    ('smash', 0x41, 217, 0),
    ('smell', 0x41, 147, 0),
    ('smelly', 0x22, 216, 0),
    ('sniff', 0x41, 147, 0),
    ('solid', 0x22, 195, 0),
    ('song', 0x22, 253, 0),
    ('songbird', 0x80, 1, 0),
    ('south', 0x13, 28, 0),
    ('southe', 0x13, 25, 0),
    ('southwest', 0x13, 24, 0),
    ('spill', 0x41, 166, 0),
    ('spin', 0x41, 146, 0),
    ('spirits', 0x80, 1, 0),
    ('spray', 0x41, 145, 0),
    ('squeeze', 0x41, 144, 0),
    ('stab', 0x41, 191, 0),
    ('staircase', 0x80, 1, 0),
    ('stairs', 0x80, 1, 0),
    ('stairway', 0x80, 1, 0),
    ('stand', 0x41, 143, 0),
    ('stare', 0x41, 182, 0),
    ('startle', 0x41, 129, 0),
    ('stay', 0x41, 142, 0),
    ('steep', 0x22, 220, 0),
    ('step', 0x41, 128, 0),
    ('steps', 0x80, 1, 0),
    ('stiletto', 0x80, 1, 0),
    ('stone', 0x22, 199, 0),
    ('storm', 0x22, 248, 0),
    ('strange', 0x22, 162, 0),
    ('stream', 0x80, 1, 0),
    ('strike', 0x41, 141, 0),
    ('stuff', 0x41, 161, 0),
    ('super', 0x41, 253, 0),
    ('superbrief', 0x41, 253, 0),
    ('surprise', 0x41, 129, 0),
    ('surrounding', 0x22, 255, 0),
    ('suspicious', 0x22, 155, 0),
    ('sw', 0x13, 24, 0),
    ('swallow', 0x41, 213, 0),
    ('swim', 0x41, 140, 0),
    ('swing', 0x41, 139, 0),
    ('switch', 0x80, 1, 0),
    ('sword', 0x80, 1, 0),
    ('table', 0x80, 1, 0),
    ('take', 0x41, 138, 0),
    ('talk', 0x41, 154, 0),
    ('tan', 0x22, 158, 0),
    ('taste', 0x41, 211, 0),
    ('taunt', 0x41, 193, 0),
    ('teeth', 0x80, 1, 0),
    ('tell', 0x41, 137, 0),
    ('temple', 0xc0, 1, 134),
    ('the', 0x04, 250, 0),
    ('them', 0x80, 1, 0),
    ('then', 0x04, 246, 0),
    ('thief', 0x80, 1, 0),
    ('thiefs', 0x22, 165, 0),
    ('through', 0x08, 254, 0),
    ('throw', 0x41, 136, 0),
    ('thru', 0x08, 254, 0),
    ('thrust', 0x41, 139, 0),
    ('tie', 0x41, 135, 0),
    ('timbers', 0x80, 1, 0),
    ('to', 0x08, 255, 0),
    ('tomb', 0x80, 1, 0),
    ('tool', 0xa2, 215, 1),
    ('toolchests', 0x80, 1, 0),
    ('tools', 0x80, 1, 0),
    ('tooth', 0x80, 1, 0),
    ('torch', 0x80, 1, 0),
    ('toss', 0x41, 136, 0),
    ('touch', 0x41, 155, 0),
    ('tour', 0x22, 150, 0),
    ('trail', 0x80, 1, 0),
    ('trap', 0x22, 204, 0),
    ('trap-door', 0x80, 1, 0),
    ('trapdoor', 0x80, 1, 0),
    ('treasure', 0xc0, 1, 134),
    ('tree', 0x80, 1, 0),
    ('trees', 0x80, 1, 0),
    ('trident', 0x80, 1, 0),
    ('troll', 0x80, 1, 0),
    ('trophy', 0x22, 212, 0),
    ('trunk', 0x80, 1, 0),
    ('tube', 0x80, 1, 0),
    ('tug', 0x41, 164, 0),
    ('turn', 0x41, 133, 0),
    ('twisting', 0x22, 219, 0),
    ('u', 0x18, 252, 23),
    ('ulysses', 0x41, 174, 0),
    ('unattach', 0x41, 131, 0),
    ('under', 0x08, 240, 0),
    ('underneath', 0x08, 240, 0),
    ('unfasten', 0x41, 131, 0),
    ('unhook', 0x41, 131, 0),
    ('unlock', 0x41, 132, 0),
    ('unrusty', 0x22, 188, 0),
    ('unscript', 0x41, 244, 0),
    ('untie', 0x41, 131, 0),
    ('up', 0x18, 252, 23),
    ('useless', 0x22, 184, 0),
    ('using', 0x08, 254, 0),
    ('valve', 0x80, 1, 0),
    ('vampire', 0xa0, 1, 235),
    ('verbose', 0x41, 255, 0),
    ('version', 0x41, 243, 0),
    ('vicious', 0x22, 164, 0),
    ('viscous', 0x22, 148, 0),
    ('vitreous', 0x22, 176, 0),
    ('w', 0x33, 29, 161),
    ('wade', 0x41, 140, 0),
    ('wait', 0x41, 130, 0),
    ('wake', 0x41, 129, 0),
    ('walk', 0x41, 128, 0),
    ('wall', 0x80, 1, 0),
    ('walls', 0x80, 1, 0),
    ('water', 0x80, 1, 0),
    ('wave', 0x41, 127, 0),
    ('wear', 0x41, 126, 0),
    ('west', 0x33, 29, 161),
    ('what', 0x41, 206, 0),
    ('whats', 0x41, 206, 0),
    ('where', 0x41, 202, 0),
    ('white', 0x22, 252, 0),
    ('win', 0x41, 125, 0),
    ('wind', 0x41, 124, 0),
    ('winding', 0x22, 131, 0),
    ('window', 0x80, 1, 0),
    ('winnage', 0x41, 125, 0),
    ('wish', 0x41, 123, 0),
    ('with', 0x08, 254, 0),
    ('wooden', 0x22, 221, 0),
    ('wrench', 0x80, 1, 0),
    ('writing', 0x80, 1, 0),
    ('xyzzy', 0x41, 169, 0),
    ('y', 0x04, 236, 0),
    ('yank', 0x41, 164, 0),
    ('yell', 0x41, 122, 0),
    ('yellow', 0x22, 214, 0),
    ('yes', 0x04, 238, 0),
    ('z', 0x41, 130, 0),
    ('zork', 0x62, 147, 121),
    ('zorkmid', 0x80, 1, 0),
    ('zzmgck', 0x80, 1, 0),
])
_A = {'ancient': 223, 'antique': 159, 'bare': 130, 'beauti': 251, 'birds': 142, 'black': 227, 'bloody': 231, 'blue': 213, 'boarded': 202, 'brass': 233, 'broken': 226, 'brown': 218, 'burned': 186, 'burning': 177, 'carved': 167, 'clear': 197, 'clockwork': 139, 'coloni': 250, 'control': 143, 'crystal': 239, 'dark': 243, 'dead': 185, 'deranged': 234, 'dusty': 203, 'egyptian': 224, 'elongated': 217, 'elvish': 160, 'enameled': 222, 'encrusted': 141, 'engravings': 209, 'enormous': 192, 'evil': 240, 'exquisite': 191, 'fine': 157, 'flaming': 152, 'flathead': 246, 'forbidding': 137, 'forest': 133, 'frigid': 172, 'front': 201, 'giant': 205, 'glass': 196, 'gold': 194, 'golden': 138, 'gothic': 163, 'granite': 254, 'green': 229, 'guide': 149, 'hand-held': 193, 'hot': 237, 'huge': 200, 'hungry': 206, 'impassable': 247, 'inflat': 181, 'invisible': 241, 'ivory': 151, 'jade': 190, 'jewel': 140, 'jeweled': 166, 'kitchen': 245, 'large': 249, 'leather': 182, 'long': 132, 'lowered': 238, 'lurking': 136, 'magic': 180, 'mangled': 175, 'marble': 153, 'massive': 198, 'match': 178, 'metal': 230, 'narrow': 242, 'nasty': 189, 'old': 183, 'oriental': 211, 'own': 207, 'owners': 146, 'pepper': 236, 'plastic': 228, 'platinum': 173, 'poseidon': 208, 'puncture': 174, 'red': 232, 'rickety': 168, 'rocky': 145, 'rusty': 187, 'sapphire': 171, 'screw': 170, 'seaworthy': 179, 'seedy': 154, 'shady': 156, 'sharp': 225, 'sheer': 144, 'silent': 134, 'silver': 210, 'sinister': 135, 'skeleton': 169, 'small': 244, 'smelly': 216, 'solid': 195, 'song': 253, 'steep': 220, 'stone': 199, 'storm': 248, 'strange': 162, 'surrounding': 255, 'suspicious': 155, 'tan': 158, 'thiefs': 165, 'tool': 215, 'tour': 150, 'trap': 204, 'trophy': 212, 'twisting': 219, 'unrusty': 188, 'useless': 184, 'vampire': 235, 'vicious': 164, 'viscous': 148, 'vitreous': 176, 'w': 161, 'west': 161, 'white': 252, 'winding': 131, 'wooden': 221, 'yellow': 214, 'zork': 147}

# Words referred to by the code (W?...)
W_A = _W['a']
W_AGAIN = _W['again']
W_ALL = _W['all']
W_AN = _W['an']
W_AND = _W['and']
W_BUG = _W['bug']
W_BUT = _W['but']
W_COMMA = _W[',']
W_E = _W['e']
W_EAST = _W['east']
W_ECHO = _W['echo']
W_EXCEPT = _W['except']
W_G = _W['g']
W_GO = _W['go']
W_HELLO = _W['hello']
W_INTNUM = _W['intnum']
W_IT = _W['it']
W_ME = _W['me']
W_OF = _W['of']
W_ONE = _W['one']
W_OOPS = _W['oops']
W_OUT = _W['out']
W_PERIOD = _W['.']
W_Q = _W['q']
W_QUIT = _W['quit']
W_QUOTE = _W['"']
W_RESTART = _W['restart']
W_RESTORE = _W['restore']
W_RUN = _W['run']
W_SAVE = _W['save']
W_SAY = _W['say']
W_THE = _W['the']
W_THEN = _W['then']
W_TO = _W['to']
W_U = _W['u']
W_UP = _W['up']
W_W = _W['w']
W_WALK = _W['walk']
W_WALL = _W['wall']
W_WEST = _W['west']
W_Y = _W['y']
W_YES = _W['yes']

# Global variables, numbered from 16 as in the Z-machine
z.declare_globals([
    'SCORE_MAX',
    'FALSE_FLAG',
    'CYCLOPS_FLAG',
    'DEFLATE',
    'DOME_FLAG',
    'EMPTY_HANDED',
    'LLD_FLAG',
    'LOW_TIDE',
    'MAGIC_FLAG',
    'RAINBOW_FLAG',
    'TROLL_FLAG',
    'WON_FLAG',
    'COFFIN_CURE',
    'HOUSE_AROUND',
    'FOREST_AROUND',
    'IN_HOUSE_AROUND',
    'ABOVE_GROUND',
    'LOAD_MAX',
    'LOAD_ALLOWED',
    'C_TABLE',
    'C_DEMONS',
    'C_INTS',
    'CLOCK_WAIT',
    'PLAYER',
    'P_WON',
    'P_MULT',
    'P_NOT_HERE',
    'PRSA',
    'PRSI',
    'PRSO',
    'P_TABLE',
    'P_ONEOBJ',
    'P_SYNTAX',
    'P_CCTBL',
    'P_LEN',
    'P_DIR',
    'HERE',
    'WINNER',
    'P_LEXV',
    'AGAIN_LEXV',
    'RESERVE_LEXV',
    'RESERVE_PTR',
    'P_INBUF',
    'OOPS_INBUF',
    'OOPS_TABLE',
    'P_CONT',
    'P_IT_OBJECT',
    'P_OFLAG',
    'P_MERGED',
    'P_ACLAUSE',
    'P_ANAM',
    'P_AADJ',
    'P_ITBL',
    'P_OTBL',
    'P_VTBL',
    'P_OVTBL',
    'P_NCN',
    'QUOTE_FLAG',
    'P_END_ON_PREP',
    'P_ACT',
    'P_WALK_DIR',
    'AGAIN_DIR',
    'P_NUMBER',
    'P_DIRECTION',
    'P_SLOCBITS',
    'P_GWIMBIT',
    'P_NAM',
    'P_ADJ',
    'P_ADVERB',
    'P_ADJN',
    'P_PRSO',
    'P_PRSI',
    'P_BUTS',
    'P_MERGE',
    'P_OCLAUSE',
    'P_MATCHLEN',
    'P_GETFLAGS',
    'P_AND',
    'P_XNAM',
    'P_XADJ',
    'P_XADJN',
    'ALWAYS_LIT',
    'VERBOSE',
    'SUPER_BRIEF',
    'HS',
    'JUMPLOSS',
    'WHEEEEE',
    'LIT',
    'SPRAYED_P',
    'DESC_OBJECT',
    'MOVES',
    'SCORE',
    'BASE_SCORE',
    'DEAD',
    'DEATHS',
    'LUCKY',
    'FUMBLE_NUMBER',
    'FUMBLE_PROB',
    'INDENTS',
    'HO_HUM',
    'SWIMYUKS',
    'HELLOS',
    'YUKS',
    'DUMMY',
    'KITCHEN_WINDOW_FLAG',
    'CAGE_TOP',
    'BAT_DROPS',
    'RUG_MOVED',
    'GRATE_REVEALED',
    'GRUNLOCK',
    'MIRROR_MUNG',
    'XB',
    'XC',
    'GATE_FLAG',
    'GATES_OPEN',
    'LOUD_RUNS',
    'DROWNINGS',
    'WATER_LEVEL',
    'CYCLOWRATH',
    'CYCLOMAD',
    'LOUD_FLAG',
    'EGG_SOLVE',
    'THIEF_HERE',
    'THIEF_ENGROSSED',
    'ROBBER_C_DESC',
    'ROBBER_U_DESC',
    'LAMP_TABLE',
    'MATCH_COUNT',
    'CANDLE_TABLE',
    'LIGHT_SHAFT',
    'RIVER_SPEEDS',
    'RIVER_NEXT',
    'RIVER_LAUNCH',
    'BUOY_FLAG',
    'BEACH_DIG',
    'BDIGS',
    'SING_SONG',
    'DEF1',
    'DEF2A',
    'DEF2B',
    'DEF3A',
    'DEF3B',
    'DEF3C',
    'DEF1_RES',
    'DEF2_RES',
    'DEF3_RES',
    'HERO_MELEE',
    'CYCLOPS_MELEE',
    'TROLL_MELEE',
    'THIEF_MELEE',
    'VILLAINS',
])

# Objects, in definition order.  Children are linked in reverse
# definition order, as the original compiler did.
z.property_defaults({P_SIZE: 5, P_CAPACITY: 0, P_VALUE: 0, P_TVALUE: 0})

z.define_object(BOARD, 'board', parent=LOCAL_GLOBALS,
    flags=[NDESCBIT],
    props=[
        (P_SYNONYM, z.words(_W['boards'], _W['board'])),
        (P_ACTION, z.words(z.rtn(board_f))),
    ])
z.define_object(TEETH, 'set of teeth', parent=GLOBAL_OBJECTS,
    flags=[NDESCBIT],
    props=[
        (P_SYNONYM, z.words(_W['overboard'], _W['teeth'])),
        (P_ACTION, z.words(z.rtn(teeth_f))),
    ])
z.define_object(WALL, 'surrounding wall', parent=GLOBAL_OBJECTS,
    flags=[],
    props=[
        (P_SYNONYM, z.words(_W['wall'], _W['walls'])),
        (P_ADJECTIVE, z.bytes_(_A['surrounding'])),
    ])
z.define_object(GRANITE_WALL, 'granite wall', parent=GLOBAL_OBJECTS,
    flags=[],
    props=[
        (P_SYNONYM, z.words(_W['wall'])),
        (P_ACTION, z.words(z.rtn(granite_wall_f))),
        (P_ADJECTIVE, z.bytes_(_A['granite'])),
    ])
z.define_object(SONGBIRD, 'songbird', parent=LOCAL_GLOBALS,
    flags=[NDESCBIT],
    props=[
        (P_SYNONYM, z.words(_W['bird'], _W['songbird'])),
        (P_ACTION, z.words(z.rtn(songbird_f))),
        (P_ADJECTIVE, z.bytes_(_A['song'])),
    ])
z.define_object(WHITE_HOUSE, 'white house', parent=LOCAL_GLOBALS,
    flags=[NDESCBIT],
    props=[
        (P_SYNONYM, z.words(_W['house'])),
        (P_ACTION, z.words(z.rtn(white_house_f))),
        (P_ADJECTIVE, z.bytes_(_A['white'], _A['beauti'], _A['coloni'])),
    ])
z.define_object(FOREST, 'forest', parent=LOCAL_GLOBALS,
    flags=[NDESCBIT],
    props=[
        (P_SYNONYM, z.words(_W['forest'], _W['trees'], _W['pines'], _W['hemlocks'])),
        (P_ACTION, z.words(z.rtn(forest_f))),
    ])
z.define_object(TREE, 'tree', parent=LOCAL_GLOBALS,
    flags=[NDESCBIT, CLIMBBIT],
    props=[
        (P_SYNONYM, z.words(_W['tree'], _W['branch'])),
        (P_ADJECTIVE, z.bytes_(_A['large'], _A['storm'])),
    ])
z.define_object(MOUNTAIN_RANGE, 'mountain range', parent=MOUNTAINS,
    flags=[NDESCBIT, CLIMBBIT],
    props=[
        (P_SYNONYM, z.words(_W['mountain'], _W['range'])),
        (P_ACTION, z.words(z.rtn(mountain_range_f))),
        (P_ADJECTIVE, z.bytes_(_A['impassable'], _A['flathead'])),
    ])
z.define_object(GLOBAL_WATER, 'water', parent=LOCAL_GLOBALS,
    flags=[DRINKBIT],
    props=[
        (P_SYNONYM, z.words(_W['water'], _W['quantity'])),
        (P_ACTION, z.words(z.rtn(water_f))),
    ])
z.define_object(WATER, 'quantity of water', parent=BOTTLE,
    flags=[TRYTAKEBIT, TAKEBIT, DRINKBIT],
    props=[
        (P_SYNONYM, z.words(_W['water'], _W['quantity'], _W['liquid'], _W['h2o'])),
        (P_ACTION, z.words(z.rtn(water_f))),
        (P_SIZE, z.words(4)),
    ])
z.define_object(KITCHEN_WINDOW, 'kitchen window', parent=LOCAL_GLOBALS,
    flags=[DOORBIT, NDESCBIT],
    props=[
        (P_SYNONYM, z.words(_W['window'])),
        (P_ACTION, z.words(z.rtn(kitchen_window_f))),
        (P_ADJECTIVE, z.bytes_(_A['kitchen'], _A['small'])),
    ])
z.define_object(CHIMNEY, 'chimney', parent=LOCAL_GLOBALS,
    flags=[CLIMBBIT, NDESCBIT],
    props=[
        (P_SYNONYM, z.words(_W['chimney'])),
        (P_ACTION, z.words(z.rtn(chimney_f))),
        (P_ADJECTIVE, z.bytes_(_A['dark'], _A['narrow'])),
    ])
z.define_object(GHOSTS, 'number of ghosts', parent=ENTRANCE_TO_HADES,
    flags=[ACTORBIT, NDESCBIT],
    props=[
        (P_SYNONYM, z.words(_W['ghosts'], _W['spirits'], _W['fiends'], _W['force'])),
        (P_ACTION, z.words(z.rtn(ghosts_f))),
        (P_ADJECTIVE, z.bytes_(_A['invisible'], _A['evil'])),
    ])
z.define_object(SKULL, 'crystal skull', parent=LAND_OF_LIVING_DEAD,
    flags=[TAKEBIT],
    props=[
        (P_SYNONYM, z.words(_W['skull'], _W['head'], _W['treasure'])),
        (P_ADJECTIVE, z.bytes_(_A['crystal'])),
        (P_FDESC, z.words('Lying in one corner of the room is a beautifully carved crystal skull. It appears to be grinning at you rather nastily.')),
        (P_VALUE, z.words(10)),
        (P_TVALUE, z.words(10)),
    ])
z.define_object(LOWERED_BASKET, 'basket', parent=LOWER_SHAFT,
    flags=[TRYTAKEBIT],
    props=[
        (P_SYNONYM, z.words(_W['cage'], _W['dumbwaiter'], _W['basket'])),
        (P_ACTION, z.words(z.rtn(basket_f))),
        (P_ADJECTIVE, z.bytes_(_A['lowered'])),
        (P_LDESC, z.words('From the chain is suspended a basket.')),
    ])
z.define_object(RAISED_BASKET, 'basket', parent=SHAFT_ROOM,
    flags=[TRANSBIT, TRYTAKEBIT, CONTBIT, OPENBIT],
    props=[
        (P_SYNONYM, z.words(_W['cage'], _W['dumbwaiter'], _W['basket'])),
        (P_ACTION, z.words(z.rtn(basket_f))),
        (P_LDESC, z.words('At the end of the chain is a basket.')),
        (P_CAPACITY, z.words(50)),
    ])
z.define_object(LUNCH, 'lunch', parent=SANDWICH_BAG,
    flags=[TAKEBIT, FOODBIT],
    props=[
        (P_SYNONYM, z.words(_W['food'], _W['sandwich'], _W['lunch'], _W['dinner'])),
        (P_ADJECTIVE, z.bytes_(_A['hot'], _A['pepper'])),
        (P_LDESC, z.words('A hot pepper sandwich is here.')),
    ])
z.define_object(BAT, 'bat', parent=BAT_ROOM,
    flags=[ACTORBIT, TRYTAKEBIT],
    props=[
        (P_SYNONYM, z.words(_W['bat'], _W['vampire'])),
        (P_ACTION, z.words(z.rtn(bat_f))),
        (P_ADJECTIVE, z.bytes_(_A['vampire'], _A['deranged'])),
        (P_DESCFCN, z.words(z.rtn(bat_d))),
    ])
z.define_object(BELL, 'brass bell', parent=NORTH_TEMPLE,
    flags=[TAKEBIT],
    props=[
        (P_SYNONYM, z.words(_W['bell'])),
        (P_ACTION, z.words(z.rtn(bell_f))),
        (P_ADJECTIVE, z.bytes_(_A['small'], _A['brass'])),
    ])
z.define_object(HOT_BELL, 'red hot brass bell', parent=0,
    flags=[TRYTAKEBIT],
    props=[
        (P_SYNONYM, z.words(_W['bell'])),
        (P_ACTION, z.words(z.rtn(hot_bell_f))),
        (P_ADJECTIVE, z.bytes_(_A['brass'], _A['hot'], _A['red'], _A['small'])),
        (P_LDESC, z.words('On the ground is a red hot bell.')),
    ])
z.define_object(AXE, 'bloody axe', parent=TROLL,
    flags=[WEAPONBIT, TRYTAKEBIT, TAKEBIT, NDESCBIT],
    props=[
        (P_SYNONYM, z.words(_W['axe'], _W['ax'])),
        (P_ACTION, z.words(z.rtn(axe_f))),
        (P_ADJECTIVE, z.bytes_(_A['bloody'])),
        (P_SIZE, z.words(25)),
    ])
z.define_object(BOLT, 'bolt', parent=DAM_ROOM,
    flags=[NDESCBIT, TURNBIT, TRYTAKEBIT],
    props=[
        (P_SYNONYM, z.words(_W['bolt'], _W['nut'])),
        (P_ACTION, z.words(z.rtn(bolt_f))),
        (P_ADJECTIVE, z.bytes_(_A['metal'], _A['large'])),
    ])
z.define_object(BUBBLE, 'green bubble', parent=DAM_ROOM,
    flags=[NDESCBIT, TRYTAKEBIT],
    props=[
        (P_SYNONYM, z.words(_W['bubble'])),
        (P_ACTION, z.words(z.rtn(bubble_f))),
        (P_ADJECTIVE, z.bytes_(_A['small'], _A['green'], _A['plastic'])),
    ])
z.define_object(ALTAR, 'altar', parent=SOUTH_TEMPLE,
    flags=[NDESCBIT, SURFACEBIT, CONTBIT, OPENBIT],
    props=[
        (P_SYNONYM, z.words(_W['altar'])),
        (P_CAPACITY, z.words(50)),
    ])
z.define_object(BOOK, 'black book', parent=ALTAR,
    flags=[READBIT, TAKEBIT, CONTBIT, BURNBIT, TURNBIT],
    props=[
        (P_SYNONYM, z.words(_W['book'], _W['prayer'], _W['page'], _W['books'])),
        (P_ACTION, z.words(z.rtn(black_book))),
        (P_ADJECTIVE, z.bytes_(_A['large'], _A['black'])),
        (P_SIZE, z.words(10)),
        (P_FDESC, z.words('On the altar is a large black book, open to page 569.')),
        (P_TEXT, z.words('Commandment #12592\n\nOh ye who go about saying unto each:  "Hello sailor":\nDost thou know the magnitude of thy sin before the gods?\nYea, verily, thou shalt be ground between two stones.\nShall the angry gods cast thy body into the whirlpool?\nSurely, thy eye shall be put out with a sharp stick!\nEven unto the ends of the earth shalt thou wander and\nUnto the land of the dead shalt thou be sent at last.\nSurely thou shalt repent of thy cunning.')),
    ])
z.define_object(BROKEN_LAMP, 'broken lantern', parent=0,
    flags=[TAKEBIT],
    props=[
        (P_SYNONYM, z.words(_W['lamp'], _W['lantern'])),
        (P_ADJECTIVE, z.bytes_(_A['broken'])),
    ])
z.define_object(SCEPTRE, 'sceptre', parent=COFFIN,
    flags=[TAKEBIT, WEAPONBIT],
    props=[
        (P_SYNONYM, z.words(_W['sceptre'], _W['scepter'], _W['treasure'])),
        (P_ACTION, z.words(z.rtn(sceptre_function))),
        (P_ADJECTIVE, z.bytes_(_A['sharp'], _A['egyptian'], _A['ancient'], _A['enameled'])),
        (P_SIZE, z.words(3)),
        (P_FDESC, z.words('A sceptre, possibly that of ancient Egypt itself, is in the coffin. The sceptre is ornamented with colored enamel, and tapers to a sharp point.')),
        (P_VALUE, z.words(4)),
        (P_TVALUE, z.words(6)),
        (P_LDESC, z.words('An ornamented sceptre, tapering to a sharp point, is here.')),
    ])
z.define_object(TIMBERS, 'broken timber', parent=TIMBER_ROOM,
    flags=[TAKEBIT],
    props=[
        (P_SYNONYM, z.words(_W['timbers'], _W['pile'])),
        (P_ADJECTIVE, z.bytes_(_A['wooden'], _A['broken'])),
        (P_SIZE, z.words(50)),
    ])
z.define_object(SLIDE, 'chute', parent=LOCAL_GLOBALS,
    flags=[CLIMBBIT],
    props=[
        (P_SYNONYM, z.words(_W['chute'], _W['ramp'], _W['slide'])),
        (P_ACTION, z.words(z.rtn(slide_function))),
        (P_ADJECTIVE, z.bytes_(_A['steep'], _A['metal'], _A['twisting'])),
    ])
z.define_object(KITCHEN_TABLE, 'kitchen table', parent=KITCHEN,
    flags=[NDESCBIT, CONTBIT, OPENBIT, SURFACEBIT],
    props=[
        (P_SYNONYM, z.words(_W['table'])),
        (P_ADJECTIVE, z.bytes_(_A['kitchen'])),
        (P_CAPACITY, z.words(50)),
    ])
z.define_object(ATTIC_TABLE, 'table', parent=ATTIC,
    flags=[NDESCBIT, CONTBIT, OPENBIT, SURFACEBIT],
    props=[
        (P_SYNONYM, z.words(_W['table'])),
        (P_CAPACITY, z.words(40)),
    ])
z.define_object(SANDWICH_BAG, 'brown sack', parent=KITCHEN_TABLE,
    flags=[TAKEBIT, CONTBIT, BURNBIT],
    props=[
        (P_SYNONYM, z.words(_W['bag'], _W['sack'])),
        (P_ACTION, z.words(z.rtn(sandwich_bag_fcn))),
        (P_ADJECTIVE, z.bytes_(_A['brown'], _A['elongated'], _A['smelly'])),
        (P_SIZE, z.words(9)),
        (P_FDESC, z.words('On the table is an elongated brown sack, smelling of hot peppers.')),
        (P_CAPACITY, z.words(9)),
    ])
z.define_object(TOOL_CHEST, 'group of tool chests', parent=MAINTENANCE_ROOM,
    flags=[CONTBIT, OPENBIT, TRYTAKEBIT, SACREDBIT],
    props=[
        (P_SYNONYM, z.words(_W['chest'], _W['chests'], _W['group'], _W['toolchests'])),
        (P_ACTION, z.words(z.rtn(tool_chest_fcn))),
        (P_ADJECTIVE, z.bytes_(_A['tool'])),
    ])
z.define_object(YELLOW_BUTTON, 'yellow button', parent=MAINTENANCE_ROOM,
    flags=[NDESCBIT],
    props=[
        (P_SYNONYM, z.words(_W['button'], _W['switch'])),
        (P_ACTION, z.words(z.rtn(button_f))),
        (P_ADJECTIVE, z.bytes_(_A['yellow'])),
    ])
z.define_object(BROWN_BUTTON, 'brown button', parent=MAINTENANCE_ROOM,
    flags=[NDESCBIT],
    props=[
        (P_SYNONYM, z.words(_W['button'], _W['switch'])),
        (P_ACTION, z.words(z.rtn(button_f))),
        (P_ADJECTIVE, z.bytes_(_A['brown'])),
    ])
z.define_object(RED_BUTTON, 'red button', parent=MAINTENANCE_ROOM,
    flags=[NDESCBIT],
    props=[
        (P_SYNONYM, z.words(_W['button'], _W['switch'])),
        (P_ACTION, z.words(z.rtn(button_f))),
        (P_ADJECTIVE, z.bytes_(_A['red'])),
    ])
z.define_object(BLUE_BUTTON, 'blue button', parent=MAINTENANCE_ROOM,
    flags=[NDESCBIT],
    props=[
        (P_SYNONYM, z.words(_W['button'], _W['switch'])),
        (P_ACTION, z.words(z.rtn(button_f))),
        (P_ADJECTIVE, z.bytes_(_A['blue'])),
    ])
z.define_object(TROPHY_CASE, 'trophy case', parent=LIVING_ROOM,
    flags=[TRANSBIT, CONTBIT, NDESCBIT, TRYTAKEBIT, SEARCHBIT],
    props=[
        (P_SYNONYM, z.words(_W['case'])),
        (P_ACTION, z.words(z.rtn(trophy_case_fcn))),
        (P_ADJECTIVE, z.bytes_(_A['trophy'])),
        (P_CAPACITY, z.words(10000)),
    ])
z.define_object(RUG, 'carpet', parent=LIVING_ROOM,
    flags=[NDESCBIT, TRYTAKEBIT],
    props=[
        (P_SYNONYM, z.words(_W['rug'], _W['carpet'])),
        (P_ACTION, z.words(z.rtn(rug_fcn))),
        (P_ADJECTIVE, z.bytes_(_A['large'], _A['oriental'])),
    ])
z.define_object(CHALICE, 'chalice', parent=TREASURE_ROOM,
    flags=[TAKEBIT, TRYTAKEBIT, CONTBIT],
    props=[
        (P_SYNONYM, z.words(_W['chalice'], _W['cup'], _W['silver'], _W['treasure'])),
        (P_ACTION, z.words(z.rtn(chalice_fcn))),
        (P_ADJECTIVE, z.bytes_(_A['silver'], _A['engravings'])),
        (P_SIZE, z.words(10)),
        (P_VALUE, z.words(10)),
        (P_TVALUE, z.words(5)),
        (P_LDESC, z.words('There is a silver chalice, intricately engraved, here.')),
        (P_CAPACITY, z.words(5)),
    ])
z.define_object(GARLIC, 'clove of garlic', parent=SANDWICH_BAG,
    flags=[TAKEBIT, FOODBIT],
    props=[
        (P_SYNONYM, z.words(_W['garlic'], _W['clove'])),
        (P_ACTION, z.words(z.rtn(garlic_f))),
        (P_SIZE, z.words(4)),
    ])
z.define_object(TRIDENT, 'crystal trident', parent=ATLANTIS_ROOM,
    flags=[TAKEBIT],
    props=[
        (P_SYNONYM, z.words(_W['trident'], _W['fork'], _W['treasure'])),
        (P_ADJECTIVE, z.bytes_(_A['poseidon'], _A['own'], _A['crystal'])),
        (P_SIZE, z.words(20)),
        (P_FDESC, z.words("On the shore lies Poseidon's own crystal trident.")),
        (P_VALUE, z.words(4)),
        (P_TVALUE, z.words(11)),
    ])
z.define_object(CYCLOPS, 'cyclops', parent=CYCLOPS_ROOM,
    flags=[ACTORBIT, NDESCBIT, TRYTAKEBIT],
    props=[
        (P_SYNONYM, z.words(_W['cyclops'], _W['monster'], _W['eye'])),
        (P_ACTION, z.words(z.rtn(cyclops_fcn))),
        (P_ADJECTIVE, z.bytes_(_A['hungry'], _A['giant'])),
        (P_STRENGTH, z.words(10000)),
    ])
z.define_object(DAM, 'dam', parent=DAM_ROOM,
    flags=[NDESCBIT, TRYTAKEBIT],
    props=[
        (P_SYNONYM, z.words(_W['dam'], _W['gate'], _W['gates'], _W['fcd#3'])),
        (P_ACTION, z.words(z.rtn(dam_function))),
    ])
z.define_object(TRAP_DOOR, 'trap door', parent=LIVING_ROOM,
    flags=[DOORBIT, NDESCBIT, INVISIBLE],
    props=[
        (P_SYNONYM, z.words(_W['door'], _W['trapdoor'], _W['trap-door'], _W['cover'])),
        (P_ACTION, z.words(z.rtn(trap_door_fcn))),
        (P_ADJECTIVE, z.bytes_(_A['trap'], _A['dusty'])),
    ])
z.define_object(BOARDED_WINDOW, 'boarded window', parent=LOCAL_GLOBALS,
    flags=[NDESCBIT],
    props=[
        (P_SYNONYM, z.words(_W['window'])),
        (P_ACTION, z.words(z.rtn(boarded_window_fcn))),
        (P_ADJECTIVE, z.bytes_(_A['boarded'])),
    ])
z.define_object(FRONT_DOOR, 'door', parent=WEST_OF_HOUSE,
    flags=[DOORBIT, NDESCBIT],
    props=[
        (P_SYNONYM, z.words(_W['door'])),
        (P_ACTION, z.words(z.rtn(front_door_fcn))),
        (P_ADJECTIVE, z.bytes_(_A['front'], _A['boarded'])),
    ])
z.define_object(BARROW_DOOR, 'stone door', parent=STONE_BARROW,
    flags=[DOORBIT, NDESCBIT, OPENBIT],
    props=[
        (P_SYNONYM, z.words(_W['door'])),
        (P_ACTION, z.words(z.rtn(barrow_door_fcn))),
        (P_ADJECTIVE, z.bytes_(_A['huge'], _A['stone'])),
    ])
z.define_object(BARROW, 'stone barrow', parent=STONE_BARROW,
    flags=[NDESCBIT],
    props=[
        (P_SYNONYM, z.words(_W['barrow'], _W['tomb'])),
        (P_ACTION, z.words(z.rtn(barrow_fcn))),
        (P_ADJECTIVE, z.bytes_(_A['massive'], _A['stone'])),
    ])
z.define_object(BOTTLE, 'glass bottle', parent=KITCHEN_TABLE,
    flags=[TAKEBIT, TRANSBIT, CONTBIT],
    props=[
        (P_SYNONYM, z.words(_W['bottle'], _W['container'])),
        (P_ACTION, z.words(z.rtn(bottle_function))),
        (P_ADJECTIVE, z.bytes_(_A['clear'], _A['glass'])),
        (P_FDESC, z.words('A bottle is sitting on the table.')),
        (P_CAPACITY, z.words(4)),
    ])
z.define_object(CRACK, 'crack', parent=LOCAL_GLOBALS,
    flags=[NDESCBIT],
    props=[
        (P_SYNONYM, z.words(_W['crack'])),
        (P_ACTION, z.words(z.rtn(crack_fcn))),
        (P_ADJECTIVE, z.bytes_(_A['narrow'])),
    ])
z.define_object(COFFIN, 'gold coffin', parent=EGYPT_ROOM,
    flags=[TAKEBIT, CONTBIT, SACREDBIT, SEARCHBIT],
    props=[
        (P_SYNONYM, z.words(_W['coffin'], _W['casket'], _W['treasure'])),
        (P_ADJECTIVE, z.bytes_(_A['solid'], _A['gold'])),
        (P_SIZE, z.words(55)),
        (P_VALUE, z.words(10)),
        (P_TVALUE, z.words(15)),
        (P_LDESC, z.words('The solid-gold coffin used for the burial of Ramses II is here.')),
        (P_CAPACITY, z.words(35)),
    ])
z.define_object(GRATE, 'grating', parent=LOCAL_GLOBALS,
    flags=[DOORBIT, NDESCBIT, INVISIBLE],
    props=[
        (P_SYNONYM, z.words(_W['grate'], _W['grating'])),
        (P_ACTION, z.words(z.rtn(grate_function))),
    ])
z.define_object(PUMP, 'hand-held air pump', parent=RESERVOIR_NORTH,
    flags=[TAKEBIT, TOOLBIT],
    props=[
        (P_SYNONYM, z.words(_W['pump'], _W['air-pump'], _W['tool'], _W['tools'])),
        (P_ADJECTIVE, z.bytes_(_A['small'], _A['hand-held'])),
    ])
z.define_object(DIAMOND, 'huge diamond', parent=0,
    flags=[TAKEBIT],
    props=[
        (P_SYNONYM, z.words(_W['diamond'], _W['treasure'])),
        (P_ADJECTIVE, z.bytes_(_A['huge'], _A['enormous'])),
        (P_VALUE, z.words(10)),
        (P_TVALUE, z.words(10)),
        (P_LDESC, z.words('There is an enormous diamond (perfectly cut) here.')),
    ])
z.define_object(JADE, 'jade figurine', parent=BAT_ROOM,
    flags=[TAKEBIT],
    props=[
        (P_SYNONYM, z.words(_W['figurine'], _W['treasure'])),
        (P_ADJECTIVE, z.bytes_(_A['exquisite'], _A['jade'])),
        (P_SIZE, z.words(10)),
        (P_VALUE, z.words(5)),
        (P_TVALUE, z.words(5)),
        (P_LDESC, z.words('There is an exquisite jade figurine here.')),
    ])
z.define_object(KNIFE, 'nasty knife', parent=ATTIC_TABLE,
    flags=[TAKEBIT, WEAPONBIT, TRYTAKEBIT],
    props=[
        (P_SYNONYM, z.words(_W['knives'], _W['knife'], _W['blade'])),
        (P_ACTION, z.words(z.rtn(knife_f))),
        (P_ADJECTIVE, z.bytes_(_A['nasty'], _A['unrusty'])),
        (P_FDESC, z.words('On a table is a nasty-looking knife.')),
    ])
z.define_object(BONES, 'skeleton', parent=MAZE_5,
    flags=[TRYTAKEBIT, NDESCBIT],
    props=[
        (P_SYNONYM, z.words(_W['bones'], _W['skeleton'], _W['body'])),
        (P_ACTION, z.words(z.rtn(skeleton))),
    ])
z.define_object(BURNED_OUT_LANTERN, 'burned-out lantern', parent=MAZE_5,
    flags=[TAKEBIT],
    props=[
        (P_SYNONYM, z.words(_W['lantern'], _W['lamp'])),
        (P_ADJECTIVE, z.bytes_(_A['rusty'], _A['burned'], _A['dead'], _A['useless'])),
        (P_SIZE, z.words(20)),
        (P_FDESC, z.words("The deceased adventurer's useless lantern is here.")),
    ])
z.define_object(BAG_OF_COINS, 'leather bag of coins', parent=MAZE_5,
    flags=[TAKEBIT],
    props=[
        (P_SYNONYM, z.words(_W['bag'], _W['coins'], _W['treasure'])),
        (P_ACTION, z.words(z.rtn(bag_of_coins_f))),
        (P_ADJECTIVE, z.bytes_(_A['old'], _A['leather'])),
        (P_SIZE, z.words(15)),
        (P_VALUE, z.words(10)),
        (P_TVALUE, z.words(5)),
        (P_LDESC, z.words('An old leather bag, bulging with coins, is here.')),
    ])
z.define_object(LAMP, 'brass lantern', parent=LIVING_ROOM,
    flags=[TAKEBIT, LIGHTBIT],
    props=[
        (P_SYNONYM, z.words(_W['lamp'], _W['lantern'], _W['light'])),
        (P_ACTION, z.words(z.rtn(lantern))),
        (P_ADJECTIVE, z.bytes_(_A['brass'])),
        (P_SIZE, z.words(15)),
        (P_FDESC, z.words('A battery-powered brass lantern is on the trophy case.')),
        (P_LDESC, z.words('There is a brass lantern (battery-powered) here.')),
    ])
z.define_object(EMERALD, 'large emerald', parent=BUOY,
    flags=[TAKEBIT],
    props=[
        (P_SYNONYM, z.words(_W['emerald'], _W['treasure'])),
        (P_ADJECTIVE, z.bytes_(_A['large'])),
        (P_VALUE, z.words(5)),
        (P_TVALUE, z.words(10)),
    ])
z.define_object(ADVERTISEMENT, 'leaflet', parent=MAILBOX,
    flags=[READBIT, TAKEBIT, BURNBIT],
    props=[
        (P_SYNONYM, z.words(_W['advertisement'], _W['leaflet'], _W['booklet'], _W['mail'])),
        (P_ADJECTIVE, z.bytes_(_A['small'])),
        (P_SIZE, z.words(2)),
        (P_LDESC, z.words('A small leaflet is on the ground.')),
        (P_TEXT, z.words('"WELCOME TO ZORK!\n\nZORK is a game of adventure, danger, and low cunning. In it you will explore some of the most amazing territory ever seen by mortals. No computer should be without one!"')),
    ])
z.define_object(LEAK, 'leak', parent=MAINTENANCE_ROOM,
    flags=[NDESCBIT, INVISIBLE],
    props=[
        (P_SYNONYM, z.words(_W['leak'], _W['drip'], _W['pipe'])),
        (P_ACTION, z.words(z.rtn(leak_function))),
    ])
z.define_object(MACHINE, 'machine', parent=MACHINE_ROOM,
    flags=[CONTBIT, NDESCBIT, TRYTAKEBIT],
    props=[
        (P_SYNONYM, z.words(_W['machine'], _W['pdp10'], _W['dryer'], _W['lid'])),
        (P_ACTION, z.words(z.rtn(machine_f))),
        (P_CAPACITY, z.words(50)),
    ])
z.define_object(INFLATED_BOAT, 'magic boat', parent=0,
    flags=[TAKEBIT, BURNBIT, VEHBIT, OPENBIT, SEARCHBIT],
    props=[
        (P_SYNONYM, z.words(_W['boat'], _W['raft'])),
        (P_ACTION, z.words(z.rtn(rboat_function))),
        (P_ADJECTIVE, z.bytes_(_A['inflat'], _A['magic'], _A['plastic'], _A['seaworthy'])),
        (P_SIZE, z.words(20)),
        (P_CAPACITY, z.words(100)),
        (P_VTYPE, z.words(NONLANDBIT)),
    ])
z.define_object(MAILBOX, 'small mailbox', parent=WEST_OF_HOUSE,
    flags=[CONTBIT, TRYTAKEBIT],
    props=[
        (P_SYNONYM, z.words(_W['mailbox'], _W['box'])),
        (P_ACTION, z.words(z.rtn(mailbox_f))),
        (P_ADJECTIVE, z.bytes_(_A['small'])),
        (P_CAPACITY, z.words(10)),
    ])
z.define_object(MATCH, 'matchbook', parent=DAM_LOBBY,
    flags=[READBIT, TAKEBIT],
    props=[
        (P_SYNONYM, z.words(_W['match'], _W['matches'], _W['matchbook'])),
        (P_ACTION, z.words(z.rtn(match_function))),
        (P_ADJECTIVE, z.bytes_(_A['match'])),
        (P_SIZE, z.words(2)),
        (P_LDESC, z.words('There is a matchbook whose cover says "Visit Beautiful FCD#3" here.')),
        (P_TEXT, z.words('\n(Close cover before striking)\n\nYOU too can make BIG MONEY in the exciting field of PAPER SHUFFLING!\n\nMr. Anderson of Muddle, Mass. says: "Before I took this course I was a lowly bit twiddler. Now with what I learned at GUE Tech I feel really important and can obfuscate and confuse with the best."\n\nDr. Blank had this to say: "Ten short days ago all I could look forward to was a dead-end job as a doctor. Now I have a promising future and make really big Zorkmids."\n\nGUE Tech can\'t promise these fantastic results to everyone. But when you earn your degree from GUE Tech, your future will be brighter.')),
    ])
z.define_object(MIRROR_2, 'mirror', parent=MIRROR_ROOM_2,
    flags=[TRYTAKEBIT, NDESCBIT],
    props=[
        (P_SYNONYM, z.words(_W['reflection'], _W['mirror'], _W['enormous'])),
        (P_ACTION, z.words(z.rtn(mirror_mirror))),
    ])
z.define_object(MIRROR_1, 'mirror', parent=MIRROR_ROOM_1,
    flags=[TRYTAKEBIT, NDESCBIT],
    props=[
        (P_SYNONYM, z.words(_W['reflection'], _W['mirror'], _W['enormous'])),
        (P_ACTION, z.words(z.rtn(mirror_mirror))),
    ])
z.define_object(PAINTING, 'painting', parent=GALLERY,
    flags=[TAKEBIT, BURNBIT],
    props=[
        (P_SYNONYM, z.words(_W['painting'], _W['art'], _W['canvas'], _W['treasure'])),
        (P_ACTION, z.words(z.rtn(painting_fcn))),
        (P_ADJECTIVE, z.bytes_(_A['beauti'])),
        (P_SIZE, z.words(15)),
        (P_FDESC, z.words('Fortunately, there is still one chance for you to be a vandal, for on the far wall is a painting of unparalleled beauty.')),
        (P_VALUE, z.words(4)),
        (P_TVALUE, z.words(6)),
        (P_LDESC, z.words('A painting by a neglected genius is here.')),
    ])
z.define_object(CANDLES, 'pair of candles', parent=SOUTH_TEMPLE,
    flags=[TAKEBIT, FLAMEBIT, ONBIT, LIGHTBIT],
    props=[
        (P_SYNONYM, z.words(_W['candles'], _W['pair'])),
        (P_ACTION, z.words(z.rtn(candles_fcn))),
        (P_ADJECTIVE, z.bytes_(_A['burning'])),
        (P_SIZE, z.words(10)),
        (P_FDESC, z.words('On the two ends of the altar are burning candles.')),
    ])
z.define_object(GUNK, 'small piece of vitreous slag', parent=0,
    flags=[TAKEBIT, TRYTAKEBIT],
    props=[
        (P_SYNONYM, z.words(_W['gunk'], _W['piece'], _W['slag'])),
        (P_ACTION, z.words(z.rtn(gunk_function))),
        (P_ADJECTIVE, z.bytes_(_A['small'], _A['vitreous'])),
        (P_SIZE, z.words(10)),
    ])
z.define_object(BODIES, 'pile of bodies', parent=LOCAL_GLOBALS,
    flags=[NDESCBIT, TRYTAKEBIT],
    props=[
        (P_SYNONYM, z.words(_W['bodies'], _W['body'], _W['remains'], _W['pile'])),
        (P_ACTION, z.words(z.rtn(body_function))),
        (P_ADJECTIVE, z.bytes_(_A['mangled'])),
    ])
z.define_object(LEAVES, 'pile of leaves', parent=GRATING_CLEARING,
    flags=[TAKEBIT, BURNBIT, TRYTAKEBIT],
    props=[
        (P_SYNONYM, z.words(_W['leaves'], _W['leaf'], _W['pile'])),
        (P_ACTION, z.words(z.rtn(leaf_pile))),
        (P_SIZE, z.words(25)),
        (P_LDESC, z.words('On the ground is a pile of leaves.')),
    ])
z.define_object(PUNCTURED_BOAT, 'punctured boat', parent=0,
    flags=[TAKEBIT, BURNBIT],
    props=[
        (P_SYNONYM, z.words(_W['boat'], _W['pile'], _W['plastic'])),
        (P_ACTION, z.words(z.rtn(dboat_function))),
        (P_ADJECTIVE, z.bytes_(_A['plastic'], _A['puncture'], _A['large'])),
        (P_SIZE, z.words(20)),
    ])
z.define_object(INFLATABLE_BOAT, 'pile of plastic', parent=DAM_BASE,
    flags=[TAKEBIT, BURNBIT],
    props=[
        (P_SYNONYM, z.words(_W['boat'], _W['pile'], _W['plastic'], _W['valve'])),
        (P_ACTION, z.words(z.rtn(iboat_function))),
        (P_ADJECTIVE, z.bytes_(_A['plastic'], _A['inflat'])),
        (P_SIZE, z.words(20)),
        (P_LDESC, z.words('There is a folded pile of plastic here which has a small valve attached.')),
    ])
z.define_object(BAR, 'platinum bar', parent=LOUD_ROOM,
    flags=[TAKEBIT, SACREDBIT],
    props=[
        (P_SYNONYM, z.words(_W['bar'], _W['platinum'], _W['treasure'])),
        (P_ADJECTIVE, z.bytes_(_A['platinum'], _A['large'])),
        (P_SIZE, z.words(20)),
        (P_VALUE, z.words(10)),
        (P_TVALUE, z.words(5)),
        (P_LDESC, z.words('On the ground is a large platinum bar.')),
    ])
z.define_object(POT_OF_GOLD, 'pot of gold', parent=END_OF_RAINBOW,
    flags=[TAKEBIT, INVISIBLE],
    props=[
        (P_SYNONYM, z.words(_W['pot'], _W['gold'], _W['treasure'])),
        (P_ADJECTIVE, z.bytes_(_A['gold'])),
        (P_SIZE, z.words(15)),
        (P_FDESC, z.words('At the end of the rainbow is a pot of gold.')),
        (P_VALUE, z.words(10)),
        (P_TVALUE, z.words(10)),
    ])
z.define_object(PRAYER, 'prayer', parent=NORTH_TEMPLE,
    flags=[READBIT, SACREDBIT, NDESCBIT],
    props=[
        (P_SYNONYM, z.words(_W['prayer'], _W['inscription'])),
        (P_ADJECTIVE, z.bytes_(_A['ancient'], _A['old'])),
        (P_TEXT, z.words('The prayer is inscribed in an ancient script, rarely used today. It seems to be a philippic against small insects, absent-mindedness, and the picking up and dropping of small objects. The final verse consigns trespassers to the land of the dead. All evidence indicates that the beliefs of the ancient Zorkers were obscure.')),
    ])
z.define_object(RAILING, 'wooden railing', parent=DOME_ROOM,
    flags=[NDESCBIT],
    props=[
        (P_SYNONYM, z.words(_W['railing'], _W['rail'])),
        (P_ADJECTIVE, z.bytes_(_A['wooden'])),
    ])
z.define_object(RAINBOW, 'rainbow', parent=LOCAL_GLOBALS,
    flags=[NDESCBIT, CLIMBBIT],
    props=[
        (P_SYNONYM, z.words(_W['rainbow'])),
        (P_ACTION, z.words(z.rtn(rainbow_fcn))),
    ])
z.define_object(RIVER, 'river', parent=LOCAL_GLOBALS,
    flags=[NDESCBIT],
    props=[
        (P_SYNONYM, z.words(_W['river'])),
        (P_ACTION, z.words(z.rtn(river_function))),
        (P_ADJECTIVE, z.bytes_(_A['frigid'])),
    ])
z.define_object(BUOY, 'red buoy', parent=RIVER_4,
    flags=[TAKEBIT, CONTBIT],
    props=[
        (P_SYNONYM, z.words(_W['buoy'])),
        (P_ACTION, z.words(z.rtn(treasure_inside))),
        (P_ADJECTIVE, z.bytes_(_A['red'])),
        (P_SIZE, z.words(10)),
        (P_FDESC, z.words('There is a red buoy here (probably a warning).')),
        (P_CAPACITY, z.words(20)),
    ])
z.define_object(ROPE, 'rope', parent=ATTIC,
    flags=[TAKEBIT, SACREDBIT, TRYTAKEBIT],
    props=[
        (P_SYNONYM, z.words(_W['rope'], _W['hemp'], _W['coil'])),
        (P_ACTION, z.words(z.rtn(rope_function))),
        (P_ADJECTIVE, z.bytes_(_A['large'])),
        (P_SIZE, z.words(10)),
        (P_FDESC, z.words('A large coil of rope is lying in the corner.')),
    ])
z.define_object(RUSTY_KNIFE, 'rusty knife', parent=MAZE_5,
    flags=[TAKEBIT, TRYTAKEBIT, WEAPONBIT, TOOLBIT],
    props=[
        (P_SYNONYM, z.words(_W['knives'], _W['knife'])),
        (P_ACTION, z.words(z.rtn(rusty_knife_fcn))),
        (P_ADJECTIVE, z.bytes_(_A['rusty'])),
        (P_SIZE, z.words(20)),
        (P_FDESC, z.words('Beside the skeleton is a rusty knife.')),
    ])
z.define_object(SAND, 'sand', parent=SANDY_CAVE,
    flags=[NDESCBIT],
    props=[
        (P_SYNONYM, z.words(_W['sand'])),
        (P_ACTION, z.words(z.rtn(sand_function))),
    ])
z.define_object(BRACELET, 'sapphire-encrusted bracelet', parent=GAS_ROOM,
    flags=[TAKEBIT],
    props=[
        (P_SYNONYM, z.words(_W['bracelet'], _W['jewel'], _W['sapphire'], _W['treasure'])),
        (P_ADJECTIVE, z.bytes_(_A['sapphire'])),
        (P_SIZE, z.words(10)),
        (P_VALUE, z.words(5)),
        (P_TVALUE, z.words(5)),
    ])
z.define_object(SCREWDRIVER, 'screwdriver', parent=MAINTENANCE_ROOM,
    flags=[TAKEBIT, TOOLBIT],
    props=[
        (P_SYNONYM, z.words(_W['screwdriver'], _W['tool'], _W['tools'], _W['driver'])),
        (P_ADJECTIVE, z.bytes_(_A['screw'])),
    ])
z.define_object(KEYS, 'skeleton key', parent=MAZE_5,
    flags=[TAKEBIT, TOOLBIT],
    props=[
        (P_SYNONYM, z.words(_W['key'])),
        (P_ADJECTIVE, z.bytes_(_A['skeleton'])),
        (P_SIZE, z.words(10)),
    ])
z.define_object(SHOVEL, 'shovel', parent=SANDY_BEACH,
    flags=[TAKEBIT, TOOLBIT],
    props=[
        (P_SYNONYM, z.words(_W['shovel'], _W['tool'], _W['tools'])),
        (P_SIZE, z.words(15)),
    ])
z.define_object(COAL, 'small pile of coal', parent=DEAD_END_5,
    flags=[TAKEBIT, BURNBIT],
    props=[
        (P_SYNONYM, z.words(_W['coal'], _W['pile'], _W['heap'])),
        (P_ADJECTIVE, z.bytes_(_A['small'])),
        (P_SIZE, z.words(20)),
    ])
z.define_object(LADDER, 'wooden ladder', parent=LOCAL_GLOBALS,
    flags=[NDESCBIT, CLIMBBIT],
    props=[
        (P_SYNONYM, z.words(_W['ladder'])),
        (P_ADJECTIVE, z.bytes_(_A['wooden'], _A['rickety'], _A['narrow'])),
    ])
z.define_object(SCARAB, 'beautiful jeweled scarab', parent=SANDY_CAVE,
    flags=[TAKEBIT, INVISIBLE],
    props=[
        (P_SYNONYM, z.words(_W['scarab'], _W['bug'], _W['beetle'], _W['treasure'])),
        (P_ADJECTIVE, z.bytes_(_A['beauti'], _A['carved'], _A['jeweled'])),
        (P_SIZE, z.words(8)),
        (P_VALUE, z.words(5)),
        (P_TVALUE, z.words(5)),
    ])
z.define_object(LARGE_BAG, 'large bag', parent=THIEF,
    flags=[TRYTAKEBIT, NDESCBIT],
    props=[
        (P_SYNONYM, z.words(_W['bag'])),
        (P_ACTION, z.words(z.rtn(large_bag_f))),
        (P_ADJECTIVE, z.bytes_(_A['large'], _A['thiefs'])),
    ])
z.define_object(STILETTO, 'stiletto', parent=THIEF,
    flags=[WEAPONBIT, TRYTAKEBIT, TAKEBIT, NDESCBIT],
    props=[
        (P_SYNONYM, z.words(_W['stiletto'])),
        (P_ACTION, z.words(z.rtn(stiletto_function))),
        (P_ADJECTIVE, z.bytes_(_A['vicious'])),
        (P_SIZE, z.words(10)),
    ])
z.define_object(MACHINE_SWITCH, 'switch', parent=MACHINE_ROOM,
    flags=[NDESCBIT, TURNBIT],
    props=[
        (P_SYNONYM, z.words(_W['switch'])),
        (P_ACTION, z.words(z.rtn(mswitch_function))),
    ])
z.define_object(WOODEN_DOOR, 'wooden door', parent=LIVING_ROOM,
    flags=[READBIT, DOORBIT, NDESCBIT, TRANSBIT],
    props=[
        (P_SYNONYM, z.words(_W['door'], _W['lettering'], _W['writing'])),
        (P_ACTION, z.words(z.rtn(front_door_fcn))),
        (P_ADJECTIVE, z.bytes_(_A['wooden'], _A['gothic'], _A['strange'], _A['west'])),
        (P_TEXT, z.words('The engravings translate to "This space intentionally left blank."')),
    ])
z.define_object(SWORD, 'sword', parent=LIVING_ROOM,
    flags=[TAKEBIT, WEAPONBIT, TRYTAKEBIT],
    props=[
        (P_SYNONYM, z.words(_W['sword'], _W['orcrist'], _W['glamdring'], _W['blade'])),
        (P_ACTION, z.words(z.rtn(sword_fcn))),
        (P_ADJECTIVE, z.bytes_(_A['elvish'], _A['old'], _A['antique'])),
        (P_SIZE, z.words(30)),
        (P_FDESC, z.words('Above the trophy case hangs an elvish sword of great antiquity.')),
        (P_TVALUE, z.words(0)),
    ])
z.define_object(MAP, 'ancient map', parent=TROPHY_CASE,
    flags=[INVISIBLE, READBIT, TAKEBIT],
    props=[
        (P_SYNONYM, z.words(_W['parchment'], _W['map'])),
        (P_ADJECTIVE, z.bytes_(_A['antique'], _A['old'], _A['ancient'])),
        (P_SIZE, z.words(2)),
        (P_FDESC, z.words('In the trophy case is an ancient parchment which appears to be a map.')),
        (P_TEXT, z.words('The map shows a forest with three clearings. The largest clearing contains a house. Three paths leave the large clearing. One of these paths, leading southwest, is marked "To Stone Barrow".')),
    ])
z.define_object(BOAT_LABEL, 'tan label', parent=INFLATED_BOAT,
    flags=[READBIT, TAKEBIT, BURNBIT],
    props=[
        (P_SYNONYM, z.words(_W['label'], _W['fineprint'], _W['print'])),
        (P_ADJECTIVE, z.bytes_(_A['tan'], _A['fine'])),
        (P_SIZE, z.words(2)),
        (P_TEXT, z.words('  !!!!FROBOZZ MAGIC BOAT COMPANY!!!!\n\nHello, Sailor!\n\nInstructions for use:\n\n   To get into a body of water, say "Launch".\n   To get to shore, say "Land" or the direction in which you want to maneuver the boat.\n\nWarranty:\n\n  This boat is guaranteed against all defects for a period of 76 milliseconds from date of purchase or until first used, whichever comes first.\n\nWarning:\n   This boat is made of thin plastic.\n   Good Luck!')),
    ])
z.define_object(THIEF, 'thief', parent=ROUND_ROOM,
    flags=[ACTORBIT, INVISIBLE, CONTBIT, OPENBIT, TRYTAKEBIT],
    props=[
        (P_SYNONYM, z.words(_W['thief'], _W['robber'], _W['man'], _W['person'])),
        (P_ACTION, z.words(z.rtn(robber_function))),
        (P_ADJECTIVE, z.bytes_(_A['shady'], _A['suspicious'], _A['seedy'])),
        (P_LDESC, z.words('There is a suspicious-looking individual, holding a large bag, leaning against one wall. He is armed with a deadly stiletto.')),
        (P_STRENGTH, z.words(5)),
    ])
z.define_object(PEDESTAL, 'pedestal', parent=TORCH_ROOM,
    flags=[NDESCBIT, CONTBIT, OPENBIT, SURFACEBIT],
    props=[
        (P_SYNONYM, z.words(_W['pedestal'])),
        (P_ACTION, z.words(z.rtn(dumb_container))),
        (P_ADJECTIVE, z.bytes_(_A['white'], _A['marble'])),
        (P_CAPACITY, z.words(30)),
    ])
z.define_object(TORCH, 'torch', parent=PEDESTAL,
    flags=[TAKEBIT, FLAMEBIT, ONBIT, LIGHTBIT],
    props=[
        (P_SYNONYM, z.words(_W['torch'], _W['ivory'], _W['treasure'])),
        (P_ACTION, z.words(z.rtn(torch_object))),
        (P_ADJECTIVE, z.bytes_(_A['flaming'], _A['ivory'])),
        (P_SIZE, z.words(20)),
        (P_FDESC, z.words('Sitting on the pedestal is a flaming torch, made of ivory.')),
        (P_VALUE, z.words(14)),
        (P_TVALUE, z.words(6)),
    ])
z.define_object(GUIDE, 'tour guidebook', parent=DAM_LOBBY,
    flags=[READBIT, TAKEBIT, BURNBIT],
    props=[
        (P_SYNONYM, z.words(_W['guide'], _W['book'], _W['books'], _W['guidebooks'])),
        (P_ADJECTIVE, z.bytes_(_A['tour'], _A['guide'])),
        (P_FDESC, z.words('Some guidebooks entitled "Flood Control Dam #3" are on the reception desk.')),
        (P_TEXT, z.words('"\tFlood Control Dam #3\n\nFCD#3 was constructed in year 783 of the Great Underground Empire to harness the mighty Frigid River. This work was supported by a grant of 37 million zorkmids from your omnipotent local tyrant Lord Dimwit Flathead the Excessive. This impressive structure is composed of 370,000 cubic feet of concrete, is 256 feet tall at the center, and 193 feet wide at the top. The lake created behind the dam has a volume of 1.7 billion cubic feet, an area of 12 million square feet, and a shore line of 36 thousand feet.\n\nThe construction of FCD#3 took 112 days from ground breaking to the dedication. It required a work force of 384 slaves, 34 slave drivers, 12 engineers, 2 turtle doves, and a partridge in a pear tree. The work was managed by a command team composed of 2345 bureaucrats, 2347 secretaries (at least two of whom could type), 12,256 paper shufflers, 52,469 rubber stampers, 245,193 red tape processors, and nearly one million dead trees.\n\nWe will now point out some of the more interesting features of FCD#3 as we conduct you on a guided tour of the facilities:\n\n        1) You start your tour here in the Dam Lobby. You will notice on your right that....')),
    ])
z.define_object(TROLL, 'troll', parent=TROLL_ROOM,
    flags=[ACTORBIT, OPENBIT, TRYTAKEBIT],
    props=[
        (P_SYNONYM, z.words(_W['troll'])),
        (P_ACTION, z.words(z.rtn(troll_fcn))),
        (P_ADJECTIVE, z.bytes_(_A['nasty'])),
        (P_LDESC, z.words('A nasty-looking troll, brandishing a bloody axe, blocks all passages out of the room.')),
        (P_STRENGTH, z.words(2)),
    ])
z.define_object(TRUNK, 'trunk of jewels', parent=RESERVOIR,
    flags=[TAKEBIT, INVISIBLE],
    props=[
        (P_SYNONYM, z.words(_W['trunk'], _W['chest'], _W['jewels'], _W['treasure'])),
        (P_ACTION, z.words(z.rtn(trunk_f))),
        (P_ADJECTIVE, z.bytes_(_A['old'])),
        (P_SIZE, z.words(35)),
        (P_FDESC, z.words('Lying half buried in the mud is an old trunk, bulging with jewels.')),
        (P_VALUE, z.words(15)),
        (P_TVALUE, z.words(5)),
        (P_LDESC, z.words('There is an old trunk here, bulging with assorted jewels.')),
    ])
z.define_object(TUBE, 'tube', parent=MAINTENANCE_ROOM,
    flags=[TAKEBIT, CONTBIT, READBIT],
    props=[
        (P_SYNONYM, z.words(_W['tube'], _W['tooth'], _W['paste'])),
        (P_ACTION, z.words(z.rtn(tube_function))),
        (P_SIZE, z.words(5)),
        (P_LDESC, z.words('There is an object which looks like a tube of toothpaste here.')),
        (P_CAPACITY, z.words(7)),
        (P_TEXT, z.words('---> Frobozz Magic Gunk Company <---\n\t  All-Purpose Gunk')),
    ])
z.define_object(PUTTY, 'viscous material', parent=TUBE,
    flags=[TAKEBIT, TOOLBIT],
    props=[
        (P_SYNONYM, z.words(_W['material'], _W['gunk'])),
        (P_ACTION, z.words(z.rtn(putty_fcn))),
        (P_ADJECTIVE, z.bytes_(_A['viscous'])),
        (P_SIZE, z.words(6)),
    ])
z.define_object(ENGRAVINGS, 'wall with engravings', parent=ENGRAVINGS_CAVE,
    flags=[READBIT, SACREDBIT],
    props=[
        (P_SYNONYM, z.words(_W['wall'], _W['engravings'], _W['inscription'])),
        (P_ADJECTIVE, z.bytes_(_A['old'], _A['ancient'])),
        (P_LDESC, z.words('There are old engravings on the walls here.')),
        (P_TEXT, z.words('The engravings were incised in the living rock of the cave wall by an unknown hand. They depict, in symbolic form, the beliefs of the ancient Zorkers. Skillfully interwoven with the bas reliefs are excerpts illustrating the major religious tenets of that time. Unfortunately, a later age seems to have considered them blasphemous and just as skillfully excised them.')),
    ])
z.define_object(OWNERS_MANUAL, "ZORK owner's manual", parent=STUDIO,
    flags=[READBIT, TAKEBIT],
    props=[
        (P_SYNONYM, z.words(_W['manual'], _W['piece'], _W['paper'])),
        (P_ADJECTIVE, z.bytes_(_A['zork'], _A['owners'], _A['small'])),
        (P_FDESC, z.words('Loosely attached to a wall is a small piece of paper.')),
        (P_TEXT, z.words('Congratulations!\n\nYou are the privileged owner of ZORK I: The Great Underground Empire, a self-contained and self-maintaining universe. If used and maintained in accordance with normal operating practices for small universes, ZORK will provide many months of trouble-free operation.')),
    ])
z.define_object(CLIMBABLE_CLIFF, 'cliff', parent=LOCAL_GLOBALS,
    flags=[NDESCBIT, CLIMBBIT],
    props=[
        (P_SYNONYM, z.words(_W['wall'], _W['cliff'], _W['walls'], _W['ledge'])),
        (P_ACTION, z.words(z.rtn(cliff_object))),
        (P_ADJECTIVE, z.bytes_(_A['rocky'], _A['sheer'])),
    ])
z.define_object(WHITE_CLIFF, 'white cliffs', parent=LOCAL_GLOBALS,
    flags=[NDESCBIT, CLIMBBIT],
    props=[
        (P_SYNONYM, z.words(_W['cliff'], _W['cliffs'])),
        (P_ACTION, z.words(z.rtn(wclif_object))),
        (P_ADJECTIVE, z.bytes_(_A['white'])),
    ])
z.define_object(WRENCH, 'wrench', parent=MAINTENANCE_ROOM,
    flags=[TAKEBIT, TOOLBIT],
    props=[
        (P_SYNONYM, z.words(_W['wrench'], _W['tool'], _W['tools'])),
        (P_SIZE, z.words(10)),
    ])
z.define_object(CONTROL_PANEL, 'control panel', parent=DAM_ROOM,
    flags=[NDESCBIT],
    props=[
        (P_SYNONYM, z.words(_W['panel'])),
        (P_ADJECTIVE, z.bytes_(_A['control'])),
    ])
z.define_object(NEST, "bird's nest", parent=UP_A_TREE,
    flags=[TAKEBIT, BURNBIT, CONTBIT, OPENBIT, SEARCHBIT],
    props=[
        (P_SYNONYM, z.words(_W['nest'])),
        (P_ADJECTIVE, z.bytes_(_A['birds'])),
        (P_FDESC, z.words("Beside you on the branch is a small bird's nest.")),
        (P_CAPACITY, z.words(20)),
    ])
z.define_object(EGG, 'jewel-encrusted egg', parent=NEST,
    flags=[TAKEBIT, CONTBIT, SEARCHBIT],
    props=[
        (P_SYNONYM, z.words(_W['egg'], _W['treasure'])),
        (P_ACTION, z.words(z.rtn(egg_object))),
        (P_ADJECTIVE, z.bytes_(_A['birds'], _A['encrusted'], _A['jeweled'])),
        (P_FDESC, z.words("In the bird's nest is a large egg encrusted with precious jewels, apparently scavenged by a childless songbird. The egg is covered with fine gold inlay, and ornamented in lapis lazuli and mother-of-pearl. Unlike most eggs, this one is hinged and closed with a delicate looking clasp. The egg appears extremely fragile.")),
        (P_VALUE, z.words(5)),
        (P_TVALUE, z.words(5)),
        (P_CAPACITY, z.words(6)),
    ])
z.define_object(BROKEN_EGG, 'broken jewel-encrusted egg', parent=0,
    flags=[TAKEBIT, CONTBIT, OPENBIT],
    props=[
        (P_SYNONYM, z.words(_W['egg'], _W['treasure'])),
        (P_ADJECTIVE, z.bytes_(_A['broken'], _A['birds'], _A['encrusted'], _A['jewel'])),
        (P_TVALUE, z.words(2)),
        (P_LDESC, z.words('There is a somewhat ruined egg here.')),
        (P_CAPACITY, z.words(6)),
    ])
z.define_object(BAUBLE, 'beautiful brass bauble', parent=0,
    flags=[TAKEBIT],
    props=[
        (P_SYNONYM, z.words(_W['bauble'], _W['treasure'])),
        (P_ADJECTIVE, z.bytes_(_A['brass'], _A['beauti'])),
        (P_VALUE, z.words(1)),
        (P_TVALUE, z.words(1)),
    ])
z.define_object(CANARY, 'golden clockwork canary', parent=EGG,
    flags=[TAKEBIT, SEARCHBIT],
    props=[
        (P_SYNONYM, z.words(_W['canary'], _W['treasure'])),
        (P_ACTION, z.words(z.rtn(canary_object))),
        (P_ADJECTIVE, z.bytes_(_A['clockwork'], _A['gold'], _A['golden'])),
        (P_FDESC, z.words('There is a golden clockwork canary nestled in the egg. It has ruby eyes and a silver beak. Through a crystal window below its left wing you can see intricate machinery inside. It appears to have wound down.')),
        (P_VALUE, z.words(6)),
        (P_TVALUE, z.words(4)),
    ])
z.define_object(BROKEN_CANARY, 'broken clockwork canary', parent=BROKEN_EGG,
    flags=[TAKEBIT],
    props=[
        (P_SYNONYM, z.words(_W['canary'], _W['treasure'])),
        (P_ACTION, z.words(z.rtn(canary_object))),
        (P_ADJECTIVE, z.bytes_(_A['broken'], _A['clockwork'], _A['gold'], _A['golden'])),
        (P_FDESC, z.words('There is a golden clockwork canary nestled in the egg. It seems to have recently had a bad experience. The mountings for its jewel-like eyes are empty, and its silver beak is crumpled. Through a cracked crystal window below its left wing you can see the remains of intricate machinery. It is not clear what result winding it would have, as the mainspring seems sprung.')),
        (P_TVALUE, z.words(1)),
    ])
z.define_object(WEST_OF_HOUSE, 'West of House', parent=ROOMS,
    flags=[RLANDBIT, ONBIT, SACREDBIT],
    props=[
        (P_NORTH, z.uexit(NORTH_OF_HOUSE)),
        (P_EAST, z.nexit("The door is boarded and you can't remove the boards.")),
        (P_WEST, z.uexit(FOREST_1)),
        (P_SOUTH, z.uexit(SOUTH_OF_HOUSE)),
        (P_NE, z.uexit(NORTH_OF_HOUSE)),
        (P_SE, z.uexit(SOUTH_OF_HOUSE)),
        (P_SW, z.cexit(STONE_BARROW, 'WON_FLAG', 0)),
        (P_IN, z.cexit(STONE_BARROW, 'WON_FLAG', 0)),
        (P_ACTION, z.words(z.rtn(west_house))),
        (P_GLOBAL, z.bytes_(WHITE_HOUSE, BOARD, FOREST)),
    ])
z.define_object(STONE_BARROW, 'Stone Barrow', parent=ROOMS,
    flags=[RLANDBIT, ONBIT, SACREDBIT],
    props=[
        (P_NE, z.uexit(WEST_OF_HOUSE)),
        (P_ACTION, z.words(z.rtn(stone_barrow_fcn))),
        (P_LDESC, z.words('You are standing in front of a massive barrow of stone. In the east face is a huge stone door which is open. You cannot see into the dark of the tomb.')),
    ])
z.define_object(NORTH_OF_HOUSE, 'North of House', parent=ROOMS,
    flags=[RLANDBIT, ONBIT, SACREDBIT],
    props=[
        (P_NORTH, z.uexit(PATH)),
        (P_EAST, z.uexit(EAST_OF_HOUSE)),
        (P_WEST, z.uexit(WEST_OF_HOUSE)),
        (P_SOUTH, z.nexit('The windows are all boarded.')),
        (P_SE, z.uexit(EAST_OF_HOUSE)),
        (P_SW, z.uexit(WEST_OF_HOUSE)),
        (P_LDESC, z.words('You are facing the north side of a white house. There is no door here, and all the windows are boarded up. To the north a narrow path winds through the trees.')),
        (P_GLOBAL, z.bytes_(BOARDED_WINDOW, BOARD, WHITE_HOUSE, FOREST)),
    ])
z.define_object(SOUTH_OF_HOUSE, 'South of House', parent=ROOMS,
    flags=[RLANDBIT, ONBIT, SACREDBIT],
    props=[
        (P_NORTH, z.nexit('The windows are all boarded.')),
        (P_EAST, z.uexit(EAST_OF_HOUSE)),
        (P_WEST, z.uexit(WEST_OF_HOUSE)),
        (P_SOUTH, z.uexit(FOREST_3)),
        (P_NE, z.uexit(EAST_OF_HOUSE)),
        (P_NW, z.uexit(WEST_OF_HOUSE)),
        (P_LDESC, z.words('You are facing the south side of a white house. There is no door here, and all the windows are boarded.')),
        (P_GLOBAL, z.bytes_(BOARDED_WINDOW, BOARD, WHITE_HOUSE, FOREST)),
    ])
z.define_object(EAST_OF_HOUSE, 'Behind House', parent=ROOMS,
    flags=[RLANDBIT, ONBIT, SACREDBIT],
    props=[
        (P_NORTH, z.uexit(NORTH_OF_HOUSE)),
        (P_EAST, z.uexit(CLEARING)),
        (P_WEST, z.dexit(KITCHEN, KITCHEN_WINDOW, 0)),
        (P_SOUTH, z.uexit(SOUTH_OF_HOUSE)),
        (P_NW, z.uexit(NORTH_OF_HOUSE)),
        (P_SW, z.uexit(SOUTH_OF_HOUSE)),
        (P_IN, z.dexit(KITCHEN, KITCHEN_WINDOW, 0)),
        (P_ACTION, z.words(z.rtn(east_house))),
        (P_GLOBAL, z.bytes_(WHITE_HOUSE, KITCHEN_WINDOW, FOREST)),
    ])
z.define_object(FOREST_1, 'Forest', parent=ROOMS,
    flags=[RLANDBIT, ONBIT, SACREDBIT],
    props=[
        (P_NORTH, z.uexit(GRATING_CLEARING)),
        (P_EAST, z.uexit(PATH)),
        (P_WEST, z.nexit('You would need a machete to go further west.')),
        (P_SOUTH, z.uexit(FOREST_3)),
        (P_UP, z.nexit('There is no tree here suitable for climbing.')),
        (P_ACTION, z.words(z.rtn(forest_room))),
        (P_LDESC, z.words('This is a forest, with trees in all directions. To the east, there appears to be sunlight.')),
        (P_GLOBAL, z.bytes_(TREE, SONGBIRD, WHITE_HOUSE, FOREST)),
    ])
z.define_object(FOREST_2, 'Forest', parent=ROOMS,
    flags=[RLANDBIT, ONBIT, SACREDBIT],
    props=[
        (P_NORTH, z.nexit('The forest becomes impenetrable to the north.')),
        (P_EAST, z.uexit(MOUNTAINS)),
        (P_WEST, z.uexit(PATH)),
        (P_SOUTH, z.uexit(CLEARING)),
        (P_UP, z.nexit('There is no tree here suitable for climbing.')),
        (P_ACTION, z.words(z.rtn(forest_room))),
        (P_LDESC, z.words('This is a dimly lit forest, with large trees all around.')),
        (P_GLOBAL, z.bytes_(TREE, SONGBIRD, WHITE_HOUSE, FOREST)),
    ])
z.define_object(MOUNTAINS, 'Forest', parent=ROOMS,
    flags=[RLANDBIT, ONBIT, SACREDBIT],
    props=[
        (P_NORTH, z.uexit(FOREST_2)),
        (P_EAST, z.nexit('The mountains are impassable.')),
        (P_WEST, z.uexit(FOREST_2)),
        (P_SOUTH, z.uexit(FOREST_2)),
        (P_UP, z.nexit('The mountains are impassable.')),
        (P_LDESC, z.words('The forest thins out, revealing impassable mountains.')),
        (P_GLOBAL, z.bytes_(TREE, WHITE_HOUSE)),
    ])
z.define_object(FOREST_3, 'Forest', parent=ROOMS,
    flags=[RLANDBIT, ONBIT, SACREDBIT],
    props=[
        (P_NORTH, z.uexit(CLEARING)),
        (P_EAST, z.nexit('The rank undergrowth prevents eastward movement.')),
        (P_WEST, z.uexit(FOREST_1)),
        (P_SOUTH, z.nexit('Storm-tossed trees block your way.')),
        (P_NW, z.uexit(SOUTH_OF_HOUSE)),
        (P_UP, z.nexit('There is no tree here suitable for climbing.')),
        (P_ACTION, z.words(z.rtn(forest_room))),
        (P_LDESC, z.words('This is a dimly lit forest, with large trees all around.')),
        (P_GLOBAL, z.bytes_(TREE, SONGBIRD, WHITE_HOUSE, FOREST)),
    ])
z.define_object(PATH, 'Forest Path', parent=ROOMS,
    flags=[RLANDBIT, ONBIT, SACREDBIT],
    props=[
        (P_NORTH, z.uexit(GRATING_CLEARING)),
        (P_EAST, z.uexit(FOREST_2)),
        (P_WEST, z.uexit(FOREST_1)),
        (P_SOUTH, z.uexit(NORTH_OF_HOUSE)),
        (P_UP, z.uexit(UP_A_TREE)),
        (P_ACTION, z.words(z.rtn(forest_room))),
        (P_LDESC, z.words('This is a path winding through a dimly lit forest. The path heads north-south here. One particularly large tree with some low branches stands at the edge of the path.')),
        (P_GLOBAL, z.bytes_(TREE, SONGBIRD, WHITE_HOUSE, FOREST)),
    ])
z.define_object(UP_A_TREE, 'Up a Tree', parent=ROOMS,
    flags=[RLANDBIT, ONBIT, SACREDBIT],
    props=[
        (P_UP, z.nexit('You cannot climb any higher.')),
        (P_DOWN, z.uexit(PATH)),
        (P_ACTION, z.words(z.rtn(tree_room))),
        (P_GLOBAL, z.bytes_(TREE, FOREST, SONGBIRD, WHITE_HOUSE)),
    ])
z.define_object(GRATING_CLEARING, 'Clearing', parent=ROOMS,
    flags=[RLANDBIT, ONBIT, SACREDBIT],
    props=[
        (P_NORTH, z.nexit('The forest becomes impenetrable to the north.')),
        (P_EAST, z.uexit(FOREST_2)),
        (P_WEST, z.uexit(FOREST_1)),
        (P_SOUTH, z.uexit(PATH)),
        (P_DOWN, z.fexit(z.rtn(grating_exit))),
        (P_ACTION, z.words(z.rtn(clearing_fcn))),
        (P_GLOBAL, z.bytes_(WHITE_HOUSE, GRATE)),
    ])
z.define_object(CLEARING, 'Clearing', parent=ROOMS,
    flags=[RLANDBIT, ONBIT, SACREDBIT],
    props=[
        (P_NORTH, z.uexit(FOREST_2)),
        (P_EAST, z.uexit(CANYON_VIEW)),
        (P_WEST, z.uexit(EAST_OF_HOUSE)),
        (P_SOUTH, z.uexit(FOREST_3)),
        (P_UP, z.nexit('There is no tree here suitable for climbing.')),
        (P_ACTION, z.words(z.rtn(forest_room))),
        (P_LDESC, z.words('You are in a small clearing in a well marked forest path that extends to the east and west.')),
        (P_GLOBAL, z.bytes_(TREE, SONGBIRD, WHITE_HOUSE, FOREST)),
    ])
z.define_object(KITCHEN, 'Kitchen', parent=ROOMS,
    flags=[RLANDBIT, ONBIT, SACREDBIT],
    props=[
        (P_EAST, z.dexit(EAST_OF_HOUSE, KITCHEN_WINDOW, 0)),
        (P_WEST, z.uexit(LIVING_ROOM)),
        (P_UP, z.uexit(ATTIC)),
        (P_DOWN, z.cexit(STUDIO, 'FALSE_FLAG', 'Only Santa Claus climbs down chimneys.')),
        (P_OUT, z.dexit(EAST_OF_HOUSE, KITCHEN_WINDOW, 0)),
        (P_ACTION, z.words(z.rtn(kitchen_fcn))),
        (P_VALUE, z.words(10)),
        (P_GLOBAL, z.bytes_(KITCHEN_WINDOW, CHIMNEY, STAIRS)),
    ])
z.define_object(ATTIC, 'Attic', parent=ROOMS,
    flags=[RLANDBIT, SACREDBIT],
    props=[
        (P_DOWN, z.uexit(KITCHEN)),
        (P_LDESC, z.words('This is the attic. The only exit is a stairway leading down.')),
        (P_GLOBAL, z.bytes_(STAIRS)),
    ])
z.define_object(LIVING_ROOM, 'Living Room', parent=ROOMS,
    flags=[RLANDBIT, ONBIT, SACREDBIT],
    props=[
        (P_EAST, z.uexit(KITCHEN)),
        (P_WEST, z.cexit(STRANGE_PASSAGE, 'MAGIC_FLAG', 'The door is nailed shut.')),
        (P_DOWN, z.fexit(z.rtn(trap_door_exit))),
        (P_ACTION, z.words(z.rtn(living_room_fcn))),
        (P_GLOBAL, z.bytes_(STAIRS)),
        (P_PSEUDO, z.words(_W['nails'], z.rtn(nails_pseudo), _W['nail'], z.rtn(nails_pseudo))),
    ])
z.define_object(CELLAR, 'Cellar', parent=ROOMS,
    flags=[RLANDBIT],
    props=[
        (P_NORTH, z.uexit(TROLL_ROOM)),
        (P_WEST, z.nexit('You try to ascend the ramp, but it is impossible, and you slide back down.')),
        (P_SOUTH, z.uexit(EAST_OF_CHASM)),
        (P_UP, z.dexit(LIVING_ROOM, TRAP_DOOR, 0)),
        (P_ACTION, z.words(z.rtn(cellar_fcn))),
        (P_VALUE, z.words(25)),
        (P_GLOBAL, z.bytes_(TRAP_DOOR, SLIDE, STAIRS)),
    ])
z.define_object(TROLL_ROOM, 'The Troll Room', parent=ROOMS,
    flags=[RLANDBIT],
    props=[
        (P_EAST, z.cexit(EW_PASSAGE, 'TROLL_FLAG', 'The troll fends you off with a menacing gesture.')),
        (P_WEST, z.cexit(MAZE_1, 'TROLL_FLAG', 'The troll fends you off with a menacing gesture.')),
        (P_SOUTH, z.uexit(CELLAR)),
        (P_ACTION, z.words(z.rtn(troll_room_f))),
        (P_LDESC, z.words('This is a small room with passages to the east and south and a forbidding hole leading west. Bloodstains and deep scratches (perhaps made by an axe) mar the walls.')),
    ])
z.define_object(EAST_OF_CHASM, 'East of Chasm', parent=ROOMS,
    flags=[RLANDBIT],
    props=[
        (P_NORTH, z.uexit(CELLAR)),
        (P_EAST, z.uexit(GALLERY)),
        (P_DOWN, z.nexit('The chasm probably leads straight to the infernal regions.')),
        (P_LDESC, z.words('You are on the east edge of a chasm, the bottom of which cannot be seen. A narrow passage goes north, and the path you are on continues to the east.')),
        (P_PSEUDO, z.words(_W['chasm'], z.rtn(chasm_pseudo))),
    ])
z.define_object(GALLERY, 'Gallery', parent=ROOMS,
    flags=[RLANDBIT, ONBIT],
    props=[
        (P_NORTH, z.uexit(STUDIO)),
        (P_WEST, z.uexit(EAST_OF_CHASM)),
        (P_LDESC, z.words('This is an art gallery. Most of the paintings have been stolen by vandals with exceptional taste. The vandals left through either the north or west exits.')),
    ])
z.define_object(STUDIO, 'Studio', parent=ROOMS,
    flags=[RLANDBIT],
    props=[
        (P_SOUTH, z.uexit(GALLERY)),
        (P_UP, z.fexit(z.rtn(up_chimney_function))),
        (P_LDESC, z.words("This appears to have been an artist's studio. The walls and floors are splattered with paints of 69 different colors. Strangely enough, nothing of value is hanging here. At the south end of the room is an open door (also covered with paint). A dark and narrow chimney leads up from a fireplace; although you might be able to get up it, it seems unlikely you could get back down.")),
        (P_GLOBAL, z.bytes_(CHIMNEY)),
        (P_PSEUDO, z.words(_W['door'], z.rtn(door_pseudo), _W['paint'], z.rtn(paint_pseudo))),
    ])
z.define_object(MAZE_1, 'Maze', parent=ROOMS,
    flags=[RLANDBIT, MAZEBIT],
    props=[
        (P_NORTH, z.uexit(MAZE_1)),
        (P_EAST, z.uexit(TROLL_ROOM)),
        (P_WEST, z.uexit(MAZE_4)),
        (P_SOUTH, z.uexit(MAZE_2)),
        (P_LDESC, z.words('This is part of a maze of twisty little passages, all alike.')),
    ])
z.define_object(MAZE_2, 'Maze', parent=ROOMS,
    flags=[RLANDBIT, MAZEBIT],
    props=[
        (P_EAST, z.uexit(MAZE_3)),
        (P_SOUTH, z.uexit(MAZE_1)),
        (P_DOWN, z.fexit(z.rtn(maze_diodes))),
        (P_LDESC, z.words('This is part of a maze of twisty little passages, all alike.')),
    ])
z.define_object(MAZE_3, 'Maze', parent=ROOMS,
    flags=[RLANDBIT, MAZEBIT],
    props=[
        (P_NORTH, z.uexit(MAZE_4)),
        (P_WEST, z.uexit(MAZE_2)),
        (P_UP, z.uexit(MAZE_5)),
        (P_LDESC, z.words('This is part of a maze of twisty little passages, all alike.')),
    ])
z.define_object(MAZE_4, 'Maze', parent=ROOMS,
    flags=[RLANDBIT, MAZEBIT],
    props=[
        (P_NORTH, z.uexit(MAZE_1)),
        (P_EAST, z.uexit(DEAD_END_1)),
        (P_WEST, z.uexit(MAZE_3)),
        (P_LDESC, z.words('This is part of a maze of twisty little passages, all alike.')),
    ])
z.define_object(DEAD_END_1, 'Dead End', parent=ROOMS,
    flags=[RLANDBIT, MAZEBIT],
    props=[
        (P_SOUTH, z.uexit(MAZE_4)),
        (P_LDESC, z.words('You have come to a dead end in the maze.')),
    ])
z.define_object(MAZE_5, 'Maze', parent=ROOMS,
    flags=[RLANDBIT, MAZEBIT],
    props=[
        (P_NORTH, z.uexit(MAZE_3)),
        (P_EAST, z.uexit(DEAD_END_2)),
        (P_SW, z.uexit(MAZE_6)),
        (P_LDESC, z.words('This is part of a maze of twisty little passages, all alike. A skeleton, probably the remains of a luckless adventurer, lies here.')),
    ])
z.define_object(DEAD_END_2, 'Dead End', parent=ROOMS,
    flags=[RLANDBIT, MAZEBIT],
    props=[
        (P_WEST, z.uexit(MAZE_5)),
        (P_LDESC, z.words('You have come to a dead end in the maze.')),
    ])
z.define_object(MAZE_6, 'Maze', parent=ROOMS,
    flags=[RLANDBIT, MAZEBIT],
    props=[
        (P_EAST, z.uexit(MAZE_7)),
        (P_WEST, z.uexit(MAZE_6)),
        (P_UP, z.uexit(MAZE_9)),
        (P_DOWN, z.uexit(MAZE_5)),
        (P_LDESC, z.words('This is part of a maze of twisty little passages, all alike.')),
    ])
z.define_object(MAZE_7, 'Maze', parent=ROOMS,
    flags=[RLANDBIT, MAZEBIT],
    props=[
        (P_EAST, z.uexit(MAZE_8)),
        (P_WEST, z.uexit(MAZE_6)),
        (P_SOUTH, z.uexit(MAZE_15)),
        (P_UP, z.uexit(MAZE_14)),
        (P_DOWN, z.fexit(z.rtn(maze_diodes))),
        (P_LDESC, z.words('This is part of a maze of twisty little passages, all alike.')),
    ])
z.define_object(MAZE_8, 'Maze', parent=ROOMS,
    flags=[RLANDBIT, MAZEBIT],
    props=[
        (P_WEST, z.uexit(MAZE_8)),
        (P_NE, z.uexit(MAZE_7)),
        (P_SE, z.uexit(DEAD_END_3)),
        (P_LDESC, z.words('This is part of a maze of twisty little passages, all alike.')),
    ])
z.define_object(DEAD_END_3, 'Dead End', parent=ROOMS,
    flags=[RLANDBIT, MAZEBIT],
    props=[
        (P_NORTH, z.uexit(MAZE_8)),
        (P_LDESC, z.words('You have come to a dead end in the maze.')),
    ])
z.define_object(MAZE_9, 'Maze', parent=ROOMS,
    flags=[RLANDBIT, MAZEBIT],
    props=[
        (P_NORTH, z.uexit(MAZE_6)),
        (P_EAST, z.uexit(MAZE_10)),
        (P_WEST, z.uexit(MAZE_12)),
        (P_SOUTH, z.uexit(MAZE_13)),
        (P_NW, z.uexit(MAZE_9)),
        (P_DOWN, z.fexit(z.rtn(maze_diodes))),
        (P_LDESC, z.words('This is part of a maze of twisty little passages, all alike.')),
    ])
z.define_object(MAZE_10, 'Maze', parent=ROOMS,
    flags=[RLANDBIT, MAZEBIT],
    props=[
        (P_EAST, z.uexit(MAZE_9)),
        (P_WEST, z.uexit(MAZE_13)),
        (P_UP, z.uexit(MAZE_11)),
        (P_LDESC, z.words('This is part of a maze of twisty little passages, all alike.')),
    ])
z.define_object(MAZE_11, 'Maze', parent=ROOMS,
    flags=[RLANDBIT, MAZEBIT],
    props=[
        (P_NE, z.uexit(GRATING_ROOM)),
        (P_NW, z.uexit(MAZE_13)),
        (P_SW, z.uexit(MAZE_12)),
        (P_DOWN, z.uexit(MAZE_10)),
        (P_LDESC, z.words('This is part of a maze of twisty little passages, all alike.')),
    ])
z.define_object(GRATING_ROOM, 'Grating Room', parent=ROOMS,
    flags=[RLANDBIT],
    props=[
        (P_SW, z.uexit(MAZE_11)),
        (P_UP, z.dexit(GRATING_CLEARING, GRATE, 'The grating is closed.')),
        (P_ACTION, z.words(z.rtn(maze_11_fcn))),
        (P_GLOBAL, z.bytes_(GRATE)),
    ])
z.define_object(MAZE_12, 'Maze', parent=ROOMS,
    flags=[RLANDBIT, MAZEBIT],
    props=[
        (P_NORTH, z.uexit(DEAD_END_4)),
        (P_EAST, z.uexit(MAZE_13)),
        (P_SW, z.uexit(MAZE_11)),
        (P_UP, z.uexit(MAZE_9)),
        (P_DOWN, z.fexit(z.rtn(maze_diodes))),
        (P_LDESC, z.words('This is part of a maze of twisty little passages, all alike.')),
    ])
z.define_object(DEAD_END_4, 'Dead End', parent=ROOMS,
    flags=[RLANDBIT, MAZEBIT],
    props=[
        (P_SOUTH, z.uexit(MAZE_12)),
        (P_LDESC, z.words('You have come to a dead end in the maze.')),
    ])
z.define_object(MAZE_13, 'Maze', parent=ROOMS,
    flags=[RLANDBIT, MAZEBIT],
    props=[
        (P_EAST, z.uexit(MAZE_9)),
        (P_WEST, z.uexit(MAZE_11)),
        (P_SOUTH, z.uexit(MAZE_10)),
        (P_DOWN, z.uexit(MAZE_12)),
        (P_LDESC, z.words('This is part of a maze of twisty little passages, all alike.')),
    ])
z.define_object(MAZE_14, 'Maze', parent=ROOMS,
    flags=[RLANDBIT, MAZEBIT],
    props=[
        (P_WEST, z.uexit(MAZE_15)),
        (P_SOUTH, z.uexit(MAZE_7)),
        (P_NE, z.uexit(MAZE_7)),
        (P_NW, z.uexit(MAZE_14)),
        (P_LDESC, z.words('This is part of a maze of twisty little passages, all alike.')),
    ])
z.define_object(MAZE_15, 'Maze', parent=ROOMS,
    flags=[RLANDBIT, MAZEBIT],
    props=[
        (P_WEST, z.uexit(MAZE_14)),
        (P_SOUTH, z.uexit(MAZE_7)),
        (P_SE, z.uexit(CYCLOPS_ROOM)),
        (P_LDESC, z.words('This is part of a maze of twisty little passages, all alike.')),
    ])
z.define_object(CYCLOPS_ROOM, 'Cyclops Room', parent=ROOMS,
    flags=[RLANDBIT],
    props=[
        (P_EAST, z.cexit(STRANGE_PASSAGE, 'MAGIC_FLAG', 'The east wall is solid rock.')),
        (P_NW, z.uexit(MAZE_15)),
        (P_UP, z.cexit(TREASURE_ROOM, 'CYCLOPS_FLAG', "The cyclops doesn't look like he'll let you past.")),
        (P_ACTION, z.words(z.rtn(cyclops_room_fcn))),
        (P_GLOBAL, z.bytes_(STAIRS)),
    ])
z.define_object(STRANGE_PASSAGE, 'Strange Passage', parent=ROOMS,
    flags=[RLANDBIT],
    props=[
        (P_EAST, z.uexit(LIVING_ROOM)),
        (P_WEST, z.uexit(CYCLOPS_ROOM)),
        (P_IN, z.uexit(CYCLOPS_ROOM)),
        (P_LDESC, z.words('This is a long passage. To the west is one entrance. On the east there is an old wooden door, with a large opening in it (about cyclops sized).')),
    ])
z.define_object(TREASURE_ROOM, 'Treasure Room', parent=ROOMS,
    flags=[RLANDBIT],
    props=[
        (P_DOWN, z.uexit(CYCLOPS_ROOM)),
        (P_ACTION, z.words(z.rtn(treasure_room_fcn))),
        (P_VALUE, z.words(25)),
        (P_LDESC, z.words('This is a large room, whose east wall is solid granite. A number of discarded bags, which crumble at your touch, are scattered about on the floor. There is an exit down a staircase.')),
        (P_GLOBAL, z.bytes_(STAIRS)),
    ])
z.define_object(RESERVOIR_SOUTH, 'Reservoir South', parent=ROOMS,
    flags=[RLANDBIT],
    props=[
        (P_NORTH, z.cexit(RESERVOIR, 'LOW_TIDE', 'You would drown.')),
        (P_EAST, z.uexit(DAM_ROOM)),
        (P_WEST, z.uexit(STREAM_VIEW)),
        (P_SE, z.uexit(DEEP_CANYON)),
        (P_SW, z.uexit(CHASM_ROOM)),
        (P_ACTION, z.words(z.rtn(reservoir_south_fcn))),
        (P_GLOBAL, z.bytes_(GLOBAL_WATER)),
        (P_PSEUDO, z.words(_W['lake'], z.rtn(lake_pseudo), _W['chasm'], z.rtn(chasm_pseudo))),
    ])
z.define_object(RESERVOIR, 'Reservoir', parent=ROOMS,
    flags=[NONLANDBIT],
    props=[
        (P_NORTH, z.uexit(RESERVOIR_NORTH)),
        (P_WEST, z.uexit(IN_STREAM)),
        (P_SOUTH, z.uexit(RESERVOIR_SOUTH)),
        (P_UP, z.uexit(IN_STREAM)),
        (P_DOWN, z.nexit('The dam blocks your way.')),
        (P_ACTION, z.words(z.rtn(reservoir_fcn))),
        (P_GLOBAL, z.bytes_(GLOBAL_WATER)),
        (P_PSEUDO, z.words(_W['stream'], z.rtn(stream_pseudo))),
    ])
z.define_object(RESERVOIR_NORTH, 'Reservoir North', parent=ROOMS,
    flags=[RLANDBIT],
    props=[
        (P_NORTH, z.uexit(ATLANTIS_ROOM)),
        (P_SOUTH, z.cexit(RESERVOIR, 'LOW_TIDE', 'You would drown.')),
        (P_ACTION, z.words(z.rtn(reservoir_north_fcn))),
        (P_GLOBAL, z.bytes_(GLOBAL_WATER, STAIRS)),
        (P_PSEUDO, z.words(_W['lake'], z.rtn(lake_pseudo))),
    ])
z.define_object(STREAM_VIEW, 'Stream View', parent=ROOMS,
    flags=[RLANDBIT],
    props=[
        (P_EAST, z.uexit(RESERVOIR_SOUTH)),
        (P_WEST, z.nexit('The stream emerges from a spot too small for you to enter.')),
        (P_LDESC, z.words('You are standing on a path beside a gently flowing stream. The path follows the stream, which flows from west to east.')),
        (P_GLOBAL, z.bytes_(GLOBAL_WATER)),
        (P_PSEUDO, z.words(_W['stream'], z.rtn(stream_pseudo))),
    ])
z.define_object(IN_STREAM, 'Stream', parent=ROOMS,
    flags=[NONLANDBIT],
    props=[
        (P_EAST, z.uexit(RESERVOIR)),
        (P_WEST, z.nexit('The channel is too narrow.')),
        (P_UP, z.nexit('The channel is too narrow.')),
        (P_DOWN, z.uexit(RESERVOIR)),
        (P_LAND, z.uexit(STREAM_VIEW)),
        (P_LDESC, z.words('You are on the gently flowing stream. The upstream route is too narrow to navigate, and the downstream route is invisible due to twisting walls. There is a narrow beach to land on.')),
        (P_GLOBAL, z.bytes_(GLOBAL_WATER)),
        (P_PSEUDO, z.words(_W['stream'], z.rtn(stream_pseudo))),
    ])
z.define_object(MIRROR_ROOM_1, 'Mirror Room', parent=ROOMS,
    flags=[RLANDBIT],
    props=[
        (P_NORTH, z.uexit(COLD_PASSAGE)),
        (P_EAST, z.uexit(SMALL_CAVE)),
        (P_WEST, z.uexit(TWISTING_PASSAGE)),
        (P_ACTION, z.words(z.rtn(mirror_room))),
    ])
z.define_object(MIRROR_ROOM_2, 'Mirror Room', parent=ROOMS,
    flags=[RLANDBIT, ONBIT],
    props=[
        (P_NORTH, z.uexit(NARROW_PASSAGE)),
        (P_EAST, z.uexit(TINY_CAVE)),
        (P_WEST, z.uexit(WINDING_PASSAGE)),
        (P_ACTION, z.words(z.rtn(mirror_room))),
    ])
z.define_object(SMALL_CAVE, 'Cave', parent=ROOMS,
    flags=[RLANDBIT],
    props=[
        (P_NORTH, z.uexit(MIRROR_ROOM_1)),
        (P_WEST, z.uexit(TWISTING_PASSAGE)),
        (P_SOUTH, z.uexit(ATLANTIS_ROOM)),
        (P_DOWN, z.uexit(ATLANTIS_ROOM)),
        (P_LDESC, z.words('This is a tiny cave with entrances west and north, and a staircase leading down.')),
        (P_GLOBAL, z.bytes_(STAIRS)),
    ])
z.define_object(TINY_CAVE, 'Cave', parent=ROOMS,
    flags=[RLANDBIT],
    props=[
        (P_NORTH, z.uexit(MIRROR_ROOM_2)),
        (P_WEST, z.uexit(WINDING_PASSAGE)),
        (P_DOWN, z.uexit(ENTRANCE_TO_HADES)),
        (P_ACTION, z.words(z.rtn(cave2_room))),
        (P_LDESC, z.words('This is a tiny cave with entrances west and north, and a dark, forbidding staircase leading down.')),
        (P_GLOBAL, z.bytes_(STAIRS)),
    ])
z.define_object(COLD_PASSAGE, 'Cold Passage', parent=ROOMS,
    flags=[RLANDBIT],
    props=[
        (P_WEST, z.uexit(SLIDE_ROOM)),
        (P_SOUTH, z.uexit(MIRROR_ROOM_1)),
        (P_LDESC, z.words('This is a cold and damp corridor where a long east-west passageway turns into a southward path.')),
    ])
z.define_object(NARROW_PASSAGE, 'Narrow Passage', parent=ROOMS,
    flags=[RLANDBIT],
    props=[
        (P_NORTH, z.uexit(ROUND_ROOM)),
        (P_SOUTH, z.uexit(MIRROR_ROOM_2)),
        (P_LDESC, z.words('This is a long and narrow corridor where a long north-south passageway briefly narrows even further.')),
    ])
z.define_object(WINDING_PASSAGE, 'Winding Passage', parent=ROOMS,
    flags=[RLANDBIT],
    props=[
        (P_NORTH, z.uexit(MIRROR_ROOM_2)),
        (P_EAST, z.uexit(TINY_CAVE)),
        (P_LDESC, z.words('This is a winding passage. It seems that there are only exits on the east and north.')),
    ])
z.define_object(TWISTING_PASSAGE, 'Twisting Passage', parent=ROOMS,
    flags=[RLANDBIT],
    props=[
        (P_NORTH, z.uexit(MIRROR_ROOM_1)),
        (P_EAST, z.uexit(SMALL_CAVE)),
        (P_LDESC, z.words('This is a winding passage. It seems that there are only exits on the east and north.')),
    ])
z.define_object(ATLANTIS_ROOM, 'Atlantis Room', parent=ROOMS,
    flags=[RLANDBIT],
    props=[
        (P_SOUTH, z.uexit(RESERVOIR_NORTH)),
        (P_UP, z.uexit(SMALL_CAVE)),
        (P_LDESC, z.words('This is an ancient room, long under water. There is an exit to the south and a staircase leading up.')),
        (P_GLOBAL, z.bytes_(STAIRS)),
    ])
z.define_object(EW_PASSAGE, 'East-West Passage', parent=ROOMS,
    flags=[RLANDBIT],
    props=[
        (P_NORTH, z.uexit(CHASM_ROOM)),
        (P_EAST, z.uexit(ROUND_ROOM)),
        (P_WEST, z.uexit(TROLL_ROOM)),
        (P_DOWN, z.uexit(CHASM_ROOM)),
        (P_VALUE, z.words(5)),
        (P_LDESC, z.words('This is a narrow east-west passageway. There is a narrow stairway leading down at the north end of the room.')),
        (P_GLOBAL, z.bytes_(STAIRS)),
    ])
z.define_object(ROUND_ROOM, 'Round Room', parent=ROOMS,
    flags=[RLANDBIT],
    props=[
        (P_NORTH, z.uexit(NS_PASSAGE)),
        (P_EAST, z.uexit(LOUD_ROOM)),
        (P_WEST, z.uexit(EW_PASSAGE)),
        (P_SOUTH, z.uexit(NARROW_PASSAGE)),
        (P_SE, z.uexit(ENGRAVINGS_CAVE)),
        (P_LDESC, z.words('This is a circular stone room with passages in all directions. Several of them have unfortunately been blocked by cave-ins.')),
    ])
z.define_object(DEEP_CANYON, 'Deep Canyon', parent=ROOMS,
    flags=[RLANDBIT],
    props=[
        (P_EAST, z.uexit(DAM_ROOM)),
        (P_NW, z.uexit(RESERVOIR_SOUTH)),
        (P_SW, z.uexit(NS_PASSAGE)),
        (P_DOWN, z.uexit(LOUD_ROOM)),
        (P_ACTION, z.words(z.rtn(deep_canyon_f))),
        (P_GLOBAL, z.bytes_(STAIRS)),
    ])
z.define_object(DAMP_CAVE, 'Damp Cave', parent=ROOMS,
    flags=[RLANDBIT],
    props=[
        (P_EAST, z.uexit(WHITE_CLIFFS_NORTH)),
        (P_WEST, z.uexit(LOUD_ROOM)),
        (P_SOUTH, z.nexit('It is too narrow for most insects.')),
        (P_LDESC, z.words('This cave has exits to the west and east, and narrows to a crack toward the south. The earth is particularly damp here.')),
        (P_GLOBAL, z.bytes_(CRACK)),
    ])
z.define_object(LOUD_ROOM, 'Loud Room', parent=ROOMS,
    flags=[RLANDBIT],
    props=[
        (P_EAST, z.uexit(DAMP_CAVE)),
        (P_WEST, z.uexit(ROUND_ROOM)),
        (P_UP, z.uexit(DEEP_CANYON)),
        (P_ACTION, z.words(z.rtn(loud_room_fcn))),
        (P_GLOBAL, z.bytes_(STAIRS)),
    ])
z.define_object(NS_PASSAGE, 'North-South Passage', parent=ROOMS,
    flags=[RLANDBIT],
    props=[
        (P_NORTH, z.uexit(CHASM_ROOM)),
        (P_SOUTH, z.uexit(ROUND_ROOM)),
        (P_NE, z.uexit(DEEP_CANYON)),
        (P_LDESC, z.words('This is a high north-south passage, which forks to the northeast.')),
    ])
z.define_object(CHASM_ROOM, 'Chasm', parent=ROOMS,
    flags=[RLANDBIT],
    props=[
        (P_SOUTH, z.uexit(NS_PASSAGE)),
        (P_NE, z.uexit(RESERVOIR_SOUTH)),
        (P_SW, z.uexit(EW_PASSAGE)),
        (P_UP, z.uexit(EW_PASSAGE)),
        (P_DOWN, z.nexit('Are you out of your mind?')),
        (P_LDESC, z.words('A chasm runs southwest to northeast and the path follows it. You are on the south side of the chasm, where a crack opens into a passage.')),
        (P_GLOBAL, z.bytes_(CRACK, STAIRS)),
        (P_PSEUDO, z.words(_W['chasm'], z.rtn(chasm_pseudo))),
    ])
z.define_object(ENTRANCE_TO_HADES, 'Entrance to Hades', parent=ROOMS,
    flags=[RLANDBIT, ONBIT],
    props=[
        (P_SOUTH, z.cexit(LAND_OF_LIVING_DEAD, 'LLD_FLAG', 'Some invisible force prevents you from passing through the gate.')),
        (P_UP, z.uexit(TINY_CAVE)),
        (P_IN, z.cexit(LAND_OF_LIVING_DEAD, 'LLD_FLAG', 'Some invisible force prevents you from passing through the gate.')),
        (P_ACTION, z.words(z.rtn(lld_room))),
        (P_GLOBAL, z.bytes_(BODIES)),
        (P_PSEUDO, z.words(_W['gate'], z.rtn(gate_pseudo), _W['gates'], z.rtn(gate_pseudo))),
    ])
z.define_object(LAND_OF_LIVING_DEAD, 'Land of the Dead', parent=ROOMS,
    flags=[RLANDBIT, ONBIT],
    props=[
        (P_NORTH, z.uexit(ENTRANCE_TO_HADES)),
        (P_OUT, z.uexit(ENTRANCE_TO_HADES)),
        (P_LDESC, z.words('You have entered the Land of the Living Dead. Thousands of lost souls can be heard weeping and moaning. In the corner are stacked the remains of dozens of previous adventurers less fortunate than yourself. A passage exits to the north.')),
        (P_GLOBAL, z.bytes_(BODIES)),
    ])
z.define_object(ENGRAVINGS_CAVE, 'Engravings Cave', parent=ROOMS,
    flags=[RLANDBIT],
    props=[
        (P_EAST, z.uexit(DOME_ROOM)),
        (P_NW, z.uexit(ROUND_ROOM)),
        (P_LDESC, z.words('You have entered a low cave with passages leading northwest and east.')),
    ])
z.define_object(EGYPT_ROOM, 'Egyptian Room', parent=ROOMS,
    flags=[RLANDBIT],
    props=[
        (P_WEST, z.uexit(NORTH_TEMPLE)),
        (P_UP, z.uexit(NORTH_TEMPLE)),
        (P_LDESC, z.words('This is a room which looks like an Egyptian tomb. There is an ascending staircase to the west.')),
        (P_GLOBAL, z.bytes_(STAIRS)),
    ])
z.define_object(DOME_ROOM, 'Dome Room', parent=ROOMS,
    flags=[RLANDBIT],
    props=[
        (P_WEST, z.uexit(ENGRAVINGS_CAVE)),
        (P_DOWN, z.cexit(TORCH_ROOM, 'DOME_FLAG', 'You cannot go down without fracturing many bones.')),
        (P_ACTION, z.words(z.rtn(dome_room_fcn))),
        (P_PSEUDO, z.words(_W['dome'], z.rtn(dome_pseudo))),
    ])
z.define_object(TORCH_ROOM, 'Torch Room', parent=ROOMS,
    flags=[RLANDBIT],
    props=[
        (P_SOUTH, z.uexit(NORTH_TEMPLE)),
        (P_UP, z.nexit('You cannot reach the rope.')),
        (P_DOWN, z.uexit(NORTH_TEMPLE)),
        (P_ACTION, z.words(z.rtn(torch_room_fcn))),
        (P_GLOBAL, z.bytes_(STAIRS)),
        (P_PSEUDO, z.words(_W['dome'], z.rtn(dome_pseudo))),
    ])
z.define_object(NORTH_TEMPLE, 'Temple', parent=ROOMS,
    flags=[RLANDBIT, ONBIT, SACREDBIT],
    props=[
        (P_NORTH, z.uexit(TORCH_ROOM)),
        (P_EAST, z.uexit(EGYPT_ROOM)),
        (P_SOUTH, z.uexit(SOUTH_TEMPLE)),
        (P_UP, z.uexit(TORCH_ROOM)),
        (P_DOWN, z.uexit(EGYPT_ROOM)),
        (P_OUT, z.uexit(TORCH_ROOM)),
        (P_LDESC, z.words('This is the north end of a large temple. On the east wall is an ancient inscription, probably a prayer in a long-forgotten language. Below the prayer is a staircase leading down. The west wall is solid granite. The exit to the north end of the room is through huge marble pillars.')),
        (P_GLOBAL, z.bytes_(STAIRS)),
    ])
z.define_object(SOUTH_TEMPLE, 'Altar', parent=ROOMS,
    flags=[RLANDBIT, ONBIT, SACREDBIT],
    props=[
        (P_NORTH, z.uexit(NORTH_TEMPLE)),
        (P_DOWN, z.cexit(TINY_CAVE, 'COFFIN_CURE', "You haven't a prayer of getting the coffin down there.")),
        (P_ACTION, z.words(z.rtn(south_temple_fcn))),
        (P_LDESC, z.words('This is the south end of a large temple. In front of you is what appears to be an altar. In one corner is a small hole in the floor which leads into darkness. You probably could not get back up it.')),
    ])
z.define_object(DAM_ROOM, 'Dam', parent=ROOMS,
    flags=[RLANDBIT, ONBIT],
    props=[
        (P_NORTH, z.uexit(DAM_LOBBY)),
        (P_EAST, z.uexit(DAM_BASE)),
        (P_WEST, z.uexit(RESERVOIR_SOUTH)),
        (P_SOUTH, z.uexit(DEEP_CANYON)),
        (P_DOWN, z.uexit(DAM_BASE)),
        (P_ACTION, z.words(z.rtn(dam_room_fcn))),
        (P_GLOBAL, z.bytes_(GLOBAL_WATER)),
    ])
z.define_object(DAM_LOBBY, 'Dam Lobby', parent=ROOMS,
    flags=[RLANDBIT, ONBIT],
    props=[
        (P_NORTH, z.uexit(MAINTENANCE_ROOM)),
        (P_EAST, z.uexit(MAINTENANCE_ROOM)),
        (P_SOUTH, z.uexit(DAM_ROOM)),
        (P_LDESC, z.words('This room appears to have been the waiting room for groups touring the dam. There are open doorways here to the north and east marked "Private", and there is a path leading south over the top of the dam.')),
    ])
z.define_object(MAINTENANCE_ROOM, 'Maintenance Room', parent=ROOMS,
    flags=[RLANDBIT],
    props=[
        (P_WEST, z.uexit(DAM_LOBBY)),
        (P_SOUTH, z.uexit(DAM_LOBBY)),
        (P_LDESC, z.words('This is what appears to have been the maintenance room for Flood Control Dam #3. Apparently, this room has been ransacked recently, for most of the valuable equipment is gone. On the wall in front of you is a group of buttons colored blue, yellow, brown, and red. There are doorways to the west and south.')),
    ])
z.define_object(DAM_BASE, 'Dam Base', parent=ROOMS,
    flags=[RLANDBIT, ONBIT, SACREDBIT],
    props=[
        (P_NORTH, z.uexit(DAM_ROOM)),
        (P_UP, z.uexit(DAM_ROOM)),
        (P_LDESC, z.words('You are at the base of Flood Control Dam #3, which looms above you and to the north. The river Frigid is flowing by here. Along the river are the White Cliffs which seem to form giant walls stretching from north to south along the shores of the river as it winds its way downstream.')),
        (P_GLOBAL, z.bytes_(GLOBAL_WATER, RIVER)),
    ])
z.define_object(RIVER_1, 'Frigid River', parent=ROOMS,
    flags=[NONLANDBIT, SACREDBIT, ONBIT],
    props=[
        (P_EAST, z.nexit('The White Cliffs prevent your landing here.')),
        (P_WEST, z.uexit(DAM_BASE)),
        (P_UP, z.nexit('You cannot go upstream due to strong currents.')),
        (P_DOWN, z.uexit(RIVER_2)),
        (P_LAND, z.uexit(DAM_BASE)),
        (P_LDESC, z.words('You are on the Frigid River in the vicinity of the Dam. The river flows quietly here. There is a landing on the west shore.')),
        (P_GLOBAL, z.bytes_(GLOBAL_WATER, RIVER)),
    ])
z.define_object(RIVER_2, 'Frigid River', parent=ROOMS,
    flags=[NONLANDBIT, SACREDBIT],
    props=[
        (P_EAST, z.nexit('The White Cliffs prevent your landing here.')),
        (P_WEST, z.nexit('Just in time you steer away from the rocks.')),
        (P_UP, z.nexit('You cannot go upstream due to strong currents.')),
        (P_DOWN, z.uexit(RIVER_3)),
        (P_LAND, z.nexit('There is no safe landing spot here.')),
        (P_LDESC, z.words('The river turns a corner here making it impossible to see the Dam. The White Cliffs loom on the east bank and large rocks prevent landing on the west.')),
        (P_GLOBAL, z.bytes_(GLOBAL_WATER, RIVER)),
    ])
z.define_object(RIVER_3, 'Frigid River', parent=ROOMS,
    flags=[NONLANDBIT, SACREDBIT],
    props=[
        (P_WEST, z.uexit(WHITE_CLIFFS_NORTH)),
        (P_UP, z.nexit('You cannot go upstream due to strong currents.')),
        (P_DOWN, z.uexit(RIVER_4)),
        (P_LAND, z.uexit(WHITE_CLIFFS_NORTH)),
        (P_LDESC, z.words('The river descends here into a valley. There is a narrow beach on the west shore below the cliffs. In the distance a faint rumbling can be heard.')),
        (P_GLOBAL, z.bytes_(GLOBAL_WATER, RIVER)),
    ])
z.define_object(WHITE_CLIFFS_NORTH, 'White Cliffs Beach', parent=ROOMS,
    flags=[RLANDBIT, SACREDBIT],
    props=[
        (P_WEST, z.cexit(DAMP_CAVE, 'DEFLATE', 'The path is too narrow.')),
        (P_SOUTH, z.cexit(WHITE_CLIFFS_SOUTH, 'DEFLATE', 'The path is too narrow.')),
        (P_ACTION, z.words(z.rtn(white_cliffs_function))),
        (P_LDESC, z.words('You are on a narrow strip of beach which runs along the base of the White Cliffs. There is a narrow path heading south along the Cliffs and a tight passage leading west into the cliffs themselves.')),
        (P_GLOBAL, z.bytes_(GLOBAL_WATER, WHITE_CLIFF, RIVER)),
    ])
z.define_object(WHITE_CLIFFS_SOUTH, 'White Cliffs Beach', parent=ROOMS,
    flags=[RLANDBIT, SACREDBIT],
    props=[
        (P_NORTH, z.cexit(WHITE_CLIFFS_NORTH, 'DEFLATE', 'The path is too narrow.')),
        (P_ACTION, z.words(z.rtn(white_cliffs_function))),
        (P_LDESC, z.words('You are on a rocky, narrow strip of beach beside the Cliffs. A narrow path leads north along the shore.')),
        (P_GLOBAL, z.bytes_(GLOBAL_WATER, WHITE_CLIFF, RIVER)),
    ])
z.define_object(RIVER_4, 'Frigid River', parent=ROOMS,
    flags=[NONLANDBIT, SACREDBIT],
    props=[
        (P_EAST, z.uexit(SANDY_BEACH)),
        (P_WEST, z.uexit(WHITE_CLIFFS_SOUTH)),
        (P_UP, z.nexit('You cannot go upstream due to strong currents.')),
        (P_DOWN, z.uexit(RIVER_5)),
        (P_LAND, z.nexit('You can land either to the east or the west.')),
        (P_ACTION, z.words(z.rtn(rivr4_room))),
        (P_LDESC, z.words('The river is running faster here and the sound ahead appears to be that of rushing water. On the east shore is a sandy beach. A small area of beach can also be seen below the cliffs on the west shore.')),
        (P_GLOBAL, z.bytes_(GLOBAL_WATER, RIVER)),
    ])
z.define_object(RIVER_5, 'Frigid River', parent=ROOMS,
    flags=[NONLANDBIT, SACREDBIT, ONBIT],
    props=[
        (P_EAST, z.uexit(SHORE)),
        (P_UP, z.nexit('You cannot go upstream due to strong currents.')),
        (P_LAND, z.uexit(SHORE)),
        (P_LDESC, z.words('The sound of rushing water is nearly unbearable here. On the east shore is a large landing area.')),
        (P_GLOBAL, z.bytes_(GLOBAL_WATER, RIVER)),
    ])
z.define_object(SHORE, 'Shore', parent=ROOMS,
    flags=[RLANDBIT, SACREDBIT, ONBIT],
    props=[
        (P_NORTH, z.uexit(SANDY_BEACH)),
        (P_SOUTH, z.uexit(ARAGAIN_FALLS)),
        (P_LDESC, z.words('You are on the east shore of the river. The water here seems somewhat treacherous. A path travels from north to south here, the south end quickly turning around a sharp corner.')),
        (P_GLOBAL, z.bytes_(GLOBAL_WATER, RIVER)),
    ])
z.define_object(SANDY_BEACH, 'Sandy Beach', parent=ROOMS,
    flags=[RLANDBIT, SACREDBIT],
    props=[
        (P_SOUTH, z.uexit(SHORE)),
        (P_NE, z.uexit(SANDY_CAVE)),
        (P_LDESC, z.words('You are on a large sandy beach on the east shore of the river, which is flowing quickly by. A path runs beside the river to the south here, and a passage is partially buried in sand to the northeast.')),
        (P_GLOBAL, z.bytes_(GLOBAL_WATER, RIVER)),
    ])
z.define_object(SANDY_CAVE, 'Sandy Cave', parent=ROOMS,
    flags=[RLANDBIT],
    props=[
        (P_SW, z.uexit(SANDY_BEACH)),
        (P_LDESC, z.words('This is a sand-filled cave whose exit is to the southwest.')),
    ])
z.define_object(ARAGAIN_FALLS, 'Aragain Falls', parent=ROOMS,
    flags=[RLANDBIT, SACREDBIT, ONBIT],
    props=[
        (P_NORTH, z.uexit(SHORE)),
        (P_WEST, z.cexit(ON_RAINBOW, 'RAINBOW_FLAG', 0)),
        (P_UP, z.cexit(ON_RAINBOW, 'RAINBOW_FLAG', 0)),
        (P_DOWN, z.nexit("It's a long way...")),
        (P_ACTION, z.words(z.rtn(falls_room))),
        (P_GLOBAL, z.bytes_(GLOBAL_WATER, RIVER, RAINBOW)),
    ])
z.define_object(ON_RAINBOW, 'On the Rainbow', parent=ROOMS,
    flags=[RLANDBIT, ONBIT, SACREDBIT],
    props=[
        (P_EAST, z.uexit(ARAGAIN_FALLS)),
        (P_WEST, z.uexit(END_OF_RAINBOW)),
        (P_LDESC, z.words('You are on top of a rainbow (I bet you never thought you would walk on a rainbow), with a magnificent view of the Falls. The rainbow travels east-west here.')),
        (P_GLOBAL, z.bytes_(RAINBOW)),
    ])
z.define_object(END_OF_RAINBOW, 'End of Rainbow', parent=ROOMS,
    flags=[RLANDBIT, ONBIT],
    props=[
        (P_EAST, z.cexit(ON_RAINBOW, 'RAINBOW_FLAG', 0)),
        (P_NE, z.cexit(ON_RAINBOW, 'RAINBOW_FLAG', 0)),
        (P_SW, z.uexit(CANYON_BOTTOM)),
        (P_UP, z.cexit(ON_RAINBOW, 'RAINBOW_FLAG', 0)),
        (P_LDESC, z.words('You are on a small, rocky beach on the continuation of the Frigid River past the Falls. The beach is narrow due to the presence of the White Cliffs. The river canyon opens here and sunlight shines in from above. A rainbow crosses over the falls to the east and a narrow path continues to the southwest.')),
        (P_GLOBAL, z.bytes_(GLOBAL_WATER, RAINBOW, RIVER)),
    ])
z.define_object(CANYON_BOTTOM, 'Canyon Bottom', parent=ROOMS,
    flags=[RLANDBIT, ONBIT, SACREDBIT],
    props=[
        (P_NORTH, z.uexit(END_OF_RAINBOW)),
        (P_UP, z.uexit(CLIFF_MIDDLE)),
        (P_LDESC, z.words('You are beneath the walls of the river canyon which may be climbable here. The lesser part of the runoff of Aragain Falls flows by below. To the north is a narrow path.')),
        (P_GLOBAL, z.bytes_(GLOBAL_WATER, CLIMBABLE_CLIFF, RIVER)),
    ])
z.define_object(CLIFF_MIDDLE, 'Rocky Ledge', parent=ROOMS,
    flags=[RLANDBIT, ONBIT, SACREDBIT],
    props=[
        (P_UP, z.uexit(CANYON_VIEW)),
        (P_DOWN, z.uexit(CANYON_BOTTOM)),
        (P_LDESC, z.words('You are on a ledge about halfway up the wall of the river canyon. You can see from here that the main flow from Aragain Falls twists along a passage which it is impossible for you to enter. Below you is the canyon bottom. Above you is more cliff, which appears climbable.')),
        (P_GLOBAL, z.bytes_(CLIMBABLE_CLIFF, RIVER)),
    ])
z.define_object(CANYON_VIEW, 'Canyon View', parent=ROOMS,
    flags=[RLANDBIT, ONBIT, SACREDBIT],
    props=[
        (P_EAST, z.uexit(CLIFF_MIDDLE)),
        (P_WEST, z.uexit(FOREST_3)),
        (P_SOUTH, z.nexit('Storm-tossed trees block your way.')),
        (P_NW, z.uexit(CLEARING)),
        (P_DOWN, z.uexit(CLIFF_MIDDLE)),
        (P_ACTION, z.words(z.rtn(canyon_view_f))),
        (P_LDESC, z.words('You are at the top of the Great Canyon on its west wall. From here there is a marvelous view of the canyon and parts of the Frigid River upstream. Across the canyon, the walls of the White Cliffs join the mighty ramparts of the Flathead Mountains to the east. Following the Canyon upstream to the north, Aragain Falls may be seen, complete with rainbow. The mighty Frigid River flows out from a great dark cavern. To the west and south can be seen an immense forest, stretching for miles around. A path leads northwest. It is possible to climb down into the canyon from here.')),
        (P_GLOBAL, z.bytes_(CLIMBABLE_CLIFF, RIVER, RAINBOW)),
    ])
z.define_object(MINE_ENTRANCE, 'Mine Entrance', parent=ROOMS,
    flags=[RLANDBIT],
    props=[
        (P_WEST, z.uexit(SQUEEKY_ROOM)),
        (P_SOUTH, z.uexit(SLIDE_ROOM)),
        (P_IN, z.uexit(SQUEEKY_ROOM)),
        (P_LDESC, z.words('You are standing at the entrance of what might have been a coal mine. The shaft enters the west wall, and there is another exit on the south end of the room.')),
    ])
z.define_object(SQUEEKY_ROOM, 'Squeaky Room', parent=ROOMS,
    flags=[RLANDBIT],
    props=[
        (P_NORTH, z.uexit(BAT_ROOM)),
        (P_EAST, z.uexit(MINE_ENTRANCE)),
        (P_LDESC, z.words('You are in a small room. Strange squeaky sounds may be heard coming from the passage at the north end. You may also escape to the east.')),
    ])
z.define_object(BAT_ROOM, 'Bat Room', parent=ROOMS,
    flags=[RLANDBIT, SACREDBIT],
    props=[
        (P_EAST, z.uexit(SHAFT_ROOM)),
        (P_SOUTH, z.uexit(SQUEEKY_ROOM)),
        (P_ACTION, z.words(z.rtn(bats_room))),
    ])
z.define_object(SHAFT_ROOM, 'Shaft Room', parent=ROOMS,
    flags=[RLANDBIT],
    props=[
        (P_NORTH, z.uexit(SMELLY_ROOM)),
        (P_WEST, z.uexit(BAT_ROOM)),
        (P_DOWN, z.nexit("You wouldn't fit and would die if you could.")),
        (P_LDESC, z.words('This is a large room, in the middle of which is a small shaft descending through the floor into darkness below. To the west and the north are exits from this room. Constructed over the top of the shaft is a metal framework to which a heavy iron chain is attached.')),
        (P_PSEUDO, z.words(_W['chain'], z.rtn(chain_pseudo))),
    ])
z.define_object(SMELLY_ROOM, 'Smelly Room', parent=ROOMS,
    flags=[RLANDBIT],
    props=[
        (P_SOUTH, z.uexit(SHAFT_ROOM)),
        (P_DOWN, z.uexit(GAS_ROOM)),
        (P_LDESC, z.words('This is a small nondescript room. However, from the direction of a small descending staircase a foul odor can be detected. To the south is a narrow tunnel.')),
        (P_GLOBAL, z.bytes_(STAIRS)),
        (P_PSEUDO, z.words(_W['odor'], z.rtn(gas_pseudo), _W['gas'], z.rtn(gas_pseudo))),
    ])
z.define_object(GAS_ROOM, 'Gas Room', parent=ROOMS,
    flags=[RLANDBIT, SACREDBIT],
    props=[
        (P_EAST, z.uexit(MINE_1)),
        (P_UP, z.uexit(SMELLY_ROOM)),
        (P_ACTION, z.words(z.rtn(boom_room))),
        (P_LDESC, z.words('This is a small room which smells strongly of coal gas. There is a short climb up some stairs and a narrow tunnel leading east.')),
        (P_GLOBAL, z.bytes_(STAIRS)),
        (P_PSEUDO, z.words(_W['gas'], z.rtn(gas_pseudo), _W['odor'], z.rtn(gas_pseudo))),
    ])
z.define_object(LADDER_TOP, 'Ladder Top', parent=ROOMS,
    flags=[RLANDBIT],
    props=[
        (P_UP, z.uexit(MINE_4)),
        (P_DOWN, z.uexit(LADDER_BOTTOM)),
        (P_LDESC, z.words('This is a very small room. In the corner is a rickety wooden ladder, leading downward. It might be safe to descend. There is also a staircase leading upward.')),
        (P_GLOBAL, z.bytes_(LADDER, STAIRS)),
    ])
z.define_object(LADDER_BOTTOM, 'Ladder Bottom', parent=ROOMS,
    flags=[RLANDBIT],
    props=[
        (P_WEST, z.uexit(TIMBER_ROOM)),
        (P_SOUTH, z.uexit(DEAD_END_5)),
        (P_UP, z.uexit(LADDER_TOP)),
        (P_LDESC, z.words('This is a rather wide room. On one side is the bottom of a narrow wooden ladder. To the west and the south are passages leaving the room.')),
        (P_GLOBAL, z.bytes_(LADDER)),
    ])
z.define_object(DEAD_END_5, 'Dead End', parent=ROOMS,
    flags=[RLANDBIT],
    props=[
        (P_NORTH, z.uexit(LADDER_BOTTOM)),
        (P_LDESC, z.words('You have come to a dead end in the mine.')),
    ])
z.define_object(TIMBER_ROOM, 'Timber Room', parent=ROOMS,
    flags=[RLANDBIT, SACREDBIT],
    props=[
        (P_EAST, z.uexit(LADDER_BOTTOM)),
        (P_WEST, z.cexit(LOWER_SHAFT, 'EMPTY_HANDED', 'You cannot fit through this passage with that load.')),
        (P_ACTION, z.words(z.rtn(no_objs))),
        (P_LDESC, z.words('This is a long and narrow passage, which is cluttered with broken timbers. A wide passage comes from the east and turns at the west end of the room into a very narrow passageway. From the west comes a strong draft.')),
    ])
z.define_object(LOWER_SHAFT, 'Drafty Room', parent=ROOMS,
    flags=[RLANDBIT, SACREDBIT],
    props=[
        (P_EAST, z.cexit(TIMBER_ROOM, 'EMPTY_HANDED', 'You cannot fit through this passage with that load.')),
        (P_SOUTH, z.uexit(MACHINE_ROOM)),
        (P_OUT, z.cexit(TIMBER_ROOM, 'EMPTY_HANDED', 'You cannot fit through this passage with that load.')),
        (P_ACTION, z.words(z.rtn(no_objs))),
        (P_LDESC, z.words('This is a small drafty room in which is the bottom of a long shaft. To the south is a passageway and to the east a very narrow passage. In the shaft can be seen a heavy iron chain.')),
        (P_PSEUDO, z.words(_W['chain'], z.rtn(chain_pseudo))),
    ])
z.define_object(MACHINE_ROOM, 'Machine Room', parent=ROOMS,
    flags=[RLANDBIT],
    props=[
        (P_NORTH, z.uexit(LOWER_SHAFT)),
        (P_ACTION, z.words(z.rtn(machine_room_fcn))),
    ])
z.define_object(MINE_1, 'Coal Mine', parent=ROOMS,
    flags=[RLANDBIT],
    props=[
        (P_NORTH, z.uexit(GAS_ROOM)),
        (P_EAST, z.uexit(MINE_1)),
        (P_NE, z.uexit(MINE_2)),
        (P_LDESC, z.words('This is a nondescript part of a coal mine.')),
    ])
z.define_object(MINE_2, 'Coal Mine', parent=ROOMS,
    flags=[RLANDBIT],
    props=[
        (P_NORTH, z.uexit(MINE_2)),
        (P_SOUTH, z.uexit(MINE_1)),
        (P_SE, z.uexit(MINE_3)),
        (P_LDESC, z.words('This is a nondescript part of a coal mine.')),
    ])
z.define_object(MINE_3, 'Coal Mine', parent=ROOMS,
    flags=[RLANDBIT],
    props=[
        (P_EAST, z.uexit(MINE_2)),
        (P_SOUTH, z.uexit(MINE_3)),
        (P_SW, z.uexit(MINE_4)),
        (P_LDESC, z.words('This is a nondescript part of a coal mine.')),
    ])
z.define_object(MINE_4, 'Coal Mine', parent=ROOMS,
    flags=[RLANDBIT],
    props=[
        (P_NORTH, z.uexit(MINE_3)),
        (P_WEST, z.uexit(MINE_4)),
        (P_DOWN, z.uexit(LADDER_TOP)),
        (P_LDESC, z.words('This is a nondescript part of a coal mine.')),
    ])
z.define_object(SLIDE_ROOM, 'Slide Room', parent=ROOMS,
    flags=[RLANDBIT],
    props=[
        (P_NORTH, z.uexit(MINE_ENTRANCE)),
        (P_EAST, z.uexit(COLD_PASSAGE)),
        (P_DOWN, z.uexit(CELLAR)),
        (P_LDESC, z.words('This is a small chamber, which appears to have been part of a coal mine. On the south wall of the chamber the letters "Granite Wall" are etched in the rock. To the east is a long passage, and there is a steep metal slide twisting downward. To the north is a small opening.')),
        (P_GLOBAL, z.bytes_(SLIDE)),
    ])
z.define_object(GLOBAL_OBJECTS, '', parent=0,
    flags=[RMUNGBIT, INVISIBLE, TOUCHBIT, SURFACEBIT, TRYTAKEBIT, OPENBIT, SEARCHBIT, TRANSBIT, ONBIT, RLANDBIT, FIGHTBIT, STAGGERED, WEARBIT],
    props=[])
z.define_object(LOCAL_GLOBALS, '', parent=GLOBAL_OBJECTS,
    flags=[],
    props=[
        (P_SYNONYM, z.words(_W['zzmgck'])),
        (P_SIZE, z.words(0)),
        (P_FDESC, z.words('F')),
        (P_LDESC, z.words('F')),
        (P_CAPACITY, z.words(0)),
        (P_DESCFCN, z.words(z.rtn(path_object))),
        (P_VTYPE, z.words(1)),
        (P_GLOBAL, z.bytes_(GLOBAL_OBJECTS)),
        (P_PSEUDO, z.words(_W['foobar'], z.rtn(v_walk))),
        (P_ADVFCN, z.words(0)),
        (P_CONTFCN, z.words(0)),
    ])
z.define_object(ROOMS, '', parent=0,
    flags=[],
    props=[
        (P_IN, z.uexit(ROOMS)),
    ])
z.define_object(INTNUM, 'number', parent=GLOBAL_OBJECTS,
    flags=[TOOLBIT],
    props=[
        (P_SYNONYM, z.words(_W['intnum'])),
    ])
z.define_object(PSEUDO_OBJECT, 'pseudo', parent=LOCAL_GLOBALS,
    flags=[],
    props=[
        (P_ACTION, z.words(z.rtn(cretin_fcn))),
    ])
z.define_object(IT, 'random object', parent=GLOBAL_OBJECTS,
    flags=[NDESCBIT, TOUCHBIT],
    props=[
        (P_SYNONYM, z.words(_W['it'], _W['them'], _W['her'], _W['him'])),
    ])
z.define_object(NOT_HERE_OBJECT, 'such thing', parent=0,
    flags=[],
    props=[
        (P_ACTION, z.words(z.rtn(not_here_object_f))),
    ])
z.define_object(BLESSINGS, 'blessings', parent=GLOBAL_OBJECTS,
    flags=[NDESCBIT],
    props=[
        (P_SYNONYM, z.words(_W['blessings'], _W['graces'])),
    ])
z.define_object(STAIRS, 'stairs', parent=LOCAL_GLOBALS,
    flags=[NDESCBIT, CLIMBBIT],
    props=[
        (P_SYNONYM, z.words(_W['stairs'], _W['steps'], _W['staircase'], _W['stairway'])),
        (P_ACTION, z.words(z.rtn(stairs_f))),
        (P_ADJECTIVE, z.bytes_(_A['stone'], _A['dark'], _A['marble'], _A['forbidding'], _A['steep'])),
    ])
z.define_object(SAILOR, 'sailor', parent=GLOBAL_OBJECTS,
    flags=[NDESCBIT],
    props=[
        (P_SYNONYM, z.words(_W['sailor'], _W['footpad'], _W['aviator'])),
        (P_ACTION, z.words(z.rtn(sailor_fcn))),
    ])
z.define_object(GROUND, 'ground', parent=GLOBAL_OBJECTS,
    flags=[],
    props=[
        (P_SYNONYM, z.words(_W['ground'], _W['sand'], _W['dirt'], _W['floor'])),
        (P_ACTION, z.words(z.rtn(ground_function))),
    ])
z.define_object(GRUE, 'lurking grue', parent=GLOBAL_OBJECTS,
    flags=[],
    props=[
        (P_SYNONYM, z.words(_W['grue'])),
        (P_ACTION, z.words(z.rtn(grue_function))),
        (P_ADJECTIVE, z.bytes_(_A['lurking'], _A['sinister'], _A['hungry'], _A['silent'])),
    ])
z.define_object(LUNGS, 'blast of air', parent=GLOBAL_OBJECTS,
    flags=[NDESCBIT],
    props=[
        (P_SYNONYM, z.words(_W['lungs'], _W['air'], _W['mouth'], _W['breath'])),
    ])
z.define_object(ME, 'you', parent=GLOBAL_OBJECTS,
    flags=[ACTORBIT],
    props=[
        (P_SYNONYM, z.words(_W['me'], _W['myself'], _W['self'], _W['cretin'])),
        (P_ACTION, z.words(z.rtn(cretin_fcn))),
    ])
z.define_object(ADVENTURER, 'cretin', parent=0,
    flags=[NDESCBIT, INVISIBLE, SACREDBIT, ACTORBIT],
    props=[
        (P_SYNONYM, z.words(_W['adventurer'])),
        (P_ACTION, z.words(0)),
        (P_STRENGTH, z.words(0)),
    ])
z.define_object(PATHOBJ, 'passage', parent=GLOBAL_OBJECTS,
    flags=[NDESCBIT],
    props=[
        (P_SYNONYM, z.words(_W['trail'], _W['path'])),
        (P_ACTION, z.words(z.rtn(path_object))),
        (P_ADJECTIVE, z.bytes_(_A['forest'], _A['narrow'], _A['long'], _A['winding'])),
    ])
z.define_object(ZORKMID, 'zorkmid', parent=GLOBAL_OBJECTS,
    flags=[],
    props=[
        (P_SYNONYM, z.words(_W['zorkmid'])),
        (P_ACTION, z.words(z.rtn(zorkmid_function))),
    ])
z.define_object(HANDS, 'pair of hands', parent=GLOBAL_OBJECTS,
    flags=[NDESCBIT, TOOLBIT],
    props=[
        (P_SYNONYM, z.words(_W['pair'], _W['hands'], _W['hand'])),
        (P_ADJECTIVE, z.bytes_(_A['bare'])),
    ])
z.link_objects()

# Globals and table constants, in source order
SCORE_MAX = 350
FALSE_FLAG = 0
CYCLOPS_FLAG = 0
DEFLATE = 0
DOME_FLAG = 0
EMPTY_HANDED = 0
LLD_FLAG = 0
LOW_TIDE = 0
MAGIC_FLAG = 0
RAINBOW_FLAG = 0
TROLL_FLAG = 0
WON_FLAG = 0
COFFIN_CURE = 0
HOUSE_AROUND = z.table([WEST_OF_HOUSE, NORTH_OF_HOUSE, EAST_OF_HOUSE, SOUTH_OF_HOUSE, WEST_OF_HOUSE], length=True)
FOREST_AROUND = z.table([FOREST_1, FOREST_2, FOREST_3, PATH, CLEARING, FOREST_1], length=True)
IN_HOUSE_AROUND = z.table([LIVING_ROOM, KITCHEN, ATTIC, KITCHEN], length=True)
ABOVE_GROUND = z.table([WEST_OF_HOUSE, NORTH_OF_HOUSE, EAST_OF_HOUSE, SOUTH_OF_HOUSE, FOREST_1, FOREST_2, FOREST_3, PATH, CLEARING, GRATING_CLEARING, CANYON_VIEW], length=True)
LOAD_MAX = 100
LOAD_ALLOWED = 100
C_TABLE = z.itable(180, [0])
C_DEMONS = 180
C_INTS = 180
CLOCK_WAIT = 0
PLAYER = 0
P_WON = 0
P_MULT = 0
P_NOT_HERE = 0
PRSA = 0
PRSI = 0
PRSO = 0
P_TABLE = 0
P_ONEOBJ = 0
P_SYNTAX = 0
P_CCTBL = z.table([0, 0, 0, 0])
P_LEN = 0
P_DIR = 0
HERE = 0
WINNER = 0
P_LEXV = z.itable(59, [0, z.BYTE(0), z.BYTE(0)], lexv=True)
AGAIN_LEXV = z.itable(59, [0, z.BYTE(0), z.BYTE(0)], lexv=True)
RESERVE_LEXV = z.itable(59, [0, z.BYTE(0), z.BYTE(0)], lexv=True)
RESERVE_PTR = 0
P_INBUF = z.itable(120, [0], byte=True, length=True)
OOPS_INBUF = z.itable(120, [0], byte=True, length=True)
OOPS_TABLE = z.table([0, 0, 0, 0])
P_CONT = 0
P_IT_OBJECT = 0
P_OFLAG = 0
P_MERGED = 0
P_ACLAUSE = 0
P_ANAM = 0
P_AADJ = 0
P_ITBL = z.table([0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
P_OTBL = z.table([0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
P_VTBL = z.table([0, 0, 0, 0])
P_OVTBL = z.table([0, z.BYTE(0), z.BYTE(0)])
P_NCN = 0
QUOTE_FLAG = 0
P_END_ON_PREP = 0
P_ACT = 0
P_WALK_DIR = 0
AGAIN_DIR = 0
P_NUMBER = 0
P_DIRECTION = 0
P_SLOCBITS = 0
P_GWIMBIT = 0
P_NAM = 0
P_ADJ = 0
P_ADVERB = 0
P_ADJN = 0
P_PRSO = z.itable(50, [0])
P_PRSI = z.itable(50, [0])
P_BUTS = z.itable(50, [0])
P_MERGE = z.itable(50, [0])
P_OCLAUSE = z.itable(100, [0])
P_MATCHLEN = 0
P_GETFLAGS = 0
P_AND = 0
P_XNAM = 0
P_XADJ = 0
P_XADJN = 0
ALWAYS_LIT = 0
VERBOSE = 0
SUPER_BRIEF = 0
HS = 0
JUMPLOSS = z.table([0, 'You should have looked before you leaped.', 'In the movies, your life would be passing before your eyes.', 'Geronimo...'], length=True)
WHEEEEE = z.table([0, 'Very good. Now you can go to the second grade.', 'Are you enjoying yourself?', 'Wheeeeeeeeee!!!!!', 'Do you expect me to applaud?'], length=True)
LIT = 0
SPRAYED_P = 0
DESC_OBJECT = 0
MOVES = 0
SCORE = 0
BASE_SCORE = 0
DEAD = 0
DEATHS = 0
LUCKY = 1
FUMBLE_NUMBER = 7
FUMBLE_PROB = 8
INDENTS = z.table(['', '  ', '    ', '      ', '        ', '          '])
HO_HUM = z.table([0, " doesn't seem to work.", " isn't notably helpful.", ' has no effect.'], length=True)
SWIMYUKS = z.table([0, "You can't swim in the dungeon."], length=True)
HELLOS = z.table([0, 'Hello.', 'Good day.', "Nice weather we've been having lately.", 'Goodbye.'], length=True)
YUKS = z.table([0, 'A valiant attempt.', "You can't be serious.", 'An interesting idea...', 'What a concept!'], length=True)
DUMMY = z.table([0, 'Look around.', 'Too late for that.', 'Have your eyes checked.'], length=True)
KITCHEN_WINDOW_FLAG = 0
CAGE_TOP = 1
BAT_DROPS = z.table([0, MINE_1, MINE_2, MINE_3, MINE_4, LADDER_TOP, LADDER_BOTTOM, SQUEEKY_ROOM, MINE_ENTRANCE], length=True)
RUG_MOVED = 0
GRATE_REVEALED = 0
GRUNLOCK = 0
MIRROR_MUNG = 0
XB = 0
XC = 0
GATE_FLAG = 0
GATES_OPEN = 0
LOUD_RUNS = z.table([0, DAMP_CAVE, ROUND_ROOM, DEEP_CANYON], length=True)
DROWNINGS = z.table(['up to your ankles.', 'up to your shin.', 'up to your knees.', 'up to your hips.', 'up to your waist.', 'up to your chest.', 'up to your neck.', 'over your head.', 'high in your lungs.'])
WATER_LEVEL = 0
CYCLOWRATH = 0
CYCLOMAD = z.table(['The cyclops seems somewhat agitated.', 'The cyclops appears to be getting more agitated.', 'The cyclops is moving about the room, looking for something.', 'The cyclops was looking for salt and pepper. No doubt they are condiments for his upcoming snack.', 'The cyclops is moving toward you in an unfriendly manner.', 'You have two choices: 1. Leave  2. Become dinner.'])
LOUD_FLAG = 0
EGG_SOLVE = 0
THIEF_HERE = 0
THIEF_ENGROSSED = 0
ROBBER_C_DESC = 'There is a suspicious-looking individual, holding a bag, leaning against one wall. He is armed with a vicious-looking stiletto.'
ROBBER_U_DESC = 'There is a suspicious-looking individual lying unconscious on the ground.'
LAMP_TABLE = z.table([100, 'The lamp appears a bit dimmer.', 70, 'The lamp is definitely dimmer now.', 15, 'The lamp is nearly out.', 0])
MATCH_COUNT = 6
CANDLE_TABLE = z.table([20, 'The candles grow shorter.', 10, 'The candles are becoming quite short.', 5, "The candles won't last long now.", 0])
LIGHT_SHAFT = 13
RIVER_SPEEDS = z.table([RIVER_1, 4, RIVER_2, 4, RIVER_3, 3, RIVER_4, 2, RIVER_5, 1], length=True)
RIVER_NEXT = z.table([RIVER_1, RIVER_2, RIVER_3, RIVER_4, RIVER_5], length=True)
RIVER_LAUNCH = z.table([DAM_BASE, RIVER_1, WHITE_CLIFFS_NORTH, RIVER_3, WHITE_CLIFFS_SOUTH, RIVER_4, SHORE, RIVER_5, SANDY_BEACH, RIVER_4, RESERVOIR_SOUTH, RESERVOIR, RESERVOIR_NORTH, RESERVOIR, STREAM_VIEW, IN_STREAM], length=True)
BUOY_FLAG = 1
BEACH_DIG = -1
BDIGS = z.table(['You seem to be digging a hole here.', "The hole is getting deeper, but that's about it.", 'You are surrounded by a wall of sand on all sides.'])
SING_SONG = 0
DEF1 = z.table([MISSED, MISSED, MISSED, MISSED, STAGGER, STAGGER, UNCONSCIOUS, UNCONSCIOUS, KILLED, KILLED, KILLED, KILLED, KILLED])
DEF2A = z.table([MISSED, MISSED, MISSED, MISSED, MISSED, STAGGER, STAGGER, LIGHT_WOUND, LIGHT_WOUND, UNCONSCIOUS])
DEF2B = z.table([MISSED, MISSED, MISSED, STAGGER, STAGGER, LIGHT_WOUND, LIGHT_WOUND, LIGHT_WOUND, UNCONSCIOUS, KILLED, KILLED, KILLED])
DEF3A = z.table([MISSED, MISSED, MISSED, MISSED, MISSED, STAGGER, STAGGER, LIGHT_WOUND, LIGHT_WOUND, SERIOUS_WOUND, SERIOUS_WOUND])
DEF3B = z.table([MISSED, MISSED, MISSED, STAGGER, STAGGER, LIGHT_WOUND, LIGHT_WOUND, LIGHT_WOUND, SERIOUS_WOUND, SERIOUS_WOUND, SERIOUS_WOUND])
DEF3C = z.table([MISSED, STAGGER, STAGGER, LIGHT_WOUND, LIGHT_WOUND, LIGHT_WOUND, LIGHT_WOUND, SERIOUS_WOUND, SERIOUS_WOUND, SERIOUS_WOUND])
DEF1_RES = z.table([DEF1, 0, 0])
DEF2_RES = z.table([DEF2A, DEF2B, 0, 0])
DEF3_RES = z.table([DEF3A, 0, DEF3B, 0, DEF3C])
HERO_MELEE = z.table([z.table([z.table(['Your ', F_WEP, ' misses the ', F_DEF, ' by an inch.'], length=True), z.table(['A good slash, but it misses the ', F_DEF, ' by a mile.'], length=True), z.table(['You charge, but the ', F_DEF, ' jumps nimbly aside.'], length=True), z.table(['Clang! Crash! The ', F_DEF, ' parries.'], length=True), z.table(['A quick stroke, but the ', F_DEF, ' is on guard.'], length=True), z.table(["A good stroke, but it's too slow; the ", F_DEF, ' dodges.'], length=True)], length=True), z.table([z.table(['Your ', F_WEP, ' crashes down, knocking the ', F_DEF, ' into dreamland.'], length=True), z.table(['The ', F_DEF, ' is battered into unconsciousness.'], length=True), z.table(['A furious exchange, and the ', F_DEF, ' is knocked out!'], length=True), z.table(['The haft of your ', F_WEP, ' knocks out the ', F_DEF, '.'], length=True), z.table(['The ', F_DEF, ' is knocked out!'], length=True)], length=True), z.table([z.table(["It's curtains for the ", F_DEF, ' as your ', F_WEP, ' removes his head.'], length=True), z.table(['The fatal blow strikes the ', F_DEF, ' square in the heart: He dies.'], length=True), z.table(['The ', F_DEF, ' takes a fatal blow and slumps to the floor dead.'], length=True)], length=True), z.table([z.table(['The ', F_DEF, ' is struck on the arm; blood begins to trickle down.'], length=True), z.table(['Your ', F_WEP, ' pinks the ', F_DEF, " on the wrist, but it's not serious."], length=True), z.table(['Your stroke lands, but it was only the flat of the blade.'], length=True), z.table(['The blow lands, making a shallow gash in the ', F_DEF, "'s arm!"], length=True)], length=True), z.table([z.table(['The ', F_DEF, ' receives a deep gash in his side.'], length=True), z.table(['A savage blow on the thigh! The ', F_DEF, ' is stunned but can still fight!'], length=True), z.table(['Slash! Your blow lands! That one hit an artery, it could be serious!'], length=True), z.table(['Slash! Your stroke connects! This could be serious!'], length=True)], length=True), z.table([z.table(['The ', F_DEF, ' is staggered, and drops to his knees.'], length=True), z.table(['The ', F_DEF, " is momentarily disoriented and can't fight back."], length=True), z.table(['The force of your blow knocks the ', F_DEF, ' back, stunned.'], length=True), z.table(['The ', F_DEF, " is confused and can't fight back."], length=True), z.table(['The quickness of your thrust knocks the ', F_DEF, ' back, stunned.'], length=True)], length=True), z.table([z.table(['The ', F_DEF, "'s weapon is knocked to the floor, leaving him unarmed."], length=True), z.table(['The ', F_DEF, ' is disarmed by a subtle feint past his guard.'], length=True)], length=True)])
CYCLOPS_MELEE = z.table([z.table([z.table(['The Cyclops misses, but the backwash almost knocks you over.'], length=True), z.table(['The Cyclops rushes you, but runs into the wall.'], length=True)], length=True), z.table([z.table(['The Cyclops sends you crashing to the floor, unconscious.'], length=True)], length=True), z.table([z.table(['The Cyclops breaks your neck with a massive smash.'], length=True)], length=True), z.table([z.table(['A quick punch, but it was only a glancing blow.'], length=True), z.table(["A glancing blow from the Cyclops' fist."], length=True)], length=True), z.table([z.table(['The monster smashes his huge fist into your chest, breaking several ribs.'], length=True), z.table(['The Cyclops almost knocks the wind out of you with a quick punch.'], length=True)], length=True), z.table([z.table(['The Cyclops lands a punch that knocks the wind out of you.'], length=True), z.table(['Heedless of your weapons, the Cyclops tosses you against the rock wall of the room.'], length=True)], length=True), z.table([z.table(['The Cyclops grabs your ', F_WEP, ', tastes it, and throws it to the ground in disgust.'], length=True), z.table(['The monster grabs you on the wrist, squeezes, and you drop your ', F_WEP, ' in pain.'], length=True)], length=True), z.table([z.table(['The Cyclops seems unable to decide whether to broil or stew his dinner.'], length=True)], length=True), z.table([z.table(['The Cyclops, no sportsman, dispatches his unconscious victim.'], length=True)], length=True)])
TROLL_MELEE = z.table([z.table([z.table(['The troll swings his axe, but it misses.'], length=True), z.table(["The troll's axe barely misses your ear."], length=True), z.table(['The axe sweeps past as you jump aside.'], length=True), z.table(['The axe crashes against the rock, throwing sparks!'], length=True)], length=True), z.table([z.table(["The flat of the troll's axe hits you delicately on the head, knocking you out."], length=True)], length=True), z.table([z.table(['The troll neatly removes your head.'], length=True), z.table(["The troll's axe stroke cleaves you from the nave to the chops."], length=True), z.table(["The troll's axe removes your head."], length=True)], length=True), z.table([z.table(['The axe gets you right in the side. Ouch!'], length=True), z.table(["The flat of the troll's axe skins across your forearm."], length=True), z.table(["The troll's swing almost knocks you over as you barely parry in time."], length=True), z.table(['The troll swings his axe, and it nicks your arm as you dodge.'], length=True)], length=True), z.table([z.table(['The troll charges, and his axe slashes you on your ', F_WEP, ' arm.'], length=True), z.table(['An axe stroke makes a deep wound in your leg.'], length=True), z.table(["The troll's axe swings down, gashing your shoulder."], length=True)], length=True), z.table([z.table(['The troll hits you with a glancing blow, and you are momentarily stunned.'], length=True), z.table(['The troll swings; the blade turns on your armor but crashes broadside into your head.'], length=True), z.table(['You stagger back under a hail of axe strokes.'], length=True), z.table(["The troll's mighty blow drops you to your knees."], length=True)], length=True), z.table([z.table(['The axe hits your ', F_WEP, ' and knocks it spinning.'], length=True), z.table(['The troll swings, you parry, but the force of his blow knocks your ', F_WEP, ' away.'], length=True), z.table(['The axe knocks your ', F_WEP, ' out of your hand. It falls to the floor.'], length=True)], length=True), z.table([z.table(['The troll hesitates, fingering his axe.'], length=True), z.table(['The troll scratches his head ruminatively:  Might you be magically protected, he wonders?'], length=True)], length=True), z.table([z.table(['Conquering his fears, the troll puts you to death.'], length=True)], length=True)])
THIEF_MELEE = z.table([z.table([z.table(['The thief stabs nonchalantly with his stiletto and misses.'], length=True), z.table(['You dodge as the thief comes in low.'], length=True), z.table(['You parry a lightning thrust, and the thief salutes you with a grim nod.'], length=True), z.table(['The thief tries to sneak past your guard, but you twist away.'], length=True)], length=True), z.table([z.table(['Shifting in the midst of a thrust, the thief knocks you unconscious with the haft of his stiletto.'], length=True), z.table(['The thief knocks you out.'], length=True)], length=True), z.table([z.table(['Finishing you off, the thief inserts his blade into your heart.'], length=True), z.table(['The thief comes in from the side, feints, and inserts the blade into your ribs.'], length=True), z.table(['The thief bows formally, raises his stiletto, and with a wry grin, ends the battle and your life.'], length=True)], length=True), z.table([z.table(['A quick thrust pinks your left arm, and blood starts to trickle down.'], length=True), z.table(['The thief draws blood, raking his stiletto across your arm.'], length=True), z.table(['The stiletto flashes faster than you can follow, and blood wells from your leg.'], length=True), z.table(['The thief slowly approaches, strikes like a snake, and leaves you wounded.'], length=True)], length=True), z.table([z.table(['The thief strikes like a snake! The resulting wound is serious.'], length=True), z.table(['The thief stabs a deep cut in your upper arm.'], length=True), z.table(['The stiletto touches your forehead, and the blood obscures your vision.'], length=True), z.table(['The thief strikes at your wrist, and suddenly your grip is slippery with blood.'], length=True)], length=True), z.table([z.table(['The butt of his stiletto cracks you on the skull, and you stagger back.'], length=True), z.table(['The thief rams the haft of his blade into your stomach, leaving you out of breath.'], length=True), z.table(['The thief attacks, and you fall back desperately.'], length=True)], length=True), z.table([z.table(['A long, theatrical slash. You catch it on your ', F_WEP, ', but the thief twists his knife, and the ', F_WEP, ' goes flying.'], length=True), z.table(['The thief neatly flips your ', F_WEP, ' out of your hands, and it drops to the floor.'], length=True), z.table(['You parry a low thrust, and your ', F_WEP, ' slips out of your hand.'], length=True)], length=True), z.table([z.table(['The thief, a man of superior breeding, pauses for a moment to consider the propriety of finishing you off.'], length=True), z.table(['The thief amuses himself by searching your pockets.'], length=True), z.table(['The thief entertains himself by rifling your pack.'], length=True)], length=True), z.table([z.table(['The thief, forgetting his essentially genteel upbringing, cuts your throat.'], length=True), z.table(['The thief, a pragmatist, dispatches you as a threat to his livelihood.'], length=True)], length=True)])
VILLAINS = z.table([z.table([TROLL, SWORD, 1, 0, TROLL_MELEE]), z.table([THIEF, KNIFE, 1, 0, THIEF_MELEE]), z.table([CYCLOPS, 0, 0, 0, CYCLOPS_MELEE])], length=True)

# Tables that appear inside routine bodies

# Syntax tables used by the parser
_SYNTAX = {}
# Each entry: (objects, prep1, prep2, find1, find2, loc1, loc2, action)
_SYNTAX[ACT_VERBOSE] = [
    (0, 0, 0, 0, 0, 0, 0, V_VERBOSE),
]
_SYNTAX[ACT_BRIEF] = [
    (0, 0, 0, 0, 0, 0, 0, V_BRIEF),
]
_SYNTAX[ACT_SUPER] = [
    (0, 0, 0, 0, 0, 0, 0, V_SUPER_BRIEF),
]
_SYNTAX[ACT_DIAGNOSE] = [
    (0, 0, 0, 0, 0, 0, 0, V_DIAGNOSE),
]
_SYNTAX[ACT_INVENTORY] = [
    (0, 0, 0, 0, 0, 0, 0, V_INVENTORY),
]
_SYNTAX[ACT_QUIT] = [
    (0, 0, 0, 0, 0, 0, 0, V_QUIT),
]
_SYNTAX[ACT_RESTART] = [
    (0, 0, 0, 0, 0, 0, 0, V_RESTART),
]
_SYNTAX[ACT_RESTORE] = [
    (0, 0, 0, 0, 0, 0, 0, V_RESTORE),
]
_SYNTAX[ACT_SAVE] = [
    (0, 0, 0, 0, 0, 0, 0, V_SAVE),
]
_SYNTAX[ACT_SCORE] = [
    (0, 0, 0, 0, 0, 0, 0, V_SCORE),
]
_SYNTAX[ACT_SCRIPT] = [
    (0, 0, 0, 0, 0, 0, 0, V_SCRIPT),
]
_SYNTAX[ACT_UNSCRIPT] = [
    (0, 0, 0, 0, 0, 0, 0, V_UNSCRIPT),
]
_SYNTAX[ACT_VERSION] = [
    (0, 0, 0, 0, 0, 0, 0, V_VERSION),
]
_SYNTAX[ACT_S_VERIFY] = [
    (0, 0, 0, 0, 0, 0, 0, V_VERIFY),
]
_SYNTAX[ACT_H_RANDOM] = [
    (1, 0, 0, 0, 0, 0, 0, V_RANDOM),
]
_SYNTAX[ACT_H_COMMAND] = [
    (0, 0, 0, 0, 0, 0, 0, V_COMMAND_FILE),
]
_SYNTAX[ACT_H_RECORD] = [
    (0, 0, 0, 0, 0, 0, 0, V_RECORD),
]
_SYNTAX[ACT_H_UNRECORD] = [
    (0, 0, 0, 0, 0, 0, 0, V_UNRECORD),
]
_SYNTAX[ACT_ACTIVATE] = [
    (1, 0, 0, LIGHTBIT, 0, 240, 0, V_LAMP_ON),
]
_SYNTAX[ACT_ANSWER] = [
    (1, 0, 0, 0, 0, 0, 0, V_REPLY),
    (0, 0, 0, 0, 0, 0, 0, V_ANSWER),
]
_SYNTAX[ACT_APPLY] = [
    (2, 0, PR_TO, 0, 0, 0, 0, V_PUT),
]
_SYNTAX[ACT_ATTACK] = [
    (2, 0, PR_WITH, ACTORBIT, WEAPONBIT, 48, 194, V_ATTACK),
]
_SYNTAX[ACT_BACK] = [
    (0, 0, 0, 0, 0, 0, 0, V_BACK),
]
_SYNTAX[ACT_BLAST] = [
    (0, 0, 0, 0, 0, 0, 0, V_BLAST),
]
_SYNTAX[ACT_BLOW] = [
    (1, PR_IN, 0, 0, 0, 0, 0, V_BREATHE),
    (1, PR_UP, 0, 0, 0, 0, 0, V_BLAST),
    (2, PR_UP, PR_WITH, 0, TOOLBIT, 0, 240, V_INFLATE),
    (1, PR_OUT, 0, 0, 0, 0, 0, V_LAMP_OFF),
]
_SYNTAX[ACT_BOARD] = [
    (1, 0, 0, VEHBIT, 0, 48, 0, V_BOARD),
]
_SYNTAX[ACT_BRUSH] = [
    (2, 0, PR_WITH, 0, 0, 240, 0, V_BRUSH),
    (1, 0, 0, 0, 0, 240, 0, V_BRUSH),
]
_SYNTAX[ACT_BUG] = [
    (0, 0, 0, 0, 0, 0, 0, V_BUG),
]
_SYNTAX[ACT_BURN] = [
    (2, PR_DOWN, PR_WITH, BURNBIT, FLAMEBIT, 240, 242, V_BURN),
    (2, 0, PR_WITH, BURNBIT, FLAMEBIT, 240, 242, V_BURN),
]
_SYNTAX[ACT_CHOMP] = [
    (0, 0, 0, 0, 0, 0, 0, V_CHOMP),
]
_SYNTAX[ACT_CLIMB] = [
    (1, PR_WITH, 0, 0, 0, 0, 0, V_THROUGH),
    (1, PR_ON, 0, VEHBIT, 0, 48, 0, V_CLIMB_ON),
    (1, PR_IN, 0, VEHBIT, 0, 48, 0, V_BOARD),
    (1, 0, 0, CLIMBBIT, 0, 48, 0, V_CLIMB_FOO),
    (1, PR_DOWN, 0, CLIMBBIT, 0, 48, 0, V_CLIMB_DOWN),
    (1, PR_DOWN, 0, RMUNGBIT, 0, 0, 0, V_CLIMB_DOWN),
    (1, PR_UP, 0, CLIMBBIT, 0, 48, 0, V_CLIMB_UP),
    (1, PR_UP, 0, RMUNGBIT, 0, 0, 0, V_CLIMB_UP),
]
_SYNTAX[ACT_CLOSE] = [
    (1, 0, 0, DOORBIT, 0, 240, 0, V_CLOSE),
]
_SYNTAX[ACT_COMMAND] = [
    (1, 0, 0, ACTORBIT, 0, 0, 0, V_COMMAND),
]
_SYNTAX[ACT_COUNT] = [
    (1, 0, 0, 0, 0, 0, 0, V_COUNT),
]
_SYNTAX[ACT_CROSS] = [
    (1, 0, 0, 0, 0, 0, 0, V_CROSS),
]
_SYNTAX[ACT_CUT] = [
    (2, 0, PR_WITH, 0, WEAPONBIT, 0, 192, V_CUT),
]
_SYNTAX[ACT_CURSE] = [
    (1, 0, 0, ACTORBIT, 0, 0, 0, V_CURSES),
    (0, 0, 0, 0, 0, 0, 0, V_CURSES),
]
_SYNTAX[ACT_DEFLATE] = [
    (1, 0, 0, 0, 0, 0, 0, V_DEFLATE),
]
_SYNTAX[ACT_DESTROY] = [
    (1, PR_IN, 0, 0, 0, 240, 0, V_OPEN),
    (2, PR_DOWN, PR_WITH, 0, 0, 240, 200, V_MUNG),
    (2, 0, PR_WITH, 0, 0, 240, 200, V_MUNG),
]
_SYNTAX[ACT_DIG] = [
    (2, 0, PR_WITH, 0, TOOLBIT, 48, 194, V_DIG),
    (2, PR_IN, PR_WITH, 0, TOOLBIT, 48, 194, V_DIG),
    (1, PR_IN, 0, 0, 0, 48, 0, V_DIG),
]
_SYNTAX[ACT_DISEMBARK] = [
    (1, 0, 0, VEHBIT, 0, 48, 0, V_DISEMBARK),
]
_SYNTAX[ACT_DISENCHANT] = [
    (1, 0, 0, 0, 0, 0, 0, V_DISENCHANT),
]
_SYNTAX[ACT_DRINK] = [
    (1, PR_FROM, 0, 0, 0, 192, 0, V_DRINK_FROM),
    (1, 0, 0, DRINKBIT, 0, 240, 0, V_DRINK),
]
_SYNTAX[ACT_DROP] = [
    (2, 0, PR_ON, 0, 0, 134, 0, V_PUT_ON),
    (2, 0, PR_IN, 0, 0, 134, 0, V_PUT),
    (2, 0, PR_DOWN, 0, 0, 134, 0, V_PUT),
    (1, 0, 0, 0, 0, 134, 0, V_DROP),
]
_SYNTAX[ACT_EAT] = [
    (1, 0, 0, FOODBIT, 0, 248, 0, V_EAT),
]
_SYNTAX[ACT_ECHO] = [
    (0, 0, 0, 0, 0, 0, 0, V_ECHO),
]
_SYNTAX[ACT_ENCHANT] = [
    (1, 0, 0, 0, 0, 48, 0, V_ENCHANT),
]
_SYNTAX[ACT_ENTER] = [
    (1, 0, 0, 0, 0, 0, 0, V_THROUGH),
    (0, 0, 0, 0, 0, 0, 0, V_ENTER),
]
_SYNTAX[ACT_EXIT] = [
    (1, 0, 0, 0, 0, 0, 0, V_EXIT),
    (0, 0, 0, 0, 0, 0, 0, V_EXIT),
]
_SYNTAX[ACT_EXAMINE] = [
    (1, PR_ON, 0, 0, 0, 244, 0, V_LOOK_INSIDE),
    (1, PR_IN, 0, 0, 0, 244, 0, V_LOOK_INSIDE),
    (1, 0, 0, 0, 0, 4, 0, V_EXAMINE),
]
_SYNTAX[ACT_EXORCISE] = [
    (1, PR_AWAY, 0, ACTORBIT, 0, 0, 0, V_EXORCISE),
    (1, PR_OUT, 0, ACTORBIT, 0, 0, 0, V_EXORCISE),
    (1, 0, 0, 0, 0, 0, 0, V_EXORCISE),
]
_SYNTAX[ACT_EXTINGUISH] = [
    (1, 0, 0, ONBIT, 0, 250, 0, V_LAMP_OFF),
]
_SYNTAX[ACT_FILL] = [
    (1, 0, 0, CONTBIT, 0, 240, 0, V_FILL),
    (2, 0, PR_WITH, CONTBIT, 0, 240, 0, V_FILL),
]
_SYNTAX[ACT_FIND] = [
    (1, 0, 0, 0, 0, 0, 0, V_FIND),
]
_SYNTAX[ACT_FOLLOW] = [
    (1, 0, 0, 0, 0, 0, 0, V_FOLLOW),
    (0, 0, 0, 0, 0, 0, 0, V_FOLLOW),
]
_SYNTAX[ACT_FROBOZZ] = [
    (0, 0, 0, 0, 0, 0, 0, V_FROBOZZ),
]
_SYNTAX[ACT_GIVE] = [
    (2, 0, 0, ACTORBIT, 0, 16, 134, V_SGIVE),
    (2, 0, PR_TO, 0, ACTORBIT, 134, 16, V_GIVE),
]
_SYNTAX[ACT_HATCH] = [
    (1, 0, 0, 0, 0, 0, 0, V_HATCH),
]
_SYNTAX[ACT_HELLO] = [
    (1, 0, 0, 0, 0, 0, 0, V_HELLO),
    (0, 0, 0, 0, 0, 0, 0, V_HELLO),
]
_SYNTAX[ACT_INCANT] = [
    (0, 0, 0, 0, 0, 0, 0, V_INCANT),
]
_SYNTAX[ACT_INFLAT] = [
    (2, 0, PR_WITH, 0, TOOLBIT, 0, 240, V_INFLATE),
]
_SYNTAX[ACT_JUMP] = [
    (1, PR_OFF, 0, 0, 0, 0, 0, V_LEAP),
    (1, PR_FROM, 0, 0, 0, 0, 0, V_LEAP),
    (1, PR_IN, 0, 0, 0, 0, 0, V_LEAP),
    (1, PR_ACROSS, 0, 0, 0, 0, 0, V_LEAP),
    (1, PR_OVER, 0, 0, 0, 0, 0, V_LEAP),
    (0, 0, 0, 0, 0, 0, 0, V_LEAP),
]
_SYNTAX[ACT_KICK] = [
    (1, 0, 0, 0, 0, 0, 0, V_KICK),
]
_SYNTAX[ACT_KILL] = [
    (2, 0, PR_WITH, ACTORBIT, WEAPONBIT, 48, 194, V_ATTACK),
]
_SYNTAX[ACT_STAB] = [
    (2, 0, PR_WITH, ACTORBIT, WEAPONBIT, 48, 194, V_ATTACK),
    (1, 0, 0, ACTORBIT, 0, 48, 0, V_STAB),
]
_SYNTAX[ACT_KISS] = [
    (1, 0, 0, ACTORBIT, 0, 48, 0, V_KISS),
]
_SYNTAX[ACT_KNOCK] = [
    (1, PR_DOWN, 0, ACTORBIT, 0, 48, 0, V_ATTACK),
    (1, PR_ON, 0, 0, 0, 0, 0, V_KNOCK),
    (1, PR_AT, 0, 0, 0, 0, 0, V_KNOCK),
]
_SYNTAX[ACT_LAUNCH] = [
    (1, 0, 0, VEHBIT, 0, 0, 0, V_LAUNCH),
]
_SYNTAX[ACT_LEAN] = [
    (1, PR_ON, 0, 0, 0, 130, 0, V_LEAN_ON),
]
_SYNTAX[ACT_LEAVE] = [
    (1, 0, 0, 0, 0, 0, 0, V_DROP),
    (0, 0, 0, 0, 0, 0, 0, V_LEAVE),
]
_SYNTAX[ACT_LIGHT] = [
    (2, 0, PR_WITH, LIGHTBIT, FLAMEBIT, 240, 202, V_BURN),
    (1, 0, 0, LIGHTBIT, 0, 250, 0, V_LAMP_ON),
]
_SYNTAX[ACT_LISTEN] = [
    (1, PR_FOR, 0, 0, 0, 0, 0, V_LISTEN),
    (1, PR_TO, 0, 0, 0, 0, 0, V_LISTEN),
]
_SYNTAX[ACT_LOCK] = [
    (2, 0, PR_WITH, 0, TOOLBIT, 48, 248, V_LOCK),
]
_SYNTAX[ACT_LOOK] = [
    (1, PR_FOR, 0, 0, 0, 0, 0, V_FIND),
    (2, PR_AT, PR_WITH, 0, 0, 240, 0, V_READ),
    (1, PR_IN, 0, 0, 0, 244, 0, V_LOOK_INSIDE),
    (1, PR_BEHIND, 0, 0, 0, 0, 0, V_LOOK_BEHIND),
    (1, PR_UNDER, 0, 0, 0, 0, 0, V_LOOK_UNDER),
    (1, PR_WITH, 0, 0, 0, 244, 0, V_LOOK_INSIDE),
    (1, PR_ON, 0, 0, 0, 0, 0, V_LOOK_ON),
    (1, PR_AT, 0, 0, 0, 244, 0, V_EXAMINE),
    (1, PR_DOWN, 0, RMUNGBIT, 0, 0, 0, V_LOOK),
    (1, PR_UP, 0, RMUNGBIT, 0, 0, 0, V_LOOK),
    (1, PR_AROUND, 0, RMUNGBIT, 0, 0, 0, V_LOOK),
    (0, 0, 0, 0, 0, 0, 0, V_LOOK),
]
_SYNTAX[ACT_LOWER] = [
    (1, 0, 0, 0, 0, 0, 0, V_LOWER),
]
_SYNTAX[ACT_LUBRICATE] = [
    (2, 0, PR_WITH, 0, 0, 0, 192, V_OIL),
]
_SYNTAX[ACT_MAKE] = [
    (1, 0, 0, 0, 0, 0, 0, V_MAKE),
]
_SYNTAX[ACT_MELT] = [
    (2, 0, PR_WITH, 0, FLAMEBIT, 0, 240, V_MELT),
]
_SYNTAX[ACT_MOVE] = [
    (2, 0, PR_WITH, 0, TOOLBIT, 0, 0, V_TURN),
    (2, 0, PR_IN, 0, 0, 134, 0, V_PUT),
    (2, 0, PR_TO, 0, 0, 48, 0, V_PUSH_TO),
    (2, 0, 0, 0, 0, 48, 0, V_PUSH_TO),
    (1, 0, 0, 0, 0, 48, 0, V_MOVE),
]
_SYNTAX[ACT_ROLL] = [
    (1, 0, 0, 0, 0, 48, 0, V_MOVE),
    (1, PR_UP, 0, 0, 0, 48, 0, V_MOVE),
]
_SYNTAX[ACT_MUMBLE] = [
    (0, 0, 0, 0, 0, 0, 0, V_MUMBLE),
]
_SYNTAX[ACT_ODYSSEUS] = [
    (0, 0, 0, 0, 0, 0, 0, V_ODYSSEUS),
]
_SYNTAX[ACT_OPEN] = [
    (2, 0, PR_WITH, DOORBIT, TOOLBIT, 240, 242, V_OPEN),
    (1, PR_UP, 0, DOORBIT, 0, 240, 0, V_OPEN),
    (1, 0, 0, DOORBIT, 0, 240, 0, V_OPEN),
]
_SYNTAX[ACT_PICK] = [
    (1, PR_UP, 0, TAKEBIT, 0, 20, 0, V_TAKE),
    (2, 0, PR_WITH, 0, 0, 0, 0, V_PICK),
    (1, 0, 0, 0, 0, 0, 0, V_PICK),
]
_SYNTAX[ACT_PLAY] = [
    (1, 0, 0, 0, 0, 0, 0, V_PLAY),
]
_SYNTAX[ACT_PLUG] = [
    (2, 0, PR_WITH, 0, 0, 0, 0, V_PLUG),
]
_SYNTAX[ACT_PLUGH] = [
    (0, 0, 0, 0, 0, 0, 0, V_ADVENT),
]
_SYNTAX[ACT_POKE] = [
    (2, 0, PR_WITH, ACTORBIT, WEAPONBIT, 48, 194, V_MUNG),
]
_SYNTAX[ACT_PUNCTURE] = [
    (2, 0, PR_WITH, ACTORBIT, WEAPONBIT, 48, 194, V_MUNG),
]
_SYNTAX[ACT_POUR] = [
    (2, 0, PR_FROM, 0, 0, 192, 0, V_DROP),
    (2, 0, PR_ON, 0, 0, 192, 0, V_POUR_ON),
    (2, 0, PR_IN, 0, 0, 192, 0, V_DROP),
    (1, 0, 0, 0, 0, 192, 0, V_DROP),
]
_SYNTAX[ACT_PRAY] = [
    (0, 0, 0, 0, 0, 0, 0, V_PRAY),
]
_SYNTAX[ACT_PULL] = [
    (1, PR_UP, 0, 0, 0, 48, 0, V_MOVE),
    (1, PR_ON, 0, 0, 0, 48, 0, V_MOVE),
    (1, 0, 0, 0, 0, 48, 0, V_MOVE),
]
_SYNTAX[ACT_PUMP] = [
    (2, PR_UP, PR_WITH, 0, 0, 0, 0, V_PUMP),
    (1, PR_UP, 0, 0, 0, 0, 0, V_PUMP),
]
_SYNTAX[ACT_PUSH] = [
    (2, 0, PR_UNDER, 0, 0, 0, 0, V_PUT_UNDER),
    (2, 0, PR_WITH, 0, TOOLBIT, 0, 0, V_TURN),
    (1, PR_ON, 0, 0, 0, 52, 0, V_PUSH),
    (1, 0, 0, 0, 0, 52, 0, V_PUSH),
    (2, 0, PR_TO, 0, 0, 48, 0, V_PUSH_TO),
    (2, 0, 0, 0, 0, 48, 0, V_PUSH_TO),
]
_SYNTAX[ACT_PUT] = [
    (2, 0, PR_BEHIND, 0, 0, 134, 0, V_PUT_BEHIND),
    (1, PR_ON, 0, 0, 0, 116, 0, V_WEAR),
    (1, PR_OUT, 0, ONBIT, 0, 250, 0, V_LAMP_OFF),
    (2, 0, PR_UNDER, 0, 0, 130, 0, V_PUT_UNDER),
    (1, PR_DOWN, 0, 0, 0, 132, 0, V_DROP),
    (2, 0, PR_ON, 0, 0, 134, 0, V_PUT_ON),
    (2, 0, PR_IN, 0, 0, 134, 0, V_PUT),
]
_SYNTAX[ACT_RAISE] = [
    (1, PR_UP, 0, 0, 0, 0, 0, V_RAISE),
    (1, 0, 0, 0, 0, 0, 0, V_RAISE),
]
_SYNTAX[ACT_RAPE] = [
    (1, 0, 0, ACTORBIT, 0, 0, 0, V_RAPE),
]
_SYNTAX[ACT_READ] = [
    (2, 0, 0, READBIT, 0, 248, 0, V_READ_PAGE),
    (2, 0, PR_WITH, READBIT, 0, 248, 0, V_READ),
    (1, PR_FROM, 0, READBIT, 0, 248, 0, V_READ),
    (1, 0, 0, READBIT, 0, 248, 0, V_READ),
]
_SYNTAX[ACT_REPENT] = [
    (0, 0, 0, 0, 0, 0, 0, V_REPENT),
]
_SYNTAX[ACT_RING] = [
    (2, 0, PR_WITH, 0, 0, 8, 0, V_RING),
    (1, 0, 0, 0, 0, 8, 0, V_RING),
]
_SYNTAX[ACT_RUB] = [
    (2, 0, PR_WITH, 0, 0, 0, 0, V_RUB),
    (1, 0, 0, 0, 0, 0, 0, V_RUB),
]
_SYNTAX[ACT_TALK] = [
    (1, PR_TO, 0, ACTORBIT, 0, 32, 0, V_TELL),
]
_SYNTAX[ACT_SAY] = [
    (0, 0, 0, 0, 0, 0, 0, V_SAY),
]
_SYNTAX[ACT_SEARCH] = [
    (1, PR_FOR, 0, 0, 0, 0, 0, V_FIND),
    (1, PR_IN, 0, 0, 0, 0, 0, V_SEARCH),
    (1, 0, 0, 0, 0, 0, 0, V_SEARCH),
]
_SYNTAX[ACT_SEND] = [
    (1, PR_FOR, 0, 0, 0, 0, 0, V_SEND),
]
_SYNTAX[ACT_SHAKE] = [
    (1, 0, 0, 0, 0, 2, 0, V_SHAKE),
]
_SYNTAX[ACT_SKIP] = [
    (0, 0, 0, 0, 0, 0, 0, V_SKIP),
]
_SYNTAX[ACT_SLIDE] = [
    (2, 0, PR_TO, 0, 0, 48, 0, V_PUSH_TO),
    (2, 0, 0, 0, 0, 48, 0, V_PUSH_TO),
    (2, 0, PR_UNDER, 0, 0, 0, 0, V_PUT_UNDER),
]
_SYNTAX[ACT_SMELL] = [
    (1, 0, 0, 0, 0, 0, 0, V_SMELL),
]
_SYNTAX[ACT_SPIN] = [
    (1, 0, 0, 0, 0, 0, 0, V_SPIN),
]
_SYNTAX[ACT_SPRAY] = [
    (2, 0, PR_WITH, 0, 0, 0, 0, V_SSPRAY),
    (2, 0, PR_ON, 0, 0, 0, 0, V_SPRAY),
]
_SYNTAX[ACT_SQUEEZE] = [
    (2, 0, PR_ON, 0, 0, 0, 0, V_PUT),
    (1, 0, 0, 0, 0, 0, 0, V_SQUEEZE),
]
_SYNTAX[ACT_STAND] = [
    (1, PR_UP, 0, RMUNGBIT, 0, 0, 0, V_STAND),
    (0, 0, 0, 0, 0, 0, 0, V_STAND),
]
_SYNTAX[ACT_STAY] = [
    (0, 0, 0, 0, 0, 0, 0, V_STAY),
]
_SYNTAX[ACT_STRIKE] = [
    (1, 0, 0, 0, 0, 240, 0, V_STRIKE),
    (2, 0, PR_WITH, ACTORBIT, WEAPONBIT, 48, 242, V_ATTACK),
]
_SYNTAX[ACT_SWIM] = [
    (1, PR_ACROSS, 0, 0, 0, 0, 0, V_SWIM),
    (1, PR_IN, 0, 0, 0, 0, 0, V_SWIM),
    (0, 0, 0, 0, 0, 0, 0, V_SWIM),
]
_SYNTAX[ACT_SWING] = [
    (2, 0, PR_AT, WEAPONBIT, ACTORBIT, 194, 48, V_SWING),
    (1, 0, 0, WEAPONBIT, 0, 194, 0, V_SWING),
]
_SYNTAX[ACT_TAKE] = [
    (2, 0, PR_FROM, TAKEBIT, 0, 100, 0, V_TAKE),
    (2, 0, PR_OFF, TAKEBIT, 0, 100, 0, V_TAKE),
    (2, 0, PR_OUT, TAKEBIT, 0, 100, 0, V_TAKE),
    (1, PR_UP, 0, RMUNGBIT, 0, 0, 0, V_STAND),
    (1, PR_ON, 0, VEHBIT, 0, 48, 0, V_CLIMB_ON),
    (1, PR_OUT, 0, RMUNGBIT, 0, 48, 0, V_DISEMBARK),
    (1, PR_IN, 0, VEHBIT, 0, 48, 0, V_BOARD),
    (1, 0, 0, TAKEBIT, 0, 52, 0, V_TAKE),
]
_SYNTAX[ACT_TELL] = [
    (2, 0, PR_ABOUT, ACTORBIT, 0, 32, 0, V_TELL),
    (1, 0, 0, ACTORBIT, 0, 32, 0, V_TELL),
]
_SYNTAX[ACT_THROW] = [
    (2, 0, PR_OVER, 0, 0, 194, 0, V_THROW_OFF),
    (2, 0, PR_OFF, 0, 0, 194, 0, V_THROW_OFF),
    (2, 0, PR_ON, 0, 0, 194, 0, V_PUT_ON),
    (2, 0, PR_IN, 0, 0, 194, 0, V_PUT),
    (2, 0, 0, 0, 0, 0, 0, V_OVERBOARD),
    (2, 0, PR_WITH, 0, ACTORBIT, 194, 48, V_THROW),
    (2, 0, PR_AT, 0, ACTORBIT, 194, 48, V_THROW),
]
_SYNTAX[ACT_TIE] = [
    (2, PR_UP, PR_WITH, ACTORBIT, TOOLBIT, 48, 242, V_TIE_UP),
    (2, 0, PR_TO, 0, 0, 0, 0, V_TIE),
]
_SYNTAX[ACT_TREASURE] = [
    (0, 0, 0, 0, 0, 0, 0, V_TREASURE),
]
_SYNTAX[ACT_TURN] = [
    (2, 0, PR_FOR, TURNBIT, 0, 0, 0, V_TURN),
    (2, 0, PR_TO, TURNBIT, 0, 0, 0, V_TURN),
    (1, PR_OFF, 0, ONBIT, 0, 250, 0, V_LAMP_OFF),
    (2, PR_ON, PR_WITH, 0, 0, 0, 2, V_LAMP_ON),
    (1, PR_ON, 0, LIGHTBIT, 0, 240, 0, V_LAMP_ON),
    (2, 0, PR_WITH, TURNBIT, RMUNGBIT, 240, 0, V_TURN),
]
_SYNTAX[ACT_UNLOCK] = [
    (2, 0, PR_WITH, 0, TOOLBIT, 48, 248, V_UNLOCK),
]
_SYNTAX[ACT_UNTIE] = [
    (2, 0, PR_FROM, 0, 0, 240, 0, V_UNTIE),
    (1, 0, 0, 0, 0, 240, 0, V_UNTIE),
]
_SYNTAX[ACT_WAIT] = [
    (0, 0, 0, 0, 0, 0, 0, V_WAIT),
]
_SYNTAX[ACT_WAKE] = [
    (1, PR_UP, 0, ACTORBIT, 0, 48, 0, V_ALARM),
    (1, 0, 0, ACTORBIT, 0, 48, 0, V_ALARM),
]
_SYNTAX[ACT_WALK] = [
    (1, PR_DOWN, 0, CLIMBBIT, 0, 48, 0, V_CLIMB_DOWN),
    (1, PR_UP, 0, CLIMBBIT, 0, 48, 0, V_CLIMB_UP),
    (1, PR_AROUND, 0, 0, 0, 0, 0, V_WALK_AROUND),
    (1, PR_TO, 0, 0, 0, 0, 0, V_WALK_TO),
    (1, PR_OVER, 0, 0, 0, 0, 0, V_LEAP),
    (1, PR_ON, 0, 0, 0, 0, 0, V_THROUGH),
    (1, PR_WITH, 0, 0, 0, 0, 0, V_THROUGH),
    (1, PR_IN, 0, 0, 0, 0, 0, V_THROUGH),
    (1, PR_AWAY, 0, 0, 0, 0, 0, V_WALK),
    (1, 0, 0, 0, 0, 0, 0, V_WALK),
    (0, 0, 0, 0, 0, 0, 0, V_WALK_AROUND),
]
_SYNTAX[ACT_WAVE] = [
    (1, PR_AT, 0, 0, 0, 0, 0, V_WAVE),
    (2, 0, PR_AT, 0, 0, 202, 0, V_WAVE),
    (1, 0, 0, 0, 0, 202, 0, V_WAVE),
]
_SYNTAX[ACT_WEAR] = [
    (1, 0, 0, 0, 0, 0, 0, V_WEAR),
]
_SYNTAX[ACT_WIN] = [
    (0, 0, 0, 0, 0, 0, 0, V_WIN),
]
_SYNTAX[ACT_WIND] = [
    (1, PR_UP, 0, 0, 0, 0, 0, V_WIND),
    (1, 0, 0, 0, 0, 0, 0, V_WIND),
]
_SYNTAX[ACT_WISH] = [
    (0, 0, 0, 0, 0, 0, 0, V_WISH),
]
_SYNTAX[ACT_YELL] = [
    (0, 0, 0, 0, 0, 0, 0, V_YELL),
]
_SYNTAX[ACT_ZORK] = [
    (0, 0, 0, 0, 0, 0, 0, V_ZORK),
]
VERBS = z.verbs_table(_SYNTAX)
ACTIONS = z.action_table({
    V_VERBOSE: z.rtn(v_verbose),
    V_BRIEF: z.rtn(v_brief),
    V_SUPER_BRIEF: z.rtn(v_super_brief),
    V_DIAGNOSE: z.rtn(v_diagnose),
    V_INVENTORY: z.rtn(v_inventory),
    V_QUIT: z.rtn(v_quit),
    V_RESTART: z.rtn(v_restart),
    V_RESTORE: z.rtn(v_restore),
    V_SAVE: z.rtn(v_save),
    V_SCORE: z.rtn(v_score),
    V_SCRIPT: z.rtn(v_script),
    V_UNSCRIPT: z.rtn(v_unscript),
    V_VERSION: z.rtn(v_version),
    V_VERIFY: z.rtn(v_verify),
    V_RANDOM: z.rtn(v_random),
    V_COMMAND_FILE: z.rtn(v_command_file),
    V_RECORD: z.rtn(v_record),
    V_UNRECORD: z.rtn(v_unrecord),
    V_LAMP_ON: z.rtn(v_lamp_on),
    V_ANSWER: z.rtn(v_answer),
    V_REPLY: z.rtn(v_reply),
    V_PUT: z.rtn(v_put),
    V_ATTACK: z.rtn(v_attack),
    V_BACK: z.rtn(v_back),
    V_BLAST: z.rtn(v_blast),
    V_LAMP_OFF: z.rtn(v_lamp_off),
    V_INFLATE: z.rtn(v_inflate),
    V_BREATHE: z.rtn(v_breathe),
    V_BOARD: z.rtn(v_board),
    V_BRUSH: z.rtn(v_brush),
    V_BUG: z.rtn(v_bug),
    V_BURN: z.rtn(v_burn),
    V_CHOMP: z.rtn(v_chomp),
    V_CLIMB_UP: z.rtn(v_climb_up),
    V_CLIMB_DOWN: z.rtn(v_climb_down),
    V_CLIMB_FOO: z.rtn(v_climb_foo),
    V_CLIMB_ON: z.rtn(v_climb_on),
    V_THROUGH: z.rtn(v_through),
    V_CLOSE: z.rtn(v_close),
    V_COMMAND: z.rtn(v_command),
    V_COUNT: z.rtn(v_count),
    V_CROSS: z.rtn(v_cross),
    V_CUT: z.rtn(v_cut),
    V_CURSES: z.rtn(v_curses),
    V_DEFLATE: z.rtn(v_deflate),
    V_MUNG: z.rtn(v_mung),
    V_OPEN: z.rtn(v_open),
    V_DIG: z.rtn(v_dig),
    V_DISEMBARK: z.rtn(v_disembark),
    V_DISENCHANT: z.rtn(v_disenchant),
    V_DRINK: z.rtn(v_drink),
    V_DRINK_FROM: z.rtn(v_drink_from),
    V_DROP: z.rtn(v_drop),
    V_PUT_ON: z.rtn(v_put_on),
    V_EAT: z.rtn(v_eat),
    V_ECHO: z.rtn(v_echo),
    V_ENCHANT: z.rtn(v_enchant),
    V_ENTER: z.rtn(v_enter),
    V_EXIT: z.rtn(v_exit),
    V_EXAMINE: z.rtn(v_examine),
    V_LOOK_INSIDE: z.rtn(v_look_inside),
    V_EXORCISE: z.rtn(v_exorcise),
    V_FILL: z.rtn(v_fill),
    V_FIND: z.rtn(v_find),
    V_FOLLOW: z.rtn(v_follow),
    V_FROBOZZ: z.rtn(v_frobozz),
    V_GIVE: z.rtn(v_give),
    V_SGIVE: z.rtn(v_sgive),
    V_HATCH: z.rtn(v_hatch),
    V_HELLO: z.rtn(v_hello),
    V_INCANT: z.rtn(v_incant),
    V_LEAP: z.rtn(v_leap),
    V_KICK: z.rtn(v_kick),
    V_STAB: z.rtn(v_stab),
    V_KISS: z.rtn(v_kiss),
    V_KNOCK: z.rtn(v_knock),
    V_LAUNCH: z.rtn(v_launch),
    V_LEAN_ON: z.rtn(v_lean_on),
    V_LEAVE: z.rtn(v_leave),
    V_LISTEN: z.rtn(v_listen),
    V_LOCK: z.rtn(v_lock),
    V_LOOK: z.rtn(v_look),
    V_LOOK_ON: z.rtn(v_look_on),
    V_LOOK_UNDER: z.rtn(v_look_under),
    V_LOOK_BEHIND: z.rtn(v_look_behind),
    V_READ: z.rtn(v_read),
    V_LOWER: z.rtn(v_lower),
    V_OIL: z.rtn(v_oil),
    V_MAKE: z.rtn(v_make),
    V_MELT: z.rtn(v_melt),
    V_MOVE: z.rtn(v_move),
    V_PUSH_TO: z.rtn(v_push_to),
    V_TURN: z.rtn(v_turn),
    V_MUMBLE: z.rtn(v_mumble),
    V_ODYSSEUS: z.rtn(v_odysseus),
    V_PICK: z.rtn(v_pick),
    V_TAKE: z.rtn(v_take),
    V_PLAY: z.rtn(v_play),
    V_PLUG: z.rtn(v_plug),
    V_ADVENT: z.rtn(v_advent),
    V_POUR_ON: z.rtn(v_pour_on),
    V_PRAY: z.rtn(v_pray),
    V_PUMP: z.rtn(v_pump),
    V_PUSH: z.rtn(v_push),
    V_PUT_UNDER: z.rtn(v_put_under),
    V_WEAR: z.rtn(v_wear),
    V_PUT_BEHIND: z.rtn(v_put_behind),
    V_RAISE: z.rtn(v_raise),
    V_RAPE: z.rtn(v_rape),
    V_READ_PAGE: z.rtn(v_read_page),
    V_REPENT: z.rtn(v_repent),
    V_RING: z.rtn(v_ring),
    V_RUB: z.rtn(v_rub),
    V_TELL: z.rtn(v_tell),
    V_SAY: z.rtn(v_say),
    V_SEARCH: z.rtn(v_search),
    V_SEND: z.rtn(v_send),
    V_SHAKE: z.rtn(v_shake),
    V_SKIP: z.rtn(v_skip),
    V_SMELL: z.rtn(v_smell),
    V_SPIN: z.rtn(v_spin),
    V_SPRAY: z.rtn(v_spray),
    V_SSPRAY: z.rtn(v_sspray),
    V_SQUEEZE: z.rtn(v_squeeze),
    V_STAND: z.rtn(v_stand),
    V_STAY: z.rtn(v_stay),
    V_STRIKE: z.rtn(v_strike),
    V_SWIM: z.rtn(v_swim),
    V_SWING: z.rtn(v_swing),
    V_THROW: z.rtn(v_throw),
    V_OVERBOARD: z.rtn(v_overboard),
    V_THROW_OFF: z.rtn(v_throw_off),
    V_TIE: z.rtn(v_tie),
    V_TIE_UP: z.rtn(v_tie_up),
    V_TREASURE: z.rtn(v_treasure),
    V_UNLOCK: z.rtn(v_unlock),
    V_UNTIE: z.rtn(v_untie),
    V_WAIT: z.rtn(v_wait),
    V_ALARM: z.rtn(v_alarm),
    V_WALK_AROUND: z.rtn(v_walk_around),
    V_WALK: z.rtn(v_walk),
    V_WALK_TO: z.rtn(v_walk_to),
    V_WAVE: z.rtn(v_wave),
    V_WIN: z.rtn(v_win),
    V_WIND: z.rtn(v_wind),
    V_WISH: z.rtn(v_wish),
    V_YELL: z.rtn(v_yell),
    V_ZORK: z.rtn(v_zork),
}, size=149)
PREACTIONS = z.action_table({
    V_PUT: z.rtn(pre_put),
    V_BOARD: z.rtn(pre_board),
    V_BURN: z.rtn(pre_burn),
    V_MUNG: z.rtn(pre_mung),
    V_DROP: z.rtn(pre_drop),
    V_PUT_ON: z.rtn(pre_put),
    V_FILL: z.rtn(pre_fill),
    V_GIVE: z.rtn(pre_give),
    V_SGIVE: z.rtn(pre_sgive),
    V_READ: z.rtn(pre_read),
    V_MOVE: z.rtn(pre_move),
    V_TURN: z.rtn(pre_turn),
    V_TAKE: z.rtn(pre_take),
}, size=149)
PREPOSITIONS = z.prepositions_table([(_W['about'], PR_ABOUT), (_W['behind'], PR_BEHIND), (_W['under'], PR_UNDER), (_W['around'], PR_AROUND), (_W['for'], PR_FOR), (_W['at'], PR_AT), (_W['off'], PR_OFF), (_W['across'], PR_ACROSS), (_W['over'], PR_OVER), (_W['away'], PR_AWAY), (_W['from'], PR_FROM), (_W['on'], PR_ON), (_W['down'], PR_DOWN), (_W['in'], PR_IN), (_W['up'], PR_UP), (_W['out'], PR_OUT), (_W['with'], PR_WITH), (_W['to'], PR_TO)])

z.end_build()

"""
Data from "Lost Person Behavior" by Robert J. Koester. Copyright 2008.

All data is for temperate climates, and the distances are in kilometers.

If offset or dispersion angle are given for dry and not temperate, the dry values are used.
"""

from .enums import LPB, Terrain

DISTANCE = "distance"
ANGLE = "angle"
OFFSET = "offset"

data = {
    LPB.ANGLER: {
        DISTANCE: {
            Terrain.MOUNTAIN: [0.3, 1.5, 5.5, 9.9],
            Terrain.FLAT: [0.8, 1.6, 3.9, 14.9],
        },
        ANGLE: [28, 50, 59, 111],
    },
    LPB.ATV: {
        DISTANCE: {
            Terrain.MOUNTAIN: [1.6, 3.2, 5.6, 8.0],
        }
    },
    LPB.AUTISTIC: {
        DISTANCE: {
            Terrain.FLAT: [0.6, 1.6, 3.7, 15.2],
            Terrain.URBAN: [0.3, 1.0, 3.8, 8.0],
        },
        OFFSET: [9, 15, 22, 335],
    },
    LPB.CAMPER: {
        DISTANCE: {
            Terrain.MOUNTAIN: [0.2, 2.2, 3.0, 39.5],
            Terrain.FLAT: [0.2, 1.1, 3.2, 12.8],
        }
    },
    LPB.CHILD_1_3: {
        DISTANCE: {
            Terrain.MOUNTAIN: [0.2, 0.3, 0.6, 4.5],
            Terrain.FLAT: [0.2, 0.3, 1.0, 3.2],
            Terrain.URBAN: [0.2, 0.5, 0.8, 1.1],
        },
        ANGLE: [0, 23, 66, 137],
    },
    LPB.CHILD_4_6: {
        DISTANCE: {
            Terrain.MOUNTAIN: [0.2, 0.8, 1.5, 3.7],
            Terrain.FLAT: [0.2, 0.6, 1.5, 6.6],
            Terrain.URBAN: [0.1, 0.5, 1.0, 3.4],
        },
        ANGLE: [0, 23, 66, 137],
    },
    LPB.CHILD_7_9: {
        DISTANCE: {
            Terrain.MOUNTAIN: [0.8, 1.6, 3.2, 11.3],
            Terrain.FLAT: [0.2, 0.8, 2.0, 8.0],
            Terrain.URBAN: [0.2, 0.5, 1.5, 5.2],
        },
        ANGLE: [21, 40, 57, 146],
    },
    LPB.CHILD_10_12: {
        DISTANCE: {
            Terrain.MOUNTAIN: [0.8, 1.6, 3.2, 9.0],
            Terrain.FLAT: [0.4, 1.6, 4.8, 10.0],
            Terrain.URBAN: [0.3, 1.5, 2.9, 5.8],
        },
        ANGLE: [21, 40, 57, 146],
    },
    LPB.CHILD_13_15: {
        DISTANCE: {
            Terrain.MOUNTAIN: [0.8, 2.1, 4.8, 21.4],
            Terrain.FLAT: [0.6, 1.3, 3.2, 10.0],
        },
        ANGLE: [0, 6, 48, 139],
    },
    LPB.DEMENTIA: {
        DISTANCE: {
            Terrain.MOUNTAIN: [0.3, 0.8, 1.9, 8.3],
            Terrain.FLAT: [0.3, 1.0, 2.4, 12.8],
            Terrain.URBAN: [0.3, 1.1, 3.2, 12.6],
        },
        ANGLE: [11, 23, 66, 70],
        OFFSET: [4, 15, 71, 307],
    },
    LPB.DESPONDENT: {
        DISTANCE: {
            Terrain.MOUNTAIN: [0.3, 1.1, 3.2, 21.6],
            Terrain.FLAT: [0.3, 0.8, 2.3, 17.3],
            Terrain.URBAN: [0.1, 0.5, 1.5, 13.1],
        },
        ANGLE: [0, 0, 3, 30],
        OFFSET: [30, 50, 100, 275],
    },
    LPB.GATHERER: {
        DISTANCE: {
            Terrain.MOUNTAIN: [1.5, 3.2, 6.4, 12.9],
        },
    },
    LPB.HIKER: {
        DISTANCE: {
            Terrain.MOUNTAIN: [1.1, 3.1, 5.8, 18.3],
            Terrain.FLAT: [0.6, 1.8, 3.2, 9.9],
        },
        ANGLE: [20, 47, 124, 175],
        OFFSET: [50, 100, 238, 424],
    },
    LPB.HORSEBACK_RIDER: {
        DISTANCE: {
            Terrain.ALL: [0.3, 3.2, 8.1, 19.8],
        },
    },
    LPB.HUNTER: {
        DISTANCE: {
            Terrain.MOUNTAIN: [1.0, 2.1, 4.8, 17.2],
            Terrain.FLAT: [0.6, 1.6, 3.1, 13.7],
        },
        ANGLE: [12, 45, 90, 156],
        OFFSET: [20, 100, 200, 380],
    },
    LPB.MENTAL_ILLNESS: {
        DISTANCE: {
            Terrain.MOUNTAIN: [0.6, 2.3, 8.3, 14.6],
            Terrain.FLAT: [0.8, 1.0, 2.3, 8.1],
            Terrain.URBAN: [0.3, 0.6, 1.5, 12.5],
        },
    },
    LPB.MENTAL_RETARDATION: {
        DISTANCE: {
            Terrain.MOUNTAIN: [0.6, 1.6, 3.2, 11.3],
            Terrain.FLAT: [0.3, 1.0, 2.1, 11.8],
            Terrain.URBAN: [0.3, 0.8, 3.7, 9.9],
        },
        OFFSET: [11, 15, 49, 230],
    },
    LPB.MOUNTAIN_BIKER: {
        DISTANCE: {
            Terrain.MOUNTAIN: [3.1, 4.0, 11.3, 25.0],
        },
        ANGLE: [15, 37, 68, 115],
    },
    LPB.RUNNER: {
        DISTANCE: {
            Terrain.ALL: [0.9, 1.6, 2.1, 3.6],
        },
    },
    LPB.SKIER_ALPINE: {
        DISTANCE: {
            Terrain.MOUNTAIN: [0.7, 1.7, 3.0, 9.4],
        },
    },
    LPB.SKIER_NORDIC: {
        DISTANCE: {
            Terrain.MOUNTAIN: [1.6, 3.5, 6.4, 19.6],
        },
        ANGLE: [16, 48, 149, 165],
    },
    LPB.SNOWBOARDER: {
        DISTANCE: {
            Terrain.MOUNTAIN: [1.6, 3.22, 6.2, 15.4],
        },
    },
    LPB.SNOWMOBILER: {
        DISTANCE: {
            Terrain.MOUNTAIN: [3.2, 6.4, 11.1, 16.1],
            Terrain.FLAT: [1.3, 4.7, 41.1, 96.1],
        },
        ANGLE: [7, 11, 58, 169],
    },
    LPB.SUBSTANCE_ABUSE: {
        DISTANCE: {
            Terrain.ALL: [0.3, 0.7, 2.6, 6.0],
        },
    },
    LPB.VEHICLE: {
        DISTANCE: {
            Terrain.ALL: [2.0, 5.0, 12.6, 62.7],
        },
    },
}

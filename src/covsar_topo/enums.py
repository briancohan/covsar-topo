from enum import Enum


class Terrain(Enum):
    MOUNTAIN = "Mountain"
    FLAT = "Flat"
    URBAN = "Urban"
    ALL = "All"


class LPB(Enum):
    # ABDUCTION = "Abduction"
    # AIRCRAFT = "Aircraft"
    ANGLER = "Angler"
    ATV = "Atv"
    AUTISTIC = "Autistic"
    CAMPER = "Camper"
    # CAVER = "Caver"
    CHILD_1_3 = "Child 1-3"
    CHILD_4_6 = "Child 4-6"
    CHILD_7_9 = "Child 7-9"
    CHILD_10_12 = "Child 10-12"
    CHILD_13_15 = "Child 13-15"
    # CLIMBER = "Climber"
    DEMENTIA = "Dementia"
    DESPONDENT = "Despondent"
    GATHERER = "Gatherer"
    HIKER = "Hiker"
    HORSEBACK_RIDER = "Horseback Rider"
    HUNTER = "Hunter"
    MENTAL_ILLNESS = "Mental Illness"
    MENTAL_RETARDATION = "Mental Retardation"
    MOUNTAIN_BIKER = "Mountain Biker"
    # OTHER = "Other"
    RUNNER = "Runner"
    SKIER_ALPINE = "Skier Alpine"
    SKIER_NORDIC = "Skier Nordic"
    SNOWBOARDER = "Snowboarder"
    SNOWMOBILER = "Snowmobiler"
    # SNOWSHOER = "Snowshoer"
    SUBSTANCE_ABUSE = "Substance Abuse"
    # URBAN_ENTRAPMENT = "Urban Entrapment"
    VEHICLE = "Vehicle"
    # WATER_RELATED = "Water Related"
    # WORKER = "Worker"


class Line(Enum):
    # Basic
    SOLID = "solid"
    DASHED = "M0%20-3%20L0%203%2C%2C12%2CF"
    DASH_DOT = "M0%20-3%20L0%203%2C0%2C16%2CF%3BM0%20-1L0%200%2C8%2C16"
    DOTTED = "M0%20-1%20L0%201%2C%2C8%2CF"
    DOTTED_MD = (
        "M4%204M-4%20-4M2%200A2%202%200%201%200%20-2%200%20A2%202%200%201%200%202%200%2C%2C15%2CF"  # noqa:E501
    )
    DOTTED_LG = (
        "M5%205M-5%20-5M3%200A3%203%200%201%200%20-3%200%20A3%203%200%201%200%203%200%2C%2C15%2CF"  # noqa:E501
    )
    RAIL = "M-4%200L4%200%2C%2C8%2CT"
    X_LINE = "M-6%200M6%200M-5%20-5%20L5%205%20M5%20-5%20L-5%205%2C7%2C60%2CT"
    X_DENSE = "M-6%200M6%200M-5%20-5%20L5%205%20M5%20-5%20L-5%205%2C%2C10%2CF"
    X_SPACED = "M-6%200M6%200M-5%20-5%20L5%205%20M5%20-5%20L-5%205%2C%2C15%2CF"
    # Directional
    ARROW1 = "M-5%205L0%20-5M5%205L0%20-5%2C40%2C80%2CT"
    ARROW2 = "M-5%205L0%20-5M5%205L0%20-5%2C20%2C40%2CT"
    ARROW1_OPEN = "M-6%208L0%20-8M6%208L0%20-8M0%200L-6%208M0%200L6%208%2C40%2C80%2CT"
    ARROW2_OPEN = "M-6%208L0%20-8M6%208L0%20-8M0%200L-6%208M0%200L6%208%2C20%2C40%2CT"
    END_ARROW_SOLID = "M-5%208%20L0%20-2%20L5%208%20Z%2C100%25%2C%2CT"
    END_ARROW_OPEN = "M-6%2014L0%20-2M6%2014L0%20-2M0%206L-6%2014M0%206L6%2014%2C100%25%2C%2CT"
    # ICS/FIRE
    UNCONTROLLED_FIRE_EDGE = "M0%200L%206%200%2C%2C10%2CT"
    PLANNED_FIRELINE = "M0%20-3%20L0%203%2C%2C12%2CF"
    PLANNED_SECONDARY_LINE = (
        "M4%204M-4%20-4M2%200A2%202%200%201%200%20-2%200%20A2%202%200%201%200%202%200%2C%2C10%2CF"  # noqa:E501
    )
    FIRE_SPREAD_PREDICTION = "solid"
    ESCAPE_ROUTE = "M-4%20-4L-4%204L4%204L4%20-4Z%2C%2C25%2CT"
    AERIAL_HAZARD = "M-8%20-8M8%208M-7%200L7%200M-5%200L-4%202L-2%204L-1%204L0%206M5%200L4%202L2%204L1%204L0%206M-5%200L-4%20-2L-2%20-4L-1%20-4L0%20-6M5%200L4%20-2L2%20-4L1%20-4L0%20-6%2C%2C30%2CT"  # noqa:E501
    PROPOSED_BURNOUT = "M-6%200L6%200%2C%2C10%2CF"
    COMPLETED_BURNOUT = "M12%20-7M0%205M9%200A3%203%200%201%200%206%200%20A3%203%200%200%200%209%200%2C2%2C20%2CT%3BM0%200L12%200%2C15%2C20"  # noqa:E501
    PROPOSED_DOZER_LINE = "M4%204M-4%20-4M2%200A2%202%200%201%200%20-2%200%20A2%202%200%201%200%202%200%2C%2C15%2CF%3BM-6%200M6%200M-5%20-5%20L5%205%20M5%20-5%20L-5%205%2C7%2C45%2CF"  # noqa:E501
    COMPLETED_DOZER_LINE = "M-7%200M7%200M-6%200L-2%20-4M-6%200L-2%204M2%200L-2%20-4M2%200L-2%204M2%200L6%20-4M2%200L6%204%2C%2C8%2CF"  # noqa:E501
    COMPLETED_LINE_BREAK = "M-5%203L5%200M-5%20-3L5%200%2C%2C6%2CF"
    FIRE_BREAK_PLANNED = (
        "M5%206L-5%203M5%200L-5%203M5%200L-5%20-2M-5%20-5L-5%20-2M5%20-6L-5%20-6%2C%2C14%2CF"  # noqa:E501
    )
    FOAM_DROP = "M-8%20-6M8%206M-6%200L0%204L6%200L0%20-4Z%2C%2C10%2CF"
    RETARDANT_DROP = (
        "M6%206M-6%20-6M-5%200L0%205%20M5%200L0%205M-5%200L0%20-5M5%200L0%20-5%2C%2C12%2CF"  # noqa:E501
    )
    HELITANKER_FOAM = "M4%204M-4%20-4M2%200A2%202%200%201%200%20-2%200%20A2%202%200%201%200%202%200%2C%2C20%2CF%3BM-8%206L-4%201M4%206L-4%201M4%206L8%201%09M-8%20-1L-4%20-6M4%20-1L-4%20-6M4%20-1L8%20-6%2C10%2C40"  # noqa:E501
    HELITANKER_WATER = "M4%204M-4%20-4M2%200A2%202%200%201%200%20-2%200%20A2%202%200%201%200%202%200%2C%2C20%2CF%3BM0%205L7%207M-7%2013L7%207M-7%2013L0%2015%2C0%2C20"  # noqa:E501
    AERIAL_IGNITION = "M-12%20-12%20M12%2012%20M2%206A2%202%200%201%200%20-2%206%20A2%202%200%201%200%202%206%09%20M10%206A2%202%200%201%200%206%206%20A2%202%200%200%200%2010%206%09M-10%206A2%202%200%201%200%20-6%206%20A2%202%200%200%200%20-10%206%09M6%200A2%202%200%201%200%202%200%20A2%202%200%200%200%206%200%20M-6%200A2%202%200%201%200%20-2%200%20A2%202%200%200%200%20-6%200%09M2%20-6A2%202%200%201%200%20-2%20-6%20A2%202%200%201%200%202%20-6%2C%2C25%2CF"  # noqa:E501
    HIGHLIGHTED_GEOGRAPHIC_FEATURE = "M-6%205L-4%202M0%200L-4%202M0%200L4%202M6%205L4%202%20M-6%20-5L-4%20-2M0%200L-4%20-2M0%200L4%20-2M6%20-5L4%20-2%2C%2C16%2CF"  # noqa:E501
    HIGHLIGHTED_MANMADE_FEATURE = "M0%20-3%20L0%203%2C%2C12%2CF%3BM4%204M-4%20-4M2%200A2%202%200%201%200%20-2%200%20A2%202%200%201%200%202%200%2C5%2C36%2CF"  # noqa:E501


class MarkerColor(Enum):
    PLANNING = "#0000FF"
    SUBJECT = "#FF0000"
    RINGS = "#000000"

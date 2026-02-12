from dataclasses import dataclass

from Options import (
    Choice,
    OptionGroup,
    PerGameCommonOptions,
    Range,
    Toggle,
    Visibility,
    OptionCounter,
)


# Current "Sanity" options. Operating Under Assumption of Under Development.


class RoomDraftSanity(Toggle):
    """

    Currently a Development option:
    Room Draft Sanity puts every single room (sans a single one chosen at random) into the item pool.
    Rooms can not be drafted until they are received from the item pool.

    """

    display_name = "Dev: Room Draft Sanity"

    # Unknown Viability. Keeping false until deemed viable.
    default = False
    # Development Option. Disable visible until implemented.
    visibility = Visibility.none


class ItemSanity(Toggle):
    """
    Currently a Development option:
    ItemSanity enables the ability for items to be placed into the item pool.
    That is, the blue prince item in question can not be received in any way
    until the item is received from the server.

    IE This option would limit simon to only being able to find a sledgehammer once that ability
    is granted by the "Sledgehammers" item being found.
    """

    display_name = "Dev: Item Sanity"

    # Unknown Viability. Keeping false until deemed viable.
    default = False
    # Development Option. Disable visible until implemented.
    visibility = Visibility.none


# TODO-2 Crate Sanity?
# TODO-2 Document full list of potential checks/locations posted in blue prince thread.


class LockedTrunkCount(Range):
    """
    This is the number of locked trunks per room that need to be opened for archipelago items.
    """

    display_name = "Locked Trunks"

    range_start = 0
    range_end = 100

    default = 2


# Filler Options.
class FillerItemDistribution(OptionCounter):
    """
    This option allows the user to set the weight chance of any particular item to show up as a filler item.
    """

    rich_text_doc = True

    min = 0
    max = 100

    default = {
        "extra_allowance": 50,
        "extra_allowance_1": 0,
        "extra_allowance_2": 0,
        "extra_gold": 50,
        "extra_gold_1": 0,
        "extra_gold_2": 0,
        "extra_gold_5": 0,
        "extra_dice": 50,
        "extra_dice_1": 0,
        "extra_dice_2": 0,
        "extra_dice_4": 0,
        "extra_fruit": 50,
        "extra_fruit_apple": 0,
        "extra_fruit_banana": 0,
        "extra_fruit_orange": 0,
        "extra_gems": 50,
        "extra_gems_1": 0,
        "extra_gems_2": 0,
        "extra_keys": 50,
        "extra_keys_1": 0,
        "extra_keys_2": 0,
        "extra_keys_3": 0,
        "extra_stars": 50,
        "extra_stars_1": 0,
        "extra_stars_2": 0,
        "extra_stars_5": 0,
        "extra_starting_dice": 0,
        "extra_starting_dice_1": 0,
        "extra_starting_dice_2": 0,
        "extra_starting_gems": 0,
        "extra_starting_gems_1": 0,
        "extra_starting_gems_2": 0,
        "extra_starting_key": 0,
        "extra_starting_key_1": 0,
        "extra_starting_key_2": 0,
        "extra_starting_luck": 0,
        "extra_starting_luck_1": 0,
        "extra_starting_luck_2": 0,
        "extra_starting_steps": 0,
        "extra_starting_steps_5": 0,
        "extra_starting_steps_10": 0,
        "extra_steps": 50,
        "extra_steps_1": 0,
        "extra_steps_2": 0,
        "extra_steps_5": 0,
        "nothing": 50,
    }

    valid_keys = default.keys()


class TrapTypeDistribution(OptionCounter):
    """
    This allows the user to set the weight chance of any particular trap to show up.

    Possible traps are

    - **Freeze Trap**: Freeze items as if the player entered a freezer.
    - **Lose Steps Trap**: Lose between one and five steps.
    - **Lose Item Trap**: Loose an item as if the player entered the lost and found.
    - **Lose Stars Trap**: Lose one or more stars
    - **End Day Trap**: End the day immediately.

    Setting the trap with a number will remove that many specifically.
    Setting the option without a number following will pick the count based on default weights.
    """

    rich_text_doc = True

    min = 0
    max = 100

    # TODO-1 traps for consideration
    # Tax trap: Loose 10% of your gold.
    # Pickpocket trap: Loose some number of resources
    # Toll trap: Loose 1 gold per room you walk through (everywhere is chapel)

    default = {
        "freeze_traps": 50,
        "step_traps": 50,
        "step_traps_1": 0,
        "step_traps_2": 0,
        "step_traps_5": 0,
        "step_traps_set_to_1": 50,
        "step_traps_set_to_10": 50,
        "item_traps": 50,
        "star_traps": 50,
        "star_traps_1": 0,
        "star_traps_2": 0,
        "star_traps_5": 0,
        "eod_traps": 50,
    }

    valid_keys = default.keys()


class TrapPercentage(Range):
    """
    This is the percentage that a given fill item will be a trap instead of an item.
    """

    display_name = "Trap Percentage"

    range_start = 0
    range_end = 100
    default = 0


# Death Link Options
class DeathLinkType(Choice):
    """

    Sets the circumstances under which a death-link is sent out.

    - **none:** Death Link is disabled.
    - **eod:** A Death Link is sent whenever the day ends.
    - **bedroom:** A Death Link is sent whenever the player ends outside a bedroom.
    - **steps:** A Death Link is sent whenever the player runs out of steps.

    """

    display_name = "Death Link Type"
    rich_text_doc = True
    option_none = 0
    option_eod = 1
    option_bedroom = 2
    option_steps = 3

    default = 0


class DeathLinkGrace(Range):
    """
    Death Link Grace is the number of times that the player may trigger the death link circumstance
    before the death link will actually be sent.

    - When 0, a death link will be triggered upon every matching circumstance.

    - When 1, the death link will be deferred once before being triggered.
    AKA death link will trigger every other time.
    """

    display_name = "Death Link grace"
    rich_text_doc = True

    range_start = 0
    range_end = 100
    default = 0


class DeathLinkMonkException(Toggle):
    """
    Death Link will be ignored if the "Blessing Of The Monk" is currently active.
    """

    display_name = "Death Link Monk Exception"
    rich_text_doc = True

    default = True


# Goal Options
class GoalType(Choice):
    """

    This selection determines what goal the player needs to aim for.

    - **antechamber:** Reach the antechamber once
    - **room46:** Reach room 46 once
    - **sanctum:** Open a select number of sanctum keys
    - **ascend:** Ascend the throne
    - **blueprints:** Find the Blue Prints

    """

    display_name = "Goal"

    rich_text_doc = True
    option_antechamber = 0
    option_room46 = 1
    option_sanctum = 2
    option_ascend = 3
    option_blueprints = 4

    default = 0


class GoalSanctumSolves(Range):
    """
    GoalSanctumSolves is the number of sanctum keys to find, and sanctum doors to open for the goal to be achieved.
    """

    display_name = "Goal: Sanctums Solved"

    range_start = 1
    range_end = 8
    default = 8


# We must now define a dataclass inheriting from PerGameCommonOptions that we put all our options in.
# This is in the format "option_name_in_snake_case: OptionClassName".
@dataclass
class BluePrinceOptions(PerGameCommonOptions):

    # Development Options
    room_draft_sanity: RoomDraftSanity
    item_sanity: ItemSanity
    locked_trunks: LockedTrunkCount
    # upgrade_disk_sanity: UpgradeDiskSanity

    # Extra item options.
    filler_item_distribution: FillerItemDistribution
    trap_type_distribution: TrapTypeDistribution
    trap_percentage: TrapPercentage

    # DeathLink Options
    death_link_type: DeathLinkType
    death_link_grace: DeathLinkGrace
    death_link_monk_exception: DeathLinkMonkException

    # Goal Options
    goal_type: GoalType
    goal_sanctum_solves: GoalSanctumSolves


# If we want to group our options by similar type, we can do so as well. This looks nice on the website.
option_groups = [
    OptionGroup(
        "Sanity Options",
        [
            RoomDraftSanity,
            ItemSanity,
            LockedTrunkCount,
            # UpgradeDiskSanity
        ],
    ),
    OptionGroup(
        "Filler Options",
        [FillerItemDistribution, TrapTypeDistribution, TrapPercentage],
    ),
    OptionGroup(
        "Death Link Options",
        [DeathLinkType, DeathLinkGrace, DeathLinkMonkException],
    ),
    OptionGroup(
        "Goal Options",
        [GoalType, GoalSanctumSolves],
    ),
]


# Finally, we can define some option presets if we want the player to be able to quickly choose a specific "mode".
option_presets = {
    # Room 46 Extra Drafting is to be a "vanilla" play through to reach room 46,
    # with no death link, with the goal set to room 64, and with no extra items or traps added to the pool.
    "Room 46 Extra Drafting": {
        "room_draft_sanity": True,
        "item_sanity": True,
        "locked_trunks": 2,
        # "upgrade_disk_sanity": True,
        "filler_item_distribution": {"nothing": 100},
        "trap_type_distribution": {},
        "trap_percentage": TrapPercentage.range_start,
        "death_link_type": DeathLinkType.option_none,
        "death_link_grace": DeathLinkGrace.range_start,
        "death_link_monk_exception": True,
        "goal_type": GoalType.option_room46,
        "goal_sanctum_solves": GoalSanctumSolves.range_end,
    },
}

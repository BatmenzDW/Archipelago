# Limitations

This is the list of limitations beeing assumed while writing the initial generator apworld

- Sanctum keys each open SPECIFIC sanctum doors.
- Upgrade Disks are NOT unique, but their locations ARE.
- The game client mod has the ability to completely modify what rooms can be drafted under any circumstances.
- The game client mod can restrict/enable items showing up in rooms/other places.
- The game client mod can add/remove items to inventories.
  - Specific assumption: an Upgrade disks will be in inventory until the number recieved are upgraded.
- Restrict or add to ability to create items in workshop.

- Due to blue prince drafting limitations, it is theoretically possible to only unlock one room, (ie south lever) and the generator assume you can use that to get to the antechamber. This is a known issue and so antechamber rules will assume 1: a lever, 2: 12 rooms unlocked. Foundation (and associated elevator access) subtracts 4 from room count. South lever subtracts 1. This is a statistical approach that needs testing/tuning.
- Similarly, other rooms assume minimum room count, or foundation. Most of these have specific placement restrictions, such as HLC and garage requiring being on an edge.

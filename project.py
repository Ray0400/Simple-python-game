class Location:
    def __init__(self, name, description, items, paths, locked=False):
        self.name = name
        self.description = description
        self.items = items
        self.paths = paths
        self.locked = locked

    def __str__(self):
        return self.name


class Item:
    def __init__(self, name, description):
        self.name = name
        self.description = description

    def __str__(self):
        return self.name


def main():
    # Initialize game locations
    forest = Location(
        "Forest", "A dense forest with tall trees and a narrow path.", [], {"north": "cave", "east": "river"})
    cave = Location("Cave", "A dark and damp cave with a mysterious glow.", [Item(
        "key", "A rusty old key.")], {"south": "forest", "east": "river"})

    river = Location("River", "A fast-flowing river with dangerous rapids.", [Item(
        "boat", "A sturdy boat.")], {"west": "cave", "south": "waterfall"})
    waterfall = Location(
        "Waterfall", "A magnificent waterfall cascading down from a great height.", [], {"north": "river", "east": "hidden_cave"})
    hidden_cave = Location("Hidden Cave", "A secret cave hidden behind the waterfall.", [
        Item("map", "A map showing the location of the next level.")], {"west": "waterfall", "north": "library"})
    library = Location("Library", "A grand library filled with ancient tomes.", [Item(
        "book", "A book containing the knowledge required to progress further.")], {"east": "dungeon"})
    dungeon = Location(
        "Dungeon", "A dark and dangerous dungeon filled with traps and monsters.", [], {"west": "library", "north": "final_battle"})
    final_battle = Location(
        "Final Battle", "The final showdown against the boss.", [], {"south": "dungeon", "west": "treasure_room", "east": "forest"})
    treasure_room = Location("Treasure Room", "A hidden room filled with unimaginable treasures.", [
                             Item("artifact", "The mysterious artifact you've been searching for."), Item("sword", "A sharp sword.")], {"east": "forest"})
    treasure_room.locked = True

    # Map location names to objects
    locations = {
        "forest": forest,
        "cave": cave,
        "treasure_room": treasure_room,
        "river": river,
        "waterfall": waterfall,
        "hidden_cave": hidden_cave,
        "library": library,
        "dungeon": dungeon,
        "final_battle": final_battle,
    }

    # Set starting location
    current_location = forest
    inventory = []

    print("Welcome to The Quest for the Mysterious Artifact!\n")
    print("Type 'help' for a list of commands.")
    while True:
        print(f"\nYou are in the {current_location}.")
        print(current_location.description)

        command = input("\nWhere do you want to do? ").lower().split()

        if len(command) == 0:
            continue

        if command[0] == "help":
            print(
                "Commands: go [north, south, east, west], look, take [item name], inventory, forfeit")

        elif command[0] == "go":
            if len(command) > 1:
                direction = command[1]
                if direction in current_location.paths:
                    next_location = locations[current_location.paths[direction]]
                    if next_location.locked:
                        if "key" in [item.name for item in inventory]:
                            next_location.locked = False
                            print("You unlock the door and enter the room.")
                            current_location = next_location
                        else:
                            print("The door is locked.")
                    else:
                        current_location = next_location
                else:
                    print("You can't go that way.")
            else:
                print("Please specify a direction.")

        elif command[0] == "look":
            if current_location.items:
                print("You see the following items:")
                for item in current_location.items:
                    print(f"- {item}")
            else:
                print("There are no items here.")

        elif command[0] == "take":
            if len(command) > 1:
                item_name = command[1]
                item_found = False
                for item in current_location.items:
                    if item.name == item_name:
                        inventory.append(item)
                        current_location.items.remove(item)
                        print(f"You picked up the {item}.")
                        item_found = True
                        if item.name == "key" and current_location == cave:
                            print(
                                "Congratulations! You now have the key to the treasure room")
                            treasure_room.locked = False
                        break
                if not item_found:
                    for item in inventory:
                        if item.name == item_name:
                            print("You already have that item.")
                            item_found = True
                            break
                if not item_found:
                    print("That item is not here.")
            else:
                print("Please specify an item to take.")

        elif command[0] == "inventory":
            if inventory:
                print("You have the following items:")
                for item in inventory:
                    print(f"- {item}")
            else:
                print("Your inventory is empty.")

        elif command[0] == "forfeit":
            print("Thanks for playing! Goodbye.")
            break

        else:
            print("Invalid command. Type 'help' for a list of commands.")
    
    


if __name__ == "__main__":
    main()

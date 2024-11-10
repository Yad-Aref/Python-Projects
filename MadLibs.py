def mad_libs():
    print("Welcome to the Mad Libs game! Please provide words for the following prompts:")

    # Asking the user for inputs
    noun1 = input("Enter a noun: ")
    verb1 = input("Enter a verb (present tense): ")
    adjective1 = input("Enter an adjective: ")
    place = input("Enter a place: ")
    animal = input("Enter an animal: ")
    food = input("Enter a type of food: ")

    # Story template with placeholders for user inputs
    story = f"""
    Once upon a time, in a faraway land, there was a {adjective1} {animal} who lived in {place}.
    Every day, the {animal} would {verb1} around, looking for its favorite food, {food}.
    One day, the {animal} met a magical {noun1} that changed its life forever.
    Together, they went on an adventure that no one will ever forget!
    """

    # Displaying the completed story
    print("\nHere is your Mad Libs story:")
    print(story)

# Run the Mad Libs generator
mad_libs()

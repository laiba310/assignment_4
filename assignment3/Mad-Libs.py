

name = input("Enter a name: ")
place = input("Enter a place: ")
adjective = input("Enter an adjective: ")
noun = input("Enter a noun: ")
verb = input("Enter a verb (past tense): ")

story = f"""
Once upon a time, there was a person named {name}.
They lived in {place}, a very {adjective} town.
One day, they found a mysterious {noun}.
They picked it up and {verb} away happily.
"""

print("\nHere is your Mad Libs story:")
print(story)

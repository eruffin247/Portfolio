# This is a program that simulates rolling a die.
# The user can specify how many sides the die has and how many times to roll it.
import random
def roll_die(sides, rolls):
    results = []
    for _ in range(rolls):
        result = random.randint(1, sides)
        results.append(result)
    return results
def main():
    sides = int(input("Enter the number of sides on the die: "))
    rolls = int(input("Enter the number of times to roll the die: "))
    results = roll_die(sides, rolls)
    print(f"Results of rolling a {sides}-sided die {rolls} times: {results}")
if __name__ == "__main__":
    main()
    
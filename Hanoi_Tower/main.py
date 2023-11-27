from stack import Stack

# Introduction to the Towers of Hanoi game
print("\nLet's play Towers of Hanoi!!")

# Create the Stacks
stacks = []
left_stack = Stack("Left")
middle_stack = Stack("Middle")
right_stack = Stack("Right")
stacks.extend([left_stack, middle_stack, right_stack])

# Set up the Game
num_disks = int(input("How many disks do you want to play with?\n"))

# Ensure at least 3 disks to play
while num_disks < 3:
    num_disks = int(input("Enter a number greater than or equal to 3\n"))

# Add disks to the left stack in descending order
for i in range(num_disks, 0, -1):
    left_stack.push(i)

# Calculate the optimal number of moves to solve the game
num_optimal_moves = 2**num_disks - 1
print(f"\nThe fastest you can solve this game is in {num_optimal_moves} moves")

# Function to get user input for choosing stacks
def get_input():
    choices = [stack.get_name()[0] for stack in stacks]
    while True:
        for i in range(len(stacks)):
            name = stacks[i].get_name()
            letter = choices[i]
            print(f"Enter {letter} for {name}\n")

        user_input = input("")
        if user_input in choices:
            for i in range(len(stacks)):
                if user_input == choices[i]:
                    return stacks[i]

# Play the Game
num_user_moves = 0

while right_stack.get_size() != num_disks:

    # Display the current state of the stacks
    print("\n\n\n...Current Stacks...")
    for stack in stacks:
        stack.print_items()

    while True:
        print("\nWhich stack do you want to move from?\n")
        from_stack = get_input()
        print("\nWhich stack do you want to move to?\n")
        to_stack = get_input()

        # Validate the move and perform it if valid
        if from_stack.is_empty():
            print("\n\nInvalid Move. Try Again!")
        elif to_stack.is_empty() or from_stack.peek() < to_stack.peek():
            disk = from_stack.pop()
            to_stack.push(disk)
            num_user_moves += 1
            break
        else:
            print("\n\nInvalid Move. Try Again!")

# Display the result after the game ends
print(f"\n\nYou completed the game in {num_user_moves} and the optimal number of moves is {num_optimal_moves}")

# Import the contextlib module for context managers
from contextlib import contextmanager

# Define a context manager for generating generic cards
@contextmanager
def generic(card_type, sender, recipient):
    # Open the card template file in read mode (`'r'`)
    card_file = open(card_type, 'r')

    # Open a new file for the generated card with write mode (`'w'`)
    # Use f-strings to dynamically create the filename
    order = open(f"{sender}_generic.txt", "w")

    try:
        # Read the entire content of the card template file
        card_content = card_file.read()

        # Create the message using f-strings, inserting recipient name,
        # content, and sender name
        msg = f"Dear {recipient},\n{card_content}\nSincerely, {sender}"

        # Write the message to the generated card file
        order.write(msg)

        # Yield the open file object to be used within the `with` block
        yield order

    finally:
        # Ensure proper resource management by closing both files
        # even if an exception occurs
        card_file.close()
        order.close()


# Example usage of the `generic` context manager
with generic('thankyou_card.txt', 'Mwenda', 'Amanda') as f:
    # Code within the `with` block has access to the open file object `f`
    print("Card Generated!")


# Define a class for creating personalized cards
class personalized:
    def __init__(self, sender, recipient):
        # Store sender and recipient names in object attributes
        self.sender = sender
        self.recipient = recipient

        # Open a new file for the personalized card with write mode (`'w'`)
        # Use f-strings to dynamically create the filename
        self.opened_file = open(f'{sender}_personalized.txt', 'w')

    def __enter__(self):
        # Write the first part of the message (greeting) to the file
        self.opened_file.write(f"Dear {self.recipient},\n")

        # Return the open file object to be used within the `with` block
        return self.opened_file

    def __exit__(self, *exc):
        # Write the closing part of the message (signature) to the file,
        # including sender name
        self.opened_file.write(f"\nSincerely, {self.sender}")

        # Close the file
        self.opened_file.close()


# Example usage of the `personalized` class
with personalized('John', 'Michael') as p:
    # Code within the `with` block has access to the open file object `p`
    p.write(f"I am so proud of you! Being your friend for all these years has been nothing but a blessing. I don't say it often but I just wanted to let you know that you inspire me and I love you! All the best. Always.")
    print("Successfully created!")


# Another example using the `generic` context manager
with generic('happy_bday.txt', 'Josiah', 'Remy') as g:
    # Read the entire content of the generated card file (previously written)
    card_content = g.read()
    print(card_content)

# Commented-out example: replace with your personalized message
# with personalized('Josiah', 'Esther') as p:
#     p.write(f"Happy Birthday!! I love you to the moon and back. Even though you're a pain sometimes, you're a pain I can't live without. I am incredibly proud of you and grateful to have you as a sister. Cheers to 25!! You're getting old!")
#     print("Successfully!!!!!!!")


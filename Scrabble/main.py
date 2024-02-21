# This list contains all the letters in the alphabet (uppercase)
letters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]

# This list assigns point values to each letter (same order as "letters")
points = [1, 3, 3, 2, 1, 4, 2, 4, 1, 8, 5, 1, 3, 4, 1, 3, 10, 1, 1, 1, 1, 4, 4, 8, 4, 10]

# This dictionary maps lowercase letters to their point values (created efficiently using a list comprehension)
letter_to_points = {letter.lower(): point for letter, point in zip(letters, points)}

# Special case: assign 0 points to blank spaces
letter_to_points[" "] = 0


# This function calculates the score of a word based on its letters and their point values
def score_word(word):
    """
    This function takes a word and adds up the points of each letter based on the "letter_to_points" dictionary.
    It converts all letters to lowercase first for case-insensitivity.
    """
    score = 0
    for letter in word.lower():  # Convert word to lowercase for consistent scoring
        score += letter_to_points[letter]
    return score


# This function adds a played word to a player's list and updates their score
def play_word(player, word):
    """
    This function checks if a player exists, adds a played word (in uppercase) to their list,
    and then calls "update_point_totals" to recalculate their score based on all their words.
    """
    if player not in player_to_words:  # Check if player already has a list of words
        player_to_words[player] = []  # Create a new list if not
    player_to_words[player].append(word.upper())  # Add the word to the player's list (uppercase)
    update_point_totals()  # Recalculate scores after adding the word


# This function updates the score for each player based on their played words
def update_point_totals():
    """
    This function iterates through each player and their played words,
    calculates their total score using "score_word", and then stores it in a dictionary.
    Finally, it prints the updated scores for all players.
    """
    player_to_points = {}  # Start with an empty dictionary to store updated scores
    for player, words in player_to_words.items():  # Loop through each player and their words
        player_points = 0  # Initialize player's score to 0
        for word in words:  # Loop through each word played by the player
            player_points += score_word(word)  # Add the word's score to player's total
        player_to_points[player] = player_points  # Store the updated score in the dictionary
    print(player_to_points)  # Print the final dictionary with all player scores


# Sample data: dictionary mapping players to their played words
player_to_words = {"player1": ["BLUE", "TENNIS", "EXIT"], "wordNerd": ["EARTH", "EYES", "MACHINE"],
                  "Lexi Con": ["ERASER", "BELLY", "HUSKY"], "Prof Reader": ["ZAP", "COMA", "PERIOD"]}

# Start by printing initial scores
update_point_totals()

# Add new words and print updated scores
play_word("player1", "score")
play_word("wordNerd", "books")
update_point_totals()

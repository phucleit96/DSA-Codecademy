# Define a base class 'School' to represent general educational institutions.
class School:
    # Initialize the school object with its name, level (e.g., 'primary', 'high'), and number of students.
    def __init__(self, name, level, numberOfStudents):
        self.name = name
        self.level = level
        self.numberOfStudents = numberOfStudents

    # Getter methods to access the name, level, and number of students.
    def get_name(self):
        return self.name

    def get_level(self):
        return self.level

    def get_numberOfStudents(self):
        return self.numberOfStudents

    # Setter method to update the number of students.
    def set_numberOfStudents(self, new_number):
        self.numberOfStudents = new_number

    # Define a string representation for the school object showing its level, name, and student count.
    def __repr__(self):
        return f"A {self.level} school named {self.name} with {self.numberOfStudents} students"

# Define a subclass 'PrimarySchool' inheriting from 'School' and adding a pickup policy attribute.
class PrimarySchool(School):
    # Initialize the primary school object with its name, number of students, and pickup policy.
    def __init__(self, name, numberOfStudents, pickupPolicy):
        # Call the parent constructor (School.__init__) with a default level of 'primary'.
        super().__init__(name, 'primary', numberOfStudents)
        self.pickupPolicy = pickupPolicy

    # Getter method to access the pickup policy.
    def get_pickupPolicy(self):
        return self.pickupPolicy

    # Override the string representation to include the pickup policy in addition to the parent representation.
    def __repr__(self):
        parent_repr = super().__repr__()  # Get the parent class representation
        child_repr = f" has the pickup policy of {self.pickupPolicy}."  # Add pickup policy information
        return parent_repr + child_repr

# Define another subclass 'HighSchool' also inheriting from 'School' and adding a sports teams attribute.
class HighSchool(School):
    # Initialize the high school object with its name, number of students, and a list of sports teams.
    def __init__(self, name, numberOfStudents, sportsTeams):
        # Call the parent constructor (School.__init__) with a default level of 'high'.
        super().__init__(name, 'high', numberOfStudents)
        self.sportsTeams = sportsTeams

    # Getter method to access the sports teams list.
    def get_sportsTeams(self):
        return self.sportsTeams

    # Override the string representation to include the sports teams in a comma-separated list.
    def __repr__(self):
        parent_repr = super().__repr__()  # Get the parent class representation
        team_string = ""
        for i, team in enumerate(self.sportsTeams):
            # Add a comma and space for all teams except the last one.
            if i == len(self.sportsTeams) - 1:
                team_string += f"{team}"
            else:
                team_string += f"{team}, "
        child_repr = f" has sportsteams such as: {team_string}."  # Add sports team information
        return parent_repr + child_repr

# Create a HighSchool object and print its string representation.
hanoi_amsterdam = HighSchool("Hanoi Amsterdam", 3000, ["Soccer", "Game", "Basketball", "Volleyball"])
print(hanoi_amsterdam)

# Create a PrimarySchool object, print its string representation, and then call its get_pickupPolicy() method.
cva = PrimarySchool("Chu Van An", 4000, "pick up after 5pm")
print(cva)
print(cva.get_pickupPolicy())

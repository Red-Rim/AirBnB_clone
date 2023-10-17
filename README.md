________________AirBnB Clone - The Console________________________


Description

AirBnB Clone - The Console is a command-line interface (CLI) program that emulates the basic functionalities of the popular Airbnb vacation rental platform. It allows users to interact with and manage property listings, user accounts, and bookings through text-based commands. This project is intended for educational purposes and provides a simplified version of Airbnb's core features.

Command Interpreter

The command interpreter in AirBnB Clone - The Console is a lightweight, text-based interface designed to interact with and manage property listings, users, and bookings within the system. It provides a convenient way to create, read, update, and delete objects such as users, properties, and bookings.

How to Start

To start using the AirBnB Clone - The Console, follow these steps:
Prerequisites: Ensure you have a working Python environment installed on your system. The console is developed in Python and requires a compatible Python installation.
Installation: Clone the project repository to your local machine. You can use the following command to do so:
git clone https://github.com/your-username/AirBnB_clone.git
Navigate to Project Directory: Change your working directory to the location where you cloned the project:
cd AirBnB_clone
Launch the CLI: Start the console by running the following command:
./console.py

How to Use

Using the AirBnB Clone - The Console is straightforward. Once you have launched the CLI, you can interact with the system by entering commands. Here are some general instructions for usage:
Interactive Mode: After starting the console, you'll be in interactive mode. You can type commands and press Enter to execute them.

Non-Interactive Mode: You can also run the console in non-interactive mode by providing a command as an argument. For example:
echo "help" | ./console.py

Available Commands: The console supports a variety of commands for managing users, properties, and bookings. Some common commands include:
create: Create a new object (e.g., user, property, booking).
show: Display information about a specific object.
update: Update attributes of an object.
destroy: Remove an object from the system.
all: List all objects of a specific class.
help: Get information on available commands.
quit or EOF (Ctrl+D): Exit the console.


Command Syntax: Command syntax typically follows the pattern:
(command) (class) (ID) (attributes)

For example:

create User to create a new user.
show Place 1234 to display information about a property with ID 1234.




Examples

Here are some examples of how to use the AirBnB Clone - The Console:

Create a new user:
create User email="user@example.com" password="12345" first_name="John" last_name="Doe"

Display information about a property:
show Place 1234

Update a user's attributes:
update User 5678 email="new_email@example.com"

List all objects of a specific class:
all User

Remove an object from the system:
destroy User 5678


Get a list of available commands:
help
These are just a few examples of how to use the AirBnB Clone - The Console. For more detailed information about the available commands and their usage, consult the project's documentation or use the help command within the console.

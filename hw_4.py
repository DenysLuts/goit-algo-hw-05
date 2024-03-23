def input_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except (KeyError, ValueError, IndexError) as e:
            if isinstance(e, KeyError):
                return "Contact not found."
            elif isinstance(e, ValueError):
                return "Enter the argument for the command"
            elif isinstance(e, IndexError):
                return "Invalid command. Usage: change [name] [phone]"
    return inner

def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, args

@input_error
def add_contact(args, contacts):
    if len(args) != 2:
        raise ValueError
    name, phone = args
    contacts[name] = phone
    return "Contact added."

@input_error
def change_contact(args, contacts):
    if len(args) != 2:
        raise IndexError
    name, phone = args
    if name in contacts:
        contacts[name] = phone
        return "Contact updated successfully"
    else:
        raise KeyError

@input_error
def show_contact(args, contacts):
    if len(args) != 1:
        raise ValueError
    name = args[0]
    return contacts[name]

@input_error
def show_all(contacts):
    if not contacts:
        return "No contacts found."
    else:
        return "\n".join([f"{name}: {phone}" for name, phone in contacts.items()])

def main():
    contacts = {}
    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command: ")
        command, args = parse_input(user_input)

        if command in ["close", "exit"]:
            print("Good bye!")
            break

        elif command == "hello":
            print("How can I help you?")

        elif command == "add":
            print(add_contact(args, contacts))

        elif command == "change":
            print(change_contact(args, contacts))

        elif command == "phone":
            print(show_contact(args, contacts))

        elif command == "all":
            print(show_all(contacts))

        else:
            print("Invalid command.")

if __name__ == "__main__":
    main()
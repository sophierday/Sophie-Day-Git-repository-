import argparse, os, re, sys

parser = argparse.ArgumentParser()

# Create a new user:
parser.add_argument('--create')

parser.add_argument('--age', type=int)
parser.add_argument('--gender')
parser.add_argument('--height', type=int)
parser.add_argument('--weight', type=float)

# Show user:
parser.add_argument('--show')

# Update a new user:
parser.add_argument('--update')

parser.add_argument('--mood')
parser.add_argument('--time')
parser.add_argument('--water', type=float)

args = parser.parse_args()

# Create a user.
if args.create:
    username = args.create
    if not args.age:
        sys.exit(f"Please specify the age of {username}.")
    if not args.age:
        sys.exit(f"Please specify the gender of {username}.")
    if not args.height:
        sys.exit(f"Please specify the height of {username} in cm.")
    if not args.weight:
        sys.exit(f"Please specify the weight of {username} in kg.")

    print(f"Creating user {username}...")
    filename = f"{username}.txt"
    if os.path.exists(filename):
        sys.exit(f"User {username} already exists! Delete {filename} manually first.")
    with open(filename, 'a') as f:
        f.write(f"Name:{username}\n")
        f.write(f"Age:{args.age}\n")
        f.write(f"Gender:{args.gender}\n")
        f.write(f"Height:{args.height}\n")
        f.write(f"Weight:{args.weight}\n")
    print(f"User {username} created!")
    sys.exit(0)

# Show a user.
if args.show:
    username = args.show
    filename = f"{username}.txt"
    if not os.path.exists(filename):
        sys.exit(f"User {username} does not exist! Create it first.")
    with open(filename, 'r') as f:
        print(f"User {username}")
        print(f.read())
    sys.exit(0)

# Update a user.
if args.update:
    username = args.update
    time_err_msg = "Please specify a time using the following format:\nddmmyy_HH (24h format). For example:\n"
    time_err_msg += "100123_23"
    if not args.time:
        sys.exit(time_err_msg)
    else:
        # Verify the format.
        time_check = re.search("^[0-9]{6}_[0-23]{2}$", args.time)
        if not time_check:
            sys.exit(time_err_msg)
    if args.water is None:
        sys.exit("Please specify the water in litres.")
    if not args.mood:
        sys.exit("Please specify the mood.")
    filename = f"{username}.txt"
    if not os.path.exists(filename):
        sys.exit(f"User {username} does not exist! Create it first.")
    with open(filename, 'a') as f:
        f.write("\n")
        f.write("=====\n")
        f.write(f"Time:{args.time}\n")
        f.write(f"Water:{args.water}\n")
        f.write(f"Mood:{args.mood}\n")
    print(f"User {username} updated!")
    sys.exit(0)

import argparse

# Create the parser
parser = argparse.ArgumentParser(description="A simple argument parser example")

# Add arguments
parser.add_argument('--name', type=str, help='Your name')
# parser.add_argument('name', type=str, help='Your name')
parser.add_argument('--age', type=int, default=30, help='Your age', required=True)


# Parse the arguments
args = parser.parse_args()

# Access the arguments
print(f"Hello, {args.name}! You are {args.age} years old.")
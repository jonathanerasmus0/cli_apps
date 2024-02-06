import sys

def main():
    if "--help" in sys.argv:
        print("Usage:", sys.argv[0], "[--fast]")
        print("--help  : Display this help text")
        print("--fast  : Enable fast mode")
        sys.exit(0)

    print("Fast mode enabled" if "--fast" in sys.argv else "Slow mode enabled")

if __name__ == "__main__":
    main()

import argparse

def get_greeting(name=None):
    if name:
        return f"Guten Morgen {name}!"
    else:
        return "Guten Morgen Leute!"

def main():
    parser = argparse.ArgumentParser(description="Greetings Application")
    parser.add_argument('-n', '--name', type=str, help='Set the name')
    args = parser.parse_args()
    print(get_greeting(args.name))

if __name__ == "__main__":
    main()
    
import argparse

def main():
    parser = argparse.ArgumentParser(description="Greeting App")
    parser.add_argument("first_name", nargs="?", default="Larryy", help="First name")
    parser.add_argument("last_name", nargs="?", default="Hanssson", help="Last name")
    parser.add_argument("age", nargs="?", type=int, default=100, help="Age")
    parser.add_argument("--fast", action="store_true", help="Enable fast mode")

    args = parser.parse_args()

    print("fast mode enabled" if args.fast else "")

    age_plus_one = args.age + 1
    print(f"Hello {args.first_name} {args.last_name}! I see that you have had {age_plus_one} birthdays.")

if __name__ == "__main__":
    main()



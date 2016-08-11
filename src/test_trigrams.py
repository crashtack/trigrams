import sys


def main():
    if len(sys.argv) != 3:
        # print(USAGE)
        sys.exit(1)

        try:
            # result = ackermann(int(sys.argv[1]), int(sys.argv[2]))
            print('Arg 1: {} Arg 2: {}'.format(sys.argv[1], sys.argv[2]))
        except RunTimeError:
            print('sorry, something failed')
            sys.exit(1)
        # print("enter something")
        something = input('Tell me something! ')
        print()
        print(something)

"{0} {1}".format(*my_tuple[:2])

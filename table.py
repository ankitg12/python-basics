import argparse

class MultiplicationTable(argparse.Action):
    def __call__(self, parser, namespace, values, option_string=None):
        print("Multiplication table of", values)
        for i in range(1,11):
            print(values,"*",i,"=",values*i)
        parser.exit()

parser = argparse.ArgumentParser()
parser.add_argument("number", help="display multiplication table of a number", type=int, action=MultiplicationTable)
args = parser.parse_args()


# # give multiplication table of a number

# if len(sys.argv) != 2:
#     print("Usage: python table.py <number>")
#     sys.exit(1)

# n = int(input("Enter a number: "))
# for i in range(1,11):
#     print(n,"*",i,"=",n*i)

# # Path: table.py

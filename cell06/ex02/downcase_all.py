import sys
def downcase_it(string):
    return string.lower()
if __name__ == "__main__":
    if len(sys.argv) <= 1:
        print("none")
    else:
        for arg in sys.argv[1:]:
            print(downcase_it(arg))
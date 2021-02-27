# Write a program for reading a text file composed of multiple lines and
# print all the triplets of adjacent words of the same length.
# Words must be printed in uppercase.
# Punctuation marks should not be considered part of the words.
# The file does not contain genitives (possessive) nor contractions, such as n't or 've.
# The program must handle possible problems during input/output.

# The output should be: ('IS', 'IN', 'MY')
#                       ('NOT', 'TOO', 'BAD')
#                       ('TOO', 'BAD', 'LET')

def main():
    a = list()
    try:
        with open('strawberry-short.txt', 'r') as strawberry:
            for line in strawberry:
                for word in line.split():
                    a.append(word.strip(",.:;"))

            for n in range(len(a)-2):
                if len(a[n]) == len(a[n+1]) == len(a[n+2]):
                    print(f"('{a[n]}', '{a[n+1]}', '{a[n+2]}')".upper())

    except IndexError as error:
        print(f'The program gives "{error}" error, check!!')


if __name__ == '__main__':
    main()

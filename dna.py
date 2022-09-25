import csv
import sys


def main():

    # TODO: Check for command-line usage
    if len(sys.argv) != 3:
        print("Incorrect command-line argument.")
        sys.exit(1)


    # TODO: Read database file into a variable
    file = open(sys.argv[1], "r")
    reader = csv.DictReader(file)
    for row in reader:
        strs = list(row.keys())
    strs.remove("name")


    # TODO: Read DNA sequence file into a variable
    with open(sys.argv[2], "r") as f:
        content = f.read()

    # TODO: Find longest match of each STR in DNA sequence
    lon_mat = []
    for i in range(0,len(strs)):
        x = longest_match(content, strs[i])
        lon_mat.append(x)

    # TODO: Check database for matching profiles
    filee = open(sys.argv[1], "r")
    test = csv.DictReader(filee)
    for data in test:
        counter = 0
        for j in range(len(lon_mat)):
            if int(data[strs[j]]) == lon_mat[j]:
                counter+=1
        if counter == 8:
            print(data['name'])
            sys.exit(0)
    print("No match")
    file.close()
    filee.close()

    return


def longest_match(sequence, subsequence):
    """Returns length of longest run of subsequence in sequence."""

    # Initialize variables
    longest_run = 0
    subsequence_length = len(subsequence)
    sequence_length = len(sequence)

    # Check each character in sequence for most consecutive runs of subsequence
    for i in range(sequence_length):

        # Initialize count of consecutive runs
        count = 0

        # Check for a subsequence match in a "substring" (a subset of characters) within sequence
        # If a match, move substring to next potential match in sequence
        # Continue moving substring and checking for matches until out of consecutive matches
        while True:

            # Adjust substring start and end
            start = i + count * subsequence_length
            end = start + subsequence_length

            # If there is a match in the substring
            if sequence[start:end] == subsequence:
                count += 1

            # If there is no match in the substring
            else:
                break

        # Update most consecutive matches found
        longest_run = max(longest_run, count)

    # After checking for runs at each character in seqeuence, return longest run found
    return longest_run


main()

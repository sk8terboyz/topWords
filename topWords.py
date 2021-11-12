# Read in file and break it up
def word_frequency(fileName):
    try:
        if(fileName):
            # Create dictionary
            dict = {}
            punctuation = '!"#$%^&*()_-=+\':;<>@/[\\]{}`~0123456789\t\n\r\x0b\x0c'
            # Open file - auto close file
            with open(fileName) as f:
                lines = f.readlines()
                for line in lines:
                    for word in line.split(' '):
                        # Clean up the words
                        key = word.strip(punctuation).lower()
                        key = ''.join([i for i in key if not i.isdigit()])
                        # Update word key count
                        if(key in dict):
                            dict[key] += 1
                        else:
                            dict[key] = 1
                    # Final clenaup
                    dict.pop('')
                    # Return dictionary
                    return dict
    except:
        print("File not found.")

# Print total number of words in the list
def total_word_count(dict = {}):
    try:
        wordCount = 0
        if(dict):
            # Add all the values to get the final count
            for val in dict.values():
                wordCount += val
            return wordCount
        else:
            print("No values found.")
    except:
        print ("Error occurred. \nTerminating...")

# Print the top n amount of words and their frequency of use in the list
def top_n_frequent_words(dict = {}, n = 0):
    try:
        count = 0
        freqWords = {}
        if(dict and n != 0):
            # Order most frequent to least
            print("Top", n, "most frequent words:")
            for i in reversed(list(sorted(dict.values()))):
                if count < n:
                    # Format the top 20 most frequent words
                    freqWords[get_key(dict, i)] = i
                    # Easier to output here than creating more loops to print it in runner()
                    print("{:>4}) {:>12}: {:>4}".format(str(count+1), get_key(dict, i), str(i)))
                    count += 1
                return freqWords
    except:
        print("Error occurred. \nTerminating...")

# Call all functions and output the 20 most frequent words
def runner():
    count = 0
    # Store input file name prompted from user
    fn = input("Type the filename to find the top 20 most frequented words:")
    # Call first function and get filled dictionary object from it
    dict = word_frequency(fn)
    # Call and output the total word count
    print("Total word count: " + str(total_word_count(dict)))
    # Call and output the top n (20) most frequent words
    freqWords = top_n_frequent_words(dict, 20)

# Support function to find the key in the dictionary based on the value
def get_key(dict, val):
    for(key, value) in dict.items():
        if val == value:
            return key
    return "key doesn't exist"

runner()
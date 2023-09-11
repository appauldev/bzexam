# bzexam solutions
Solutions for the initial exam

## Zen_of_Python solution summary
1. Read the lines of the file
2. Extract the ZOP lines using regex from the previously extracted lines
3. Remove the 'ZOP' marker from the lines and print the poem
4. To obtain the word stats, extract each word from each line. Clean and normalize each word.
5. Iterate through the word/token list obtained from #4 and use a dictionary to keep track of the occurrence of each word
6. Sort and print the dictionary

## Domain_Counters solution summary
1. Read the lines of the csv file using the csv module
2. Extract the score and domain values
3. Convert the domain string from #2 into a list[str]
4. Build the domain and subdomains by joining the contents of the list in #3 starting from the first item until the last item of the list
5. Iterate through the obtained domain list from #4 and use a dictionary to keep track of the scores (obtained from #2) of each domain/sub-domain
6. 6. Sort and print the dictionary

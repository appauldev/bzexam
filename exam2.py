# Paul Lawrence Z Sales
# Applicant: Data Engineer
# Solution summary:
# 1. Read the lines of the csv using the csv module
# 2. Extract the score and domain values
# 3. Build the sub-domain list by converting the domain into a list[str]
# 4. Building the domain is done by joining the contents of the list
#    starting from the first item until the last item of the list
# 5. Use a dictionary to keep track of the scores.
# 6. Basically, since we know the score from #2, iterate the through the
#    domain list returned from #4 and add/update their dictionary values
# 7. Sort and print the dictionary

# NOTE: this assumes that the file input is in inputs/input.csv
# This allows us to just use `python exam2.py` to run the file


import csv

FILE_PATH = 'inputs/input.csv'


def domain_builder(domain_string: str):
    # tokenize the string
    tokens = domain_string.split('.')
    # create the domains and subdomains
    domain_list = []
    # build the domains
    # basically, you start by building the domain string from the first token
    # and you iterate to each remaining tokens
    for i in range(len(tokens)):
        domain_list.append(".".join(tokens[i:]))

    return domain_list


def count_domain(file):
    try:
        # keep track of the domain score with a dictionary
        domain_stats = {}
        with open(file, 'r') as opened_file:
            csv_reader = csv.reader(opened_file)

            for row in csv_reader:
                score, domain = row
                # extract the domains and sub-domains
                domain_list = domain_builder(domain)
                # add/update the domain/subdomain score
                for d in domain_list:
                    if d in domain_stats:
                        domain_stats[d] += int(score)
                    else:
                        domain_stats[d] = int(score)

        # sort and print
        sorted_domain_stats = sorted(domain_stats.items(), key=lambda x: x[1], reverse=True)

        for domain, score in sorted_domain_stats:
            print(f'{str(score).ljust(5)} {domain}')

    except:
        print('count_domain error')


if __name__ == '__main__':
    count_domain(FILE_PATH)

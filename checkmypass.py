import requests
import hashlib
import sys

def request_api_data(query_char):
    # accept dynamic input of first 5 characters of hash [enhanced security]
    url = 'https://api.pwnedpasswords.com/range/' + query_char
    res = requests.get(url)
    if res.status_code != 200:
        raise RuntimeError(f'Error fetching :{res.status_code}, Check API and try again!!')
    else:
        return res

#to check count of leaks of our password by looping through all hashes
def get_password_leaks(hashes, hash_to_check):
    #tupple comprehension to loop through every line and get count which is prsent after :
    #to split hashes correctly use splitlines
    hashes = (line.split(':') for line in hashes.text.splitlines())
    for hash, count in hashes:
        if hash == hash_to_check:
            return count
    return 0


def pwned_api_check(password):
    sha1password = hashlib.sha1(password.encode('utf-8')).hexdigest().upper()
    #we need only first 5 charcters of our sha to send to api
    first5_char, tail = sha1password[:5],sha1password[5:]
    response = request_api_data(first5_char)
    return get_password_leaks(response, tail)




def main(args):
    for password in args:

        count = pwned_api_check(password)
        if(count):
            print(f'{password} was found {count} times..You should probably change your password!!!')
        else:
            print(f'{password} was not found..Carry on!!!')
    return 'done'


if __name__ == '__main__':
    #pass the arguments in the command line itself[omit filename]
    #sys.exit(main(sys.argv[1:]))
    filename = sys.argv[1]

    with open(filename, "r") as fileHandler:
        # Read each password in the input file
        password = list()
        for line in fileHandler:
            password.append(line.strip())

        sys.exit(main(password))



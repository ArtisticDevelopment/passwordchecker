import requests
import hashlib
import sys
#API CALL - sends hashed text to api, returns error if status_code != 200
def request_api_data(query_char):
  url = 'https://api.pwnedpasswords.com/range/'+ query_char
  res = requests.get(url)
  if res.status_code != 200:
    raise RuntimeError(f'Error Fetching: {res.status_code}, check the api and tryyyageen!')
  print("API info is valid")
  return res

def got_leaked_count(hashes, hash_to_check):
  hashes = (line.split(':') for line in hashes.text.splitlines())
  for h, count in hashes:
   if h == hash_to_check:
     return count
  return 0

#initializing function, hashes password and creates two subtext variables from said password and receives array("response") of matches based on first 5 chars
def pwned_api_check(password):
  sha1password = hashlib.sha1(password.encode('utf-8')).hexdigest().upper()
  first5_chars, tail = sha1password[:5],sha1password[5:]
  response = request_api_data(first5_chars)
  return got_leaked_count(response,tail)

def main(args):
  for password in args:
    count = pwned_api_check(password)
    if count:
      print(f'{password} was found {count} times. Youuuu should change that...haha')
    else:
      print(f'{password} was NOT found, so ... carry on!')
  return 'done!'

#sys.argv is a list of command-line arguments passed to the script.
#sys.argv[0] is always the script name (e.g., checkmypass.py)
#sys.argv[1:] grabs everything after that, which would be the actual passwords you want to check.
main(sys.argv[1:])
from google import search, get_random_user_agent
import sys

reload(sys)
sys.setdefaultencoding('utf-8')

user_agent = get_random_user_agent()
print_fmt = '{}\t{}\t{}'

for sr in search('malware', lang='en', stop=20, only_standard=False, user_agent=user_agent):
    print print_fmt.format(sr.link, sr.title, sr.snippet)

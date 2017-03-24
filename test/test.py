from google import search

for url in search('"Breaking Code" WordPress blog', stop=10, only_standard=True):
    print(url)

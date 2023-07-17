import urllib.request as libreq
import feedparser

#Basic query
base_url = 'http://export.arxiv.org/api/query?';


'''
field prefix
    ti	Title
    au	Author
    abs	Abstract
    co	Comment
    jr	Journal Reference
    cat	Subject Category
    rn	Report Number
    id	Id (use id_list instead)
    all	All of the above
'''
cat = 'astro-ph'

#Search Parameters
search_query = 'cat:%s' % (cat) # search for electron in all fields
start = 0                     # retreive the first 5 results
id_list = ''
max_results = 10



query = 'search_query=%s&start=%i&max_results=%i' % (search_query,
                                                     start,
                                                     max_results)
# perform a GET request using the base_url and query
response = libreq.urlopen(base_url+query).read()

# parse the response using feedparser
feed = feedparser.parse(response)



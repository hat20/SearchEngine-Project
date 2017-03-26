def get_page(url):
    try:
        import urllib
        return urllib.urlopen(url).read()
    except:
        return


def get_all_links(page):
    while True:
        url,endpos = get_next_link(page)
        links = []
        if url:
           links.append(url)
           page = page[endpos:]
        else:
            break
    return links


def get_next_link(page):
    start_link = page.find("<a href=")
    if start_link == -1:
        return None,0
    start_quote = page.find('"',start_link)
    end_quote = page.find('"',start_quote+1)
    url = page[start_quote + 1 : end_quote]
    return url,end_quote

def print_all_links():
    webpage = get_page('http://xkcd.com/353')
    print webpage
    print '#'*50
    print "LIST OF URL's are :"
    urls = get_all_links(webpage)
    i = 0
    while i< len(urls):
        print urls[i]
        i = i +1

print_all_links()

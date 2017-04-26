#SEARCH ENGINE PROJECT - by Harshit Tewari
#procedure that imports the python library "urllib" which then helps us in getting the content on the url

def get_page(url):
#try and except are exception handling blocks
#try will first import the library and then use its function read to read the contents of the url
#and if there is an error then the except block will execute     
    try:
        import urllib
        return urllib.urlopen(url).read()
    except:
        return ""

#this procedure helps find the next url for crawling in the and returns the url and the index it ends at

def get_next_target(page):
#start_link stores the index at which "<a href=" is found and it's value is -1 if it isn't found   
    start_link = page.find('<a href=')
    if start_link == -1: 
        return None, 0
    start_quote = page.find('"', start_link)
#start_quote stores the index at which double quotes start as the syntax for a url in the content is 
#<a href="https://xyz.com"
    end_quote = page.find('"', start_quote + 1)
    url = page[start_quote + 1:end_quote]
    return url, end_quote

# Union function appends the list p by the element 'e' if it isn't present in the list

def union(p,q):
    for e in q:
        if e not in p:
            p.append(e)



# get_all_links calls the function get_next_target for as long as there is a target i.e. there is a new url
#it then collects the all the urls and stores them in a list and then returns them

def get_all_links(page):
    links = []
    while len(links)<2:
        url,endpos = get_next_target(page)
        if url:
# if it's a legal url then we add the url in the links list
            links.append(url)
            page = page[endpos:]
        else:
            break
#returning the list links after the completion of program
    return links

#crawl_web is the function that actually does the crawling

def crawl_web(seed):
#seed is the page that is the crux of our crawler. It's kind of the main page
#that has all the urls stored in it. Seed page with less links is practically
#useless       
    tocrawl = seed
    crawled = []
    index = []
#the loop runs for as long as there are urls left for crawling
#newpage stores the content of the url popped    
    while tocrawl:
        newpage = tocrawl.pop()
        if newpage not in crawled:
            content = get_page(newpage)
            add_page_to_index(index,newpage,content)
            union(tocrawl,get_all_links(content))
            crawled.append(newpage)
    return index

#we maintain an index which is somewhat a complex list data structure
#[[<keyword1>,[<url1>,<url2>..]],[<keyword2>,[<url1>,..]],..]

def add_page_to_index(index,url,content):
    keywords = content.split()
    for words in keywords:
        add_to_index(index,words,url)

#entry represents [<keyword1>,[<url1>,<url2>..]]
#therefore entry[0] represents keywords
#and entry[1] represents list of urls        

def add_to_index(index,keyword,url):
    for entry in index:
        if(entry[0]==keyword):
#changes made so that a url is not repeated more than once for a keyword even if the keyword repeats itself in the content multiple times
            if url not in entry[1]:   
                entry[1].append(url)
                return
    index.append([keyword,[url]])


#this function finds the keyword in the index and returns the urls associated with it

def lookup(index,keyword):
    for entry in index:
        if entry[0]== keyword :
            return entry[1]
    return []    

#this is a driver function

def runsearchengine():
    print '+'*50
    print '\t'*2 + "LUCK-LUCK-GO"
#ENTER THE URL OF THE WEBPAGE YOU WANT TO USE
#I preferred using a test page that had a very limited number of links to crawl
    page = get_page("file:///C:...homepage.html")
    seed = get_all_links(page)
    index = crawl_web(seed)
    search = raw_input("Enter your query ")
    result = lookup(index,search)
    i= 0
    if result == []:
        print "Sorry result not found"
    else:
        print "KEYWORD CAN BE FOUND IN FOLLOWING URLS:"
        while i < len(result):
            print (i+1),') \t',result[i]
            i = i+1
        
    print '+'*50


runsearchengine()







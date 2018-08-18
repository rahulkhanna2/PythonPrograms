
def get_page(url):
    try:
        import urllib
        return urllib.urlopen(url).read()
    except:
        return ''


def get_next_url(page):
    start_link = page.find('<a href=') #finds the starting of the link
    if start_link == -1:
        return None , 0
    start_quote = page.find('"' , start_link)#find's the starting of the " before url but includes " in it
    end_quote = page.find('"' , start_quote + 1) #find's the end of the " after url but does not includes " in it
    url = page[start_quote+1 : end_quote] #Gives the url of the site found. +1 just skips the " included in the start_quote.
    return url , end_quote

def get_all_links(page):
    links = []
    while True:
        url ,end_position = get_next_url(page)
        if url:
            links.append(url)
            page = page[end_position:]
        else:
            break
        return links

def union(a, b):
    for i in b:
        if i not in a :
            a.append(i)



def crawl_web(seed , max_pages):
    to_crawl = [seed]
    crawled = []
    while to_crawl:
        page = to_crawl.pop()
        if page not in crawled and len(crawled) <= max_pages:
            union(to_crawl , get_all_links(get_page(page)))
            crawled.append(page)
            
    return crawled
    
print get_all_links(get_page(raw_input("Enter your Page Link \t")))

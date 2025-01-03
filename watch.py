from re import search,match, IGNORECASE

def shorten(html: str)-> str:
    """_shorten url_

    Args:
        html (str): _url in str form_

    Returns:
        str: _a shorter url_
    """
    if 'www' in html:
        html =html.replace("www.","")
    return html.replace(".com/embed","")

def parse(html: str)-> str:
    """_Given html content find the webpage url and extract it_

    Args:
        html (str): _Embeded HTML of a page_

    Returns:
        str: _Shorter url for the page_
    """
    
    pattern = r"(?P<url>(?:http|https)://(www\.)?youtube\.com/embed/[a-z0-9]+)"

    url = result.group('url') if (result := search(pattern=pattern, string=html, flags=IGNORECASE)) else None
    return shorten(html=url) if url else None
def main()-> None:
    long='<iframe width="560" height="315" src="http://youtube.com/embed/xvFZjo5PgG0" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>'

    print(parse(html=long))

if __name__ == "__main__":
    main()

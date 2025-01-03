from re import search,match, IGNORECASE

def shorten(endpoint: str)-> str:
    """_Create a url to a youtube video given the endpoint_

    Args:
        endpoint (str): _str identifying the youtube video_

    Returns:
        str: _a shorter url prefixed with https://youtu.be/_
    """
    return f"https://youtu.be/{endpoint}"
   

def parse(html: str)-> str:
    """_Given html content find the webpage url and extract it_

    Args:
        html (str): _Embeded HTML of a page_

    Returns:
        str: _Shorter url for the page_
    """
    
    pattern = r"<iframe.+src=\"(?:http|https)://(www\.)?youtube\.com/embed/(?P<endpoint>[a-z0-9]+)\".+>"

    url = result.group('endpoint') if (result := search(pattern=pattern, string=html, flags=IGNORECASE)) else None
    return shorten(endpoint=url) if url else None
def main()-> None:
    print(parse(input("HTML: ")))

if __name__ == "__main__":
    main()

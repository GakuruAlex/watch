import pytest
from watch import shorten,parse

@pytest.mark.parametrize("endpoint, youtube_url",[
    ("xvFZjo5PgG0", "https://youtu.be/xvFZjo5PgG0"),
    ("xvFZjo5PGG0", "https://youtu.be/xvFZjo5PGG0"),
    ("xvFZjo5PGG2", "https://youtu.be/xvFZjo5PGG2")
])
def test_shorten(endpoint, youtube_url):
    assert shorten(endpoint) == youtube_url

@pytest.mark.parametrize("html, url",[
    ('<iframe src="http://youtube.com/embed/xvFZjo5PgG0"></iframe>', "https://youtu.be/xvFZjo5PgG0"),
    ('<iframe src="https://youtube.com/embed/xvFZjo5PgG0"></iframe>', "https://youtu.be/xvFZjo5PgG0"),
    ('<iframe src="https://www.youtube.com/embed/xvFZjo5PgG0"></iframe>', "https://youtu.be/xvFZjo5PgG0"),
    ('<iframe src="https://cs50.harvard.edu/python"></iframe>', None),
    ('<iframe width="560" height="315" src="https://www.youtube.com/embed/xvFZjo5PgG0" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>', 'https://youtu.be/xvFZjo5PgG0'),
    ('<iframe width="560" height="315" src="https://youtube.com/embed/xvFZjo5PgG0" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>', 'https://youtu.be/xvFZjo5PgG0'),
    ('<iframe width="560" height="315" src="http://www.youtube.com/embed/xvFZjo5PgG0" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>', 'https://youtu.be/xvFZjo5PgG0')



])
def test_parse(html, url):
    assert parse(html) == url
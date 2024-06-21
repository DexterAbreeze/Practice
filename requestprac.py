import requests
import os, sys


def reading():
    #Pass parameters into URLs with params kwarg. 
    payload = {'key1': 'value1', 'key2': 'value2'}
    r = requests.get('https://httpbin.org/get', params=payload)

    print(r.url)

    #Other HTTP request types.
    p = requests.put('https://httpbin.org/put', data={'key': 'value'})
    d = requests.delete('https://httpbin.org/delete')
    h = requests.head('https://httpbin.org/get')
    o = requests.options('https://httpbin.org/get')


    #Add HTTP headers to q reuqest. 
    url = 'https://api.github.com/'
    headers = {'user-agent': 'my-app/0.0.1'}

    r = requests.get(url, headers=headers)

    print(r)

    #The timeout parameter is good in productiob to prevent functions from hanging forever.
    #timeout = requests.get('https://github.com/', timeout=0.001)

    #Access cookies
    '''
    url = 'http://example.com/some/cookie/setting/url'
    r = requests.get(url)

    r.cookies['example_cookie_name']
    '''
    #Bad request testing.
    bad_r = requests.get('https://httpbin.org/status/404')
    bad_r.status_code

    r.raise_for_status()
    #bad_r.raise_for_status()

    s = requests.Session()

    s.get('https://httpbin.org/cookies/set/sessioncookie/123456789')
    r = s.get('https://httpbin.org/cookies')

    print(r.text)
    # '{"cookies": {"sessioncookie": "123456789"}}'

    #Setting default data in a request method. . 

    s = requests.Session()
    s.auth = ('user', 'pass')
    s.headers.update({'x-test': 'true'})

    # both 'x-test' and 'x-test2' are sent
    s.get('https://httpbin.org/headers', headers={'x-test2': 'true'})

    #Comparison between getting cookies with and without specifying with the cookies parameter.  

    s = requests.Session()

    r = s.get('https://httpbin.org/cookies', cookies={'from-my': 'browser'})
    print(r.text)
    # '{"cookies": {"from-my": "browser"}}'

    r = s.get('https://httpbin.org/cookies')
    print(r.text)
    # '{"cookies": {}}'


def comicpractice():
    r = requests.get("https://xkcd.com/357/")

    # dir selects the elements within the request object that we can do more with. 
    print(dir(r))

    #print(help(r))

    #Gives HTML unicode for the page. 
    #print(r.text)

    comic = requests.get("https://imgs.xkcd.com/comics/flies.png")

    #Gives bytes from an image. 
    #print(comic.content)
    '''
    #Writes a png file from the image's bytes (wb) inside of this directory. It's named comicname.png.
    with open("comicname.png","wb") as f:
        f.write(comic.content)
    '''

    #Anything less than 400 is in good shape
    print(comic.status_code)

    #Checks if status code is less than 400. Good for quick checking site stability before messing with it.
    print(comic.ok)






comicpractice()
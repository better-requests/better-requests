# better-requests: <br> HTTP for Humans that do right

A good design makes it intuitive and convenient to do right, 
**better-requests** is a wrapper for *requests* that makes default behaviors right. 

* Default value of timeout is 30s (configurable) instead of forever, no need to specify timeout explicitly everywhere. 
* Non-successful responses raise by default, no need to call raise_for_status explicitly everywhere. 

## Usage

Write this:

``` python
>>> import better_requests as requests
>>> r = requests.get('https://www.python.org')
>>> 'Python is a programming language' in r.content
True
```

Instead of: 

``` python
>>> import requests
>>> 
>>> # You need to explicity specify timeout everywhere, or, BOOM!
... r = requests.get('https://www.python.org', timeout=30)
>>>
>>> # And explicity check status_code before reading content, everywhere, or, BOOM!
... r.raise_for_status()
>>>
>>> # And do things finally after all the ceremonies
... 'Python is a programming language' in r.content
True
```

When you need to configure default timeout, either set it globally: 

``` python
>>> import better_requests as requests
>>> requests.Session.default_timeout = 5
>>>
>>> r = requests.get('https://www.python.org')
>>> 'Python is a programming language' in r.content
True
```

Or per session:

``` python
>>> import better_requests as requests
>>> with requests.Session() as s:
>>>     s.default_timeout = 5
>>>     s.get('https://httpbin.org/get')
```

It works just as expected. 

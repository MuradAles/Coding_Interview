def URLify(url):
    url = url.rstrip()
    url = url.replace(" ", "%20")
    return url


print(URLify("Hello World   "))

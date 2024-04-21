from urllib.parse import urlparse

def get_domain_name(url):
    try:
        dict1 = urlparse(url)
        return dict1
    except:
        return 'Invalid Value'
    
url = input("Enter valid URL: ")
print(get_domain_name(url))
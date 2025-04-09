import requests
import warnings
import argparse
from colorama import Fore, Back, Style
from time import sleep

warnings.filterwarnings("ignore")

parser = argparse.ArgumentParser(description='Metadir Is Tool That Search for Metafiles (exp. Robots.txt, Sitemap.xml)', prog= 'metadir.py', epilog= 'Example: python3 metadir.py -u https://target.com')
parser.add_argument('-u', '--url', type=str, help='Set target url', metavar= 'TARGET', default=False)

args = parser.parse_args()
url = args.url
print("")
print("MetaScanner V0.1")
print("Dev: Darksider01011")

def robots(url):
    headers = {
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:91.0) Gecko/20100101 Firefox/91.0',
    'Accept': "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
    'Accept-Language': 'en-US,en;q=0.5',
    'Accept-Encoding': 'gzip, deflate, br',
    'Connection': 'keep-alive',  
    'Sec-Fetch-Dest': 'document',
    'Sec-Fetch-Mode': 'navigate',
    'Sec-Fetch-Site': 'none',
    'Sec-Fetch-User': '?1',
    'Cache-Control': 'max-age=0'
    }
    try:
        url += "/robots.txt"
        response = requests.get(url, allow_redirects=True, verify=False, headers=headers)
        code = response.status_code
        ct = response.headers.get('Content-Type')
        last = response.headers.get('last-modified')
        body = response.text
        size = len(response.content)
        

        if (ct == "text/plain") or (ct == "text/plain; charset=UTF-8") or (ct == "text/plain; charset=utf-8"):
            type = True
        else:
            type = False

        if ct:
            print("")
        else:
            print("")

        if last:
            lastmodi =  True
        else:
            lastmodi = False

        if "Disallow:" in body:
            bodyy = True
        else:
            bodyy = False
        
        if (type == True) or (lastmodi == True) or (bodyy == True):
            print(Fore.WHITE + Style.BRIGHT + url + Fore.GREEN + Style.BRIGHT + " Found" + Fore.WHITE + "  |" + Fore.BLUE + "  Status Code:" + Fore.GREEN + " " + Fore.WHITE +  str(code) + "  |" + Fore.WHITE + "  Response Size: " + str(size))
        else:
            print(Fore.WHITE + Style.BRIGHT + url + Fore.RED + Style.BRIGHT + " Not Found" + Fore.WHITE + "  |" + Fore.BLUE + "  Status Code:" + Fore.GREEN + " " + Fore.WHITE +  str(code) + "  |" + Fore.WHITE + "  Response Size: " + str(size))

                
        return ""

    except requests.exceptions.RequestException as e:
        print(Fore.WHITE + Style.BRIGHT + url + Fore.RED + Style.BRIGHT + "  ERROR: " + str(e))

def sitemap(url):
    try:
        headers = {
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:91.0) Gecko/20100101 Firefox/91.0',
        'Accept': "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
        'Accept-Language': 'en-US,en;q=0.5',
        'Accept-Encoding': 'gzip, deflate, br',
        'Connection': 'keep-alive',  
        'Sec-Fetch-Dest': 'document',
        'Sec-Fetch-Mode': 'navigate',
        'Sec-Fetch-Site': 'none',
        'Sec-Fetch-User': '?1',
        'Cache-Control': 'max-age=0'
        }
        url += "/sitemap.xml"
        response = requests.get(url, allow_redirects=True, verify=False, headers=headers)
        code = response.status_code
        body = response.text
        lastmodified = response.headers.get('last-modified')
        contenttype = response.headers.get('Content-Type')
        size = len(response.content)
        
        if lastmodified:
            last = True
        else:
            last = False
        
        if "urlset" in body:
            loc = True
        else:
            loc = False
        
        if "sitemapindex" in body:
            sitemap = True
        else:
            sitemap = False

        if (sitemap == True) or (loc == True) or (last == True):
            print(Fore.WHITE + Style.BRIGHT + url + Fore.GREEN + Style.BRIGHT + " Found" + Fore.WHITE + "  |" + Fore.BLUE + "  Status Code:" + Fore.GREEN + " " + Fore.WHITE +  str(code) + "  |" + Fore.WHITE + "  Response Size: " + str(size))
        else:
            print(Fore.WHITE + Style.BRIGHT + url + Fore.RED + Style.BRIGHT + " Not Found" + Fore.WHITE + "  |" + Fore.BLUE + "  Status Code:" + Fore.GREEN + " " + Fore.WHITE +  str(code) + "  |" + Fore.WHITE + "  Response Size: " + str(size))

    except requests.exceptions.RequestException as e:
        print(Fore.WHITE + Style.BRIGHT + url + Fore.RED + Style.BRIGHT + "  ERROR: " + str(e))

    return ""

def security(url):
    try:
        headers = {
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:91.0) Gecko/20100101 Firefox/91.0',
        'Accept': "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
        'Accept-Language': 'en-US,en;q=0.5',
        'Accept-Encoding': 'gzip, deflate, br',
        'Connection': 'keep-alive',  
        'Sec-Fetch-Dest': 'document',
        'Sec-Fetch-Mode': 'navigate',
        'Sec-Fetch-Site': 'none',
        'Sec-Fetch-User': '?1',
        'Cache-Control': 'max-age=0'
        }
        url += "/security.txt"
        response = requests.get(url, allow_redirects=True, verify=False, headers=headers)
        code = response.status_code
        body = response.text
        lastmodified = response.headers.get('last-modified')
        contenttype = response.headers.get('Content-Type')
        size = len(response.content)

        if lastmodified:
            last = True
        else:
            last = False
        
        if (contenttype == "text/plain; charset=utf-8") or (contenttype == "text/plain") or (contenttype == "text/plain; charset=UTF-8") or (contenttype == "text/plain;charset=utf-8") or (contenttype == "text/plain;charset=UTF-8"):
            content = True
        else:
            content = False
        
        if (content == True):
            print(Fore.WHITE + Style.BRIGHT + url + Fore.GREEN + Style.BRIGHT + " Found" + Fore.WHITE + "  |" + Fore.BLUE + "  Status Code:" + Fore.GREEN + " " + Fore.WHITE +  str(code) + "  |" + Fore.WHITE + "  Response Size: " + str(size))
        else:
            print(Fore.WHITE + Style.BRIGHT + url + Fore.RED + Style.BRIGHT + " Not Found" + Fore.WHITE + "  |" + Fore.BLUE + "  Status Code:" + Fore.GREEN + " " + Fore.WHITE +  str(code) + "  |" + Fore.WHITE + "  Response Size: " + str(size))

    except requests.exceptions.RequestException as e:
        print(Fore.WHITE + Style.BRIGHT + url + Fore.RED + Style.BRIGHT + "  ERROR: " + str(e))

    return "" 

def security_alter(url):
    try:
        headers = {
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:91.0) Gecko/20100101 Firefox/91.0',
        'Accept': "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
        'Accept-Language': 'en-US,en;q=0.5',
        'Accept-Encoding': 'gzip, deflate, br',
        'Connection': 'keep-alive',  
        'Sec-Fetch-Dest': 'document',
        'Sec-Fetch-Mode': 'navigate',
        'Sec-Fetch-Site': 'none',
        'Sec-Fetch-User': '?1',
        'Cache-Control': 'max-age=0'
        }
        url += "/.well-known/security.txt"
        response = requests.get(url, allow_redirects=True, verify=False, headers=headers)
        code = response.status_code
        body = response.text
        lastmodified = response.headers.get('last-modified')
        contenttype = response.headers.get('Content-Type')
        size = len(response.content)

        if lastmodified:
            last = True
        else:
            last = False
        
        if (contenttype == "text/plain; charset=utf-8") or (contenttype == "text/plain") or (contenttype == "text/plain; charset=UTF-8") or (contenttype == "text/plain;charset=utf-8") or (contenttype == "text/plain;charset=UTF-8"):
            content = True
        else:
            content = False
        
        if (content == True):
            print(Fore.WHITE + Style.BRIGHT + url + Fore.GREEN + Style.BRIGHT + " Found" + Fore.WHITE + "  |" + Fore.BLUE + "  Status Code:" + Fore.GREEN + " " + Fore.WHITE +  str(code) + "  |" + Fore.WHITE + "  Response Size: " + str(size))
        else:
            print(Fore.WHITE + Style.BRIGHT + url + Fore.RED + Style.BRIGHT + " Not Found" + Fore.WHITE + "  |" + Fore.BLUE + "  Status Code:" + Fore.GREEN + " " + Fore.WHITE +  str(code) + "  |" + Fore.WHITE + "  Response Size: " + str(size))

    except requests.exceptions.RequestException as e:
        print(Fore.WHITE + Style.BRIGHT + url + Fore.RED + Style.BRIGHT + "  ERROR: " + str(e))

    return "" 

def humans(url):
    try:
        headers = {
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:91.0) Gecko/20100101 Firefox/91.0',
        'Accept': "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
        'Accept-Language': 'en-US,en;q=0.5',
        'Accept-Encoding': 'gzip, deflate, br',
        'Connection': 'keep-alive',  
        'Sec-Fetch-Dest': 'document',
        'Sec-Fetch-Mode': 'navigprint(Fore.WHITE + Style.BRIGHT + url + Fore.GREEN + Style.BRIGHT + " Found" + Fore.BLUE + "  Status Code:" + Fore.GREEN + " " + str(code)  + Fore.WHITE + Style.BRIGHT + "  Info: sitemap.xml file that tells search engines like Google which URLs on your website should be indexed")ate',
        'Sec-Fetch-Site': 'none',
        'Sec-Fetch-User': '?1',
        'Cache-Control': 'max-age=0'}
        url += "/humans.txt"
        response = requests.get(url, allow_redirects=True, verify=False, headers=headers)
        code = response.status_code
        body = response.text
        contenttype = response.headers.get('Content-Type')
        size = len(response.content)

        if (contenttype == "text/plain; charset=utf-8") or (contenttype == "text/plain") or (contenttype == "text/plain; charset=UTF-8") or (contenttype == "text/plain;charset=utf-8") or (contenttype == "text/plain;charset=UTF-8"):
            b = True
        else:
            b = False
        
        if (b == True) and (code != 404):
            print(Fore.WHITE + Style.BRIGHT + url + Fore.GREEN + Style.BRIGHT + " Found" + Fore.WHITE + "  |" + Fore.BLUE + "  Status Code:" + Fore.GREEN + " " + Fore.WHITE +  str(code) + "  |" + Fore.WHITE + "  Response Size: " + str(size))
        else:
            print(Fore.WHITE + Style.BRIGHT + url + Fore.RED + Style.BRIGHT + " Not Found" + Fore.WHITE + "  |" + Fore.BLUE + "  Status Code:" + Fore.GREEN + " " + Fore.WHITE +  str(code) + "  |" + Fore.WHITE + "  Response Size: " + str(size))

    except requests.exceptions.RequestException as e:
        print(Fore.WHITE + Style.BRIGHT + url + Fore.RED + Style.BRIGHT + "  ERROR: " + str(e))

def pgp(url):
    try:
        headers = {
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:91.0) Gecko/20100101 Firefox/91.0',
        'Accept': "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
        'Accept-Language': 'en-US,en;q=0.5',
        'Accept-Encoding': 'gzip, deflate, br',
        'Connection': 'keep-alive',  
        'Sec-Fetch-Dest': 'document',
        'Sec-Fetch-Mode': 'navigate',
        'Sec-Fetch-Site': 'none',
        'Sec-Fetch-User': '?1',
        'Cache-Control': 'max-age=0'}
        url += "/pgp-key.txt"
        response = requests.get(url, allow_redirects=True, verify=False, headers=headers)
        code = response.status_code
        body = response.text
        size = len(response.content)

        if "-----BEGIN" in body:
            begin = True
        else:
            begin = False

        if "-----END" in body:
            end = True
        else:
            end = False
        
        if (begin == True) or (end == True):
            print(Fore.WHITE + Style.BRIGHT + url + Fore.GREEN + Style.BRIGHT + " Found" + Fore.WHITE + "  |" + Fore.BLUE + "  Status Code:" + Fore.GREEN + " " + Fore.WHITE +  str(code) + "  |" + Fore.WHITE + "  Response Size: " + str(size))
        else:
            print(Fore.WHITE + Style.BRIGHT + url + Fore.RED + Style.BRIGHT + " Not Found" + Fore.WHITE + "  |" + Fore.BLUE + "  Status Code:" + Fore.GREEN + " " + Fore.WHITE +  str(code) + "  |" + Fore.WHITE + "  Response Size: " + str(size))

        
    except requests.exceptions.RequestException as e:
        print(Fore.WHITE + Style.BRIGHT + url + Fore.RED + Style.BRIGHT + "  ERROR: " + str(e))

def wellpgp(url):
    try:
        headers = {
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:91.0) Gecko/20100101 Firefox/91.0',
        'Accept': "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
        'Accept-Language': 'en-US,en;q=0.5',
        'Accept-Encoding': 'gzip, deflate, br',
        'Connection': 'keep-alive',  
        'Sec-Fetch-Dest': 'document',
        'Sec-Fetch-Mode': 'navigate',
        'Sec-Fetch-Site': 'none',
        'Sec-Fetch-User': '?1',
        'Cache-Control': 'max-age=0'}
        url += "/.well-known/pgp-key.txt"
        response = requests.get(url, allow_redirects=True, verify=False, headers=headers)
        code = response.status_code
        body = response.text
        size = len(response.content)

        if "-----BEGIN" in body:
            begin = True
        else:
            begin = False

        if "-----END" in body:
            end = True
        else:
            end = False

        if (begin == True) or (end == True):
            print(Fore.WHITE + Style.BRIGHT + url + Fore.GREEN + Style.BRIGHT + " Found" + Fore.WHITE + "  |" + Fore.BLUE + "  Status Code:" + Fore.GREEN + " " + Fore.WHITE +  str(code) + "  |" + Fore.WHITE + "  Response Size: " + str(size))
        else:
            print(Fore.WHITE + Style.BRIGHT + url + Fore.RED + Style.BRIGHT + " Not Found" + Fore.WHITE + "  |" + Fore.BLUE + "  Status Code:" + Fore.GREEN + " " + Fore.WHITE +  str(code) + "  |" + Fore.WHITE + "  Response Size: " + str(size))

        
    except requests.exceptions.RequestException as e:
        print(Fore.WHITE + Style.BRIGHT + url + Fore.RED + Style.BRIGHT + "  ERROR: " + str(e))

def favicon(url):
    try:
        headers = {
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:91.0) Gecko/20100101 Firefox/91.0',
        'Accept': "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
        'Accept-Language': 'en-US,en;q=0.5',
        'Accept-Encoding': 'gzip, deflate, br',
        'Connection': 'keep-alive',  
        'Sec-Fetch-Dest': 'document',
        'Sec-Fetch-Mode': 'navigate',
        'Sec-Fetch-Site': 'none',
        'Sec-Fetch-User': '?1',
        'Cache-Control': 'max-age=0'}
        url += "/favicon.ico"
        response = requests.get(url, verify=False, headers=headers)
        code = response.status_code
        body = response.content
        size = len(response.content)
        contenttype = response.headers.get('Content-Type')
        
        bodyy = str(body)

        if "x00" in bodyy:
            ico = True
        else:
            ico = False
        
        if "xff" in bodyy:
            icoo = True
        else:
            icoo = False

        if (contenttype == "image/x-icon") or (contenttype == "image/png"):
            ctype = True
        else:
            ctype = False

        if (ctype == True) or (ico == True) or (icoo == True):
            print(Fore.WHITE + Style.BRIGHT + url + Fore.GREEN + Style.BRIGHT + " Found" + Fore.WHITE + "  |" + Fore.BLUE + "  Status Code:" + Fore.GREEN + " " + Fore.WHITE +  str(code) + "  |" + Fore.WHITE + "  Response Size: " + str(size))
        else:
            print(Fore.WHITE + Style.BRIGHT + url + Fore.RED + Style.BRIGHT + " Not Found" + Fore.WHITE + "  |" + Fore.BLUE + "  Status Code:" + Fore.GREEN + " " + Fore.WHITE +  str(code) + "  |" + Fore.WHITE + "  Response Size: " + str(size))

    except requests.exceptions.RequestException as e:
        print(Fore.WHITE + Style.BRIGHT + url + Fore.RED + Style.BRIGHT + "  ERROR: " + str(e))

def broconfig(url):
    try:
        headers = {
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:91.0) Gecko/20100101 Firefox/91.0',
        'Accept': "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
        'Accept-Language': 'en-US,en;q=0.5',
        'Accept-Encoding': 'gzip, deflate, br',
        'Connection': 'keep-alive',  
        'Sec-Fetch-Dest': 'document',
        'Sec-Fetch-Mode': 'navigate',
        'Sec-Fetch-Site': 'none',
        'Sec-Fetch-User': '?1',
        'Cache-Control': 'max-age=0'}
        url += "/browserconfig.xml"
        response = requests.get(url, allow_redirects=True, verify=False, headers=headers)
        code = response.status_code
        body = response.content
        size = len(response.content)
        bodyy = str(body)

        if "?xml" in bodyy:
            config = True
        else:
            config = False

        if (config == True):
            print(Fore.WHITE + Style.BRIGHT + url + Fore.GREEN + Style.BRIGHT + " Found" + Fore.WHITE + "  |" + Fore.BLUE + "  Status Code:" + Fore.GREEN + " " + Fore.WHITE +  str(code) + "  |" + Fore.WHITE + "  Response Size: " + str(size))
        else:
            print(Fore.WHITE + Style.BRIGHT + url + Fore.RED + Style.BRIGHT + " Not Found" + Fore.WHITE + "  |" + Fore.BLUE + "  Status Code:" + Fore.GREEN + " " + Fore.WHITE +  str(code) + "  |" + Fore.WHITE + "  Response Size: " + str(size))

    except requests.exceptions.RequestException as e:
        print(Fore.WHITE + Style.BRIGHT + url + Fore.RED + Style.BRIGHT + "  ERROR: " + str(e))


def crossdomain(url):
    try:
        headers = {
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:91.0) Gecko/20100101 Firefox/91.0',
        'Accept': "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
        'Accept-Language': 'en-US,en;q=0.5',
        'Accept-Encoding': 'gzip, deflate, br',
        'Connection': 'keep-alive',  
        'Sec-Fetch-Dest': 'document',
        'Sec-Fetch-Mode': 'navigate',
        'Sec-Fetch-Site': 'none',
        'Sec-Fetch-User': '?1',
        'Cache-Control': 'max-age=0'}
        url += "/crossdomain.xml"
        response = requests.get(url, allow_redirects=True, verify=False, headers=headers)
        code = response.status_code
        body = response.content
        size = len(response.content)
        bodyy = str(body)

        if "cross-domain-policy" in bodyy:
            config = True
        else:
            config = False

        if (config == True):
            print(Fore.WHITE + Style.BRIGHT + url + Fore.GREEN + Style.BRIGHT + " Found" + Fore.WHITE + "  |" + Fore.BLUE + "  Status Code:" + Fore.GREEN + " " + Fore.WHITE +  str(code) + "  |" + Fore.WHITE + "  Response Size: " + str(size))
        else:
            print(Fore.WHITE + Style.BRIGHT + url + Fore.RED + Style.BRIGHT + " Not Found" + Fore.WHITE + "  |" + Fore.BLUE + "  Status Code:" + Fore.GREEN + " " + Fore.WHITE +  str(code) + "  |" + Fore.WHITE + "  Response Size: " + str(size))

    except requests.exceptions.RequestException as e:
        print(Fore.WHITE + Style.BRIGHT + url + Fore.RED + Style.BRIGHT + "  ERROR: " + str(e))
    
def opensearch(url):
    try:
        headers = {
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:91.0) Gecko/20100101 Firefox/91.0',
        'Accept': "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
        'Accept-Language': 'en-US,en;q=0.5',
        'Accept-Encoding': 'gzip, deflate, br',
        'Connection': 'keep-alive',  
        'Sec-Fetch-Dest': 'document',
        'Sec-Fetch-Mode': 'navigate',
        'Sec-Fetch-Site': 'none',
        'Sec-Fetch-User': '?1',
        'Cache-Control': 'max-age=0'}
        url += "/opensearch.xml"
        response = requests.get(url, allow_redirects=True, verify=False, headers=headers)
        code = response.status_code
        body = response.content
        size = len(response.content)
        bodyy = str(body)

        if "OpenSearchDescription" in bodyy:
            open = True
        else:
            open = False

        if (open == True):
            print(Fore.WHITE + Style.BRIGHT + url + Fore.GREEN + Style.BRIGHT + " Found" + Fore.WHITE + "  |" + Fore.BLUE + "  Status Code:" + Fore.GREEN + " " + Fore.WHITE +  str(code) + "  |" + Fore.WHITE + "  Response Size: " + str(size))
        else:
            print(Fore.WHITE + Style.BRIGHT + url + Fore.RED + Style.BRIGHT + " Not Found" + Fore.WHITE + "  |" + Fore.BLUE + "  Status Code:" + Fore.GREEN + " " + Fore.WHITE +  str(code) + "  |" + Fore.WHITE + "  Response Size: " + str(size))
    
    except requests.exceptions.RequestException as e:
        print(Fore.WHITE + Style.BRIGHT + url + Fore.RED + Style.BRIGHT + "  ERROR: " + str(e))


if __name__ == "__main__":
    robots(url)
    sitemap(url)
    security(url)
    security_alter(url)
    humans(url)
    pgp(url),wellpgp(url)
    favicon(url)
    broconfig(url)
    crossdomain(url)
    opensearch(url)

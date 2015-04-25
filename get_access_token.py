from instagram.client import InstagramAPI
import sys


# Fix Python 2.x.
try:
    import __builtin__
    input = getattr(__builtin__, 'raw_input')
except (ImportError, AttributeError):
    pass

client_id = '32a5ddcbadd8408b9cca6937ee49df95'
client_secret = '48872a7263db4232a5c48ee61b1945f0'
redirect_uri = 'http://google.com'
raw_scope = False
scope = False
# For basic, API seems to need to be set explicitly
if not scope or scope == [""]:
    scope = ["basic"]

api = InstagramAPI(client_id=client_id, client_secret=client_secret, redirect_uri=redirect_uri)
redirect_uri = api.get_authorize_login_url(scope = scope)

print ("Visit this page and authorize access in your browser: "+ redirect_uri)

code = (str(input("Paste in code in query string after redirect: ").strip()))

access_token = api.exchange_code_for_access_token(code)
print ("access token: " )
print (access_token)
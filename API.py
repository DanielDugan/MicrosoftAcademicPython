import httplib, urllib, base64, json

headers = {
    # Request headers
    'Ocp-Apim-Subscription-Key': '{subscription key}',
}

params = urllib.urlencode({
    # Request parameters
    'expr': '{string}',
    'model': 'latest',
    'count': '10',
    'offset': '0',
    'orderby': '{string}',
    'attributes': 'Id',
})

try:
    conn = httplib.HTTPSConnection('westus.api.cognitive.microsoft.com')
    conn.request("GET", "/academic/v1.0/evaluate?%s" % params, "{body}", headers)
    response = conn.getresponse()
    data = response.read()
    print(data)
    with open('data.txt', 'w') as outfile:
        json.dump(data, outfile, sort_keys = True, indent = 4, ensure_ascii = False)
    conn.close()
    
except Exception as e:
    print("[Errno {0}] {1}".format(e.errno, e.strerror))

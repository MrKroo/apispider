 #!/usr/bin/env python3

import json

def sort_posts():
    
    with open('apispider.txt', 'r') as file:
        json_result = json.loads(file.read())
#        for x in json_result['posts']:
        for x in json_result:
            if x['score'] > 100:
                print(x['url'])

sort_posts()

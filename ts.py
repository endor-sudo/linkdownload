import requests
import re

base="""url before the segment numerator"""
suffix="""url after the segment numerator"""

excerpt=1

while True:
    url=base+str(excerpt)+suffix
    replyobj=requests.get(url,stream=True)
    #stop=re.compile('Not Found') # or request is answered
    if replyobj.text=='Not Found':
        break
    with open('ww.ts','ab') as video:
        for chunk in replyobj.iter_content(100000):#for chunk in replyobj.content():
            video.write(chunk)
    print(f'{excerpt}excerpt downloaded')

    excerpt+=1



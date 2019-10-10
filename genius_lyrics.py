import requests 
from bs4 import BeautifulSoup 
#import sys
#import subprocess
import api_func

from profanity_check import predict, predict_prob


def lyric_params(input_name):
    url2 = api_func.api(input_name)

    #url2= api('Shawn')
    if (url2!=None):
        url1='https://genius.com'
        
        url=url1+url2

        site=requests.get(url).text
        soup=BeautifulSoup(site,'lxml')

        #print(soup.prettify())


        lyric = soup.find('div',{'class':'lyrics'})

        final=lyric.text

        chop=final.split('\n')

        

        chop=[e for e in chop if e not in ('','[Verse 1]','[Verse 2]','[Verse 3]','[Verse 4]','[Verse 5]','[Intro]','[Outro]','[Chorus]','[Pre-Chorus]','[Bridge]','[Refrain]')]
        #print(chop)
        #print(len(chop))

        stick=' '.join(chop)
        #print(stick)

        split=stick.split(' ')
        
        #-------------------------------------profanity-check-----------------
        lyric_list=[]
        lyric_list.append(final)

        #-----print(predict_prob(lyric_list))
    
        tuple_out=(final,len(split),predict_prob(lyric_list))
    else:
        tuple_out=(None,0,None)
    return(tuple_out)
    
    
    


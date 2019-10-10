import requests 
from bs4 import BeautifulSoup 
from nested_lookup import nested_lookup
from difflib import SequenceMatcher


def api(search_in):
    main_api='https://api.genius.com/search?q='
    name=search_in
    api2='&access_token='
    token='' #provide the token here
    
    query= main_api+name+api2+token
    
    link=requests.get(query)
    
    #bsp=BeautifulSoup(link,'lxml')
    
    #print(bsp.prettify())
    
    #para=bsp.findAll('p')
    
    #out=para[0].json()
    
    #print(out['meta'])
    
    #print(para)
    
    out=link.json()
    #print(type(out))
    path=nested_lookup('path', out)
    
    if len(path)!=0:
        compare_1=((nested_lookup('full_title',out))[0].split('('))[0]
        #compare_1=(nested_lookup('full_title',out))[0]       
        prob_val=SequenceMatcher(None,compare_1,name).ratio()  #edited it to match with the string only outside brackets 
        
        first_word=((nested_lookup('full_title',out))[0].split(' '))[0]
        second_word=(name.split(' '))[0]
    
        if len(path)==1:
            if prob_val>0.5:
                url2=path[0]        
            elif first_word==second_word:
                url2=path[0]
            else:
                url2=None
            
        else:
            compare_2=((nested_lookup('full_title',out))[1].split('('))[0]
            prob_val2=SequenceMatcher(None,compare_2,name).ratio()
            if prob_val>0.5:
                url2=path[0]  
            elif first_word==second_word:
                url2=path[0]
            elif prob_val2>0.5:
                url2=path[1]
            else:
                url2=None
                   
    else:
        url2=None
        
    
    #print(path[0])
    
    return url2






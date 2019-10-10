import time 
start_time=time.time()
import requests
from bs4 import BeautifulSoup
import pandas as pd
import genius_lyrics

wiki=requests.get('https://en.wikipedia.org/wiki/Grammy_Award_for_Song_of_the_Year').text
soup=BeautifulSoup(wiki,'lxml')
#print(soup.prettify())

my_table = soup.find('table',{'class':'wikitable sortable'})

#print(my_table.prettify())

#--------------------Creating Nominations table------------------
links=my_table.findAll('li')

Nomin_songs=[]
Performers=[]

for single in links:
	record=(single.text)
	Nomin_songs.append(record.split('"')[1])
	Performers.append(record.split('by')[1])

#print(Nomin_songs)
#print(Performers) 	


Nominations=pd.DataFrame(list(zip(Nomin_songs,Performers)),columns=['Song','Performer'])

#print(Nominations)

#---------------------Creating Winners table----------------------
Win_songs=[]
Win_perform=[]
Year=[]

rows=my_table.findAll('tr')
id_2=0
for row in rows:
    if id_2 >0:
        year= row.findAll('th')
        year_act=(year[0].text).split('\n')
        Year.append(year_act[0])
        
    id_2+=1
    
    colum= row.findAll('td')
    id=-1
    for col in colum:
                       
         if id==1:
             Win_songs.append(col.text.split('"')[1])
         if id==2:
             Win_perform.append(col.text.split('\n')[0])
         id=id+1
    
     	
#print(Win_songs)
#print(Win_perform)

Winners=pd.DataFrame(list(zip(Year,Win_songs,Win_perform)),columns=['Year','Song','Performer'])

#print(Winners)

#-----------------------Attributes for Winners table--------------------
lyrics=[]
lyric_length=[]
profane_prob=[]
for x in range(61):
    print(x)
    final_out=genius_lyrics.lyric_params(Winners.iloc[x,1]+' '+Winners.iloc[x,2])
    lyrics.append(final_out[0])
    lyric_length.append(final_out[1])
    profane_prob.append(final_out[2])
    
Winners['Lyrics']= lyrics
Winners['Length']=lyric_length
Winners['Profanity']=profane_prob


#final_out=genius_lyrics.lyric_params(Winners.iloc[52,1]+Winners.iloc[52,2])
#print(final_out[0])


#--------------------------------Attributes for Nominee Table---------------
size_nom=Nominations.shape[0]
lyrics2=[]
lyric_length2=[]
profane_prob2=[]
for y in range(size_nom):
    print(y)
    final_out2=genius_lyrics.lyric_params(Nominations.iloc[y,0]+' '+Nominations.iloc[y,1])
    lyrics2.append(final_out2[0])
    lyric_length2.append(final_out2[1])
    profane_prob2.append(final_out2[2])
    
Nominations['Lyrics']= lyrics2
Nominations['Length']=lyric_length2
Nominations['Profanity']=profane_prob2


print("----%s seconds" %(time.time()-start_time))




import urllib2
from bs4 import BeautifulSoup
import calendar
     
year = input("Enter the Year: ")
f_name = "%d_words.txt" % year
f = open(f_name, "w")
word_count= 0
     
for month in range(1, 13):
        weeks, days = calendar.monthrange(year, month)
        #print days
        for date in range(1, days+1):
            #print date
            day = "%s/%02d/%02d" % (year, month, date)
            #print day
            limit = 0
            while limit<10:
                try:
                    url = r"http://dictionary.reference.com/wordoftheday/%s" % day 
                    page = urllib2.urlopen(url)
                    if page.geturl() == r"natter Word of the Day | Dictionary.com": 
                        print "No Words Further..."
                        import sys
                        sys.exit(1)
                    word = page.geturl().split('/')[-1].replace('%20', ' ')
                    word_count += 1
                    break
                    
            #print day, word
                except urllib2.URLError, e:
                    limit+=1
                    print "URL does not exists",e
                
            if page:
                data = BeautifulSoup(page, "html.parser")
                word_data = data.find("div", class_="definition-box")
                words = word_data.findAll("li")
                f.writelines(word+"\n")
                print day, word
                for i, w in enumerate(words):
                    line = ("\t%d. " % (i+1) +w.text)
                    print line
                    try:
                        f.writelines(line+"\n")
                    except TypeError:
                        continue
                f.writelines("\n")
                print                
                    
     
f.close()
print word_count

import requests

def get_page(url, x):
    r = requests.get(url)
    print r.status_code
    content = r.text.encode('utf-8', 'ignore')
    with open("test"+x+".html", "w") as fp:
        fp.write(content)
        
        
if __name__ == "__main__":
	#url = 'https://github.com/adafruit'
	#get_page(url,str(1))            

	for x in range(1,12):
   		url = 'https://github.com/adafruit?page='+str(x)
    		get_page(url, str(x))  

	          


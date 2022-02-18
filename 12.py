from urllib.request import Request, urlopen
import json

def toBinary(a):

  a = bin(int(a, 16))
  maxzeroes = 0
  maxones = 0
  zeroes = a.split("1")
  ones = a.split("0")

  for i in zeroes:
   if len(i) > maxzeroes:
    maxzeroes = len(i)
  for i in ones:
   if len(i) > maxones:
    maxones = len(i)

  print("The longest sequence of zeroes is: ",maxzeroes)
  print("The longest sequence of ones is: ", maxones)

def RandomToString(Round2,Luck2):

 for i in range(1,100):

     req = Request('https://drand.cloudflare.com/public/' + str(Round2-1), headers={'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:31.0) Gecko/20130401 Firefox/31.0'})
     data = urlopen(req).read()
     keys = json.loads(data.decode('utf-8'))
     Round2=keys['round']
     Luck2=Luck2+keys['randomness']
 toBinary(Luck2)


req = Request('https://drand.cloudflare.com/public/latest', headers={'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:31.0) Gecko/20130401 Firefox/31.0'})
data = urlopen(req).read()
keys = json.loads(data.decode('utf-8'))
Round = keys['round']
Luck=keys['randomness']
RandomToString(Round,Luck)
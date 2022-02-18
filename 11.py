from urllib.request import Request, urlopen
import json
from scipy.stats import entropy as en
import pandas as pd


def MyEntropy(a):
    a = str(int(a, 16))
    sixteenlist = []
    for i in a:
        sixteenlist.append(i)
    entropy = pd.Series(sixteenlist)
    entropy2 = en(entropy.value_counts())
    print("Entropy is : ", entropy2)

def RandomToString(Round2,Luck2):

 for i in range(1,20):

     req = Request('https://drand.cloudflare.com/public/' + str(Round2-1), headers={'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:31.0) Gecko/20130401 Firefox/31.0'})
     data = urlopen(req).read()
     keys = json.loads(data.decode('utf-8'))
     Round2 = keys['round']
     Luck2 = Luck2+keys['randomness']
 MyEntropy(Luck2)


req = Request('https://drand.cloudflare.com/public/latest', headers={'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:31.0) Gecko/20130401 Firefox/31.0'})
data = urlopen(req).read()
keys = json.loads(data.decode('utf-8'))
Round = keys['round']
Luck = keys['randomness']
RandomToString(Round,Luck)
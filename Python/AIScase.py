import random
type1 = ["Employee","Customer","VIP"]
package = ["199","299","399","499","599","699","799","899","999","1099","1499","1699","1899","2099"]


f = open('test2.csv','w')

for i in range(20):
    CusAge = random.randint(0,50)
    CusSpend = random.randint(0,10000000)
    CusType = random.choice(type1)
    CusPackage = random.choice(package)
    writestr = str(CusAge)+","+str(CusSpend)+","+CusType+","+CusPackage+"\n" 
    print(f.write(writestr))

f.close()
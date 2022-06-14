import random
type1 = ["Employee","Customer","VIP"]
package = ["199","299","399","499","599","699","799","899","999","1099","1499","1699","1899","2099"]

for i in range(2,100):
    filename = "AISCase/Customer_Branch_"+str(i)+".csv"
    print(filename)
    f = open(filename,'a')
    for j in range(100):
        CusAge = random.randint(0,50)
        CusSpend = random.randint(0,10000000)
        CusType = random.choice(type1)
        CusPackage = random.choice(package)
        writestr = str(CusAge)+","+str(CusSpend)+","+CusType+","+CusPackage+"\n" 
        print(f.write(writestr))
    f.close()
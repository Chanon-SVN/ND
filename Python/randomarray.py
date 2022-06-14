import random
type1 = ["Employee","Customer","VIP"]
package = ["199","299","399","499","599","699","799","899","999","1099","1499","1699","1899","2099"]
CusType = random.choice(type1)
CusPackage = random.choice(package)

for i in range(5):
    CusType = random.choice(type1)
    CusPackage = random.choice(package)
    print(CusType)
    print(CusPackage)
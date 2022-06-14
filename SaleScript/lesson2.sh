 
cd AISCase
for ((a=1; a <= 100 ; a++ ))
do
    Filename="Customer_Branch_"$a
    touch $Filename.csv
    echo "Age,Spent,Type,Package,Class" > $Filename.csv
done
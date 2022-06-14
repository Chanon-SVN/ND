for ((a=1; a <= 5 ; a++ ))
do
    Filename="Niddeaw"$a
    echo $Filename
done

cd Mak
touch aistest.csv
echo "class,age,spent,type,packsage" > aistest.csv
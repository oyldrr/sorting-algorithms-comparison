# sorting-algorithms-comparison
Python programlama dili kullanılarak Bubble sort, Selection sort, Insertion sort, Quick sort sıralama algoritmalarının hızlarının karşılaştırılması. 

Sıralama Algoritmalarının Karşılaştırılması
Python programlama dili kullanılarak Bubble sort, Selection sort, Insertion sort, Quick sort sıralama algoritmalarının hızlarının karşılaştırılması. 
Algoritmaların Python Programları

Buble Sort Algoritması

 ![image](https://user-images.githubusercontent.com/84236077/215782599-e0057771-4722-456d-89a4-d593b79b558e.png)

Selection Sort Algoritması 

![image](https://user-images.githubusercontent.com/84236077/215782639-ec904ddc-662b-4858-a5bf-2b9e5f51ad25.png)

Insertion Sort Algoritması

 ![image](https://user-images.githubusercontent.com/84236077/215782668-187ff231-e851-4558-ac80-ddbd043ab71f.png)

Quick Sort Algoritması

![image](https://user-images.githubusercontent.com/84236077/215782706-63e79a94-1870-422d-9343-67b5ec207a24.png)

  
Kodlar geeks for geeks sitesi üzerinden alınmıştır. Ancak daha fazla veri girebilmek için üzerinde değişiklikler yapılmıştır. list(range()) fonksiyonu kullanarak istenilen miktarda dizi üretilebilmekte ve dahil edilen random kütüphanesinin shuffle() fonksiyonu ile bu diziler karıştırılabilmekte. Bu sayede istenilen uzunlukta rastgele düzende diziler oluşturulabiliyor. Algoritmalar arasında karşılaştırmalar yapılırken 1.000, 10.000, 100.000 elemanı elle girmeye gerek kalmadan karşılaştırmalar yapabiliyoruz.
	Ayrıca python programlarının ne kadar sürede çalıştığını öğrenmek için terminal üzerinde “python -m cProfile <python dosyası>” kodunu kullanıyoruz. Bu kod program bittiğinde her bir fonksiyonun ne kadar sürede çalıştığını gösteriyor
 
 ![image](https://user-images.githubusercontent.com/84236077/215782750-6e1440b2-8cfb-4386-822d-209f341b9c86.png)

Yukarıdaki tabloda algoritmaların 1.000, 10.000, ve 100.000 elemanlı dizilerde ne kadar sürede sıralama yaptığı gösterilmiştir. Denemelerde diziler tamamen rastgele üretildiği için her bir deneme diğerinden farklı sonuçlar verebilir ancak çıkacak değerler yine de tablodakilere yakın olacaktır. 
Tabloda görüldüğü üzere Quick Sort algoritması diğer algoritmalara göre çok daha hızlı sürede sıralama işlemi yapabilmektedir. Düşük sayıda verilerde bu fark çok da anlaşılmasa da veri sayısı arttıkça aradaki fark da giderek artıyor.

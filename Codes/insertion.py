# Insertion Sort algoritmasının python programı olarak uygulanması

import random # Random kütüphanesinin dahil edilmesi

# Sıralama işleminin uygulanacağı fonksiyon
def insertionSort(arr):
	for i in range(1, len(arr)):
		key = arr[i]
		j = i-1
		while j >=0 and key < arr[j] :
				arr[j+1] = arr[j]
				j -= 1
		arr[j+1] = key


arr = list(range(1000)) # 0'dan başlayarak içine girilen değere kadar
						# artan düzende dizi oluşturma

random.shuffle(arr) # Oluşturulan sıralı diziyi rastgele şekilde karıştırma

print("Unsorted array : ", arr) # Karıştırılan diziyi ekrana yazdırma
print("-"*100) # Çizgi çekmek için kullanılan kod (Gerekli değil)
insertionSort(arr) # Sıralama işlemi için fonksiyonu çağırma
print("Sorted array : ", arr) # Sıralanmış diziyi ekrana yazdırma


# Selection Sort algoritmasının python programı olarak uygulanması

import random # Random kütüphanesinin dahil edilmesi

# Sıralama işleminin uygulanacağı fonksiyon
def selectionSort(array, size):
	
	for ind in range(size):
		min_index = ind

		for j in range(ind + 1, size):
			if array[j] < array[min_index]:
				min_index = j
		(array[ind], array[min_index]) = (array[min_index], array[ind])

arr = list(range(100000)) # 0'dan başlayarak içine girilen değere kadar
						# artan düzende dizi oluşturma

random.shuffle(arr) # Oluşturulan sıralı diziyi rastgele şekilde karıştırma

size = len(arr) # Dizinin uzunluğunu bir değişkene atama

print("Unsorted array", arr) # Karıştırılan diziyi ekrana yazdırma
print("-"*100) # Çizgi çekmek için kullanılan kod (Gerekli değil)
selectionSort(arr, size) # Sıralama işlemi için fonksiyonu çağırma
print('Sorted array:', arr) # Sıralanmış diziyi ekrana yazdırma


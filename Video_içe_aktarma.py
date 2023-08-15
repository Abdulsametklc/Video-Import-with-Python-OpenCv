import cv2
import time #zaman işlemleri yapmak için kullanılır.

# video ismi
video_name ="MOT17-04-DPM.mp4"

#video içe aktar: capture, cap
cap = cv2.VideoCapture(video_name) #bu fonksiyon video yakalma nesnesi oluşturmamızı sağlar. Bu nesne, videonun çerçevelerini okumak ve işlemek için kullanılır.

#videonun genişliğini ve yüksekliğini alıp ekrana yazdırır.
print("Genişlik:", cap.get(3)) 
print("Yükseklik:", cap.get(4))

#fonksiyon, video yakalama nesnesinin başarılı bir şekilde oluşturulup oluşturulmadığını kontrol eder. Eğer nesne başarılı bir şekilde oluşturulamamışsa, "Hata" yazdırılır.
if cap.isOpened() == False:
    print("Hata")

"""Bu kısım bir döngü oluşturur. 
Döngü, videodan çerçeveleri okuyarak ve her çerçeveyi görüntüleyerek devam eder. 
cap.read() fonksiyonu, videodan bir çerçeve okur ve ret değişkeni True ise okuma başarılı olmuş demektir. 
Bu çerçeveyi frame değişkenine atar ve cv2.imshow() fonksiyonuyla çerçeveyi görüntüler."""
while True:
  ret, frame = cap.read()

  if ret == True:
    
    time.sleep(0.01) #☺uyarı: kullanmaz isek çok hızlı akar.
    
    cv2.imshow("Video",frame)
    
  else: break 

  if cv2.waitKey(1) & 0xFF ==ord("q"):
      break #q tuşuna basılırsa döngü sonlanır.
  
cap.release()
#Döngü sonlandığında, cap.release() fonksiyonu video yakalama nesnesini serbest bırakır ve kaynakları geri alır. 
cv2.destroyAllWindows()
#cv2.destroyAllWindows() fonksiyonu ise tüm açık olan pencereleri kapatır.



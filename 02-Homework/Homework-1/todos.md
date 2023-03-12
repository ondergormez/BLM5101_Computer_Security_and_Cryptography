# Yapılabilecek İyileştirmeler

# 1
TODO: Hatalı bir çalışma var aşağıdakinden anlayabilirsin
önder
önder görmez hello aaaaaaaaaaaaaaaaaa

Ortaya çıkacak grafiklerden de anlaşılacağı üzere

# 2
TODO: Post processing için ile, ve gibi şeyleri verebileceğimiz bir alan ekle.

# 3
TODO: Accuracy hesaplamada hata var. 
aşağıdaki inputlarla %0 çıkması lazım bence. Yine de bi kontrol et

Önemli Not: boşluklarda hesaplamaya dahil edildikleri için tüm harfler yanlış olsada sıfırdan farklı bir match yakanabilir. Bun ortadan kaldırmak için girişteki boşluklar silinerek hesaplamalara dahil edilmeyebilir. Yada sadece accuracy hesaplama fonksiyonu white space leri discard edebilir.

Önemli Not: Harf listesini koy. Büyük küçük harfe bakmadan şifrelemeyi yapıyor. (Türkçe + İngilizce karakter seti)

# 4
TODO: Referans içerisinde bulunan kelime sayısı plaintext metin sayısından az olması durumunda veya tekrar ettiği için bar chart taki harf sayısı az odluğu durumda hata vermeyecek şekilde düzenlemeler yapılmalıdır.
Örnek:
Plaintext: Hello how are you?
Reference: aaaabc

TODO: Non karakter olanları işleme dahil etme. Çünkü onlar cipher text kısmına da dahil edilmiyorlar
TODO: Fazla olan harflere göre sıralayacak şekilde değişiklikler yapılmalıdır.

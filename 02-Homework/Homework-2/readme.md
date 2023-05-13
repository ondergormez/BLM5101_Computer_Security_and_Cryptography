# Requirements

```sh
onder@Dell:~/.../...Crypto...$ sudo apt install python3
onder@Dell:~/.../...Crypto...$ pip3 install gradio
onder@Dell:~/.../...Crypto...$ pip3 install notebook
onder@Dell:~/.../...Crypto...$ pip3 install opencv-python
```

# Presentations

[Discrete Least Significant Bit (LSB) Substitution](docs/Discrete_Least_Significant_Bit_Substitution.pdf)

# Flow Chart

* Kaç tane aralarında asal sayı olduğu bulunur. örneğin 8
* bunlardan biri sayıya kadar olan modları sağlayan seçilir. örneğin 3
* Bunun asal olan tüm elemanlar ile 3^.. mod 17 = en büyük olacak şekilde seçim yapılır. Örneğin 15
* yi = 14^i mod 17 ye göre gizleme işlemi gerçekleştirilir.


# Simple Flow Chart
![](images/SimpleFlowChart.drawio.svg)


# Original and Data Hidden Images
![](images/original_and_data_hidden_images.png.svg)


# Sunum Adımları

* İlk önce sonuç imajını göster. sunuma koy.
* Gönderilecek olan metnin önüne header ekleniyor. Örn: 000005Hello
* Bit çevrimini doğrula. 
  * [Text to Binary Converter](https://www.rapidtables.com/convert/number/ascii-to-binary.html)
  * [ASCII, Hex, Binary, Decimal, Base64 converter](https://www.rapidtables.com/convert/number/ascii-hex-bin-dec-converter.html)

# Feature Works (Nice to Have)

* Gelen mesajde okunan ilk 6 karakterin gerçekten sayı olup olmadığını kontrol etmek için, başına ve sonuna birer karakter eklenir. Örn: ##000005##Hello gibi. Böylelikle hatalı bir mesaj gelirse daha geldiği anda işlemler kesilir.
* Girilen metin uzunluğu imajın saklayabilecek metin uzunluğundan fazla ise kullanıcıya uyarı verilebilir. İşlem kesilebilir.


# Sunum
TODO: [Sunum](presentation.pdf)


# References
https://en.wikipedia.org/wiki/Symmetric-key_algorithm
https://en.wikipedia.org/wiki/Public-key_cryptography
https://www.flaticon.com/free-icon/demo_5110617?term=demo&page=1&position=5&origin=search&related_id=5110617


# TODOs
- [ ] Slaytların başlıklarını kontrol et: Basics of Cryptology
- [ ] Başlıkların büyük küçük harf olması durumunu kontrol et.
- [ ] Referansları eklemeyi unutma
- [ ] Online DES linki ekle
- [ ] Online AES linki ekle
- [ ] Online RSA linki ekle
- [ ] Kendi yaptığımız uygulamayı göster
- [ ] Enes in ismini bir yerlerde geçir ve atıf yap.
- [ ] OpenSSL gibi toolar ile nasıl key oluşturuluyor? Bu gösterilebilir.

# DES Encryption/Decryption

## DES Encyrtion Steps

* Generate Key (8 byte): https://www.browserling.com/tools/random-hex
    * Sample Key: 51a01840dc796c3a
* ASCII to Hex Conversion: https://www.rapidtables.com/convert/number/ascii-to-hex.html
    * Sample Message: Hello AI
    * Sample Message as Hex: 48656C6C6F204149
* Encrypted Text: 1B3B8256B4364C02
    * https://neapay.com/online-tools/des-calculator.html?data=48656C6C6F204149&key=51a01840dc796c3a&algo=DES&decr=false


## DES Decryption Steps

* Sample Key: 51a01840dc796c3a
* Encrypted Text: 1B3B8256B4364C02
* Plain Text: 48656C6C6F204149
    * https://neapay.com/online-tools/des-calculator.html?data=1B3B8256B4364C02&key=51a01840dc796c3a&algo=DES&decr=true
* Hex to ASCII Conversion: https://www.rapidtables.com/convert/number/hex-to-ascii.html

# AES Encryption/Decryption

## AES Encyrtion Steps
* https://www.javainuse.com/aesgenerator
    * Sample Key: aesEncryptionKey
    * Sample Message: Hello AI
    * Encrypted Text: e5d8f0e051ab96f30b6953ac70da2f51
    
## AES Decryption Steps
* https://www.javainuse.com/aesgenerator
    * Sample Key: aesEncryptionKey
    * Encrypted Text: e5d8f0e051ab96f30b6953ac70da2f51
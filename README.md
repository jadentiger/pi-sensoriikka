# 🌡️ Sense HAT – Ympäristöanturi Projekti

**Tekijä:** Jaden Brower  
**Alusta:** Raspberry Pi + Sense HAT  
**Tavoite:** Ympäristöolosuhteiden mittaaminen ja integrointi robottijärjestelmään (Unitree Go2)

---

## 📌 Projektin kuvaus
Tämä projekti käyttää Raspberry Pi -alustaa ja Sense HAT -lisäkorttia ympäristöolosuhteiden mittaamiseen. Järjestelmä mittaa lämpötilaa, ilmankosteutta ja ilmanpainetta, sekä näyttää ja jakaa datan eri tavoilla.

Lopullisena tavoitteena on integroida järjestelmä osaksi robottikoiraa, jolloin se voi toimia liikkuvana ympäristösensorina.

---

## 🎯 Ominaisuudet
- Lämpötilan mittaus (°C)
- Ilmankosteuden mittaus (%)
- Ilmanpaineen mittaus (hPa)
- CPU-lämpötilan kompensointi
- Mittausarvojen tasoitus (smoothing)
- LED-matriisin visuaalinen näyttö
- Web-sovellus reaaliaikaiseen seurantaan
- 3D-tulostettu suojakotelo

---

## 🧠 Projektin rakenne
Projektissa on kolme pääosaa:
- ympäristöantureiden mittaus
- LED-visuaalinen näyttö
- Flask-pohjainen web-sovellus

Osat toimivat tällä hetkellä erillisinä, mutta tavoitteena on yhdistää ne yhdeksi järjestelmäksi.

---

## ⚙️ Laitteisto
- Raspberry Pi
- Sense HAT
- 3D-tulostettu kotelo
- (tulevaisuudessa) Unitree Go2 -robottikoira

---

## 📊 Mittaustarkkuus ja rajoitukset

Tämä projekti on hyvä esimerkki siitä, miten sulautettu järjestelmä voi toimia kokonaisena ympäristön mittausratkaisuna. Se kattaa datan keruun, käsittelyn ja esittämisen sekä paikallisesti että verkon kautta.

### ⚠️ Lämpötilamittauksen rajoitukset
Sense HAT -lämpötila-anturi ei ole täysin tarkka, koska se sijaitsee lähellä Raspberry Pi -prosessoria. Prosessori tuottaa lämpöä, joka voi nostaa mitattua arvoa.

Tästä seuraa:
- lämpötila voi olla hieman liian korkea
- arvot voivat vaihdella nopeasti
- tarkkuus ei ole laboratoriotason mittalaite

---

### 📉 Keskiarvoistus ja parannukset
Yksi tärkeimmistä parannuksista on **pitkän aikavälin keskiarvon käyttö**.

Kun mittauksia kerätään jatkuvasti ja niistä lasketaan keskiarvo, tuloksista tulee:
- tasaisempia
- vähemmän herkkiä satunnaisille piikeille
- lähempänä todellista ympäristön lämpötilaa

---

### 📈 Käytetyt parannustekniikat
Paras lopputulos saavutetaan yhdistämällä:
- CPU-lämpötilan kompensointi
- lyhyen aikavälin smoothing
- pitkän aikavälin keskiarvoistus

Tämä tekee järjestelmästä huomattavasti luotettavamman.

---

## 💡 LED-visualisointi
Lämpötila näytetään väreillä:
- 🔵 Sininen = kylmä
- 🟢 Vihreä = normaali
- 🔴 Punainen = kuuma

---

## 🌐 Web-sovellus
Web-sovellus näyttää reaaliaikaisesti:
- lämpötila
- kosteus
- ilmanpaine

Ominaisuudet:
- automaattinen päivitys
- selainkäyttö
- mahdollisuus etäkäyttöön

---

## 🧩 Haasteet ja ratkaisut

### 🔥 CPU-lämpö
- Ongelma: vääristää lämpötilaa  
- Ratkaisu: ohjelmallinen kompensointi  

### 📉 Mittausvaihtelu
- Ongelma: epävakaat arvot  
- Ratkaisu: keskiarvoistus  

### 🔌 Laitteen tunnistus
- Ongelma: Sense HAT ei aina toiminut  
- Ratkaisu: uudelleenasennus ja reboot  

---

## 📈 Tulokset
- Tarkkuus parani merkittävästi
- Lämpötilaero pieneni ~3°C → ~0.5–1°C
- Mittaukset ovat riittävän tarkkoja robotiikkakäyttöön

---

## 🚀 Tulevaisuuden kehitys
- Datan tallennus (CSV / tietokanta)
- Lisää antureita
- Web-käyttöliittymän parannus
- Langaton etäkäyttö
- Integraatio Unitree Go2 -robotin kanssa

---

## 🧠 Opitut asiat
- CPU-lämpö vaikuttaa antureihin
- Datan suodatus on välttämätöntä
- Iteratiivinen kehitys toimii parhaiten
- IoT-järjestelmät koostuvat useista kerroksista

---

## 👨‍💻 Yhteenveto
Projektissa rakennettiin toimiva ympäristön mittausjärjestelmä Raspberry Pi Sense HAT -alustalle.

Se osoittaa, miten anturidata voidaan:
- mitata
- korjata
- visualisoida
- ja jakaa verkon kautta

Lopullinen tavoite on yhdistää kaikki osat yhdeksi järjestelmäksi, joka toimii osana robottikoiraa ja reaaliaikaista ympäristön havainnointia.

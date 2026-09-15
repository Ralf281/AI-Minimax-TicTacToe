# Arenduspäevik

## 15.09.2026 – Etapp 1

**Eesmärk:**
Luua Pythonis lihtne käsureal töötav trips-traps-trull.

**Kasutatud tehisaru:**
ChatGPT

**Viip:**
„Loo Pythonis lihtne käsureal töötav trips-traps-trull.“

**Tulemus:**
Tehisaru genereeris Pythonis töötava mängu, kus mängija mängib arvuti vastu. Programm kuvab mängulaua, võimaldab mängijal valida käigu ning kontrollib võitu ja viiki.

**Testimine:**
Mängu oli võimalik edukalt läbi mängida. Mängija sai valida vaba koha numbrite 1–9 abil ning programm takistas hõivatud koha uuesti valimist. Programm tuvastas ka võidu ja viigi.

**Ebaõnnestumised/probleemid:**
Esimeses versioonis ei mänginud arvuti strateegiliselt, vaid valis lihtsalt esimese vaba koha. See on järgmises etapis eesmärgiks parandada.

**Muljed:**
Esimene versioon oli lihtne ja töötas ootuspäraselt. Järgmiseks tuleb muuta arvuti targemaks, kasutades Minimax-algoritmi.


## 15.09.2026 – Etapp 2: Minimax-algoritm

**Eesmärk:**
Muuta arvuti mängukäike targemaks, kasutades Minimax-algoritmi.

**Kasutatud viip:**
„Lisa olemasolevale Pythonis kirjutatud trips-traps-trulli mängule Minimax-algoritm, nii et arvuti valiks võimalikult hea käigu. Ära kirjuta kogu programmi nullist, vaid muuda olemasolevat koodi. Selgita ka, kuidas Minimax töötab.“

**Muudatused:**
Olemasolevat programmi ei kirjutatud täielikult ümber. Muudeti `computer_move()` funktsiooni ning lisati `minimax()` funktsioon. Ülejäänud mänguloogika jäi samaks.

**Testimise tulemus:**
Mängisin mängu uuesti läbi. Arvuti suutis minu võidukat käiku takistada ning mäng lõppes viigiga. See näitas, et Minimax-algoritm töötab ja arvuti teeb nüüd varasemast strateegilisemaid käike.

**Mulje:**
Minimax muutis arvuti mängimise oluliselt paremaks. Esimeses versioonis valis arvuti lihtsalt esimese vaba koha, kuid nüüd analüüsib ta võimalikke mängukäike.


## 15.09.2026 – Etapp 3: Arvutus- ja mäluressursside analüüs

**Eesmärk:**
Kontrollida, kas Minimax-algoritmi oleks trips-traps-trulli puhul vaja optimeerida ning hinnata programmi arvutus- ja mälukasutust.

**Kasutatud viip:**
„Analüüsi minu olemasoleva trips-traps-trulli mängu Minimax-algoritmi arvutus- ja mälukasutust. Kas selle programmi puhul on optimeerimine tegelikult vajalik? Kui ei ole, põhjenda miks. Kui on, paku välja võimalikud optimeerimisvõimalused, kuid ära muuda veel koodi.“

**AI analüüs:**
Tehisaru hinnangul ei ole praeguse programmi optimeerimine vajalik. Trips-traps-trulli mängul on ainult üheksa mänguvälja ning võimalike käikude arv on piiratud. Minimax suudab võimalikke mängukäike piisavalt kiiresti läbi analüüsida ning mälukasutus on samuti väike.

**Otsus:**
Optimeerimist praegu ei rakendatud, sest see ei annaks nii väikese mängu puhul olulist praktilist kasu.

**Tulemus:**
Programm jäeti muutmata. 


## 15.09.2026 – Etapp 4: Programmi testimine

**Eesmärk:**
Kontrollida, kas olemasolev trips-traps-trulli programm töötab erinevates olukordades korrektselt.

**Kasutatud viip:**
„Analüüsi minu olemasolevat trips-traps-trulli programmi ja paku välja konkreetsed testid, millega kontrollida, kas mäng töötab korrektselt. Ära muuda veel koodi. Testid peaksid hõlmama vigast sisendit, hõivatud mänguvälja, mängija võitu, arvuti võitu, viiki ning olukorda, kus Minimax peab mängija võidukäigu blokeerima.“

**Testimine:**
Testisin programmi järgmistes olukordades:

* vigane sisend;
* juba hõivatud mänguvälja valimine;
* mängija võit;
* arvuti võit;
* viik;
* olukord, kus Minimax peab mängija võidukäigu blokeerima.

**Tulemus:**
Kõik testid läbisid edukalt. Programm käitus kõigis kontrollitud olukordades nii, nagu oli oodatud. Vigase sisendi ja hõivatud mänguvälja puhul ei jooksnud programm kokku ning Minimax suutis mängija võidukäigu blokeerida.

**Järeldus:**
Testimise tulemusena ei leitud programmist vigu ning koodi ei olnud vaja muuta.


## 15.09.2026 – Etapp 5: Koodi lõplik ülevaatus

**Eesmärk:**
Kontrollida AI abil olemasoleva programmi koodi loetavust, ülesehitust ja võimalikke praktilisi probleeme.

**Kasutatud viip:**
„Vaata üle minu olemasolev trips-traps-trulli programm. Hinda koodi loetavust, ülesehitust ja võimalikke vigu. Ära muuda koodi. Too välja ainult sellised probleemid või parendusettepanekud, millel oleks selle väikese projekti puhul päriselt praktiline kasu.“

**AI analüüs:**
Tehisaru hinnangul on programm väikese projekti jaoks hästi üles ehitatud ja loetav. Erinevad ülesanded on jaotatud eraldi funktsioonidesse ning Minimax-algoritm töötab korrektselt.
AI tõi välja mõned väiksemad võimalikud parandused, näiteks korduvate väärtuste ("X" ja "O") koondamise ning winning_combinations loendi loomise ainult ühe korra.

**Otsus:**
Koodi ei muudetud, sest leitud punktid ei tekita praeguses programmis praktilisi probleeme. Trips-traps-trull on väga väike mäng ning olemasolev Minimax töötab piisavalt kiiresti ja kasutab vähe mälu.

**Tulemus:**
Programmi lõplikul ülevaatusel olulisi vigu ei leitud. Koodi muudatusi ei olnud vaja teha ning programm jäi samasse toimivasse seisundisse.
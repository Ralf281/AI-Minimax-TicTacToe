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

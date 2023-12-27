# FCSC2023
## Challenge de l'ANSSI à l'Hackopole rassemblant les résolutions d'années passées depuis 2019 à 2023.

### Le défi présent est dans le dossier intro et a été taggué en Crypto. Or, sa résolution s'en passe :

   ### 1. intro
   
* Clair connu

 - code source en python3 sans les imports pour simplifier
 - exécution en ligne de commande : python3 clair-connu.py
 - localisation en local du fichier de sortie : output.txt

**Le flag à trouver débute par la clé des 4 lettres :"FCSC". Il s'agit d'en déduire la suite "y".**
On prend en compte le tableau de caractères du fichier sortie et devine la clé rétroactivement.
On fait XOR FCSC avec 4 premières lettres du fichier : on a 8 premiers caractères HEX de la clé.
"FCSC" = "d91b7023" XOR "y" d'où "d91b7023" = "FCSC" XOR "y" d'où "y" = "d91b7023" XOR "FCSC".
La clé fait 140 caractères HEX soit 70 lettres. Deux paires de lettres HEX constituent 1 octet.
On n'a plus qu'à répeter 20 fois les 4 lettres : or, on en obtient 80 ; c'est trop long de 10.
L'opération XOR est réitérée au niveau du bit pour combiner les octets appariés de 2 tableaux.
On découpe le tableau résultant, de sorte à ne retenir que 70 lettres, soit 140 caractères HEX.
**Le flag en est obtenu :FCSC{3ebfb1b880d802cb96be0bb256f4239c27971310cdfd1842083fbe16b3a2dcf7}**

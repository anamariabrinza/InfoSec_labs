# Laboratory work nr 3
## Objectives
The main objective of this work is to crack the shift cipher, plain and simple. There are two approaches that can be used to "break the code":
* Frequency Analysis
* Dictonary attack 

## Implimentation 
In order to "break the code" I implimented the Frequency analysis approach. 
The basic concept of Frequency Analysis is based on fining out the most frequent character/letter.
Once we are aware of the language the message was encrypted, the whole algorithm is the following: 
* first of all we identify the most frequent letter in the message 
* secondly we determine the key used (right or left shift), knowing the used language.
* in the end the shift is performed and the original message is decrypted 

In order to count the letters in the initial message, a dictionary was initiated.
The following code shows how the most frequent letter was determined:
~~~~
for k, v in d.items():
    if v == max(numbers):
        MF = k #finding out the most frequent letter
~~~~
So, we go through all the pairs of the created dictionary (consisted of key-letter and value-number of occurrences)
and assign the most frequent letter to MF variable. 

The most frequent letter in English is E, therefore keeping that in mind we can determine 
the shift value. 

The next step is to perform the shift and decrypt the message. 

In the end we print out the original message, the next image shows the results.
![img](http://i63.tinypic.com/as7t3.png)

### Messages
Decrypt these:

1. WKHSWEC: WI XKWO SC WKHSWEC NOMSWEC WOBSNSEC, MYWWKXNOB YP DRO KBWSOC YP DRO XYBDR, QOXOBKV YP DRO POVSH VOQSYXC, VYIKV COBFKXD DY DRO DBEO OWZOBYB, WKBMEC KEBOVSEC. PKDROB DY K WEBNOBON CYX, RECLKXN DY K WEBNOBON GSPO. KXN S GSVV RKFO WI FOXQOKXMO, SX DRSC VSPO YB DRO XOHD.
* #### Output:
MAXIMUS  MY NAME IS MAXIMUS DECIMUS MERIDIUS  COMMANDER OF THE ARMIES OF THE NORTH  GENERAL OF THE FELIX LEGIONS  LOYAL SERVANT TO THE TRUE EMPEROR  MARCUS AURELIUS  FATHER TO A MURDERED SON  HUSBAND TO A MURDERED WIFE  AND I WILL HAVE MY VENGEANCE  IN THIS LIFE OR THE NEXT 

2. XOXKR IETG BL MH UX VHGLBWXKXW, XOXKR XQIXWBXGM MKBXW TGW XOXKR FXMAHW MTDXG UXYHKX FTMMXKL TKX UKHNZAM MH MABL ETLM XQMKXFBMR. ZHHW HYYBVXKL WXVEBGX ZXGXKTE XGZTZXFXGML PAXKX MAX HWWL TKX MHH ZKXTM, TGW IKXYXK MAX XFIEHRFXGM HY LMKTMTZXF TGW YBGXLLX MH WXLMKHR MAX XGXFR TL FNVA TL IHLLBUEX PBMAHNM XQIHLBGZ MAXBK HPG YHKVXL.

* #### Output: 
EVERY PLAN IS TO BE CONSIDERED  EVERY EXPEDIENT TRIED AND EVERY METHOD TAKEN BEFORE MATTERS ARE BROUGHT TO THIS LAST EXTREMITY  GOOD OFFICERS DECLINE GENERAL ENGAGEMENTS WHERE THE ODDS ARE TOO GREAT  AND PREFER THE EMPLOYMENT OF STRATAGEM AND FINESSE TO DESTROY THE ENEMY AS MUCH AS POSSIBLE WITHOUT EXPOSING THEIR OWN FORCES 

3. RD QTAJ KTW YMJ WTRFS JRUNWJ NX ZSIJSNFGQD LWJFYJW YMFS KTW RDXJQK. YMJ LWJFYJXY JRUNWJ JAJW YT MFAJ JCNXYJI. N UQJILJ RD JYJWSFQ XJWANYZIJ FSI N FR KTWJAJW GTZSI YT XJWAJ NY, NS QNKJ FSI NS IJFYM. YMJD MFAJ RJWJQD LNAJS ZX: WTFIX, HJSYWFQ MJFYNSL, HTSHWJYJ, YMJ HFQJSIFW, FSI KQZXMNSL YTNQJYX FSI XJBJWX.

* #### Output: 
MY LOVE FOR THE ROMAN EMPIRE IS UNDENIABLY GREATER THAN FOR MYSELF  THE GREATEST EMPIRE EVER TO HAVE EXISTED  I PLEDGE MY ETERNAL SERVITUDE AND I AM FOREVER BOUND TO SERVE IT  IN LIFE AND IN DEATH  THEY HAVE MERELY GIVEN US  ROADS  CENTRAL HEATING  CONCRETE  THE CALENDAR  AND FLUSHING TOILETS AND SEWERS 






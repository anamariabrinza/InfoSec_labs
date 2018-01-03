#Laboratory work nr 3
##Objectives
The main objective of this work is to crack the shift cipher, plain and simple. There are two approaches that can be used to "break the code":
* Frequency Analysis
* Dictonary attack 

##Implimentation 
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








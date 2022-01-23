#!/usr/bin/env python
# coding: utf-8

# In[2]:


age=19


# In[3]:


print(age)


# In[4]:


20 + 20


# In[5]:


age1 = 20


# In[6]:


age+age1


# In[9]:


type(age) # type nous donne le type de variable


# In[10]:


6+6


# In[11]:


_


# In[12]:


_+7


# In[13]:


_+2# le tiret de 8 garde la derniere valeur de l'operation


# In[14]:


11//2 # donne toujour l'ondie donc un nombre entier


# In[15]:


10%2 # donne le reste de la division 


# In[18]:


"""bonjour monsieur. je viens de voir votre sms""" # trois guiellemet permet d'ecrire sur plusieurs ligne


# In[19]:


val = input() # syntaxe pour saisir au clavier un nombre ou une chaine


# In[21]:


prenom = input("quel est votre prenom?  ")


# In[22]:


nom = input("quel est votre nom")


# In[25]:


print("bonjour",prenom, nom)


# In[2]:


i = 0
while i < 4:
    print("tu es fort")
    i = i + 1
print("j ai fini de parler")


# In[5]:


def projetgest():
    Nom = input("votre nom de famille svp")
    print("bonjour monsieur ", Nom)


# In[6]:


projetgest()


# In[1]:


reponse = 42
entre = int(input("Combien de plis sont-ils nécessaires pour se rendre sur la Lune ? : "))
while reponse != entre:
    print("Mauvaise réponse.")
    entre = int(input("Combien de plis sont-ils nécessaires pour se rendre sur la Lune ? : "))
print("Bravo !")


# In[11]:


nb = 0
n = 0
sommes = 0
while nb != -1:
    sommes = nb + sommes
    nb = int(input())
    if nb != -1:
        n = n + 1
    else:
        n = n + 0
    
print(sommes / n)


# In[37]:


c = int(input())
sommes = 0
if c != -1: 
    for i in range(c):
        nb = input()
        sommes = nb + sommes
    print(sommes)
else:
    nb = input()
    while nb != "F" :
        if nb != "F":
            sommes = nb + sommes
            nb = input()
            print(sommes) 
        elif nb == "F":
            print(sommes)


# In[41]:


#Insertion de nouveaux éléments dans une liste existante
t1 = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
t2 = ['Janvier','Février','Mars','Avril','Mai','Juin',
'Juillet','Août','Septembre','Octobre','Novembre','Décembre']
c, d = 1, 0
while d < 12 :
   t2[c:c] = [t1[d]] # ! l'élément inséré doit être une liste
   c, d = c+2, d+1
print(t2)
   


# ###### 

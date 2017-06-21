import random

class Clean_Extract():

    def __init__(self,fp):

        self.file=fp


    def Text(self):

        Text=""

        for i in self.file:

            print i

    def Wordify(self):

        Table=[]

        for i in self.file:

            Table.append(i.split())

        return Table

    def Word_Array(self,M):

        Mat=[]

        for i in M:

            Word=""
            Sub=[]

            for j in i:

                if(j!=" "):
                    
                      Word+=j

                else:

                      Sub.append(Word)
                      Word=""
                      
            Mat.append(Sub)

        return Mat

    def Remove_Empty_Sequence(self,ar):

        New_ar=[]

        for i in ar:

            if(len(i)>1):

                New_ar.append(i)
                
        return New_ar

    def Sentances(self,ar):

        word=""

        Dict=[]

        boo=False

        for i in ar.read():

            if(i!="."):

                if(boo==False and i!="(" and i!=")" and i!="[" and i!="]"):
             
                       word+=i

                elif(i=="(" or i=="["):

                       boo=True

                elif(i==")" or i=="]"):

                       boo=False


            else:

                Dict.append(word)
                word=""
                
        return Dict
            
    def Remove_Bracket(self,ar):

        Q=[]

        for i in ar:

            Sub=[]
            
            for j in i:

                word=""
                D=0
                for k in j:

                    if(k=="[" or k=="("):

                        D=1

                    elif(k=="]" or k==")"):

                        D=0

                    elif(D==0):

                        word+=k
                        
                Sub.append(word)

            Q.append(Sub)

        return Q

class NLP:

    def __init__(self,Dict):

        self.Corpus=Dict
        self.Length=0
        pass

    def Bigram_model(self):

        Dict={}
        self.Length=len(self.Corpus)

        for i in range(0,len(self.Corpus)):

            for j in range(1,len(self.Corpus[i])):
                            
                 Key=str(self.Corpus[i][j-1])
                 second=str(self.Corpus[i][j])
                 if(Dict.has_key(Key)):

                           found=False

                           Ar=Dict[Key]
                           for k in Ar:

                               if(str(k[0])==second):

                                   k[1]+=1
                                   found=True

                           if(found==False):

                                   Dict[Key].append([second,1])

                            

                 else:
                           Dict[Key]=[[second,1]]

                 #print Key
                 #print " "
                 #print " "
                 #print Dict[Key]

        return Dict

    def SentanceArray(self,Text):

        Ar=[]


        for i in Text.read():
            
            word=""

            sub=[]
            
            for j in i:
                 
                word+=j

                if(j=="."):

                    sub.append(word)
                    word=""

            Ar.append(sub)

        return Ar

    def Corpus_length(self):

        return self.Length

    def Corpusify(self,Dict):

        New_Dict={}

        for Key in Dict:

            New_Dict[Key]=[]

            for j in Dict[Key]:

                if(j[1]>1):

                    New_Dict[Key].append([j[0],j[1]])


        return New_Dict

class Concurrent_Matrix:


    def __init__(self):

        self.KeyValuePair={}


    def Key_Value(self,Text):

        Index=0
        New_Dict={}

        word=""
        for i in Text.read():

            if(i!=' '):

                word+=i

            else:

                if(not(New_Dict.has_key(i))):

                      New_Dict[word]=Index
                      Index+=1
                      word=""

        return New_Dict

    def Generate(self,Sen,Ref):

        Dict={}

        C=Clean_Extract(Sen)
        W=C.Word_Array(Sen)

        for i in W:

            Ar=[]
            
            for j in i:

                for k in i:

                    Ar.insert(Ref[k],1)

                Dict[j]=Ar
                

        print Dict['New'][Ref['New']]
           
           
class Node:


    def __init__(self,Word,Count):

        self.Next=None
        self.Word=""
        self.Count=0


Data=open("NYSE.txt","r")
CE=Clean_Extract(Data)
W=CE.Wordify()
W=CE.Remove_Empty_Sequence(W)
W=CE.Remove_Bracket(W)
r=NLP(W)
b=r.Bigram_model()
#b=r.Corpusify(b)

a=0

while(a==0):

  Word=raw_input("Enter a word")
  string=Word

  if(Word=="EXIT"):

      a=1
    
  while(Word!="." and Word[-1]!="."):

    word=""
    Index=0

    if((len(b[Word])>1)):
        
          Index=random.randint(0,len(b[Word])-1)

    elif(len(b[Word])==1):

          Index=1

    if(Index!=0):

         word=b[Word][Index-1][0]
         string+=" "+word
       
    if(word!=''):
        
         Word=word

  print string






from passlib.hash import sha256_crypt,sha512_crypt,md5_crypt
import multiprocessing


def checkdictionary(threadname,filename):
    shadow_arr = ""
    with open("shadow.txt","r") as f:
        shadow_arr = f.read().splitlines()

    foundpwds = []
    foundusers = []
    word = ""
    with open(filename,"r") as f:
        pwds = f.read().splitlines()
        
        for i,pwd in enumerate(pwds):
            print ("------------------------TESTING NEW PASSWORD " + str(i) +"------------------------")
            for user in shadow_arr:
                # getting user details
                user_details = user.split('$')
                user_hashing_id = user_details[1]
                user_salt = user_details[2]
                user_hash = user_details[3][:user_details[3].index(':')]

                # hashing the dictionary password
                nb_of_hashes = 5000
                user_hash_appended = ""

                found = False
                
                if(user_hashing_id == "1"):
                    user_hash_appended = "$" + user_hashing_id + "$" + user_salt + "$" + user_hash
                    found = md5_crypt.verify(pwd,user_hash_appended)
                if(user_hashing_id == "5"):
                    user_hash_appended = "$" + user_hashing_id + "$rounds=" + str(nb_of_hashes) + "$" + user_salt + "$" + user_hash
                    found = sha256_crypt.verify(pwd,user_hash_appended)
                if(user_hashing_id == "6"):
                    user_hash_appended = "$" + user_hashing_id + "$rounds=" + str(nb_of_hashes) + "$" + user_salt + "$" + user_hash
                    found = sha512_crypt.verify(pwd,user_hash_appended)
                
                # print("USER HASH :     " + user_hash_appended)

                if(found):
                    print("FOUND! from " + threadname + " " + pwd + " " + user)
                    word += pwd[:1]
                    foundpwds.append(pwd)
                    foundusers.append(user)
    with open(threadname + ".txt","w") as wf:
        wf.write(word +"   "+ ' '.join(foundpwds) +"   "+ ' '.join(foundusers) + " returned from "+threadname)


try:
    p1 = multiprocessing.Process(target=checkdictionary,args=("THREAD-1","Dictionary/dic1.txt",))
    p2 = multiprocessing.Process(target=checkdictionary,args=("THREAD-2","Dictionary/dic2.txt",))
    p3 = multiprocessing.Process(target=checkdictionary,args=("THREAD-3","Dictionary/dic3.txt",))
    p4 = multiprocessing.Process(target=checkdictionary,args=("THREAD-4","Dictionary/dic4.txt",))
    p1.start()
    p2.start()
    p3.start()
    p4.start()
except Exception as e: 
    print(e)




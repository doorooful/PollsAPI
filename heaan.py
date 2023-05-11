
import piheaan as heaan
from piheaan.math import sort
from piheaan.math import approx # for piheaan math function
import math
import os

class Heaan():
    
    def __init__(self):
        self.params = None
        self.context = None
        self.log_slot = 0
        self.num_slots = 2**(self.log_slot)
        self.eval = None
        self.dec = None
        self.enc = None
        self.path = "./keys"

    # Initializes necessary values
    def initialize(self):
        self.params = heaan.ParameterPreset.FGb
        self.context = heaan.make_context(self.params)
        context = self.context
        heaan.make_bootstrappable(context)

        sk = heaan.SecretKey(context)
        os.makedirs(self.path, mode=0o775, exist_ok=True)
        sk.save(self.path+"/secretkey.bin")

        key_generator = heaan.KeyGenerator(context, sk)
        key_generator.gen_common_keys()
        key_generator.save(self.path+"/")

        sk = heaan.SecretKey(context, self.path+"/secretkey.bin")
        pk = heaan.KeyPack(context, self.path+"/")
        pk.load_enc_key()
        pk.load_mult_key()

        self.eval = heaan.HomEvaluator(context, pk)
        self.dec = heaan.Decryptor(context)
        self.enc = heaan.Encryptor(context)
    
    # From plaintext, create ciphertext
    def encrypt(self, plaintext):
        data = [plaintext]
        msg = heaan.Message(self.log_slot)
        for i in range(self.num_slots):
            msg[i] = data[i]
        ciphertext = heaan.Ciphertext(self.context)

        pk = heaan.KeyPack(self.context, self.path+"/") # load public key
        pk.load_enc_key()
        pk.load_mult_key()
        
        self.enc.encrypt(msg, pk, ciphertext)
        
        return ciphertext

    # Returns encrypted added result
    def add(self, ciphertext1, ciphertext2):
        result = heaan.Ciphertext(self.context)
        self.eval.add(ciphertext1, ciphertext2, result)
        return result
    
    # From ciphertext, get plaintext
    def decrypt(self, ciphertext):
        result = heaan.Message(self.log_slot)
        sk = heaan.SecretKey(self.context, self.path+"/secretkey.bin")
        self.dec.decrypt(ciphertext, sk, result)
        return result
    
    # From given optionList and user's input,
    # returns updated list.
    # Regarding that discrete_equal returns 1 if the given parameters are same,
    # this method would add 1 for each vote score if the index of the option and user's input are same.
    def updateVote(self, optionList, ciphertext):
        updatedList = []
        for o in optionList:
            heaan_result = heaan.Ciphertext(self.context)
            approx.discrete_equal(self.eval, o[0], ciphertext, heaan_result)
            o[1] = self.add(o[1], heaan_result)
            updatedList.append(o)
            print(self.decrypt(o[0]))
            print(self.decrypt(o[1]))
        return updatedList
    
    # Extract real number part from heaan result
    def pretty(self, heaanresult):
        pretty = str(heaanresult)
        pretty = pretty.replace("[ (","")
        pretty = pretty.replace(") ]","")
        pretty = complex(pretty)
        pretty = float(pretty.real)
        return pretty
    
# Test code
# myHeaan = Heaan()
# myHeaan.initialize()

# mycipher1 = myHeaan.encrypt(1)
# mycipher2 = myHeaan.encrypt(2)
# mycipher3 = myHeaan.encrypt(3)

# myadd1 = myHeaan.add(mycipher1, mycipher2)
# myadd2 = myHeaan.add(myadd1, mycipher3)

# print("result is", myHeaan.decrypt(myadd2))
# print("pretty is", myHeaan.pretty(myHeaan.decrypt(myadd2)))
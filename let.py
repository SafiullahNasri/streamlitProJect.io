
# import cowsay
# import sys

# if len(sys.argv) == 2:
#     cowsay.cow("Hello", + sys.argv[1])



# print("Hello pro")




# a = 9
# print(a)

# b = 4
# print(b)

# c = True
# print(c)

# d = "pro"
# print(d)


# e = None
# print(e)


# f = 9.99
# print(f)



# operators in the python


# a = 1
# b = 2

# print(a+b)
# print("The sum of a and b is: ", a+b )
# print("The sub of a and b is: ", a-b )
# print("The mul of a and b is: ", a*b )
# print("The div of a and b is: ", a/b )






# x = 9
# # x +=2
# x -=2
# # x *=2
# # x /=2
# print(x)


# time of the cmparison operators i the python

# a = 90
# b = 35
# c = 33
# print(a>b)
# print(a>=b)
# print(a<=b)
# print(a==b)
# print(a!=b)
# print(b>a)
# print(b>=a)
# print(b<=a)
# print(b==a)
# print(b!=a)
# print(a==c)
# print(c!=a)







# print(True and True)
# print(True and False)
# print(False and True)
# print(False and False)



# print(True or True)
# print(True or False)
# print(False or True)
# print(False or False)



# a = 90
# b = 12
# print(a==b & a!=b & a<b & a<=b)


# a = 90
# b = 12
# print(a>b or a==b or b>a or a<=b)



# import pandas

# # df = pandas.read_excel("train.xlsx")
# df = pandas.read_csv("diabetes.csv")
# print(df)

# name = "professional"
# number = "9"
# print(name)
# print(name[0:3])
# print(name.lower())
# print(name.capitalize())
# print(name.count("e"))
# print(name.isalnum())
# print(number.isnumeric())



# input in the python
# name = input("Enter your name? ")
# print(name)
# print(type(name))



# no = int(input("Enterthe number? "))
# print(no + 90)
# print(type(no))

# _3dString = ''''
# Hello this is the pro world,,,,
#                 No this is the world of the hackers...
#     no this is the world of the engineers....

#                     no this the world fo the computer science...
# '''
# print(_3dString)





# lOne = [100,20,13,42,5, "pro", True, None, "kamal"]
# lOne = [100,20,13,42,5]
# lOne.sort()
# print(lOne)
# lOne.remove(100)
# print(lOne)
# PendingDeprecationWarning
# lOne.extend(10000000)
# print(lOne)
# lOne.append(50)
# print(lOne)
# lOne.extend([1,2,3,4,5,6])
# print(lOne)
# print(type(lOne))
# print(lOne)
# print(lOne.remove("pro"))
# re = lOne.remove("pro")
# print(re)
# lOne.remove("pro")
# print(lOne.count(3))
# print(lOne)
# for i in lOne:
#     print(i)

# lOne.remove("kamal")
# print(lOne)




# tuple ka time hai ab

# t = (1,2,3,4,5,5,5,5)
# PendingDeprecatinWarning
# print(t)
# print(t.count(5))
# print(t.index(3))



# d1 = {1,2,3,4,5}
# print(d1)
# d2 = {4,5,6,7,8}
# print(d2) 
# d1.clear()
# print(d1)
# print(d1)
# print(d1.union(d2))    # won't print the repated numbers inthe tuple



# a = {}
# b = ()

# print(a, type(a))
# print(b, type(b))

# words= {"apple": "mana", "orange": "narang", "banana":"kela"}
# print(words['apple'])



# marks = {"pro":90, "jamal":34, "ramzia":56}
# print(marks['pro'])
# marks['pro'] = 100
# print(marks['pro'])
# print(marks.get('jamal'))
# print(marks.keys())
# print(marks.values()) 
# print(marks.items())


# a = int(input("Enter the nmber? "))
# match a:
#     case 1:
#         print("one")
#     case 2:
#         print("two") 
#     case 3:
#         print("three")  
#     case 4:
#         print("four")
#     # break  
#     #  print("not found")
#     # case:/
#         # print("not found")

#         # print("not found")
#     case _:
#         print("not found")
# for i in range(5):
#     print(i+1)



# Now the time is of the while loop

# while (i<10):
#     print(i)
#     i+=1
# print("it is running....")

# i = 0
# while i<10:
#     print(i)
#     i+=1



# while True:
#     num = int(input("Enter the number? "))
#     # PythonFinalizationError
#     # PythonFinalizationError
#     print(num)
#     if num==10:
#         # print(num)
#         break




# for i in range(5):
#     if i == 3:
#         break
#     print(i+1)





# Now it is the itme of the functions in the python

# def detail(name, date):
#     print(f"hello thisis {name} \nm and i can not come on {date}")
# detail("pro", "25 aug")


# try:
#     a = int(input("Enter the numnber? "))
#     a = input("Enter the numnber? ")
#     print(a+6)

# except:
#     print("some error occured")

# s = "hello this is the professilnal man"

# with open("pro.txt", "w")as f:
#     # print(s)
#     f.write(s)



# s = "no matter what you gonna say to us..."
# with open("love.txt", "r")as f:
#     s = f.read()
#     print(s)

 

# now it is the time of creatign the calsses inteh ptyhon

# class Employee:
#     salary = 90
#     def getSalary(self):
#         return self.salary
# pro = Employee()
# print(pro.salary)


# class findName:
#     name = "pro"
#     def getName(self):
#         return self.name
    
# sname = findName()
# print(sname.name)



# class Employee:
#     def __init__(self, name, salary):
#         self.name = name
#         self.salary = salary

# pro = Employee("pro", 90)
# print(pro.name)
# print(pro.salary)

# robo speaker project in the python



# import os

# if __name__ == '__main__':
#     print("The iventor fo the robo boy is professinl man pro..")

#     x = input("Enter the text till robo read it! ")
#     command = f"say{x}"
#     os.system(command)
# print("Hello world")



# import re
# import spacy
# from spacy.tokens import span
# text = "dkjfkdjfkjdkflsjljfdkfkjf"
# nlp = spacy.blank("en")
# doc = nlp(text)

# pattern = []
# origional_ents = list(doc.ents)
# new_ents = []
# for mathc in re.finditer(pattern, doc,text):

# start, end= mathc.span()


# span = doc.char_span(start, end)
# print(span)

# if span is not None:
#     new_ents.append((span.start, span.end, span.text))

# print(new_ents)


# for ent in new_ents:
#     start, end, name = ent
#     per_ent = spacy(doc, start, end, label="Person")
#     origional_ents.append(per_ent)
# doc.ents = origional_ents

# for ent in doc.ents:
#     print(ent.text, ent.label_)



# from spacy.language import language


# @language.component("pauld f")
# def paul_er (doc):
    
#     import re
#     import spacy
#     from spacy.tokens import span
#     text = "dkjfkdjfkjdkflsjljfdkfkjf"
#     nlp = spacy.blank("en")
#     doc = nlp(text)

#     pattern = []
#     origional_ents = list(doc.ents)
#     new_ents = []
#     for mathc in re.finditer(pattern, doc,text):

#     start, end= mathc.span()


#     span = doc.char_span(start, end)
#     print(span)

#     if span is not None:
#         new_ents.append((span.start, span.end, span.text))

#     print(new_ents)


#     for ent in new_ents:
#         start, end, name = ent
#         per_ent = spacy(doc, start, end, label="Person")
#         origional_ents.append(per_ent)
#     doc.ents = origional_ents

#     for ent in doc.ents:
#         print(ent.text, ent.label_)

# import spacy
# smbols = df.symbol.tolist()
# companies = df.comanuName.tolist()
# print(SystemError
      
      
      
#       )
# nlp = spacy.blan("en")
# ruler = nlp.add_pipe("entitiy_ruler"
#                      )


# for symbol in symbol:
#     pattern.append({"label": "stock"})

# for compnay in companyname:
#     pattern.append({"label": "stock"})


# doc = nlp(text)
# for ent in doc.ents:
#     print(ent.text), ent.label_





# import tensorflow_probability as tf
# tfd = tfb.distrubutions 
# inititlaization_ditributions = tfd.Categorical(probs=[0.8, 0.2])
# transition_distributions = tfd.ormal(loc=[0., 15.0])


# model = tfd.HiddenMarkvModel(
#     inititlaization_ditributions = inititlaization_ditributions,
#     transition_distributions = transition_distributions,
#     observtions_distributions = observations_distributions

# )

# # Again we go for imporiting the important libraries

# import tensorflow as tf
# from tensorflow import keras  


# # Helper libraries

# import numpy as np
# import matplotlib.pylab as plt


# fasion_mnist = keras.datasets.fashion_mnist

# (train_images, train_labes) (test_images, test_labels) = fashion_mnist.load_data()


# # nwo we check the shape of the data
# trian_images.shape

# class_names = ['boot', 'trouser','shirts', ' paits', 'niker', 'sneaker', 'dress', 'bag', ' sandle']


# # now let's open it with the plots for the better visualization

# plt.figure()
# plt.imshow(transition_distributions)
# plt.Colorbar()
# plt.grid(False)
# plt.shwo()



# model = keras.Sequential([
#     keras.layers.Flatten(input_shape=(28,28)),
#     keras.layers.Dense(128, activation = "relu")
#     keras.layers.Dense(10, activation = 'softmax')

# ])

# model.compile(optimizer="adam",
#               loss = "spares_categorical_croset",
#               metrics = ['accuracy'])


# # I am gonna fit the model:
# model.fit(trian_iamegs, train_labels, epochs = 10)

# # for printing the accuracy in the tensroflow let's do this
# test_loss, test_acc = model.evaluate(test_images, test_labels, verbos=1)
# print("Test accuracy", test_acc)

# predictions = model.predict(test_images)

# test_images.shape



# # Now we gonna create the function of the gettign the ranodm images fo the fasion tools and devices

# def get_number():
#     while True:
#         num = input("Pic one number")
#         if num.isdigit():
#             num = int(num)
#             if 0<=num <= 1000:
#                 return int(num)
#         else:
#             print("Try again")
# num = get_number
# image = test_images[num]
# label = test_labels[num]
# predict (model, image, label)


# model = models.sequential()
# mdoel.add(layers.covn2d(32, (3,3), activation ='relu', input_shape = (32,32,3)
# ))
# mdoel.add(layers.MaxPooling2d((2,3)))
# model.add(layer.conv2d(64, (3,3), activations= 'relu') )


# model.summary()

# model.add(layers.fallten())
# model.add(layers.dense(64, activatio = 'relu'))
# model.add(layers.dense(10))


# model.compile(optimizers = 'admam',
#               loss = tfkeras.losses.sparsectagoricalcrossentropy(from_logits=True),
#             metrics =['accuracy']
# ])
# history = model.fit(train_images, train_labels, ephocs= 10,
#                     validations_data =(test_imaegs, tes_labels))


# test_loss, test_acc = model.evaluate(test_images, testabels, verbase = 2)



# # NOW WORKING ON A SAMALL DATASET LET'D DO TI PROPEERLY

# from keras.preprocessing import image_dataset_from_directory
# from keras.preprocessing.image import ImageDataGenaerator

# # now create data generator for the images shapes
# datagen = ImageDataGenaerator(
#     rotaition_reange = 40,
#     width_shift_rnage = 0.2,
#     height_shift_rnage = 0.2,
#     shear_range = 0.2,
#     zoom_rnage = 0.2,
#     horizental_trip = True,
#     fil_mode = 'nearest'
# )


# # now pick the image to transfomr

# test_iamge= train_images[14]
# img = image.img_to_array(test_image)
# img= img.reshape((1, )+ img.shape)

# i =  0

# for batch in datagen.flow(img, save_prefex = 'test', save_formate = 'jpeg')
# plt.figure(i)
# plot = plt.imshow(image.mg_to_array[bathc=[0]])
# i+=1
# if i>4:
#     break
# plt.show()


# import os
# import numpy as np
# import pandas as pd
# import matplotlib.pyplot as plt
# import tensorflow as tf
# keras = tf.keras

# import tensorflow_datasets as tfds
# tfds.disable_progress_bar()

# (raw_trian, raw_validations, raw_test), metadata = tfds.load(
#     'cats_vs_dogs',
#     split = ['train[':80%]', 'train[80%:90%], 'train['90:]']
#     with_info = True
#     as_supervisded = True

# )



# get_name_label = metadata.features['label'].int2str
# plt.figure()
# plt.imshow(image)
# plt.title(get_label_name(label))


# img_size = 160
# def format_example(image, label):
#     """
#     return the image int the reshapes of the word into the golden
#     """

#     image = tf.cast(image, tf.float32)
#     iamge = (image/127.5)-1
#     iamge = tf.image.resize(image, (img_size, img_size))


#     return image, label


# train = raw_trian.map(format_example)
# raw_validations = raw_validations.map(format_example)
# test  = raw_test(format_example)

# for image, label in train.tak(2):
#     plt.figure()
#     plt.imshow(image)
#     plt.title(get_label_name(label))



#     model = tf.keras.sequential([
#         base_model,
#         global_average_layer,
#         predictions_layer
#     ])

#     model.summary()

#     mode.save("dogs_vs_cats.h5")
#     new_model= tf.keras.models.load("dfjkdjfkdj")




# from keras.datasets import imdb


# vocab_size  = 88584
# maxlen = 250
# batch_size = 64

# (train_data, train_tabels), (trest_data, test_labels) = imbd.load_data(num_words=vocab_size)


# train_data[0]

# len(train_data[1])
# trian_data = sequence.pad_sequences(train_data, maxlen)
# test_data = sequence.pad_sequences(test_data, maxlen)
# trian_data[1] 

# # now we create the model for like the natural language processing 
# mdoel = tf.keras.Sequential([
#     tf.keras.layers.Embadding(vocab_size, 32),
#     tf,.keras.layers.LSTM(32),
#     tf.keras.layers.dense(1, activation='sigmoid')
# ])

# model.summary()

# word_index = imdb.get_word_index()
# def encode_text(text): 
#     tokens = keras.preprocesssing.text.text_to_word_sequence(text)
#     tokens = [word_index[word] if word in word_index else 0 for word in tokens]
#     return sequence.pda_sequences([tokens], maxlen)

#     text = 'hello this is an amzing movie of the year in the netflix'
#     encoded = encode_text(text)
#     print(encoded)
# def predice(text):
#     encoded_text = encode_text(text)
#     pred = np.zeros((1, 250))
#     pred[0] = encoded_text
#     result  = model.predict(pred)
#     print(result[0])


# positive_reveiw = "fjkdjfkjdfdlfkfjdlfdsfdfsfwuijwnvurhijwnwltdsfndsngdgsk"
# print(positive_reveiw)

# negative_revieow = 'lfdjldsjfjflsdlkfjdsfjslfsfjsdjkfsdlsdsjfdluirutiuiwjanvgdk'
# print(negative_revieow)



# # AND WE ARE TALKING ABOUT TEH RECINFORCEMENT LEARNING IN THE TENSORLFOW



# with open('wizard_of_text', 'r' encoding='utf-8') as tf:
#     text = f.read()
# # print(text[:200])
# # Now i wanna tokenize the entire file of the text here in the program

# chars = sorted(set(text))
# print(chars)


# string_to_int = {ch:i for i, ch in enumerate(cahrs)}
# int_to_string = {i:ch for i , ch in enumerate(chars)}
# encode = lambda s: [string_to_int[c] for c in s]
# decode = lambda l: ''.join([int_to_string[i] for in l])


# encoded_hello = encode("hello")
# decoded_hello = decode(encoded_hello)
# print(decoded_hello)

# blocke_size = 8
# x = train_data[:blocke_size]
# y = train_data[1:blocke_size]


# for i in range(blocke_size):
#     context = x[:t+1]
#     target = y[t]
#     print("when input is ", context, 'traget is ', target)


# import torch
# randint = torch.randint(-100, 100, (6,))
# randint
# tensor = torch.tensor([[0.1, 1.2], [4.9, 5.2]])
# zeros = torch.zeros(2,3)
# print(zeros)

# ones = torch.ones(3,4)
# print(ones)

# input = torch.empty(2,3)
# print(input)

# arange = torch.arange(5)
# print(arange)

# linespace = torch.linspace(3,10,steps = 5)
# print(linespace)

# logspace = torch.logspace(start = 10, end = 2,steps = 9)
# print(logspace)

# eye = torch.eye(5)
# eye
# a = torch.empty((2,3)), dtype = torch.int64
# empty_like = torch.empty_like(a)

# print(empty_like)

# startTime = time.time()

# zeros = torch.zeros(1,1)
# end_time = time.time()

# elapsed_time = end_time = startTime
# print(f"{elapsed_time:.10f}")

# # let's crete a model of the language of large one here in the nlp



# class BigramLanguageModel(nn.Module):
#     def __init__(self, voacab_size):
#         super().__init__()
#         self.token_embedding_table = nn.Embedding(vocab_size, vocab_size)

#     def forward(self, index, tragets=None):
#         logits = self.token_embedding_table(index)


#         if targets in None:
#             loss = None
#         else:
#             B, T, C = logits.shape(B*T, C)
#             targets = targets.view(B*T)
#             loss = F.cross_etropy(logits, targets)
            

#         return logits, loss
    
#     def generate(self, index, max_new_token):
#         for _ in range(max_new_token):
#             logits = logits[:, -1, :]
#             probs = F.sofmax(logits, dim=-1)
#             idnex_next = torch.cat(((index, index_next), dim= 1))
            

#         return index


# model = BigramLanguageModel(vocab_size)
# m = model.to(device)


# context = torch.zeros((1,1), dtype=torchy.long, device device)
# generated_chars = decode(m.generate(context,max_new_tokens=500)[0].tolist())
# print(generated_chars)






# optimizer = torch.optim.AdamW(model.parameter(), lr = learning_rate)


# for iter in range(max_iters):
#     xb, yb = get_batch('train')
#     logits, loss = model.forward(xb, yb)
#     optimizer.zeros_grad(set_to_none = True)
#     loss.backward()
#     optimizer.step()
# print(loss.item())

# context = torch.zeros((1,1), dtype=torchy.long, device device)
# generated_chars = decode(m.generate(context,max_new_tokens=500)[0].tolist())
# print(generated_chars)


# x = torch.tensor([-0.05], dtype = torch.float32)
# # y = nn.ReLU()
# y = F.sigmoid()
# print(y)






# # large language model let's do it man

# import torch
# import torch.nn as nn
# from torch.nn import fucntional as F

# device = 'cuda' f torch.cuda.is_available() else 'cpu'


# block_size = 8
# batch_size = 4
# max_iters = 1000
# leanring_rates = 3e-3
# eval_iters = 250
# n_embd = 384
# n_layers = 0

# with open('shdfdjfdfkjdkfj', 'r',encoding = 'utf-8') as f:
#     text = f.read()
# vocab_size = len(chars)



# string_to_int = {ch:i for, ch in enumerate(chars)}
# int_to_string = {i:ch for i , ch in enumerate(chars)}
# encode = lambda s: [string_to_int[c] for c in s ]
# deocde = lambda l: ''.join([int_to_string[i] for i in l]])


# data = torch.tensor(encode(text), dtype=torch.long)








# class GPTLANGUAGEMODEL(nn.Modluel):
#     def __inint__(self, vocab_size):
#         super().__ini__()

#         self.token_embading_tabel = nn.emabding(vocab_size, n_embd)
#         self.postion_emabding_table = nn.embadding(block_size, n_embd)
#         self.block = nn.sequential(8[block(n_embd), n_head=n_head] for _ i in range(n_layers))
#         self.ln_f = nn.laeyrNorm(n_embd)
#         self.lm_head = nn.linear(n_embd, vocab_size)


#     def forward(self, index, targets = None):
#         logits= self.token_emabadding_talbel (index)
#         if targets in None:
#             loss = None
#         else:
#             b, t,c = logits.shape
#             logits = logits.view(b*t,c)
#             targets = targetview(b*t)
#             loss = f.cross_entropy(logits, target)


#             return logits, loss
    
#     def generate (self, idnex, max_new_tokesn):
#         for _ in range(max_new_tokesn):
#             logtis, loss = self.forward(index)
#             logits = logits[:, -1, :]
#             probs = f.softmax(logits, dim = 1)









# def aprs_args():
#     parser = argparse.ArgumentParser(description='it is a program of the world food')
#     parser.add_argument('-llms', type = str, requried=True, help='hey safia are you okay')
#     return parser.parse_args()

# def main():
#     args= parse_args()
#     print(f"the provided llms si : {args.llms}" )

# if __name__ == '__main__':
#     main()

# import time
# start_time = time.time()

# for i in range(10000):
#     print(i*2)

# end_time = time.time()

# total_time = end_time-start_time

# print(f"time taken: {total_time}")









# a new project of the nlp in the english of the haravard university

# import torch
# import torch.nn as nn
# from torch.nn import functional as F
# import mmap
# import random
# import pickle
# import argparse

# parser = argparse.ArgumentParser(description='This is a demonstration program')


# parser.add_argument('batch_size', type=str, required=True, help='please provide a batch size here')
# args = parser.parse_args()


# print(f"batch_size: {args.batc_size}")
# device = 'cuda' if torch.cuda.is_available() else 'cpu'




# batch_size = int(args.batch_size)
# block_size = 128
# max_iters = 200
# learing_rates = 3e-4
# eval_iters = 100
# n_embd = 384
# n_head = 1
# n_layer = 1
# dropout = 0.2

# print(device)



# chars = ""

# with open("fkjfkdjkfjkjf/tct", encoding='utf-8')as f:
#     text = f.read()
#     chars = sorted(list(set(text)))

# vocab_size = len(chars)


# string_to_int = {ch:i for i, ch in enumerate(chars)}
# int_to_string = {i:ch for i,ch in enumerate(chr)}
# encode = lambda s: [string_to_int[c] for c in s]
# decode  = lambda l: ''.join([int_to_string[i] for i in l])

# # Now it is the time to create some fucntions for running the code in the project

# def get_random_chink(split):
#     filename = "dfkljdfkjsdkjdkskjsd.txt" if split == 'train' else 'dkfdkjflkdsjkjs.txt'
#     with open(filename, 'rb') as f:
#         with mmap.mmap(f.fileno(), 0, access=mmap.ACCESS_READ) as mm:
#             file_size = len(mm)
#             start_pos = random.randint(0, (file_size) - block_size*batch_size)


#             mm.seek(start_pos)
#             block = mm.read(block_size*batch_size-1)

#             decode_block = block.decode('uft-8', errors='ignore'.replace('r', ''))


#             data = torch.tensor(encode(decode_block), dtype=torch.long)
#     return data


# def get_batch(split):
#     data= get_random_chink(split)
#     ix = torch.randint(len(data)- block_size(batch_size))
#     x = torch.stack([data[i:i+block_size] for i in ix])
#     y = torch.stack([data[i+1: i+ block_size] for i in ix])
#     x,y  = x.to(device), y.to(device)
#     return x,y


# @torch.no_grad()
# def estimate_loss():
#     out = {}
#     model.eval()
#     for split in ['train', 'val']:
#         losses = torch.zeros(eval_iters)
#         for k in range(eval_iters):
#             x,y  = get_batch(split)
#             logits, loss = model(x,y)
#             losses[k]  = loss.item()
#         out[split] = losses.mean()
#     model.train()
#     return out



# # now it is the time to crete the classes of the function in tne project

# class Head(nn.Module):


#     def __init__(self,head_size ):
#         super().__init__()
#         self.key = nn.Linear(n_embd, head_size, bias=False)
#         self.query = nn.Linear(n_embd, head_size, bias=False)
#         self.value = nn.Linear(n_embd, head_size, bias=False)
#         self.register_buffer = ('trail', torch.tril(torch.ones(block_size, block_size)))
 
#        # 'trail'
#         self.dropout = nn.Dropout(dropout)

#     def forward(self, x):
#         b,t,c = x.shape
#         k = self.key*x
#         q = self.query(x)
#         wei = q @ k.transpose(-2, -1) * k.shape[-1]**0.5

# wei = wei.masked_fill(self.tril[t,:t])
# wei = F.softmax(wei, dim= 1)
# v = self.values(x)
# out = wei @ v
# return out



# class feedForwad(nn.Module):
#     def __init__(self,n_embd *args, **kwargs):
#         super().__init__(*args, **kwargs)
#         supernet = nn.Sequential(
#             Head_size= n_embd // n_head
#                     self.key = nn.Linear(n_embd, head_size, bias=False)
#         self.query = nn.Linear(n_embd, head_size, bias=False)
#         self.value = nn.Linear(n_embd, head_size, bias=False)
#         self.register_buffer = ('trail', torch.tril(torch.ones(block_size, block_size)))
 
 
#         )



#     def _slow_forward(self, *input, **kwargs):
#         return super()._slow_forward(*input, **kwargs)
    



# model = gptlanguagemodel()
# m= mdoel.to(device)



# optimizer =torch.optim.AdamW(mdoel.parameters(), lr= learing_rates)

# for iter in range(max_iters):
#     print(iter)

# if iter % eval_iters == 0:
#     lossess = estimate_loss()
#     printf("step {iter}, train_loss: {loss['train]}")


# xb, yb = get_batch('train')


# logits, loss = model.forward(xb, yb)
# optimizer.zeros_grad(set_to_none = True)
# loss.backwrd()
# optimizer.step()
# print(loss(item))



# with open('skjfjdkfk', 'wb')as f:
#     pickle.dump(model, f)
# print('model saved')






# import librosa
# import torch
# import IPython.dispaly as dispaly

# from transformers import WavevEC2ForCTC
# import numpy as np

# tokenizer = WavevEC2ForCTC.from_pretrained("facebook/wave2vec2")
# modle = wave2.from_pretrianed("jkjkjfkdjfk")
# audio, sampling_rate = librosa.loading('dfkj')

# dispaly.audio('kjfkdfkj')
# print(dispaly)

# input_values = tokenizer(audio, return_tensiors = 'pt').input_vlaues()
# print(input_values)

# logits = model(input_values).logits

# print(logits)

# predicted_ids = torch.argmax(logits, dim= 2-1)

# transcription = tokenizer.decode(predicted_ids = 0)



# import warnings
# warnings,FileNotFoundError('ignore')

# import numpy as np
# import pandas as pd
# import matplotlib.pyplot as plt
# import seaborn as sns
# sns.set()

# from sklearn.model_selection import train_test_split
# from sklearn.metrics import f1_score, confusion_matrix, roc_auc_score
# from trasformers import pipeline
# import torch



# classifer = pipeline('sentiment-analysis')
# type(classifer)


# classifer('this is a great movie')
# print(classifer)









# from helper import get_open_api_key
# OPEN_AI_KEY = get_open_api_key()
# import nest_asyncio
# nest_asyncio.apply()


# from llama_index.core.tools import Functional
# def add(x: int, y: int) -> int:
#     """adds two integers togeter"""
#     return x+y

# def mystaery(x: int, y: int) ->int:
#     """Mystrey fucniton that operate on top of two numbers"""
#     return (x+y) * (x+y)

# add_toll = Functional.form_defaults(fn==add)
# myster_toll = Functional.from_defaults(fn=mystaery)


# from llama_idex.llms.openai import OoenAI
# llm = open(mdoel = "gpt-3.5-turbo")
# response  = llm.predict_and_call(
#     [add_toll, myster_toll],
#     "Tell me yhe ouput of the mystery fucntion on 2 and 9"
#     verbose = True
# )

# print(str(response))

# from llama_index.core import SimpleDirectoryReader
# documents = SimpleDirectoryReader(input_file s= ['metagpt.pdf']).load_data()
# from llama_index.core.node_parser import SentenceSpiter
# splitter = SentenceSpiter(chunk_size = 1024)
# nodes= splitter.get_nodes_form_documnets(documents)
# print(nodes[0], get_content(metadata_mdoe= "all"))


# from llama_index.core import vectorIndex

# vecoter_index = vectorIndex(nodes)
# query_engine = vecoter_index.as_query_engine(similiraty_top_k= 2)

# from llama_inde.vector_stores import MetdataFilters

# query_engine = vectorIndex.as_index_query_engine(
#     similarity_top_k= =2,
#     [SimpleDirectoryReader"key", "page_label", "values":"2"]

# )


# response = query_engine.wuery(
#     "What are the some high level result so fthe metagpt"
# )

# print(str(response))

# import numpy as np

# n_states = 16
# n_actions = 4
# goal_satate = 15

# Q_tab = np.zeros((n_states, n_actions))



# learning_rate = 0.8
# discount_factor = 0.95
# exploaration_probs = 0.2
# epochs = 1000


# for epochs in range(epochs):
#     current_state = np.random.randint(0, n_states)

#     while current_state != goal_satate:
#         if np.random.rand() < exploaration_probs:
#             action = np.random.randint(0, n_actions)

#         else:
#             action = np.argmax(Q_tab[current_state])

#         next_state = (current_state+1)%n_states


#         reward = 1 if next_state == goal_satate else 0

#         Q_tab[current_state, action] += learning_rate * \
#             (reward + discount_factor * 
#              np.max(Q_tab[next_state]) - Q_tab[current_state, action])
        

#         current_state = next_state


# print("Learned Q_table...")
# print(Q_tab)


# import os
# # from pathlib import path
# import padnas as pd
# import numpy as np
# import seaborn as sns


# data = pd.read_csv("file.csv")
# data.head(4)
# data.info()
# data.shpe()
# data.describe()
# data.sum()
# data.isnull()
# data.isnull().sum()
# data.isnull().sum().sum()

# data.columns
# from dataclasses import dataclass
# from pathlib import Path

# @dataclass(frozen=True)

# class DataValdiationConfig:
#     root_dir = Path
#     status_file = str
#     unzip_data_dir = Path
#     all_schema = dict


# from mlProject.constants import *
# from mlProject.utils.common import read_yaml, crete_directories


# class CnfigurationManager:
#     def __init__(
#             self,
#             cofig_filpath = CONFIG_FILEPATH
#             params_filepath = PARAMS_FILEPATH
#             schema_filepath = SCHEMA_FILEPATH

#             self.config = read_yaml(config_filepath)
#             self.params = read_yaml(params_filepath)
#             self.shema = read_yaml(schema_filpath)


#     )


#     create_directories([self.config_artifacts_rooot])

# def valdiaton_dta_cofig_get(self):
#         config = self.config.data_validation
#         schema = self.schema.columns
#         create_directories([self.config_artifacts_rooot])

        
#         datavalidtion_config = DataValdiationConfig(
#              rata_dir = config.unzip. = config_root_dir

#         )

#         return datavalidtion_config
    


# import numpy as np
# import pandas as pd

# from sklearn import svm
    
# import matplotlib.pyplot as plt
# import seaborn as sns

# recips = pd.read.csv("file.csv")
# recips.head()


# # now i am gonna plot the data into parts pkay

# sns.implot('floour', 'sugar', data=recips, hure='Type')
#     plett
#      = 'stel', 'fitreg = false', scatter_kews= ("s", 790)
    
# type_label = np.where(recipee['type'] =='Muffin', 0,1)
# recepie_feature = recepie_feature.columns.values[1:].tolist()
# recepie_feature

# ingredients = recepie[['flours', 'sugar']].value
# print(ingredients)


# # now i am gonna reting the model
# mdoel= svm.SVC(kernel = 'linear')
# model.fit(ingredients, type_label)

# # now gettin spearation of the model
# w = mdoel.coef_
# a = -w[0] / w[i]
# xx = np.linespace(30, 60)
# yy = a*xx -(model.integredients)

# b = model.support_vecorrs_[0]
# yy_down= kjdk


# x = data.iloc[:,-2]
# y = data.iloc[:,:2]
# print(data.columns)

# for i in x.columns:
#     x[i] = x[i].fillna(int(x[i].mean()))

# for i in x.columns:
#     print(x[i].isnull().sum())

    



# print("Hello world")

# def main():
#     hello("world")
#     goodbye("world")

# def hello(name):
#     print(f"hello, {name}")

# def goodbye(name):
#     print(f"goodbye, {name}")

# main()







# def main():
#     x = int(input("What is x? "))
#     print("x is squared", square(x))

# def square(n):
#     return n * n
# # main()

# if __name__ == "__name__":
#     main()




# url = input("URL: ").strip()
# username = url.removeprefix("https://twitter.com/")
# print(f"Username: {username}")



# name = input("Enter your name? ")
# hsoue = input("wehere is your house ? ")
# print(f"{name} from {hsoue}")\





# do the above work through the fucntion s

# def main():
#     name = get_name()
#     hosue = get_house()

#     print(f"{name} form {hosue}")


# def get_name():
#     return input("name: ")
# def get_house():
#     return input("house: ")


# if __name__ == "__main__":
#     main()




# class Student:
#     def __init__(self, name, house):
#         self.name = name
#         self.house = house

# def get_student():
#     name = input("name")
#     house = input("house")
#     student = Student(name, house)

#     return student

# def main():
#     Student = get_student()
#     print(f"{Student.name} form{Student.house}")
# if __name__ == "__main__":
#     main()



# import pygame
# import random

# # Screen size
# WIDTH, HEIGHT = 600, 600
# ROWS, COLS = 20, 20
# CELL_SIZE = WIDTH // COLS

# # Colors
# WHITE = (255, 255, 255)
# BLACK = (0, 0, 0)
# RED   = (255, 0, 0)
# GREEN = (0, 255, 0)

# pygame.init()
# win = pygame.display.set_mode((WIDTH, HEIGHT))
# pygame.display.set_caption("Maze Game")

# # Maze grid
# grid = [[1 for _ in range(COLS)] for _ in range(ROWS)]

# # Depth-First Search Maze Generator
# def generate_maze(x, y):
#     stack = [(x, y)]
#     grid[y][x] = 0

#     while stack:
#         x, y = stack[-1]
#         directions = [(x+2, y), (x-2, y), (x, y+2), (x, y-2)]
#         random.shuffle(directions)
#         carved = False

#         for nx, ny in directions:
#             if 0 <= nx < COLS and 0 <= ny < ROWS and grid[ny][nx] == 1:
#                 grid[ny][nx] = 0
#                 grid[y + (ny-y)//2][x + (nx-x)//2] = 0
#                 stack.append((nx, ny))
#                 carved = True
#                 break
#         if not carved:
#             stack.pop()

# # Generate maze
# generate_maze(0, 0)

# # Player position
# player_x, player_y = 0, 0

# # Game loop
# running = True
# clock = pygame.time.Clock()

# while running:
#     clock.tick(30)
#     win.fill(WHITE)

#     # Draw maze
#     for y in range(ROWS):
#         for x in range(COLS):
#             if grid[y][x] == 1:
#                 pygame.draw.rect(win, BLACK, (x*CELL_SIZE, y*CELL_SIZE, CELL_SIZE, CELL_SIZE))

#     # Draw goal
#     pygame.draw.rect(win, GREEN, ((COLS-1)*CELL_SIZE, (ROWS-1)*CELL_SIZE, CELL_SIZE, CELL_SIZE))

#     # Draw player
#     pygame.draw.rect(win, RED, (player_x*CELL_SIZE, player_y*CELL_SIZE, CELL_SIZE, CELL_SIZE))

#     # Events
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             running = False

#     # Controls
#     keys = pygame.key.get_pressed()
#     if keys[pygame.K_UP] and player_y > 0 and grid[player_y-1][player_x] == 0:
#         player_y -= 1
#     if keys[pygame.K_DOWN] and player_y < ROWS-1 and grid[player_y+1][player_x] == 0:
#         player_y += 1
#     if keys[pygame.K_LEFT] and player_x > 0 and grid[player_y][player_x-1] == 0:
#         player_x -= 1
#     if keys[pygame.K_RIGHT] and player_x < COLS-1 and grid[player_y][player_x+1] == 0:
#         player_x += 1

#     # Check win condition
#     if player_x == COLS-1 and player_y == ROWS-1:
#         print("You Win!")
#         running = False

#     pygame.display.update()

# pygame.quit()



# for i in range(1,6):
#     print("Day", i)

#     for j in range(1,9):
#         print(" ", j+8, " _ ", j+9)


# for i in range



# from collections import deque





# stack = [1,2,3,4,5]
# stack = deque[stack]
# print(stack)




# def name():
#     print("hello world")
# name()



# # def add(a,b):
# #     return a+b
# # a = int(input("enter number for the a"))
# # b = int(input("enter number for the b"))
# # print(a+b)



# # # add(a+b)







# # count =  0 
# # for count in range(10):
# #     print("i love oyu")
# #     count+=1



# # def function1(function):
# #     def wrapper():
# #         print("hello")
# #         function()
# #         print("kdjfkdjl")
# #     return wrapper
# # def function2():
# #     print("dfkjslfd")
# # function2 = function1(function2)
# # function2()




# # for i in range(200):
# #     print("I love you ")



# name = "professional"

# def pro():
#     # name = "kamal"
#     print(name)

# print(name)
# pro()




# x = 90
# def fun():
#     global x
#     x = 12
# fun()
# print(x)
 





# def f1():
#     x = 88
#     def f2():
#         print(x)
#     return f2
# myResult = f1()
# myResult()





# def name():
#     student = "pro"
#     def teacher():
#         print(student)
#     return teacher
# resutl = name()
# resutl()






# class car:
#     def __init__(self, userrand, usermodel):
#         pass
#         brand = userrand
#         model = usermodel

# myCar = car("tota", "pro")
# print(myCar.brand)
# print(myCar.model)





# a = int(input("Enter the number for a "))
# b = int(input("Enter the number for a "))



# import time
# def timer(func):
#     def wrapper(**kwargs):
#        start = time.time()
#        result =  func(**kwargs)
#        end = time.time()

#        print(f"{func.__name__} ran in {end-start} time" )
#        return result
#     return wrapper
# @timer
# def example(n):
#     time.sleep(n)
# example(2 )




# def debug(func):
#     def wrapppr():
#         return wrapppr

# def hello():
#     print("hello world")


# def greet(name, greeting = "hello"):
#     print(f"{greeting}, {name}")

# greet("cahi", greeting="hello chai")



# file = open('ramizas.py', 'w')
# import json
# def load_data():
#     try:
#         with open('youtube.txt', 'r') as file:
#             return json.load(file)
    
#     except: FileNotFoundError:
#     return []

# def safe_datahelper(vidoes):
#     with open('youtube.txt', 'w') as file:
#         json.dump(vidoes, file)

# def list_all_videos(videos):
#     for index, video in enumerate(videos, start=1):
#         print(f"{index}. ")
# def add_videos(videos):
#     name = input("enter your video")
#     time = input("enter your video time")

# def update_videos(videos):
#     pass

# def delet_videos(videos):
#     pass

# def main():
#     videos = load_data()
#     while True:
#         print("\n Youube Manager | choose a option")
#         print("1: List all youtube videos")
#         print("2. Add a youtube video")
#         print("3. Update the youtbe video details")
#         print("4. Delete the youtube video")
#         print("5. Exit the group")
#         choice = input("Enter your choice")

#         # if choice == '1':
#         match choice:
#             case '1':
#                 list_all_videos(videos)
#             case '2':
#                 add_videos(videos)
#             case '3':
#                 update_videos(videos)
#             case '4':
#                 delet_videos(videos)
#             case '5':
            #     break
            # case _:
            #     print("invalid   ")




















































# a = int(in
# 
# put("Enter the number here? "))
# print(a[])





























# num  = input("Enter the number here? ")
# biggest = int(num[0])
# smallest = int(num[0])

# for digit in num:
#     d = int(digit)

#     if d>biggest:
#         biggest = d
#     if d<smallest:
#         smallest = d
# print("Largest is ", biggest)
# print("smallest is", smallest)



# numbers =  [1,-2,3,4,5,-4,5,-6]
# positive_numbers = 0

# for num in numbers:
#     if num>0:
#         positive_numbers+=1
# print(positive_numbers)

# number  =  29;
# is_prime = True

# if number>1:
#     for i in range(2,number):
#         if(number%i) == 0:
#             is_prime = False
#             break
# print(is_prime)



# letter = input("ENter the letter? ")
# if letter in "aeiou" or letter in "AEIOU":
#     print("vowel")
# else:






#     print("Consonat")




# n = 3

# for i in range(1,11):
#     print(n ,"X", i , "=", n*i )




# n = 10
# for i in range(1,20):
#     print(n, "X" , i, "=", n*i)


# n =1
# i = 7
# while n<=10:
#     print(n, "X" , i, "=", n*i)
#     n+=1
    
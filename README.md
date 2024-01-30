# cat-and-dog-machine
This repository provides code and solutions for a cat-dog generator which is an example of Experience Learning algorithms. The  cat-dog generator and the experience learning are realized by python program (catdoggenerator.py, experience_chain.py,respectively).These are meant to exhibit the advantages of experiential learning. Before that, the experience learning must have the basis of cat and dog image recognition, so the cat and dog recognition model must be trained first (The programs training.py input_data.py and model.py are used to train a cat/dog recognition model, test.py employs the model to discern.)
The training dataset and the trained model for this project can be accessed through the following link.
link：https://pan.baidu.com/s/1OuocUHylGGReK3UYXiWmzQ?pwd=sjn2 
passcode：sjn2


# Environment
python 3.7

numpy 1.21.5

tensorflow 2.11.0

Pillow 9.5.0

# catdoggenerator
This program design a hypothetical device ————cat and dog generator.
The output of the cat/dog generator is not fixed in order to simulate the randomness in real life. It produces a picture of a cat when the input is 1, and a picture of a dog when the input is 2 with some probability. Importantly, it is completely unknown to the experience learning program. Then the experience learning is assigned to detect it and find its rule.
The folder named by "picture" contains images of the cat and dog.

# experience_chain.py
Experience Learning (EL) is a machine learning method for exploring the unknown, which can be typically applied to artificial intelligence robots (AIR). According to the theory of experience learning,  the program explores the tested object (here is the cat and dog generator)and records the probability of its output, utilizing it to make decisions. 
However, the experience learning must possess the capability of recognizing cat and dog. So the cat/dog recognition model needs to be trained before we can execute our experience learning algorithm.

# model.py
The model stucture of cat and dog recognition is stored in this file.

# input_data.py
The program for image reading during model training and testing is included in this file.

# trainig.py
It is a program designed for training a model to recognize dogs and cats.

# test.py
The file is a program that utilizes the trained model for image identification.






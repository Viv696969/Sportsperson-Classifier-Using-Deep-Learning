
# Sports Celebrity Image Classification Website using Tensorflow ,Keras and Django

* Collection of multiple images of 6 sport celebrities from google.
* Using Haar Cascades from OpenCv – Python extracted only the faces of the celebrities.
* Converted images to array and splited the data in training and testing using sklearn library.
* Using Tensorflow-Keras created a CNN model.

     * 2 layer Data Augmentation of RandomFlip and RandomRotation.
    * 3 convolutional layers with ‘relu’ activation function and kernel size of 3X3  followed by a Max Pooling layer.
    * 2 fully connected deep hidden layers with ‘relu’ activation function.
    * 87% testing accuracy
    * Softmax activation function for the output layer.
    * Loss function: sparse categorical crossentropy
    * Optimizer : Adam
    * 95% training accuracy
* Backend:Django
* Frontend: HTML,BOOTSTRAP
* Database for images : Sql-Lite3
* FUNCTIONALITIES:
    * Users can Try Random testing images.
    * Users can upload any image from the 6 celebrities to use the model.
    * Classifies very well on Images uploaded by users and displays classification report based on probability.


## 🔗 Links
[![linkedin](https://img.shields.io/badge/linkedin-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/vivek-chouhan-854055269/)




# YOLO (You Only Look Once)

YOLO is the state of art object detection alogithm.

- It is so fast that it has become alomst a standard way of detection object in the field of computer vsion.
- perviously people were using sliding window object detection.

Then more faster version were invented

- R CNN
- fast RCNN
- Faster RCNN
- 2015 YOLO was invited in 2015 which out perform all previous versions

## YOLO

- In image classification problem where you have to decied that image is dog or person suppose output by neuro network is dog 1 and person 0

### loocalization

- But in object Localization we are not telling which class is like dog we are also telling the bonding box or the postion of an object with in the image output = Dog + Bonding box

output of nuronetork is like this we have 2 vector

### Yolo paramerters

```
[pc,bx,by, bw, bh, c1, c2]
[1, 50, 70, 60, 70, 1, 0]

pc    => Probabilty of a class # If there is dog/ persion then 1 else 0
bx,by => are the codinate of the center
bw,bh => are the width and height of the box
c1    => class 1 # 1 ->  this class is detected
c2    => class 2 # 0 ->  means class is not detected
```

When we have no opebject in the images then vector should look like this

```
[pc,bx,by, bw, bh, c1, c2]
[0, -, -, -, -, -, -]

```

So `x_train` will be labeled image and `y_train` will be a vector

### What about multiple objects in an image?

If we have more than 2 bounding boxes then YOLO wil  divide the image into grid cell. It could be 4by 4 3*3 19*19 any thing. then object is expnding into multiple cell of grid then we try to find center pointof dog belogin to particlular grid.
so we have 4*4*7 7 is number of vector

See the alorith migth detect multiple bounding rectongle for a given object

- suppose a person have 3 bonding box
- we cannot just take max for each clas

- If we take max then it might not detect anothere person

we use a concept called IOU

### IOU (Intersection over Union)

iou = interection/unioun

Wwe have to find overlaping area to find overlaping we use IOU

- If completly ovelaping the value will be one
- if not ovelaing at all then  0
- if IOU is grater than percentile of bonding box then we kept which has max probabilty

This technique is also called no max suppreion.

### What if one single cell has center of two objects?

So insted of 7 dimention vectore how about we have 14 size vetor

- we have concatinate 2 vector box

## History

2016 YOLO V1

- In 2016 the first version of YOLO was invented vu Joseph Redman, santosh,ross, ali

- 2017 YOLO V2 (YOLO9000): They imove the speed. 67fps (joseph,ali)
- 2018 YOLO V3: after 3 joseph stoped becouse of miltery
- 2020 YOLO v4/pp YOLO V5:
- 2021 YOLO x /YOLOR

- 2023 YOLO v8

Idea of YOLO:

- A single network (single shot) for object detectopn.
- Remove complexity of mulitple models.we dont have to train mltiple times
- Rephrase object detection as the single regression problem.

why single shot?

- Becase we are going to pass image only once.Not like muliple time like RCNN

classification:

- If you have a tar that which you want to predict is called classfication,binary and mutiple

regression

- if target is cotinous then it regression Problem,eg Predicting the height of a persion

- Mae

## Steps in YOLO V1

1. Input Image

- size: Typically YOLOv1 takes an input image of size 448x448
- Preprocessing: The image is resized to fit modelss input dimensions while preserving the aspect ratio as much as possible.

2. Grid Division

- The input image is divided into a 7x7 grid.
- Each grid cell is responsible for detecting objects whose center falls within the cell.

448/7 each cell has 64 pixels

### Which cell is responsible for object detection?

The cell where the centre of the object falls, that is responsible for the object prediction.

### How targets calculated for trainging model?

- Calculating the grid poitions basd on realtive positions based on relative postions.
- This will reduce the number scale to lower numbers

relative postion:

- Loss Function: A method to evaluate how well your algorithm models your dataset. If your predictions are totally off, your loss function will output a higher number.
- Handling Overfit Models: Strategies to reduce overfitting include adding more data, reducing the complexity of the model, and using techniques like cross-validation.

Can you explain what a loss function is and how it impacts the training of machine learning models?
A loss function, also known as a cost function, is a critical component in training machine learning models. It quantifies the difference between the predicted values by the model and the actual values in the dataset. This function provides a measure of how well the model is performing; the lower the loss, the better the model's predictions align with the true data. During the training process, the goal is to minimize this loss through various optimization techniques, such as gradient descent. The choice of loss function can significantly affect the model's training process and its ultimate performance, as it guides the optimization algorithm on how to adjust the model parameters effectively to reduce prediction errors. Common examples of loss functions include mean squared error for regression tasks and cross-entropy loss for classification tasks.

## What is semi-supervised machine learning?

Semi-supervised learning is the blend of supervised and unsupervised learning. The algorithm is trained on a mix of labeled and unlabeled data. Generally, it is utilized when we have a very small labeled dataset and a large unlabeled dataset.

In simple terms, the unsupervised algorithm is used to create clusters and by using existing labeled data to label the rest of the unlabelled data. A Semi-supervised algorithm assumes continuity assumption, cluster assumption, and manifold assumption.

It is generally used to save the cost of acquiring labeled data. For example, protein sequence classification, automatic speech recognition, and self-driving cars

## How do you choose which algorithm to use for a dataset?

part from the dataset, you need a business use case or application requirements. You can apply supervised and unsupervised learning to the same data.

Generally:

Supervised learning algorithms require labeled data.
Regression algorithms require continuous numerical targets
Classification algorithms require categorical targets
Unsupervised learning algorithms require unlabeled data.
Semi-supervised learning requires the combination of labeled and unlabeled datasets.
Reinforcement learning algorithms require environment, agent, state, and reward data.

Explain the K Nearest Neighbor algorithm.
The K Nearest Neighbor (KNN) is a supervised learning classifier. It uses proximity to classify labels or predict the grouping of individual data points. We can use it for regression and classification. KNN algorithm is non-parametric, meaning it doesn't make an underlying assumption of data distribution.

## In the KNN classifier

We find K-neighbors nearest to the white point. In the example below, we chose k=5.
To find the five nearest neighbors, we calculate the euclidean distance between the white point and the others. Then, we chose the 5 points closest to the white point.
There are three red and two green points at K=5. Since the red has a majority, we assign a red label to it.

## What is overfitting in machine learning, and how can it be avoided?

Overfitting occurs when a model performs well on training data but fails to generalize to unseen data because it has memorized the training data instead of learning the underlying patterns. It can be avoided by:

Using cross-validation techniques.
Applying regularization (L1, L2).
Reducing model complexity.
Collecting more training data or using data augmentation.

### What is the difference between supervised and unsupervised learning?

Supervised Learning: The model is trained on labeled data, where the target variable is known. Examples include classification and regression.
Unsupervised Learning: The model is trained on unlabeled data to find patterns or groupings. Examples include clustering and dimensionality reduction

## What is a confusion matrix, and why is it useful?

A confusion matrix is a table used to evaluate the performance of a classification model. It shows the counts of true positives, true negatives, false positives, and false negatives. It is useful for calculating metrics like accuracy, precision, recall, and F1 score.

## What is the difference between parametric and non-parametric models?

Parametric Models: These make assumptions about the data’s underlying distribution and have a fixed number of parameters (e.g., Linear Regression).

Non-Parametric Models: These make no assumptions about data distribution and can adapt to complexity as more data is added (e.g., K-Nearest Neighbors).

## What is the bias-variance tradeoff in machine learning?

The bias-variance tradeoff refers to the balance between a model’s ability to capture complex patterns (low bias) and its sensitivity to fluctuations in the training data (low variance). A good model achieves a balance by minimizing both bias and variance to avoid underfitting and overfitting.

## When you have a small dataset, suggest a way to train a convolutional neural network  

If you do not have enough data to train a convolutional neural network, you can use transfer learning to train your model and get state-of-the-art results. You need a pre-trained model which was trained on a general but larger dataset. After that, you will fine-tune it on newer data by training the last layers of the models.

Transfer learning allows data scientists to train models on smaller data by using fewer resources, computing, and storage. You can find open-source pre-trained models for various use cases easily, and most of them have a commercial license which means you can use them to create your application

## Q1. What is the main difference between Python lists and NumPy arrays in ML workflows?

Lists are flexible containers for mixed data types, but are slow for numerical computation. NumPy arrays store homogeneous data in contiguous memory, enabling vectorization and fast matrix operations crucial for ML tasks like batch gradient updates.

Tip: Keep this distinction in mind, using lists instead of arrays in ML code can drastically increase runtime.

## Q2. Why is NumPy preferred over pure Python for ML computations?

NumPy uses optimized C libraries under the hood, offering vectorized operations and broadcasting. This drastically reduces loop overhead, making ML algorithms like linear regression or k-means clustering faster and more scalable.

Tip: If a loop looks slow in Python, rewrite it with NumPy, since it cuts execution time by 10–100×.

## Q4. How does vectorization improve ML code?

Vectorization allows entire arrays or matrices to be processed at once, avoiding Python loops. For instance, updating all weights in a neural network can be expressed in one NumPy operation, improving speed and readability.

Q5. What are potential pitfalls of broadcasting in NumPy?

Q3. What is the bias-variance tradeoff?

Bias represents underfitting (oversimplification), while variance represents overfitting (too much complexity). The tradeoff is finding a balance where the model generalizes well (balance between overfitting and underfitting). Techniques like regularization and ensemble methods address this.

Q5. What role does cross-validation play in ML evaluation?

Cross-validation splits the dataset into multiple folds, training and testing on each to reduce variance in evaluation. It provides a more reliable performance estimate than a single train/test split.

Tip: Mention KFold or StratifiedKFold from scikit-learn, they show you know practical implementation details.

## 1. What is machine learning and how does it work?

Machine learning is a field of artificial intelligence focused on building algorithms that enable computers to learn from data without explicit programming. It uses algorithms to analyse and identify patterns in data, and make predictions based on those patterns.

2. What is overfitting in machine learning and how can it be avoided?
1. Overfitting: It occurs when a model not only learns the true patterns in the training data but also memorizes the noise or random fluctuations. This results in high accuracy on training data but poor performance on unseen/test data.

Ways to Avoid Overfitting:

Early Stopping: Stop training when validation accuracy stops improving, even if training accuracy is still increasing.
Regularization: Apply techniques like L1 (Lasso) or L2 (Ridge) regularization which add penalties to large weights to reduce model complexity.
Cross-Validation: Use k-fold cross-validation to ensure the model generalizes well.
Dropout (for Neural Networks): Randomly drop neurons during training to prevent over-reliance on specific nodes.
Simpler Models: Avoid overly complex models when simpler ones can explain the data well.
2. Underfitting: It occurs when a model is too simple to capture the underlying patterns in the data. This leads to poor accuracy on both training and test data.

Ways to Avoid Underfitting:

Use a More Complex Model: Choose models with higher complexity to learn pattern like decision trees, neural networks, etc.
Add Relevant Features: Include meaningful features that better represent the data.
Reduce Regularization: Too much regularization can restrict the model’s ability to learn.
Train Longer: Allow the model more epochs or iterations to properly learn patterns.

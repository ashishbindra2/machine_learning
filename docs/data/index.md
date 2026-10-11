# Data

## Datasets: Class-imbalanced datasets

In the real world, class-imbalanced datasets are far more common than class-balanced datasets.

For example, in a dataset of credit card transactions, fraudulent purchases might make up less than 0.1% of the examples.

Similarly, in a medical diagnosis dataset, the number of patients with a rare virus might be less than 0.01% of the total examples. In a class-imbalanced dataset:

- The more common label is called the majority class.
  - For example, given a dataset containing 99% negative labels and 1% positive labels, the negative labels are the majority class.
- The less common label is called the minority class.
  - For example, given a dataset containing 99% negative labels and 1% positive labels, the positive labels are the minority class.

For example, consider the class-imbalanced dataset illustrated in Figure 6 in which:

- 200 labels are in the majority class.
- 2 labels are in the minority class.

> Note: Accuracy is usually a poor metric for assessing a model trained on a class-imbalanced dataset

Step 1: Downsample the majority class
Downsampling means training on a disproportionately low percentage of majority class examples

Step 2: Upweight the downsampled class
Downsampling introduces a prediction bias by showing the model an artificial world where the classes are more balanced than in the real world. To correct this bias, you must "upweight" the majority classes by the factor to which you downsampled. Upweighting means treating the loss on a majority class example more harshly than the loss on a minority class example.


# ML-Research-Linear-Separability-
In this study, we explore methods to identify linearly separable SAT formulas.

Linear separability is the quality of a binary classified dataset in which the two groups of data points can be fully separated by a hyperplane. Linearly separable datasets are useful in machine learning, notably with the Perceptron algorithm.

Our study of linear separability comes from the context of SAT formulas, in which the data points are the possible variable assignments of the SAT formula, and the binary classification is the truth value of that variable assignment. To classify SAT formulas as linearly separable, we needed an efficient algorithm that could handle large SAT formulas with many variable dimensions.

While SAT is generally NP-complete, linearly separable SAT formulas can be easier to solve due to their inherent geometric properties. It is also significantly simpler to train ML models based on linear classifiers (e.g. SVM) and even neural networks in some cases. Fortunately, these problems naturally exist well outside of contrived examples like tautologies. In this study, we explore methods to identify linearly separable SAT formulas.

The main objective of our work was to develop an efficient algorithm, based on a recent paper that used the minimum covering ball problem [1], that tested linear separability of SAT formulas efficiently. To do so, we used already existing methods and also developed a new method based on the sphere model approach.

A secondary objective of the project was to explore how G2SAT, a deep generative framework, generated ‘natural’ SAT formulas, and whether those formulas were linear separable [2].

Overall, our learning objective was to familiarize ourselves with topics ranging from the theory of linear separability to machine learning related to SAT formulas.

![image](https://github.com/user-attachments/assets/038087c1-dfb6-40f9-9c90-22d9a3844119)

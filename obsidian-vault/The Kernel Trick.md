---
created:
  - 2024-10-04T15:02
modified: 2024-10-06 15:22
tags:
  - statistics
  - svm
  - kernel
  - model
  - regression
  - classification
  - rbf
type:
  - note
status:
  - completed
---
[[The Kernel Trick]] refers to the use of a function (a _kernel function_) in order to calculate the value of the dot product between 2 transformed/projected vectors $\phi(X)^T\phi(Y)$ through operations on the untransformed/unprojected vectors ($X$ and $Y$) in their original space.
A famous usage of this is in [[Support Vector Machines (SVMs)]].

Here is an example using a _polynomial kernel_ :
$$K(X,Y) = (1+X^TY)^2$$
For 2-dimensional $X$ and $Y$:

$$\begin{array}{lcl}
X &=& (x_1, x_2) \\
Y &=& (y_1, y_2) \\
K(X, Y) &=& (1 + x_1y_1 + x_2y_2)^2 \\
&=& 1 + x_1^2y_1^2 + 2x_1y_1 + 2x_1y_1x_2y_2 + 2x_2y_2 + x_2^2y_2^2\\
\end{array}$$
This result $K(X,Y)$ is the result of the dot product between $\phi(X)$ and $\phi(Y)$ where the project/transformation function is

$$\phi(X)=(1,x_1^2, x_2^2, \sqrt{2}x_1, \sqrt{2}x_2, \sqrt{2}x_1x_2)$$
Note that this calculation involved calculating the value of the dot product without transforming the vectors first. This technique can result in massive efficiency gains for projections into high dimensional spaces (e.g. [RBF kernel](https://en.wikipedia.org/wiki/Radial_basis_function_kernel) maps vectors into an infinite-dimensional feature space). 
## References
* https://blog.dailydoseofds.com/p/why-is-kernel-trick-called-a-trick
## Related
* [[Support Vector Machines (SVMs)]]
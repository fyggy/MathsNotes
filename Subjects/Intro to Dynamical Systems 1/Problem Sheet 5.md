[[LinearAlgGeo2 HW5.pdf]]
1. 
We have that the characteristic polynomial of $M$ is
$$
\chi(\lambda)=(3-\lambda)(1-\lambda)+1=\lambda^{2}-4\lambda+4=(\lambda-2)^{2}
$$
Since $M\neq 2I$, then the minimum polynomial of $M$ is also ${} \mu(\lambda)=(\lambda-2)^{2} {}$. Therefore, the Jordan normal form of $M {}$ is
$$
M=P \begin{pmatrix}2 & 1 \\ 0 & 2 \end{pmatrix} P^{-1}
$$
Now we want to find generalised eigenvectors $\mathbf{v}_{1} {}$ and $\mathbf{v}_{2} {}$ with
$$
\begin{align}
 (M-2 I)\mathbf{v}_{1} & =0 \\
	(M-2I)\mathbf{v}_{2} & =\mathbf{v}_{1}  
 \end{align}
$$

so
$$
\begin{align}
 \left( \begin{pmatrix}3 & 1 \\ -1 & 1 \end{pmatrix} -\begin{pmatrix}2 & 0 \\ 0 & 2 \end{pmatrix}   \right) \mathbf{v}_{1} & =0 \\
\begin{pmatrix}1 & 1 \\ -1 & -1 \end{pmatrix} \mathbf{v}_{1} & =0 \\
\begin{pmatrix}1 & 1 \\ 0 & 0 \end{pmatrix} \mathbf{v}_{1} & =0
 \end{align}
$$
so if ${} \mathbf{v}_{1}=(x,\, y) {}$, then ${} x+y=0 {}$. Now ${} x=1,\, y=-1 {}$ satisfies this. Therefore
$$
\mathbf{v}_{1}=\begin{pmatrix} 1 \\ -1 \end{pmatrix} 
$$
Now 
$$
\begin{pmatrix}1 & 1 \\ -1 & -1 \end{pmatrix} \mathbf{v}_{2}=\begin{pmatrix} 1 \\ -1 \end{pmatrix} 
$$Now if ${} \mathbf{v}_{2}=(x,\, y) {}$, then
$$
\begin{pmatrix} x+y \\  -x-y\end{pmatrix} =\begin{pmatrix} 1 \\ -1 \end{pmatrix} 
$$
and ${} x+y=1 {}$. We have ${} x=1 {}$, ${} y=0 {}$ satisfying this. Now we have 
$$
P=(\mathbf{v}_{1},\, \mathbf{v}_{2})=\begin{pmatrix}1 & 1 \\ -1 & 0 \end{pmatrix} 
$$
and
$$
\begin{pmatrix}2 & 1 \\ 0 & 2 \end{pmatrix} =P^{-1}MP
$$
Now from the form of the Jordan normal form, we have that
$$
A\mathbf{v}_{1}e^{2t}+B(t\mathbf{v}_{1}+\mathbf{v}_{2})e^{2t}
$$
is the general solution
2. 
a)
![[Pasted image 20240226125749.png]]
b)
We have fixed points at ${} x=2 {}$ and ${} x=3 {}$. Both of them are unstable
c) i)
$$
\begin{align}
 \tau  & = \int_{4}^{\infty} \frac{1}{(x-2)^{2}(x-3)} \ud x    \\
 & =\int_{4}^{\infty} \frac{A}{x-2}+\frac{B}{(x-2)^{2}}+\frac{C}{x-3} \ud x 
 \end{align}
$$
We have that
$$
\begin{align}
 A(x-2)(x-3)+B(x-3)+C(x-2)^{2} & =1   \\
Ax^{2}-5Ax+6A+Bx-3B+Cx^{2}-4Cx+4C & =1 \\
	(A+C)x^{2}+(-5A+B-4C)x+(6A-3B+4C) & =1
 \end{align}
$$
so 
$$
\begin{align}
 A+C & =0  \\
-5A+B-4C  & =0 \\
6A-3B+4C & =1
 \end{align}
$$
so
$$
\begin{align}
  & \left(\begin{array}{ccc|c}
1 & 0 & 1 & 0 \\
-5 & 1 & -4 & 0 \\
6 & -3 & 4 & 1
\end{array}\right)\to{} \left(\begin{array}{ccc|c}
1 & 0 & 1 & 0 \\
-5 & 1 & -4 & 0 \\
1 & -2 & 0 & 1
\end{array}\right)\to{} \left(\begin{array}{ccc|c}
1 & 0 & 1 & 0 \\
0 & 1 & 1 & 0 \\
0 & -2 & -1 & 1
\end{array}\right)  \\
 & \to{} \left(\begin{array}{ccc|c}
1 & 0 & 1 & 0 \\
0 & 1 & 1 & 0 \\
0 & 0 & 1 & 1
\end{array}\right) \to{} \left(\begin{array}{ccc|c}
1 & 0 & 0 & -1 \\
0 & 1 & 0 & -1 \\
0 & 0 & 1 & 1
\end{array}\right)
 \end{align}
$$
so
$$
\begin{align}
 \tau & =\int_{4}^{\infty} -\frac{1}{x -2}- \frac{1}{( x-2 )^{2}}+\frac{1}{x-3} \ud x  \\
 & =-\int_{4}^{\infty} \frac{1}{x-2} \ud x  -\int_{4}^{\infty} \frac{1}{( x-2 )^{2}} \ud x +\int_{4}^{\infty} \frac{1}{x-3} \ud x  \\
 & =-[\ln(x-2)]_{4}^{\infty}-\left[- \frac{1}{x-2} \right]_{4}^{\infty}+[\ln (x-3)]_{4}^{\infty} \\
 & =\left[ \frac{1}{x-2}+\ln(x-3)-\ln(x-2) \right]_{4}^{\infty} \\
 & =\left[ \frac{1}{x-2}+\ln\left( \frac{ x-3 }{ x-2 } \right) \right]_{4}^{\infty} \\
 & =-\frac{1}{4-2}-\ln\left( \frac{ 4-3 }{ 4-2 } \right)+\lim_{x\tto \infty} \left( -\frac{1}{x-2} \right)+\lim_{x\tto \infty} \ln\left( \frac{ x-3 }{ x-2 } \right) \\
 & =0.19314\dots+0+\ln\left(\lim_{x\tto \infty} \frac{ x-3 }{ x-2 }  \right) \\
 & =0.19314\dots
 \end{align}
$$
ii)
like before we have
$$
\begin{align}
 \tau & =\left[ \frac{1}{x-2}+\ln\left( \frac{ x-3 }{ x-2 } \right) \right]_{5 /2}^{2}  \\
 \end{align}
$$
Note that ${} \frac{ x-3 }{ x-2 } {}$ is negative for the entire interval ${} [5 /2,\, 2] {}$, so $\tau$ cannot exist. Therefore, ${} \tau=\infty {}$.
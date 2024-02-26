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
![[Pasted image 20240226125749.png#]]

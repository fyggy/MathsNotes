[[LinearAlgGeo2 HW5.pdf]]
2. 
a)
The characteristic polynomial of ${} A {}$ is
$$
\begin{align}
 \chi(\lambda) & =(3-\lambda)\cdot (1-\lambda)(-\lambda)+0+1\cdot (-(1-\lambda)(-2))   \\
 & =-\lambda^{3}+4\lambda^{2}-3\lambda+2-2\lambda \\
 & =-\lambda^{3}+4\lambda^{2}-5\lambda+2 \\
 & =-(\lambda-1)^{2}(\lambda-2)
 \end{align}
$$
We check if
$$
\begin{align}
 (A-I)(A-2I)  & =\begin{pmatrix}2 & 0 & 1 \\ 0 & 0 & 0 \\ -2 & 0 & -1 \end{pmatrix} \begin{pmatrix}1 & 0 & 1 \\ 0 & -1 & 0 \\ -2 & 0 & -2 \end{pmatrix}  \\
 & =\begin{pmatrix}0 & 0 & 0 \\ 0 & 0 & 0 \\ 0 & 0 & 0 \end{pmatrix}  
 \end{align}
$$
so the minimum polynomial of ${} A {}$ is ${} \mu(\lambda)=(\lambda-1)(\lambda-2) {}$.
b)
The characteristic polynomial of $B$ is
$$
\begin{align}
 \chi(\lambda) & =(5-\lambda)\left( (3-\lambda)(3-\lambda) -9\right)  \\
  & =(5-\lambda)(\lambda^{2}-6\lambda+9-9) \\
 & =5\lambda^{2}-30\lambda-\lambda^{3}+6\lambda^{2} \\
 & =-\lambda^{3}+11\lambda^{2}-30\lambda \\
 & =-\lambda(\lambda-5) (\lambda-6)
 \end{align}
$$
This is semisimple, so $B {}$ is diagonalisable and the minimum polynomial ${} \mu(\lambda)=\chi(\lambda) {}$
3. 
a)
$$
\begin{pmatrix}
2 & 0 & 0 & 0 \\
0 & 2 & 0 & 0 \\
0 & 0 & -1 & 0 \\
0 & 0 & 0 & -1
\end{pmatrix}
$$
b)
$$
\begin{pmatrix}
2 & 0 & 0 & 0 \\
0 & 2 & 0 & 0 \\
0 & 0 & -1 & 1 \\
0 & 0 & 0 & -1
\end{pmatrix}
$$
4. 
a)
$$
T_{1}=\begin{pmatrix}0 & 0 & 0 \\ 0 & 2 & 0 \\ 0 & 0 & 0 \end{pmatrix} 
$$
b)
$$
T_{2}=\begin{pmatrix}0 & 0 & 1 \\ 0 & 2 & 0 \\ 0 & 0 & 0 \end{pmatrix} 
$$
We see that the characteristic polynomials 
$$
\chi_{T_{1}}(\lambda)=\chi_{T_{2}}(\lambda)=-\lambda^{2}(\lambda-2)
$$
Now note that
$$
T_{1}(T_{1}-2I)=\begin{pmatrix}0 & 0 & 0 \\ 0 & 2 & 0 \\ 0 & 0 & 0 \end{pmatrix} \begin{pmatrix}-2 & 0 & 0 \\ 0 & 0 & 0 \\ 0 & 0 & -2 \end{pmatrix} =0
$$
So the minimum polynomial of $T_{1}$ is ${} \mu_{T_{1}}(\lambda)=\lambda(\lambda-2) {}$. We see, however, that
$$
\begin{align}
T_{2}(T_{2}-2I)=\begin{pmatrix}0 & 0 & 1 \\ 0 & 2 & 0 \\ 0 & 0 & 0 \end{pmatrix} \begin{pmatrix}-2 & 0 & 1 \\ 0 & 0 & 0 \\ 0 & 0 & -2 \end{pmatrix} =\begin{pmatrix}0 & 0 & -2 \\ 0 & 0 & 0 \\ 0 & 0 & 0 \end{pmatrix} \neq 0
\end{align}
$$
so the minimum polynomial of $T_{2}$ is ${} \mu_{T_{2}}(\lambda)=\chi_{T_{2}}(\lambda) {}$
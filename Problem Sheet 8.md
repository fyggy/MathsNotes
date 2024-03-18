[[HWsheet8-24.pdf]]
3. 
Let $A,\, B {}$ be unitary linear transformations. Then 
$$
\tilde{A}=A^{-1},\, \qquad \tilde{B}=B^{-1}
$$
and so 
$$
\begin{align}
 (x,\, \tilde{AB}y) & =(ABx,\, y)   \\
 & =(\tilde{A}^{-1}\tilde{B}^{-1}x,\, y) \\
 & =(\tilde{B}^{-1}x,\, \tilde{A}y) \\
 & =(x,\, \tilde{B}\tilde{A}y) \\
\Rightarrow \quad \tilde{AB} & =\tilde{B} \tilde{A}
 \end{align}
$$
since ${} ({}\cdot{} ,\, {}\cdot {}) {}$ is non-degenerate. Therefore, 
$$
\begin{align}
\tilde{AB} & =\tilde{B}\tilde{A} \\
 & =B^{-1}A^{-1} \\
 & =(AB)^{-1}
\end{align}
$$
and so ${} AB {}$ is unitary. 
6. 
a)
$$
\tr  A=0=\tr  B
$$

$$
\tr  A^{2}=\tr  \begin{pmatrix}1 & 0 \\ 0 & 1 \end{pmatrix} =2=\tr  \begin{pmatrix}1 & 0 \\ 0 & 1 \end{pmatrix} =\tr  B^{2}
$$
and
$$
\tr  A\tilde{A}=\tr  \begin{pmatrix}0 & -1 \\ 1 & 0 \end{pmatrix} =0=\tr  \begin{pmatrix}0 & 1 \\ 1 & 0 \end{pmatrix} =\tr  B\tilde{B}
$$
so $A {}$ and $B {}$ are unitarily equivalent.
b)
No, as
$$
\tr  A^{2}=\tr  \begin{pmatrix}1 & 0 \\ 0 & 1 \end{pmatrix} =2\neq-2\tr \begin{pmatrix}-1 & 0 \\ 0 & -1 \end{pmatrix}=\tr  B^{2}
$$
c)
No, as they don't have the same rank
d)
Yes, see that
$$
\begin{pmatrix}0 & 1 & 0 \\ -1 & 0 & 0 \\ 0 & 0 & 1 \end{pmatrix} \begin{pmatrix} 1 \\ i \\ 0 \end{pmatrix} =\begin{pmatrix} i  \\ -1 \\ 0 \end{pmatrix} =i \begin{pmatrix} 1 \\ i \\ 0 \end{pmatrix} 
$$
$$
\begin{pmatrix}0 & 1 & 0 \\ -1 & 0 & 0 \\ 0 & 0 & 1 \end{pmatrix} \begin{pmatrix} 1 \\ -i \\ 0 \end{pmatrix} =\begin{pmatrix} -i \\ -1 \\ 0 \end{pmatrix} =-i \begin{pmatrix} 1 \\ -i \\ 0 \end{pmatrix} 
$$
and finally
$$
\begin{pmatrix}0 & 1 & 0 \\ -1 & 0 & 0 \\ 0 & 0 & 1 \end{pmatrix} \begin{pmatrix} 0 \\ 0 \\ 1 \end{pmatrix} =\begin{pmatrix} 0 \\ 0 \\ 1 \end{pmatrix} =1 \begin{pmatrix} 0 \\ 0 \\ 1 \end{pmatrix} 
$$
and so
$$
\frac{1}{\sqrt{2}}\begin{pmatrix} 1 \\ i \\ 0 \end{pmatrix} ,\, \quad \frac{1}{\sqrt{2}}\begin{pmatrix} 1 \\ -i \\ 0 \end{pmatrix} ,\, \quad \begin{pmatrix} 0 \\ 0 \\ 1 \end{pmatrix} 
$$
is an orthonormal basis and is unitarily diagonalisable. 
e)

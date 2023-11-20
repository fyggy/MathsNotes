7. 
a) i)
Let ${} \alpha,\, \beta \in \mathbb{F} {}$, and let ${} p,\, q \in  \mathbb{P}_{4} {}$. We see that
$$
\begin{align}
D(\alpha p+\beta q) & =\frac{d}{dx} (\alpha p+\beta q) \\
 & =\frac{d}{dx} \alpha p+\frac{d}{dx} \beta q \\
 & =\alpha \frac{d}{dx} p+\beta \frac{d}{dx} q \\
 & =\alpha D(p)+\beta D(q)
\end{align}
$$
Therefore, $D$ is a linear map.

ii)
Let ${} \alpha,\, \beta \in \mathbb{F} {}$, and let $p,\, q \in \mathbb{P}_{3}$. We see that
$$
\begin{align}
 J(\alpha p+\beta q) & =\int_{0}^{x} (\alpha p+\beta q) \ud t    \\
 & =\int_{0}^{x} \alpha p \ud t+\int_{0}^{x} \beta q \ud t \\
 & =\alpha \int_{0}^{x} p \ud t +\int_{0}^{x} q \ud t \\
  & =\alpha J(p)+\beta J(q)
 \end{align}
$$
Therefore, $J {}$ is a linear map.

b)
Let ${} p(x)=q(x)=x {}$. Now note that 
$$
\begin{align}
F(p+q)(x) & =\left( \frac{d}{dx} (p(x)+q(x)) \right)^{2} \\
 & =(p'(x)+q'(x))^{2} \\
 & =p'(x)^{2}+q'(x)^{2}+2p'(x)q'(x) \\
 & =1^{2}+1^{2}+2\cdot 1\cdot 1 \\
 & =4
\end{align}
$$
But
$$
\begin{align}
 F(p)(x)+F(q)(x)  & =(p'(x))^{2}+(q'(x))^{2} \\
 & =1^{2}+1^{2} \\
 & =2 
 \end{align}
$$
and $2\neq 4$, so $F$ is not linear

c)
We see that
$$
\begin{align}
 D\ 1  & =0 & & =0\cdot 1+0\cdot x+0\cdot x^{2}+0\cdot x^{3}\\
Dx & =1 &  & =1\cdot 1+0\cdot x+0\cdot x^{2}+0\cdot x^{3} \\
Dx^{2} & =2x &  & =0\cdot 1+2\cdot x+0\cdot x^{2}+0\cdot x^{3} \\
Dx^{3} & =3x^{2} &  & =0\cdot 1+0\cdot x+3\cdot x^{2}+0\cdot x^{3} \\
Dx^{4} & =4x^{3} &  & =0\cdot 2+0\cdot x+3\cdot x^{2}+2\cdot x^{3}
 \end{align}
$$
So the matrix of $D$ is
$$
\begin{pmatrix}
0 & 1 & 0 & 0 & 0 \\
0 & 0 & 2 & 0 & 0 \\
0 & 0 & 0 & 3 & 0 \\
0 & 0 & 0 & 0 & 4
\end{pmatrix}
$$

Now for the matrix of $J$, we see that
$$
\begin{align}
J \ 1 & =x &  & =0\cdot 1+1\cdot x+0\cdot x^{2}+0\cdot x^{3}+0\cdot x^{4} \\
Jx & =\frac{x^{2}}{2} &  & =0\cdot 1+0\cdot x+\frac{1}{2}\cdot x^{2}+0\cdot x^{3}+0\cdot x^{4} \\
Jx^{2} & =\frac{x^{3}}{3} &  & =0\cdot 1+0\cdot x+0\cdot x^{2}+\frac{1}{3}\cdot x^{3}+0\cdot x^{4} \\
Jx^{3} & =\frac{x^{4}}{4} &  & =0\cdot 1+0\cdot x+0\cdot x^{2}+0\cdot x^{3}+\frac{1}{4}\cdot x^{4}
\end{align}
$$
So the matrix of $J {}$ is
$$
\begin{pmatrix}
0 & 0 & 0 & 0 \\
1 & 0 & 0 & 0 \\
0 & \frac{1}{2} & 0 & 0 \\
0 & 0 & \frac{1}{3} & 0 \\
0 & 0 & 0 & \frac{1}{4}
\end{pmatrix}
$$
d)
Calculating:
$$
DJ=\begin{pmatrix}
0 & 1 & 0 & 0 & 0 \\
0 & 0 & 2 & 0 & 0 \\
0 & 0 & 0 & 3 & 0 \\
0 & 0 & 0 & 0 & 4
\end{pmatrix}
\cdot \begin{pmatrix}
0 & 0 & 0 & 0 \\
1 & 0 & 0 & 0 \\
0 & \frac{1}{2} & 0 & 0 \\
0 & 0 & \frac{1}{3} & 0 \\
0 & 0 & 0 & \frac{1}{4}
\end{pmatrix}=\begin{pmatrix}
1 & 0 & 0 & 0 \\
0 & 1 & 0 & 0 \\
0 & 0 & 1 & 0 \\
0 & 0 & 0 & 1
\end{pmatrix}
$$
and
$$
JD=
\begin{pmatrix}
0 & 0 & 0 & 0 \\
1 & 0 & 0 & 0 \\
0 & \frac{1}{2} & 0 & 0 \\
0 & 0 & \frac{1}{3} & 0 \\
0 & 0 & 0 & \frac{1}{4}
\end{pmatrix}\cdot \begin{pmatrix}
0 & 1 & 0 & 0 & 0 \\
0 & 0 & 2 & 0 & 0 \\
0 & 0 & 0 & 3 & 0 \\
0 & 0 & 0 & 0 & 4
\end{pmatrix}
=\begin{pmatrix}
0 & 0 & 0 & 0 & 0 \\
0 & 1 & 0 & 0 & 0 \\
0 & 0 & 1 & 0 & 0 \\
0 & 0 & 0 & 1 & 0 \\
0 & 0 & 0 & 0 & 1
\end{pmatrix}
$$
Therefore, these maps are *kind of* inverses of each other. Since neither are square, they cannot be actual inverses. However, they lead to the identity matrix in $\mathbb{P}_{4} {}$ the case of ${} DJ$ and the identity matrix missing the first entry in $\mathbb{P}_{5}$ in the case of $JD {}$. 

This is expected, as ${} D$ is not injective; ${} D(1)=0=D(2) {}$. However, when differentiating, only the final coefficient is lost, so only information about that is lost. This is why only the first entry in $JD$ is missing. In the case of $DJ$, however, no information is lost, as the constant term gets elevated to a factor of ${} x {}$ by $J {}$, which is then preserved by ${} D {}$.
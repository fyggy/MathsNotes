3. a)
Let $A:\mathbb{R}^{3}\to{}\mathbb{R}^{5} {}$ with 
$$
\begin{pmatrix} a \\ b \\ c \end{pmatrix} \mapsto \begin{pmatrix} a \\ b \\ c \\ 0 \\0  \end{pmatrix} 
$$
$A$ is injective, as required
b)
This is impossible, as the map is surjective, so ${} \im A=\mathbb{R}^{3} {}$, so ${} r(A)=3 {}$, and we know that ${} r(A)+n(A)=\dim \mathbb{R}^{4}=4 {}$, so ${} n(A)=1\neq 3=r(A) {}$
c)
$$
A:\mathbb{R}^{3}\to{}\mathbb{R}^{3}
$$
mapping 
$$
\begin{pmatrix} a \\ b \\ c \end{pmatrix} \mapsto \begin{pmatrix} a \\ 0 \\ 0 \end{pmatrix} 
$$
d)
$$
A:\mathbb{R}^{3}\to{}\mathbb{R}^{3}
$$
mapping
$$
\begin{pmatrix} a \\ b \\ c \end{pmatrix} \mapsto \begin{pmatrix} 0 \\ b \\ c \end{pmatrix} 
$$
4. 
a)
$$
\begin{align}
 Tg(t)=T(t+1) & =\frac{d^{2}}{dt^{2}} (t+1)+t\left( \frac{d}{dt} (t+1) \right)   \\
 & =0+t\cdot 1 \\
 & =t\neq 0
 \end{align} 
$$
Therefore, ${} g \notin \ker T {}$
b)
Suppose there exists some ${} f(t)=a+bt+ct^{2} \in {\mathbb{P}_{2}} {}$ such that ${} Tf(t)=t^{2} {}$. Then
$$
\begin{align}
 \frac{d^{2}}{dt^{2}} (a+bt+ct^{2}) +t\cdot \frac{d}{dt} (a+bt+ct^{2}) & =2c+t(b+2ct) \\
 & =2c+bt+2ct^{2} 
 \end{align}
$$
Therefore, ${} 2c=0 {}$, ${} b=0 {}$, and ${} 2c=1 {}$. Therefore, we have a contradiction, so there exists no such element, so ${} t^{2} \notin \im T {}$
c)
$T$ is not surjective, so cannot be invertible
d)
No, as $T$ is not invertible.
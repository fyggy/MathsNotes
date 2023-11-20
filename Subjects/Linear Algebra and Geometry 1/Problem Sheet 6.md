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
Therefore, $J$ is a linear map.
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
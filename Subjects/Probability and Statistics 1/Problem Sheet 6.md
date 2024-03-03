[[PS1 participation 2.pdf|Exercise Sheet]]
1. 
a)
Note that if the switch is off at minute $n$, then it will always be on at minute $n+1 {}$. Conversely if it is on, then there is a ${} 2/3 {}$ chance that it is still on at minute $n+1 {}$. Therefore, if we let ${} X_{n} {}$ denote the event that the switch is on at minute ${} n {}$, then by the law of total probability, 
$$
\begin{align}
 p_{n+1}=\mathbb{P}(X_{n+1}) & =\mathbb{P}(X_{n+1}\mid X_{n})\mathbb{P}(X_{n}) + \mathbb{P}(X_{n+1} \mid X_{n}^{\mathrm{c}}) \mathbb{P}(X^{\mathrm{c}}_{n})   \\
 & =\frac{2}{3} p_{n}+1 \cdot  (1-p_{n}) \\
 & =1-\frac{1}{3} p_{n}
 \end{align}
$$
b)
We see that ${} p_{0}=0 {}$, since the light starts off. Now we have a difference equation
$$
p_{n+1}+\frac{1}{3}p_{n}=1
$$
We see that the auxiliary polynomial is
$$
\lambda+\frac{1}{3}=0
$$
so ${} \lambda=-\frac{1}{3} {}$.
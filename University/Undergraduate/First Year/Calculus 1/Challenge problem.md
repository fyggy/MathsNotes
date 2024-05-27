Show from first principles that the function ${} f(x)=x^{2}\delta(x) {}$ is differentiable at ${} x=0 {}$, where
$$
\delta(x)=\begin{cases}
x \in \mathbb{Q}: 0 \\
x\notin \mathbb{Q}: 1
\end{cases}
$$
and calculate that derivative

$$
\begin{align}
 f'(0) & =\lim_{d\tto 0} \frac{f(0+d)-f(0)}{d}   \\
 & =\lim_{d\tto 0} \frac{f(d)}{d} \\
 & =\lim_{d\tto 0} \frac{ d^{2}\delta(d) }{ d } \\
 & =\lim_{d\tto 0} d\delta(d)
 \end{align}
$$
Let $\varepsilon>0 {}$, and let ${} \delta=\varepsilon {}$. Then, for all ${} x \in \mathbb{R} {}$ such that ${} |x-0|=|x|<\delta$, then we have 2 cases:
Case 1: $x \in \mathbb{Q}$
Then ${} x\delta (x){} =0 {}$, so ${} |x\delta (x)-0|=0<\varepsilon {}$ as required.
Case 2: ${} x\notin \mathbb{Q} {}$
Then ${} x\delta(x)=x {}$, so ${} |x\delta(x)-0|=|x|< \delta=\varepsilon {}$ as required.

Therefore, the limit is $0$, so the derivative at $0$ is $0$.
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
Let $\varepsilon>0$, and let $\delta {}$ be a number with ${} \varepsilon > \delta>0 {}$. This exists because $\mathbb{R}$ are dense in ${} \mathbb{R}$. Then, for all ${} |x-0|=|x|<\delta$, then we have 
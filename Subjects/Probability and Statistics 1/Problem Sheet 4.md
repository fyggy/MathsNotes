1. 
First, note that, given ${} A \in \mathcal{E} {}$, ${} |A|\geq 0 {}$, by definition. Now ${} \mathbb{P}(A)=|A| / n \geq 0 {}$, so axiom $1$ is satisfied. 

Now, note that ${} |\Omega|=n {}$, so ${} \mathbb{P}(\Omega)=n / n = 1 {}$, so axiom $2$ is satisfied. 

Finally, let ${} \mathcal{A}=\{ A_{i} \}_{i\in I} {}$ be a collection of elements of $\mathcal{E} {}$ indexed by some well ordered set $I$ for some integer ${} k {}$. Note that since $\Omega {}$ is finite, then any collection of subsets will be finite. Now let ${} S=\sum_{i \in I} |A_{i}| {}$, and ${} \mathcal{C}=\{ 1,\,\dots,\,S \} {}$. Finally, let ${} a_{i}=|A_{i}| {}$ and ${} b_{i}=\sum_{j< i} a_{j} {}$. Therefore, let ${} \theta_{i}:A_{i}\to{}\{ 0,\,\dots,\,a_{i}-1 \} {}$ be the canonical bijection. Let ${} f_{i}:A_{i}\to{} \mathcal{C} {}$ be defined by ${} f_{i}(x)=\theta_{i}(x)+a_{j} {}$. Consider
$$
f:\bigcup_{i\in I} A_{i}\to{} \mathcal{C} \qquad f(x)=f_{i}(x) \text{ if } x \in A_{i}
$$
We see this is well defined, as all ${} A_{i} {}$ are disjoint. Since all ${} f_{i}$ are injective, then $f$ is injective. Now suppose we have ${} x,\, y \in  \bigcup_{i\in I} A_{i} {}$ with ${} f(x)=f(y) {}$. Now if ${} x,\, y \in A_{i} {}$, then 
$$
\begin{align}
 f(x)=f_{i}(x)=\theta_{i}(x)+b_{i} & =\theta_{i}(y)+b_{i}  \\
  \Rightarrow  \theta_{i} (x) &=\theta_{i}(y) \\
\Rightarrow x & =y
 \end{align}
$$
Otherwise, if ${} x \in A_{i} {}$, ${} y \in A_{j} {}$, $i\neq j$, WLOG assume that $i>j {}$. Now
$$
\begin{align}
	f(x)=f_{i}(x)=\theta_{i}(x)+b_{i} & =\theta_{j}(y)+b_{j} \\
 \theta_{i}(x)+a_{j}+c+b_{j}& =\theta_{j}(y)+b_{j} \text{ for some } c\geq 0 \\
 \theta_{i}(x)+a_{j}+c & =\theta
\end{align}
$$
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
 \theta_{i}(x)+a_{j}+c & =\theta_{j}(y) \\
\theta_{i}(x)+a_{j}+c & \leq a_{j}-1 \text{ the maximum value} \\
\theta_{i}(x)+c & \leq-1
\end{align}
$$
But since ${} \theta_{i}(x),\, c {}$ are both positive, then this is a contradiction. Therefore, ${} x=y {}$, and $f$ is bijective. Therefore, 
$${} \left|\bigcup_{i\in I} A_{i}\right|=|\mathcal{C}|=S=\sum_{i\in I}|A_{i}| {}$$
Therefore, given any such family of disjoint sets, we see that 
$$
\mathbb{P}\left( \bigcup_{i\in I} A_{i} \right)=\frac{\left| \bigcup_{i\in I} A_{i} \right| }{n}= \frac{ \sum_{i \in I} |A_{i}| }{ n }= \sum_{i \in I} \mathbb{P}(A_{i})
$$
which satisfies the third axiom. Therefore, ${} (\Omega,\, \mathcal{E},\, \mathbb{P}) {}$ is a probability model. 
2. 
a)
Tree diagrams are really hard to do with latex I'll try submitting the picture separately
b)
$$
\begin{align}
\mathbb{P}(\text{tea} \mid \text{porridge}) & =\frac{\mathbb{P}(P \cap T)}{\mathbb{P}(P)} \\
 & =\frac{\mathbb{P}(P \cap N)}{\mathbb{P}(P) \mathbb{P}(T) + \mathbb{P}(P)\mathbb{P}(T^{\mathrm{c}})}  \\
 & =\frac{1 /3 \cdot  (1- 4/5)}{1 /3 \cdot (1-4/5)+2 /3 \cdot  (5 / 7)} \\
 & =\frac{7}{57}
\end{align}
$$
3. 
a)
$$
\begin{align}
\mathbb{E}(X) & =\sum_{k \in \{ 1,\,\dots,\,i \}} k \mathbb{P}(X=k) \\
 & =\sum_{k \in \{ 1,\,\dots,\,n \}} k \frac{1}{n} \\
 & = \frac{1}{n} \cdot \sum_{k\in \{ 1,\,\dots,\,n \}} k \\
	 & =\frac{1}{n} \cdot  \frac{ (n+1)n }{ 2 } \\
 & =\frac{n+1}{2} 
\end{align}
$$
b)
$$
\mathbb{E}(D)=\mathbb{E}(3X+5)=3\mathbb{E}(X)+5=3 \cdot  \frac{12+1}{2} +5=24.5
$$
and
$$
\begin{align}
 \var(D) & = \var(3X+5)  \\
 & =9\var(X) \\
 & =9(\mathbb{E}(X^{2})-\mathbb{E}(X)^{2}) \\
 & =9\left(\frac{1}{12} \sum_{k=1}^{12} k^{2}- 6.5^{2}\right) \\
 & =9\left(  \frac{1}{12} 650-42.25 \right) \\
 & =107.25
 \end{align}
$$
c)
Note that
$$
Y=3X-1
$$
where $X$ is a discrete random variable over ${} 1,\,\dots,\,12 {}$. Now 
$$
\mathbb{E}(Y)=\mathbb{E}(3X-1)=3\mathbb{E}(X)-1=3\cdot 6.5-1=18.5
$$
and
$$
\begin{align}
 \var(Y)  & = \var(3X-1)\\
  & =9\var(X) \\
 & =107.25
 \end{align}
$$
by above.

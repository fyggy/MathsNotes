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
so ${} \lambda=-\frac{1}{3} {}$. Now ${} p_{n}=A\left( -\frac{1}{3} \right)^{n}+\alpha_{n} {}$, where ${} \alpha_{n+1}+\frac{1}{3}\alpha_{n}=1 {}$, and ${} \alpha_{n} {}$ is simply any solution. We see that ${} \alpha_{n}=\frac{3}{4} {}$ is a solution. Now
$$
p_{n}=A\left( -\frac{1}{3} \right)^{n}+\frac{3}{4}
$$
and ${} p_{0}=0 {}$, so 
$$
\begin{align}
 0=p_{0} & =A\left( -\frac{1}{3} \right)^{0}+\frac{3}{4}   \\
 & =A+\frac{3}{4} \\
	A & =-\frac{3}{4}
 \end{align}
$$
and so 
$$
p_{n}=\frac{3}{4}\left(1-\left( -\frac{1}{3} \right)^{n}\right)
$$
Now if we take ${} n\to{}\infty {}$, then ${} p_{n}\to{}3/4 {}$, so ${} C=3/4 {}$
2. 
a)
We have 
$$
\begin{align}
 \mathbb{P}(F+H\geq 3) & =1-\mathbb{P}(F+H\leq 2)  \\
  & =1-(\mathbb{P}(F+H=0)+\mathbb{P}(F+H=1)+\mathbb{P}(F+H=2))   
 \end{align}
$$
Let $E=F+H {}$. Let ${} G_{E}(s) {}$ be the probability generating function of $E$. Now
$$
\begin{align}
 G_{E}(s) & =\mathbb{E}(s^{E})   \\
 & =\mathbb{E}(s^{F}s^{H}) \\
 & =\mathbb{E}(s^{F})\mathbb{E}(s^{H}) \\
 & =e^{3(s-1)}e^{{5(s-1)}} \\
 & =e^{8(s-1)} \\
\Rightarrow E & \sim \mathrm{Poisson}(8)
 \end{align}
$$
Now
$$
\begin{align}
 \mathbb{P}(E\geq 3)  & =1-\mathbb{P}(E\leq 2) \\
 & =1-\left( \sum_{n=0}^{2}p_{E}(n) \right) \\
 & =1-\left( \sum_{n=0}^{2} \frac{e^{-8}8^{n}}{n!}  \right)  \\
 & =0.986256032256\dots
 \end{align}
$$
b)
Let $A {}$ be the event that the guest has falcons as their favourite bird and ${} B$ be the event that the guest has hawks as their favourite bird. Let $Z$ be the random variable representing the number of time that guests favourite bird is seen. Now
$$
\begin{align}
 \mathbb{E}(Z) & =\mathbb{E}(Z\mid A) \mathbb{P}(A) +\mathbb{E}(Z \mid B) \mathbb{P}(B)   \\
 & =3 \cdot  \frac{2}{3}+5 \cdot  \frac{1}{3} \\
 & =\frac{11}{3}=3.6\conj{66}\dots
 \end{align}
$$
c)
Now let $C {}$ be the event that the vehicle breaks down. We assume that ${} A,\, B,\, C {}$ are all independent (unless hawk enthusiasts have a penchant for destroying vehicles), and recall that ${} A^{\mathrm{c}}=B {}$. Now
$$
\begin{align}
 \mathbb{E}(Z)  & = \mathbb{E}(Z \mid A \cap C)\mathbb{P}(A \cap C)+\mathbb{E}(Z \mid B \cap C) \mathbb{P}(B \cap C) \\
 & +\mathbb{E}(Z \mid (A \cap C)^{\mathrm{c}})\mathbb{P}((A \cap C)^{\mathrm{c}})+\mathbb{E}(Z \mid (B \cap C)^{\mathrm{c}}) \mathbb{P}((B \cap C)^{\mathrm{c}}) \\
 & =0+\mathbb{E}(Z \mid A)
 \end{align}
$$
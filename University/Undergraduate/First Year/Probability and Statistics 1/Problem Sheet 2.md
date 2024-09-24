---
tags:
  - prob_stats1
  - homework
date: 2024-01-26
pset: 2
completed: true
---
[[Directory]], [[Probability and Statistics 1|Subject Directory]]
[[ProbStatsHW2.pdf|Exercise Sheet]]
1. 
Note that ${} \mathbb{P}(A)=\frac{1}{2} {}$, and ${} \mathbb{P}(B)=\frac{1}{2} {}$, and ${} \mathbb{P}(A\cap B)=\frac{1}{4} {}$, so ${} \mathbb{P}(A)\mathbb{P}(B)=\mathbb{P}(A\cap B) {}$, so $A$ and $B {}$ are independent

Now note that ${} \mathbb{P}(C)=\mathbb{P}(\text{both are odd})+\mathbb{P}(\text{both are even})=\frac{1}{4}+\frac{1}{4}=\frac{1}{2} {}$, and ${} \mathbb{P}(C \cap A)=\mathbb{P}(\text{both are odd})=\frac{1}{4} {}$. Therefore, ${} \mathbb{P}(A \cap C)=\mathbb{P}(A)\mathbb{P}(C) {}$, so $A  {}$ and $C$ are independent. Same goes for $B$ and $C$. 

Finally, note that
$$
\mathbb{P}(A \cap B \cap C)=\mathbb{P}(\varnothing)=0
$$
but ${} \mathbb{P}(A)\mathbb{P}(B)\mathbb{P}(C)=\frac{1}{2}\cdot \frac{1}{2}\cdot \frac{1}{2}=\frac{1}{8}\neq 0 {}$, so ${} A,\, B,\, C {}$ are not all independent.
2. 
The sample space is 
$$
\Omega=\{ \{ \text{black},\, \text{black} \},\, \{ \text{black},\, \text{red} \},\, \{\text{red},\, \text{ red} \} \}
$$
Let ${} B=\{ \text{black},\, \text{ black} \} {}$, ${} D=\{ \text{black},\, \text{red} \} {}$, ${} R=\{ \text{red},\, \text{red} \} {}$. Now ${} 3\mathbb{P}(R)=\mathbb{P}(D) {}$. Let $n$ be the number of socks in her drawer. Now there are ${} n-3 {}$ black socks. Now 
$$
\begin{align}
\mathbb{P}(B) & =\frac{ n-3 }{ n } \cdot  \frac{n-4}{n-1}  \\
\mathbb{P}(D) & =\frac{n-3}{n} \cdot \frac{3}{n-1}+\frac{3}{n}\cdot \frac{ n-3 }{ n-1 } \\
\mathbb{P}(R) & =\frac{3}{n}\cdot \frac{2}{n-1}
\end{align}
$$
Now
$$
\begin{align}
\mathbb{P}(D) & =3\mathbb{P}(R) \\
6(n-3) & =18 \\
n-3 &=3 \\
n & =6
\end{align}
$$
Therefore, there are $3$ black socks and $3 {}$ red socks.
3. 
write $$
\begin{align}
 F & =\text{first is spades}  \\
 S& = \text{second 2 are spades}
 \end{align}
$$
$$
\mathbb{P}(\text{first is spades} \mid \text{second 2 are spades})=\frac{\mathbb{P}(\text{all are spades})}{\mathbb{P}(\text{second 2 are spades})} 
$$
Now
$$
\mathbb{P}(\text{all are spades})=\frac{13}{52}\cdot \frac{12}{51}\cdot \frac{11}{50}=\mathbb{P}(A)
$$
and
$$
\begin{align}
 \mathbb{P}(S) & =\mathbb{P}(S \mid F)\cdot \mathbb{P}(F)+\mathbb{P}(S \mid F^{\mathrm{c}})\cdot \mathbb{P}(F^{\mathrm{c}})   \\
 & =\frac{\mathbb{P}(A)}{\mathbb{P}(F)}\cdot \mathbb{P}(F)+\frac{13}{51}\cdot \frac{12}{50}\cdot \frac{ 52-13 }{ 52 } \\
 & =\frac{13}{52}\cdot \frac{12}{51}\cdot \frac{11}{50}+\frac{13}{51}\cdot \frac{12}{50}\cdot \frac{3}{4} \\
 & =\frac{1}{17}
 \end{align}
$$
so we have
$$
\begin{align}
\mathbb{P}(F \mid S)=\frac{\mathbb{P}(A)}{1 /17}=\frac{11}{50}
\end{align}
$$

---
tags:
  - prob_stats1
  - homework
date: 2024-01-19
pset: 1
completed:
---
[[Directory]], [[Probability and Statistics 1|Subject Directory]]
[[ProbStatsHW1.pdf|Problem Sheet]]
1. 
a)
$$
\begin{align}
A & =\{ TTH,\, THT,\, HTT \} \\
B & =A \cup \{ TTT \}=\{ TTH,\, THT,\, HTT,\, TTT \} \\
C & =\{ H HH,\, H HT,\, HTT,\, TTT \} \\
D & =\{ T HH,\, TTH,\, THT,\, TTT \}
\end{align}
$$
b)
$$
\begin{align}
 A^{\mathrm{c}}  & =\{ HHH,\, THH,\, HTH,\, H HT,\, TTT \}  \\
B\setminus A & =\{ TTT \} \\
A \cup (C \cap D) & =A \cup \{ TTT \}=B \\
A \cap D^{\mathrm{c}} & =A \cap \{ H H H,\, HTH,\,  H HT, HTT \} = \{ HTT \}
 \end{align}
$$
2. 
a) skip
b) skip
3. 
a)
$$
\Omega=\{ f_{1}f_{2} f_{3} f_{4} \mid \forall i \in \{ 1,\, 2,\, 3,\, 4 \}:f_{i} \in \{ H,\, T \} \}
$$
and if ${} E \in \Omega {}$ then
$$
\mathbb{P}(E)=\frac{1}{16}
$$
so if ${} A \subseteq \Omega {}$ is an event in $\Omega$, then 
$$
\mathbb{P}(A)=\frac{ |A| }{ 16 }
$$

b)
$$
\Omega=\{ 0,\, 1,\, 2,\, 3,\, 4 \} 
$$
Let ${} E \in \Omega {}$. There are $4$ choose $E$ ways of getting $E$ tails, therefore, 
$$
\mathbb{P}(E)=\binom{4}{E} \cdot \frac{1}{16}
	$$
and now if ${} A \subseteq \Omega {}$, then 
$$
\mathbb{P}(E)=\sum_{a\in A} \binom{4}{a} \cdot \frac{1}{16}
$$
4. 
a) i)
We see that the probability that exactly 2 of the events occur is
$$
\begin{align}
  &\phantom{ = l} \mathbb{P}(((A \cap B) \cup (B \cap C) \cup (C \cap A)) \setminus (A \cap B \cap C))  \\
 & =\mathbb{P}((A \cap B) \setminus(A \cap B \cap C) \cup (B \cap C) \setminus(A \cap B \cap C) \cup (C \cap A) \setminus(A \cap B \cap C)) \\
 & =\mathbb{P}((A \cap B) \setminus(A \cap B \cap C)) + \mathbb{P}((B \cap C) \setminus(A \cap B \cap C)) + \mathbb{P}((C \cap A) \setminus(A \cap B \cap C)) \\
 & =\mathbb{P}(A \cap B) + \mathbb{P}(B \cap C) + \mathbb{P}(C \cap A) - 3\cdot \mathbb{P}(A \cap B \cap C) \\
 & =\frac{3}{10}+\frac{2}{5}+\frac{1}{5} - \frac{3}{10} \\
 & =\frac{3}{5}
 \end{align}
$$
ii) We see that the probability that greater than or equal to 2 events occur is

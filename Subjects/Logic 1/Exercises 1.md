---
tags:
  - exercises
  - logic1
date: 2023-10-08
---
[[Directory]], [[Logic 1|Subject Directory]]
Relavent chapter: [[1. Propositional Logic]]
1. First:
$$
\begin{align}
 & p_{1} \\
 & p_{2} \\
 & p_{3} \\
 & p_{1}\leftrightarrow p_{2} \\
 & p_{3}\vee(p_{4}\leftrightarrow p_{2}) \\
 & \neg p_{2} \\
 & \neg p_{2} \to{} (p_{3} \vee(p_{1}\leftrightarrow p_{2})) \\
 & \neg p_{3} \\
 & (\neg p_{2}\to{}(p_{3}\vee(p_{1}\leftrightarrow p_{2})))\wedge\neg p_{3}
\end{align}
$$
Second:
$$
\begin{align}
 & p_{7} \\
 & \bot \\
 & p_{4} \\
 & p_{2} \\
 & p_{1} \\
 & \neg p_{2} \\
 & \neg \bot \\
 & p_{7}\to{}\neg \bot \\
 & p_{4}\wedge\neg p_{2} \\
 & (p_{4}\wedge\neg p_{2})\to{} p_{1} \\
 & (p_{7}\to{}\neg \bot)\leftrightarrow ((p_{4}\wedge\neg p_{2})\to{} p_{1})
\end{align}
$$
Third:
$$
\begin{align}
 & p_{1} \\
 & p_{2} \\
 & p_{1}\to{} p_{2} \\
 & (p_{1}\to{} p_{2})\to{} p1 \\
 & ((p_{1}\to{} p_{2})\to{} p_{1})\to{} p_{2} \\
 & (((p_{1}\to{} p_{2})\to{} p_{1})\to{} p_{2})\to{} p_{1}
\end{align}
$$
3. Let $\ll$ denote the relation "is a subformula of". Let $\varphi,\, \psi,\, \rho \in PROP$ with $\varphi\ll \psi$ and $\psi\ll\rho$. Now we have $\psi \in Sub(\rho)$. For $\psi$ to get inside $Sub(\rho)$, there are 3 cases derived from the definition of $Sub$, and an extra one:
	1. $\psi$ atomic: Therefore, $Sub(\psi)\subseteq Sub(\rho)$, as $Sub(\psi)=\{ \psi \}$.
	2. $\psi_{1}=\psi \square \psi_{2}$, with $\psi_{1} \in Sub(\rho)$. Then we have $Sub(\psi_{1})=Sub(\psi)\cup Sub(\psi_{2})\cup\{\psi_{1}\}$, so $Sub(\psi)\subseteq Sub(\rho)$
	3. $\psi_{1}=\neg\psi$, with $\psi_{1}\in Sub(\rho)$. Then we have $Sub(\psi_{1})=Sub(\psi)\cup \{ \psi_{1} \}$, so $Sub(\psi)\subseteq Sub(\rho)$.
	4. $\psi=\rho$. Then $Sub(\psi)=Sub(\rho)$
	In each case, we have $Sub(\psi)\subseteq Sub(\rho)$. Therefore, since $\varphi \in Sub(\psi)$, then $\varphi \in Sub(\rho)$. Therefore, $\varphi\ll\rho$
4. Let $A(\varphi)=\forall\psi \in Sub(\varphi)\forall F=(\varphi_{n})_{n \in I} \text{ is a formation sequence of } \varphi: \psi \in F$. We induct on $\varphi$.
	1. $\varphi$ atomic: $\psi=\varphi$, as $Sub(\varphi)=\{ \varphi \}$. Therefore, as every formation sequence must contain the proposition its forming, $\psi \in F$.
	2. $\varphi=\varphi_{1} \square \varphi_{2}$. In order to be formed, $\varphi_{1}, \varphi_{2}$ must be in the sequence, as must their respective formation sequences. Therefore, since $Sub(\varphi)=Sub(\varphi_{1})\cup Sub(\varphi_{2})\cup \{ \varphi \}$, then either $\psi \in Sub(\varphi_{1}) \text{ or } Sub(\varphi_{2})$, or $\psi=\varphi$, so by hypothesis, $\psi$ is in the formation sequence of either $\varphi_{1}$ or $\varphi_{2}$, and therefore in the formation sequence of $\varphi$, or $\psi$ is by definition in the formation sequence of $\varphi$. Therefore, $A(\varphi)$ holds.
	3. $\varphi=\neg\varphi_{1}$. Similar argument
	Therefore by the induction principle, $A(\varphi)$ holds for all $\varphi \in PROP$
5. Define $F(\varphi)$ by the following recursion, if we let $\cup$ to be list concatenation.
	1. $\varphi$ atomic. $F(\varphi)=(\varphi)$
	2. $\varphi=\varphi_{1}\square\varphi_{2}$. $F(\varphi)=F(\varphi_{1})\cup F(\varphi_{2})\cup(\varphi)$
	3. $\varphi=\neg\varphi$. $F(\varphi)=F(\varphi_{1})\cup (\varphi)$
	We now show that $F(\varphi)$ gives the shortest formation sequence. First note that $F(\varphi)$ gives a formation sequence, as every element is either atomic, or contains as arguments previous elements. Now note that, if any element of $F(\varphi)$ is removed, then it is no longer a formation sequence. In particular, take $\rho \in F(\varphi)$. We have 3 cases:
	1. $\rho=\varphi$. In this case, then $F(\varphi)\setminus(\rho)$, can no longer be a formation sequence for $\varphi$, as it doesn't contain $\varphi$
	2. $\rho_{1}=\rho \square\rho_{2}$. In this case, $\rho$ was added to the sequence to form $\rho_{1}$. Therefore, $F(\varphi)\setminus (\rho)$ is no longer a formation sequence
	3. $\rho_{1}=\neg\rho$. Similar argument
	Therefore, $F(\varphi)$ is the smallest possible formation sequence. Since its definition coincides with the definition of $Sub$, then it must contain the same elements. Therefore, if a proposition is in the shortest formation sequence of $\varphi$, then it must be a subsequence of $\varphi$
6. 
	a) Let $\varphi$ be a proposition. Note that by the definition, wherever $r$ encounters a proposition
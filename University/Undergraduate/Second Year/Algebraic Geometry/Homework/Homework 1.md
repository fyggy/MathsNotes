---
tags:
  - homework
  - alggeo
date: 2025-01-13
pset: 1
completed: false
---
[[Directory]], [[Algebraic Geometry 1|Subject Directory]]
[[University/Undergraduate/Second Year/Algebraic Geometry/Homework/Homework 1|🞀🞀]] [[|◀]] [[University/Undergraduate/Second Year/Algebraic Geometry/Homework/Homework 2|▶]] [[University/Undergraduate/Second Year/Algebraic Geometry/Homework/Homework 11|🞂🞂]]

[[University/Undergraduate/Second Year/Algebraic Geometry/Homework/Worksheets/alg_geo_1.pdf|Worksheet]]
1. 
Since $f$ is non-constant, and $\mathbb{C}$ is algebraically complete, then $f$ must have at least $1$ root, ${} \mathbf{r}=(r_{1},\,\dots,\,r_{n}) {}$. Therefore, ${} f(\mathbf{r})=0 {}$, and so ${} \mathbf{r} \in A=\{ \mathbf{a} \in \mathbb{C}^{n} \mid  f(\mathbf{a})=0 \}\neq \varnothing  {}$. Now suppose that $n\geq 2$. Let ${} r_{i}^{j}:\mathbb{C}\to{}\mathbb{C} {}$ be the $i^{\text{th}} {}$ principle value of the $j^{\text{th}} {}$ root. WLOG suppose that $f {}$ is non constant in its first variable ${} x {}$ for some fixed value ${} \mathbf{a}=(a_{2},\,\dots,\,a_{n}) \in \mathbb{C}^{n-1} {}$. Since $f {}$ is continuous, then there must exists an open neighbourhood $B$ around ${} \mathbf{a} {}$ where $f {}$ is non-constant. Then we may rewrite ${} f {}$ as a polynomial in $x {}$, that is, 
$$
\begin{align}
 g(a_{2},\,\dots,\,a_{n})(x) & =f(x,\, a_{2},\,\dots,\,a_{n})   \\
 & =g_{0}(\mathbf{a})+g_{1}(\mathbf{a})x+\dots+g_{k}(\mathbf{a})x^{k}
 \end{align}
$$
where for ${} \mathbf{a} \in B {}$, ${} g_{1},\,\dots,\,g_{k} {}$ are not all ${} 0 {}$. 

Then for each ${} \mathbf{a} \in B {}$, there must exist at least ${} 1 {}$ root of ${} g(x)$. Then ${} (x,\, a_{2},\,\dots,\,a_{n}) \in \mathbb{C}^{n} {}$ is a root of $f$, and since ${} B \subseteq \mathbb{C}^{n-1} {}$ is open, then it must be infinite. Therefore, $A$ is infinite. 

However, in $\mathbb{R}^{2}$, consider ${} f(x,\, y)=x^{2}+y^{2}+1 {}$. Then ${} \{ f=0 \}\subseteq \mathbb{R}^{2} {}$ is empty, and so finite.
2. 
a) clear
b) 
Let $L$ be a line passing through ${} (1,\, 1) {}$. Then the equation for $L$ is of the form ${} \{ a(x-1)+b(y-1)=0 \} {}$. Now $$
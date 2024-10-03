### Definition 1.1: Functors
A functor is essentially a map between categories, that is, if ${} F: \mathscr{C} \to{}\mathscr{D} {}$ is a functor, then it maps
$$
\begin{align}
 F:\Ob(\mathscr{C}) &  \to{} \Ob(\mathscr{D}) \\
  
 \end{align}
$$
and
$$
F:\hom_{\mathscr{C}} (A,\, B)\to{} \hom _{\mathscr{D}}(F(A),\, F(B))
$$
such that ${} F(\id _{A})=\id _{F(A)} {}$, and ${} F(f \circ  g)= F(f) \circ  F(g) {}$. 
### Lemma: Yondea Lemma
More precisely, given ${} A {}$, Let a functor ${} h_{A}:\mathscr{C} \to{} \mathbf{Set}  {}$ mapping 
$$
X\mapsto \hom _{\mathscr{C}}(A,\, X)
$$
as object, and given a morphism ${} X \to{f}Y {}$ in ${} \mathscr{C} {}$ then ${} h_{A}(f) {}$ is a morphism
$$
h_{A}(f):\hom _{\mathscr{C}}(A,\, X) \to{}\hom _{\mathscr{C}}(A,\, Y)
$$
which is a map, given ${} \varphi \in \hom _{\mathscr{C}}(X,\, A) {}$, then ${} h_{A}(f)(\varphi)=f \circ \varphi {}$

Loosely, Yondea's lemma says that when ${} h_{A} \cong  h_{B} {}$, then $A \cong B {}$. 
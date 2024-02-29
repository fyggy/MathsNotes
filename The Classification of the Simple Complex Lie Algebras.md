First, we define Lie Groups. A *smooth manifold* is essentially a shape in space with a topology, and appears *locally smooth*, with smooth here being analogous to a function being infinitely differentiable. A Lie group is a smooth manifold with group structure, such that group multiplication and inversion are also smooth maps. The prototypical example is ${} \mathrm{SO}(2) {}$, the group of rotations in $2 {}$-D. It can be represented as a circle, and it is clear to see that the group operation is smooth. 

A Lie *algebra* is an algebra defined tangent to the identity of a Lie Group. The formal construction is fairly technical, but it can be surmised by the idea of creating a "map" or "projection" of your manifold onto a flat space; specifically a vector space. It turns out, when you do this, you get a multiplication of sorts from the group operation. This is called the *lie bracket*. 

In particular, given a vector space ${} \mathfrak{g} {}$ over some field $F$, we call $\mathfrak{g} {}$ a *Lie Algebra* if we have a bilinear map, the lie bracket from g to itself ${} [{}\cdot{} ,{}\cdot{} ]:\mathfrak{g}\times \mathfrak{g}\to{}\mathfrak{g} {}$ satisfying, for all ${} x,\, y,\, z \in \mathfrak{g} {}$, 
$$
\begin{align}
[x,\, x] & =0\\
 [x,\, y] & =-[y,\, x]   \\
[x,\, [y,\, z]]+[z,\, [x,\, y]]+[y,\, [z,\, x]] & =0
 \end{align}
$$
(TS: the alternating property; any element bracketed with itself is 0,
anticommutativity; x bracketed with y is equal to minus y bracket x,
and the Jacobi identity; cycling x, y and z through these brackets and adding them all up equals zero)
Note that ${} [x,\, 0]=0 {}$, as it is bilinear. In this talk we will only be concerned with finite dimensional Complex Lie algebras, that is, those with ${} F=\mathbb{C} {}$. Now you may recognise these relations as exactly those satisfied by a commutator, which is a map from an associative algebra $A {}$ , the commutator bracket from A cross A to A ${} [{}\cdot {},\, {}\cdot {}]:A \times A\to{}A {}$ defined by X commutator Y equals X Y minus Y X ${} [X,\, Y]=XY-YX {}$. Indeed, the Lie bracket is a generalisation of this idea. In fact, any associative algebra may be made into a lie algebra by taking multiplication to be the commutator. 

The most prototypical example is ${} \mathfrak{sl}_{2}(\mathbb{C}) {}$, the set of all ${} 2\times 2 {}$ matrices with trace $0 {}$. This is a lie algebra under the commutator. This can be seen as
$$
\tr  [A,\, B]=\tr  (AB-BA)=\tr  (AB)-\tr  (BA)=\tr  (AB)-\tr  (AB)=0
$$
We can take a canonical basis to be
$$
e=\begin{pmatrix}0 & 1 \\ 0 & 0 \end{pmatrix} \qquad f=\begin{pmatrix}0 & 0 \\ 1 & 0 \end{pmatrix} \qquad h=\begin{pmatrix}1 & 0 \\ 0 & -1 \end{pmatrix} 
$$
and we can calculate that
$$
[e,\, f]=h \qquad [h,\, e]=2e\qquad [h,\, f]=-2f
$$

Now we define a map ad from g to the set of linear maps on g, end g ${} \ad :\mathfrak{g}\to{}\operatorname{End}(\mathfrak{g}) {}$ as ad x of y equals x bracket y ${} \ad (x)(y)=[x,\, y] {}$. This is called the adjoint action of $x {}$. That is, ${} \ad x$ is simply $\mathfrak{g}$ acting on itself from the left. This seems silly, but it turns out to have lovely properties. In particular, if we take $x,\, y,\, z \in \mathfrak{g} {}$, we see that
$$
\begin{align}
\ad ([x,\, y])(z) & =[[x,\, y],\, z] \\
 & =-[z,\, [x,\, y]] \\
 & =[x,\, [y,\, z]]+[y,\, [z,\, x]] \\
 & =[x,\, [y,\, z]]-[y,\, [x,\, z]] \\
 & =(\ad (x)\ad (y)-\ad (y)\ad (x) )(z) \\
 & =[\ad (x),\, \ad (y)](z)
\end{align}
$$
(TS: the adjoint action of x bracket y on z is equal to x bracket y bracket z, by definition,
if we swap using anticommutativity, we see that it's exactly equal to one side of the Jacobi identity. Therefore, we can substitute that in. Now if we swap that z and x in the second term using anticommutativity again, we see that this is actually equal to ad x times ad y minus ad y times ad x evaluated at z. This is simply equal to the commutator bracket of ad x and ad y evaluated at z)
We see then, that ${} \ad {}$ is actually a *Lie homomorphism*, that is, it preserves the structure of the Lie bracket. However, it also acts on the lie algebra itself. This property will be very useful.

We now define the import concepts of nilpotency, and simplicity. We start with an *ideal*. Ideals are analogous to normal subgroups, and are simply the subalgebras of a Lie algebra which are invariant under the action of the lie algebra. In particular, if ${} \mathfrak{h} {}$ is an ideal of ${} \mathfrak{g}, {}$ then ${} [\mathfrak{g},\, \mathfrak{h}]=\{ [x,\, y] \mid x \in \mathfrak{g},\, y \in \mathfrak{h} \} {}\subseteq \mathfrak{h} {}$. Thanks to this invariance, we may quotient by ideals which I won't prove the specific reason here, with the space being the standard factor space, and the lie bracket in ${} \mathfrak{g} /\mathfrak{h} {}$ defined by
$$
[x+\mathfrak{h},\, y+\mathfrak{h}]=[x,\, y]+\mathfrak{h}
$$

We may now define the lower central series as follows: given a lie algebra ${} \mathfrak{g}$, define
$$
\begin{align}
\mathfrak{g}^{1}=\mathfrak{g}, &  & \mathfrak{g}^{k}=[\mathfrak{g},\, \mathfrak{g}^{k-1}] \\
\end{align}
$$
This can be viewed to generate a sequence of subalgebras like so:
$$
\begin{align}
 & \mathfrak{g} \to{} [\mathfrak{g},\, \mathfrak{g}]\to{} [\mathfrak{g},\, [\mathfrak{g},\, \mathfrak{g}]]\to{}\dots \\

\end{align}
$$
This may seem arbitrary, but the ${} k^{\text{th}} {}$ term in the lower central series may be thought of as the set of elements which are the product of some list of ${} k$ elements in $\mathfrak{g} {}$. We call a Lie algebra *nilpotent* if there exists some $k$ such that ${} \mathfrak{g}^{k}=0 {}$, where $0$ is the $0$-algebra. That is, a lie algebra is nilpotent if there is some length such that every product of elements of that length is $0 {}$.

On more types, an abelian lie algebra is one where every bracket is zero, that is ${} [x,\, y]=0 {}$ for all ${} x,\, y \in \mathfrak{g} {}$. The name comes from the fact that if the commutator is zero for all elements in an associative algebra, then all the elements commute. Furthermore, a *simple* lie algebra is a non-abelian Lie algebra, that is, there exists some ${} x,\, y \in \mathfrak{g} {}$ with ${} [x,\, y]\neq 0 {}$ with no non-trivial ideals, that is, other than ${} 0 {}$ and itself. These are special as they cannot be expressed as a direct product of any other lie algebras; in a sense, they are *prime*. They are also the central object of study for this talk. Finally, for our purposes, a *semisimple* lie algebra is one which is a direct product of simple lie algebras. If you know lie algebras already, you may know that this is not the typical definition, however, this is fine, since it turns out over ${} \mathbb{C}$, this definition and the traditional one is equivalent. 

All these terms may seem bewildering, but don't worry, we will constantly be recounting the definitions. Just remember: simple = prime, semisimple = product of primes, abelian = almost 0, nilpotent = eventually 0. It's also important to note that not every lie algebra is semisimple. This is actually ok, as we can decompose any arbitrary lie algebra into a semisimple one and it's *radical*. This is beyond the scope of this talk.

We will now discuss the *roots* of a semisimple Lie algebra. If we let $\mathfrak{g}$ be a semisimple Lie algebra, then a *Cartan* subalgebra is a maximal abelian subalgebra. If we now consider the adjoint action of some Cartan subalgebra ${} \mathfrak{h} \subset \mathfrak{g} {}$ on ${} \mathfrak{g} {}$, that is, we take $\ad \mathfrak{h}$ to the adjoint action of every element of $\mathfrak{h}$ on $\mathfrak{g}$. Since $\mathfrak{h}$ is abelian, then ${} (\ad X)(\ad Y)=(\ad Y)(\ad X) {}$. Since the elements of $\ad \mathfrak{h} {}$ are linear transformations, we may consider the Eigenvectors and Eigenvalues of them. In particular, consider the *minimal polynomial* $\mu {}$ of each ${} A \in \ad \mathfrak{h} {}$. We have
$$
\mu=\pi_{1}^{a_{1}}\pi_{2}^{a_{2}}\dots \pi_{n}^{a_{n}}
$$
where each ${} \pi_{i}$ are prime polynomials. Since the field is complex, then each ${} \pi_{i}=\lambda-\alpha_{i} {}$ for some complex number ${} \alpha_{i}$. 

Now a standard theorem of linear algebra tells us that, if we let ${} \mathfrak{g}_{\pi_{i}}=\{x \in \mathfrak{g} \mid \pi_{i}^{k}(x)=0 \text{ for some }k\} {}$ (that is, the generalised eigenspace with respect to ${} \alpha_{i} {}$), then 
$$
\mathfrak{g}=\bigoplus_{i=1}^{n}\mathfrak{g}_{\pi_{i}}
$$
Now the restriction of ${} A {}$ to each ${} \mathfrak{g}_{\pi_{i}} {}$ has exactly one eigenvalue, ${} \alpha_{i} {}$. Now consider ${} b \in \ad  \mathfrak{h} {}$. Note that since $\ad \mathfrak{h} {}$ is abelian, then 
$$
B\pi_{i}^{a_{i}}(A)=\pi_{i}^{a_{i}}(A)B
$$
and so for some ${} x \in \mathfrak{g}_{\pi_{i}} {}$, we have
$$
\pi_{i}^{a_{i}}(A)(B(x))=B \pi_{i}^{a_{i}}(A)(x)=B(0)=0
$$
Therefore, ${} B(x) \in \mathfrak{g}_{\pi_{i}} {}$ as well. Therefore, the restriction of any ${} B {}$ to ${} \mathfrak{g}_{\pi_{i}} {}$ is a linear transformation on ${} g_{\pi_{i}} {}$. Therefore, as before, we may decompose each ${} \mathfrak{g}_{\pi_{i}} {}$ into a direct sum of generalised eigenspaces of $B$. Note that the restriction of $A$ to each of these spaces still only has a single eigenvalue. This process can be continued, until we end up with a set of spaces, $\mathfrak{g}_{\alpha}$ where the restriction of each ${} X \in \ad \mathfrak{h} {}$ to ${} \mathfrak{g}_{\alpha} {}$ has a single eigenvalue, $\alpha(X)$. Now $\alpha(X)$ is a linear functional on $\ad \mathfrak{h}$, and the set of all such $\alpha$ are called the *roots* of $\mathfrak{g}$ with respect to $\mathfrak{h} {}$.

Let $\mathfrak{g}$ be a semisimple Lie algebra, and let $\mathfrak{h}$ be a maximal abelian subalgebra in $\mathfrak{g} {}$; we call this a Cartan subalgebra. This means that if we have another abelian subalgebra ${} \mathfrak{h}' {}$ containing ${} \mathfrak{h} {}$ then ${} \mathfrak{h}' = \mathfrak{h} {}$. We call a linear functional ${} \alpha:\mathfrak{h}\to{}\mathbb{C} {}$ a *root* if there exists some ${} x \in \mathfrak{g} {}$ with, for all ${} h \in \mathfrak{h} {}$, ${} (\ad h)(x)=\alpha(h)x {}$, that is, there exists an eigenvector of every element in $\ad \mathfrak{h}$, and ${} \alpha {}$ gives it's eigenvalue. An important theorem called Lie's Theorem tells us that every Lie algebra has at least one root.

Now given some root ${} \alpha {}$, we set the *root space* corresponding to ${} \alpha {}$ to be ${} \mathfrak{g}_{\alpha}=\{ x \in \mathfrak{g}\mid \forall h \in \mathfrak{h}:(\ad h-\alpha(h)I)^{k}(x)=0 \text{ for some }k \} {}$. This is a fairly esoteric definition, however, we may see this as the set of every ${} x {}$ which is a generalised eigenvector for all ${} \ad h {}$ with eigenvalue ${} \alpha (h) {}$. We also see that the restriction of $\ad h {}$ to $g_{\alpha} {}$ has exactly one eigenvalue, ${} \alpha(h) {}$. In particular, we see that since ${} \pi_{\alpha}^{h}=(\ad h-\alpha(h)I)^{k} {}$ is a polynomial in $\ad h {}$, and $\mathfrak{h} {}$ is abelian, then ${} \pi_{\alpha}^{h} (\ad k)(x)=(\ad k )\pi_{\alpha}^{h}(x) {}$, and so the generalised eigenspace decomposition associated with ${} \ad h {}$ are stable under all $\ad k {}$. Therefore, we may inductively keep decomposing the each generalised eigenspace into smaller generalised eigenspaces until the restriction of every $\ad k {}$ to them has exactly one eigenvalue, which is ${} \alpha(k) {}$. Therefore, we see that
$$
\mathfrak{g}=\bigoplus_{\alpha \in \Delta} \mathfrak{g}_{\alpha}
$$
If you didn't fully catch that, that's fine. All you need to know is that the roots of every semisimple lie algebra are entirely determined by $\mathfrak{h} {}$, and that $\mathfrak{g} {}$ may be directly decomposed into root spaces. This is great, as this is essentially a simultaneous generalised eigenspace decomposition.

We now only have a couple things left before we may start diving into the properties of root spaces. The first is Killing forms. They have nothing to do with death, they're just named after someone called Wilhelm Killing... Giving some Lie algebra ${} \mathfrak{g} {}$, and  ${} x,\, y \in \mathfrak{g} {}$
$$
(x,\, y)=\tr  (\ad (x) \ad (y))
$$
Since $\tr$ is linear and symmetric, then this is a symmetric bilinear form. Furthermore, we see that
$$
\begin{align}
([x, y],\, z)-(x, [y, z]) & =\tr  (\ad [x,\, y]\ad (z)-\ad (x)\ad [y,\, z]) \\
 & =\tr  (XYZ-YXZ-XYZ+XZY) \\
 & =\tr  [XZ,\, Y] \\
 & =0
 \end{align}
$$
since the trace of any commutator is zero. We have Cartan's criterion for semi-simplicity, which tells us that a Lie algebra is semisimple if and only if the killing form is non-degenerate, meaning that no vector is orthogonal to every vector. The killing form gives a sort of inner product, although it is not positive definite. However, it does give us the basis for the geometry and therefore structure of the semisimples.

We now dive in head first into the structure of the semisimple Lie algebras. Let $\mathfrak{g}$ be a semisimple finite dimensional Lie algebra over $\mathbb{C}$, let $\mathfrak{h} {}$ be a Cartan subalgebra, and let $\Delta$ be the set of it's roots. We see that $0$, the functional that maps all ${} h \in \mathfrak{h} {}$ to $0$, is a root, as ${} (\ad h)(h)=0h {}$ for all $h$, so $0$ is an eigenvalue for every $\ad h$. We also see that ${} \mathfrak{g}_{0}=\{ x \in \mathfrak{g} \mid \forall h \in \mathfrak{h}:(\ad h)^{k}(x)=0 \text{ for some }k \} {}$ contains $\mathfrak{h} {}$, as if ${} h \in \mathfrak{h} {}$, then ${} (\ad h)(k)=[h,\, k]=0 {}$ for all ${} k \in \mathfrak{h} {}$, so it is in ${} \mathfrak{g}_{0} {}$. We have
$$
\mathfrak{g} = \bigoplus_{\alpha \in \Delta} \mathfrak{g}_{\alpha}=\mathfrak{g}_{0} \oplus \mathfrak{g}_{\alpha_{1}} \oplus \mathfrak{g}_{\alpha_{2}}\oplus \dots
$$
It may be shown that, given roots ${} \alpha {} {}$, ${} \beta {}$, if ${} \alpha+\beta {}$ is a root, then
$$
[\mathfrak{g}_{\alpha},\, \mathfrak{g}_{\beta}] \subseteq \mathfrak{g}_{\alpha+\beta}
$$
and otherwise, 
$$
[\mathfrak{g}_{\alpha},\, \mathfrak{g}_{\beta}] =0
$$
The proof requires tensor products and a time consuming induction, so I'm afraid is beyond the scope of this talk, so it shall be taken for granted. Now recall that the restriction of $\ad h$ to $\mathfrak{g}_{\alpha}$ has only one eigenvalue, ${} \alpha(h) {}$. Therefore, the matrix corresponding to the restriction of ${} \ad h {}$ to ${} \mathfrak{g}_{\alpha} {}$ is of the form
$$
\begin{pmatrix}
\alpha(h) & 0 & \dots & 0 \\
* & \alpha(h) & \dots & 0 \\
\vdots  & \vdots & \ddots & \vdots \\
*  & * & \dots & \alpha(h)
\end{pmatrix}
$$
and
$$
(h,\,  k)=\sum_{\alpha \in \Delta} \dim (\mathfrak{g}_{\alpha})\alpha(h) \alpha(k)
$$
for some ${} h,\, k \in \mathfrak{h} {}$. If we now write ${} \mathfrak{h}^{*} {}$ as the dual space, the space of all linear functionals on ${} \mathfrak{h} {}$, then we see that every root is an element of ${} \mathfrak{h}^{*} {}$. A standard result from linear algebra tells us that since the killing form is non-degenerate, then for every element ${} \alpha \in \mathfrak{h}^{*} {}$, there exists some unique element ${} \mathbf{h}_{\alpha} {}$ with ${} (\mathbf{h}_{\alpha}, h)=\alpha(h) {}$ for all $h$, where this mapping ${} \alpha\mapsto \mathbf{h}_{\alpha} {}$ is bijective. This induces an analogue of the killing form on ${} \mathfrak{h}^{*}$, where if ${} \alpha,\, \beta \in \mathfrak{h}^{*} {}$, then
$$
(\alpha,\, \beta)=(\mathbf{h}_{\alpha},\, \mathbf{h}_{\beta})=\alpha(\mathbf{h}_{\beta})=\beta(\mathbf{h}_{\alpha})
$$

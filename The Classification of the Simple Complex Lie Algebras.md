We start by defining Lie algebras. Given a vector space ${} \mathfrak{g} {}$ over some field $F$, we call $\mathfrak{g} {}$ a *Lie Algebra* if we have a bilinear map, the lie bracket from g to itself ${} [{}\cdot{} ,{}\cdot{} ]:\mathfrak{g}\times \mathfrak{g}\to{}\mathfrak{g} {}$ satisfying, for all ${} x,\, y,\, z \in \mathfrak{g} {}$, 
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

We now define abelianity and simplicity. We start with an *ideal*. Ideals are analogous to normal subgroups, and are simply the subalgebras of a Lie algebra which are invariant under the action of the lie algebra. In particular, if ${} \mathfrak{h} {}$ is an ideal of ${} \mathfrak{g}, {}$ then ${} [\mathfrak{g},\, \mathfrak{h}]=\{ [x,\, y] \mid x \in \mathfrak{g},\, y \in \mathfrak{h} \} {}\subseteq \mathfrak{h} {}$. Now an abelian Lie algebra is one such that ${} [\mathfrak{g},\, \mathfrak{g}]=0 {}$, that is, for all ${} x,\, y \in \mathfrak{g} {}$, ${} [x,\, y]=0 {}$. 

Furthermore, a *simple* Lie algebra is a non-abelian Lie algebra with no non-trivial ideals, that is, other than ${} 0 {}$ and itself. These are special as they cannot be expressed as a direct product of any other lie algebras; in a sense, they are *prime*. They are also the central object of study for this talk. Finally, for our purposes, a *semisimple* lie algebra is one which is a direct product of simple lie algebras. If you know Lie algebras already, you may know that this is not the typical definition, however, this is fine, since it turns out over ${} \mathbb{C} {}$, this definition and the traditional one is equivalent. It's important to note that not every lie algebra is semisimple. This is actually ok, as we can decompose any arbitrary lie algebra into a semisimple one and it's *radical*. This is beyond the scope of this talk.

Let ${} \mathfrak{g}$ be a semisimple Lie algebra, and let $\mathfrak{h}$ be a maximal abelian subalgebra in $\mathfrak{g} {}$; we call this a Cartan subalgebra. This means that if we have another abelian subalgebra ${} \mathfrak{h}' {}$ containing ${} \mathfrak{h} {}$ then ${} \mathfrak{h}' = \mathfrak{h} {}$. We call a linear functional ${} \alpha:\mathfrak{h}\to{}\mathbb{C} {}$ a *root* if there exists some ${} x \in \mathfrak{g} {}$ with, for all ${} h \in \mathfrak{h} {}$, ${} (\ad h)(x)=\alpha(h)x {}$, that is, there exists an eigenvector of every element in $\ad \mathfrak{h}$, and ${} \alpha {}$ gives it's eigenvalue. An important theorem called Lie's Theorem tells us that every Lie algebra has at least one root.

Now given some root ${} \alpha {}$, we set the *root space* corresponding to ${} \alpha {}$ to be ${} \mathfrak{g}_{\alpha}=\{ x \in \mathfrak{g}\mid \forall h \in \mathfrak{h}:(\ad h-\alpha(h)I)^{k}(x)=0 \text{ for some }k \} {}$. This is a fairly esoteric definition, however, we may see this as the set of every ${} x {}$ which is a generalised eigenvector for all ${} \ad h {}$ with eigenvalue ${} \alpha (h) {}$. We also see that the restriction of $\ad h {}$ to $g_{\alpha} {}$ has exactly one eigenvalue, ${} \alpha(h) {}$. In particular, we see that since ${} \pi_{\alpha}^{h}=(\ad h-\alpha(h)I)^{k} {}$ is a polynomial in $\ad h {}$, and $\mathfrak{h} {}$ is abelian, then ${} \pi_{\alpha}^{h} (\ad k)(x)=(\ad k )\pi_{\alpha}^{h}(x) {}$, and so the generalised eigenspace decomposition associated with ${} \ad h {}$ are stable under all $\ad k {}$. Therefore, we may inductively keep decomposing the each generalised eigenspace into smaller generalised eigenspaces until the restriction of every $\ad k {}$ to them has exactly one eigenvalue, which is ${} \alpha(k) {}$. Therefore, we see that
$$
\mathfrak{g}=\bigoplus_{\alpha \in \Delta} \mathfrak{g}_{\alpha}
$$
If you didn't fully catch that, that's fine. All you need to know is that the roots of every semisimple lie algebra are entirely determined by $\mathfrak{h} {}$, and that $\mathfrak{g} {}$ may be directly decomposed into root spaces. This is great, as this is essentially a simultaneous generalised eigenspace decomposition.

We now only have a single obstacle left before we may start delving into the properties of root spaces; Killing forms. They have nothing to do with death, they're just named after someone called Wilhelm Killing... Giving some Lie algebra ${} \mathfrak{g} {}$, and  ${} x,\, y \in \mathfrak{g} {}$
$$
(x,\, y)=\tr  (\ad (x) \ad (y))
$$
Since $\tr {}$ is linear and symmetric, then this is a symmetric bilinear form. We have Cartan's criterion for semi-simplicity, which tells us that a Lie algebra is semisimple if and only if the killing form is non-degenerate, meaning that no vector is orthogonal to every vector. The killing form gives a sort of inner product, although it is not positive definite. However, it does give us the basis for the geometry and therefore structure of the semisimples.

We now dive in head first into the structure of the semisimple Lie algebras. Let ${} \mathfrak{g}$ be a semisimple finite dimensional Lie algebra over $\mathbb{C}$, let $\mathfrak{h} {}$ be a Cartan subalgebra, and let $\Delta$ be the set of it's roots. We see that $0$, the functional that maps all ${} h \in \mathfrak{h} {}$ to $0$, is a root, as ${} (\ad h)(h)=0h {}$ for all $h$, so $0$ is an eigenvalue for every $\ad h$. We also see that ${} \mathfrak{g}_{0}=\{ x \in \mathfrak{g} \mid \forall h \in \mathfrak{h}:(\ad h)^{k}(x)=0 \text{ for some }k \} {}$ contains $\mathfrak{h} {}$, as if ${} h \in \mathfrak{h} {}$, then ${} (\ad h)(k)=[h,\, k]=0 {}$ for all ${} k \in \mathfrak{h} {}$, so it is in ${} \mathfrak{g}_{0} {}$. 

I didn't want to have to do this, but I'm afraid I'm going to have to provide several proofs by magic and clairvoyance, chiefly due to time and sophistication constraints. Many of these results come from the representation theory of Lie algebras. To this end, I will ask you to accept without proof the following facts:
1. ${} \mathfrak{g}_{0} {}$ is abelian. Since ${} \mathfrak{h} {}$ is maximal abelian and contains $\mathfrak{g}_{0} {}$, then ${} \mathfrak{h}=\mathfrak{g}_{0} {}$.
2. If $\alpha {}$ is a nonzero root, then the only complex ${} k {}$ such that ${} k\alpha {}$ is a root is ${} k=-1,\, 0,\, 1 {}$, and ${} -\alpha {}$ is always a root. Moreover, ${} \dim \mathfrak{g}_{\alpha}=1 {}$
We have that $\mathfrak{g}_{\alpha} {}$ and $\mathfrak{g}_{\beta} {}$ are orthogonal relative to the Killing form iff ${} \alpha \neq-\beta {}$, so $\mathfrak{g} {}$ may be visualised as the flat expanse of ${} \mathfrak{h} {}$ and then a bunch of lines corresponding to $\alpha {}$ and $-\alpha {}$ shooting out.
3. The dual space of ${} \mathfrak{h} {}$, the space of all linear functionals ${} \rho:\mathfrak{h}\to{}\mathbb{C} {}$, written ${} \mathfrak{h}^{*} {}$, is spanned by all roots $\alpha$. Let ${} \ell {}$ be the dimension of ${} \mathfrak{h} {}$, that is, the number of linearly independent roots.
This can be seen as otherwise we would have a nonzero element of ${} \mathfrak{h} {}$ which is orthogonal to all others, which is impossible. This tells us that we have an isomorphism, ${} \mathbf{h}:\mathfrak{h}^{*}\to{}\mathfrak{h} {}$, mapping from each root ${} \alpha\to{}\mathbf{h}(\alpha)=\mathbf{h}_{\alpha} {}$ an element such that for all ${} h \in \mathfrak{h} {}$, ${} (\mathbf{h}_{\alpha},\, h)=\alpha(h) {}$. This allows us to induce a symmetric bilinear non-degenerate form on ${} \mathfrak{h}^{*}$ by, given 2 roots, ${} (\alpha,\, \beta)=(\mathbf{h}_{\alpha},\, \mathbf{h}_{\beta})=\alpha(\mathbf{h}_{\beta})=\beta(\mathbf{h}_{\alpha}) {}$. This leads us to fact 5:
4. For all roots ${} \alpha {}$, there exist some ${} \mathbf{e}_{\alpha} \in \mathfrak{g}_{\alpha} {}$ and ${} \mathbf{e}_{-\alpha} \in \mathfrak{g}_{-\alpha} {}$ with ${} [\mathbf{e}_{\alpha},\, \mathbf{e}_{-\alpha}]=\mathbf{h}_{\alpha} {}$.
5. for all nonzero roots, $(\alpha,\, \alpha)\neq 0 {}$. (for some reason the best proof of this I could find is long, tedious, and not very insightful)

This leaves us in the following position. We may decompose ${} \mathfrak{g} {}$ by $\mathfrak{h} {}$ as
$$
\mathfrak{g}=\mathfrak{h} \oplus \mathfrak{g}_{\alpha} \oplus \mathfrak{g}_{-\alpha} \oplus \mathfrak{g}_{\beta} \oplus \dots
$$
with $\ell$ linearly independent roots, and each ${} \mathfrak{g}_{\alpha}=\mathbf{e}_{\alpha} \mathbb{C} {}$ is one dimensional, and ${} [\mathbf{e}_{\alpha},\, \mathbf{e}_{-\alpha}]=\mathbf{h}_{\alpha} {}$, where ${} (\mathbf{h}_{\alpha},\, h)=\alpha(h) {}$, and the ${} \mathbf{h}_{\alpha} {}$ span $\mathfrak{h} {}$. Also, if ${} \beta$ is a nonzero multiple of another nonzero root $\alpha$, then ${} \beta=-\alpha_{}. {}$ 

Now we do our best to establish a theorem which blows the structure wide open. First, let
$$
\mathfrak{M}_{\alpha}= \span\{\mathbf{e}_{\alpha},\, \mathbf{e}_{-\alpha},\, \mathbf{h}_{\alpha}\}
$$
Thanks to the same magic that we can choose ${} \mathbf{e}_{\alpha} {}$ and ${} \mathbf{e}_{-\alpha} {}$, we have that
$$
[\mathbf{h}_{\alpha},\, \mathbf{e}_{\alpha}]=\alpha(\mathbf{h}_{\alpha})\mathbf{e}_{\alpha}=(\alpha,\, \alpha)\mathbf{e}_{\alpha}
$$
and
$$
[\mathbf{h}_{\alpha},\, \mathbf{e}_{-\alpha}]=-\alpha(\mathbf{h}_{\alpha})\mathbf{e}_{-\alpha}=-(\alpha,\, \alpha)\mathbf{e}_{-\alpha}
$$
and if we set
$$
\mathbf{e}'_{\alpha}=\mathbf{e}_{\alpha},\, \qquad \mathbf{e}_{-\alpha}'=\frac{2\mathbf{e}_{-\alpha}}{(\alpha,\, \alpha)},\, \qquad \mathbf{h}_{\alpha}'=\frac{2\mathbf{h}_{\alpha}}{(\alpha,\, \alpha)}
$$
then we get the relations
$$
[\mathbf{e}_{\alpha}',\, \mathbf{e}_{-\alpha}']=\mathbf{h}_{\alpha}',\, \qquad [\mathbf{h}'_{\alpha},\, \mathbf{e}_{\alpha}']=2\mathbf{e}_{\alpha}',\, \qquad [\mathbf{h}_{\alpha}',\, \mathbf{e}_{-\alpha}']=-2\mathbf{e}'_{-\alpha}
$$
If you're paying attention, you may notice this as exactly the relations for the Lie algebra ${} \mathfrak{sl}_{2}(\mathbb{C}) {}$, so ${} \mathfrak{M}_{\alpha} \cong  \mathfrak{sl}_{2}(\mathbb{C}) {}$. Thanks to the magical representation theory of ${} \mathfrak{sl}_{2}(\mathbb{C}) {}$, there exists a basis for $\mathfrak{g}$ such that $\ad \mathbf{h}_{\alpha} {}$ is diagonal; recall that in the original example, then ${} h=\begin{pmatrix}1 & 0 \\ 0 & -1 \end{pmatrix}  {}$. In fact, since ${} \mathfrak{h} {}$ is abelian, then
$$
(\ad \mathbf{h}_{\alpha})(\ad \mathbf{h}_{\beta})= (\ad \mathbf{h}_{\beta}) (\ad  \mathbf{h}_{\alpha})
$$
and there exists a basis for ${} \mathfrak{g} {}$ such that *all* ${} \ad \mathbf{h}_{\alpha} {}$ are diagonal, so every ${} \ad h \in \ad \mathfrak{h} {}$ is diagonal. Now the eigenvalues of each $\ad h {}$ are exactly the roots, that is, for some ordering of the roots ${} \alpha_{i} {}$, we have some basis ${} y_{i} {}$ of ${} \mathfrak{g} {}$ with
$$
\ad h= \begin{pmatrix}
\alpha_{1}(h) & 0 & 0 & \dots & 0 \\
0 & \alpha_{2}(h) & 0 & \dots & 0 \\
0 & 0 & \alpha_{3}(h) & \dots & 0 \\
\vdots & \vdots & \vdots & \ddots & \vdots \\
0 & 0 & 0 & \dots & \alpha_{N}(h)
\end{pmatrix}
$$
where $N {}$ is the dimension of $\mathfrak{g} {}$. Note that ${} \ell=\dim \mathfrak{h} {}$ of the roots shall be zero, and the rest shall be distinct. It is clear that the restriction of ${} \ad h$ to ${} \mathfrak{g}_{\alpha} {}$ is simply equal to multiplication by ${} \alpha(h) {}$. 

 Now if ${} \alpha,\, \beta {}$ are roots, then we have integers ${} q,\, r {}$ such that ${} \beta+q\alpha {}$ is a root but ${} \beta+(q+1)\alpha {}$ isn't, and ${} \beta-r\alpha {}$ is a root but ${} \beta-(r+1)\alpha {}$ isn't. We have that if ${} -r\leq k\leq q {}$, then ${} \beta+k\alpha {}$ is a root. Sadly, we shall have to wave the magic representation-theory wand again, and see in the crystal ball that $$
\frac{2(\beta,\, \alpha)}{(\alpha,\, \alpha)}=r-q
$$
The basic idea behind this comes from the subalgebra ${} \mathfrak{L}_{\alpha}=\mathfrak{g}_{\alpha} \oplus \mathfrak{g}_{-\alpha} \oplus  \mathfrak{h} {}$, where we consider subspaces of ${} \mathfrak{g} {}$ which are stable under $\ad \mathfrak{L}_{\alpha} {}$. These subsets have at least one root $M {}$ and an associated simultaneous eigenvector ${} y$, and ${} H=\ad \mathbf{h}_{\alpha}' {}$ from above gives 
$$
H(y)= \frac{2(M,\, \alpha)}{(\alpha,\, \alpha)}
$$
Where this is known to be an integer. Then, by fiddling around with roots, the value above can be obtained for any 2 roots.

The good news, however, is that we can do better. Call the ${} \alpha$-string containing $\beta$ the arithmetic progression
$$
\beta-r\alpha,\, \beta-(r-1)\alpha,\,\dots,\,\beta+q\alpha
$$
Assume that ${} \beta\neq\alpha, {}$ or ${} \neq-\alpha {}$, as we know what happens there (${} r=q=1 {}$). Assume that we have at least 5 roots, relabelling such that they are
$$
\beta-2\alpha,\, \quad \beta-\alpha,\, \quad \beta\phantom{+\alpha},\,\quad  \beta+\alpha,\, \quad \beta+2\alpha
$$
We know that ${} 2\alpha {}$ and ${} 2(\alpha+\beta) {}$ are not roots, as no integer multiple of a root is a root except for ${} k=-1,\, 0,\, 1 {}$. Now
$$
\begin{align}
 2\alpha & =(\beta+2\alpha)-\beta   \\
2(\alpha+\beta) & =(\beta+2\alpha)+\beta
 \end{align}
$$
are not roots, so the ${} \beta {}$-string containing ${} \beta+2\alpha {}$ has only one element. Therefore, we have ${} r=q=0 {}$, so 
$$
\frac{2(\beta+2\alpha,\, \beta)}{(\beta,\, \beta)}=r-q=0
$$
and ${} (\beta+2\alpha,\, \beta)=0 {}$. We can do the same thing for ${} \beta-2\alpha {}$, obtaining ${} (\beta-2\alpha,\, \beta)=0 {}$. Now adding these together, since the Killing form is bilinear, we get
$$
0=(\beta+2\alpha,\, \beta)+(\beta-2\alpha,\, \beta)=(2\beta,\, \beta)=2(\beta,\, \beta)
$$
which contradicts one of our facts from earlier that ${} (\beta,\, \beta)\neq 0$. Therefore, we can have no more than ${} 4$ roots in a string, so given any 2 nonzero roots $\alpha$, ${} \beta {}$, we get
$$
\frac{2(\beta,\, \alpha)}{(\alpha,\, \alpha)}=0,\, \pm1,\, \pm 2,\, \pm 3
$$
This *heavily* restricts the geometry of the roots. Finally, to restrict it even further, we introduce our last magical fact: if ${} \alpha,\, \beta {}$ are roots, then
$$
\beta'=\beta-\frac{2(\beta,\, \alpha)}{(\alpha,\, \alpha)}\alpha
$$
is a root. You may recognise this as the reflection around the hyperplane ${} \alpha^{\perp} {}$ of roots perpendicular to $\alpha$. This maps ${} \alpha\to{}-\alpha {}$.

We are now ready to fully characterise the geometry of the roots of a semisimple Lie algebra. Since the killing form is positive definite, symmetric, and bilinear, then this can be seen as an inner product on some vector space ${} \mathbb{R}^{n} {}$, with the roots as vectors. Since the only scalar multiples of a root which are also roots are just ${} -1, 0, 1 {}$, then we can embed this as a real vector space. First, let us set
$$
n_{\alpha\beta}=\frac{2(\beta,\, \alpha)}{(\alpha,\, \alpha)}
$$
Now we can give an angle between roots, in particular, 
$$
(\alpha,\, \beta)=\lVert \alpha \rVert \lVert \beta \rVert \cos\theta=\sqrt{(\alpha,\, \alpha)(\beta,\, \beta)} \cos\theta
$$
so rearranging we get
$$
n_{\alpha\beta}=\frac{2(\alpha,\, \beta)}{(\alpha,\, \alpha)}=2\frac{ \lVert \beta \rVert }{ \lVert \alpha \rVert  } \cos\theta
$$
and 
$$
n_{\alpha\beta}n_{\beta\alpha}=4 \cos ^{2}\theta
$$
If we now plot the roots as vectors according to these rules, if we normalise a specific root as having length 1, we get pictures that look like these

these are all root systems of *rank* 2, here they correspond to Cartan subalgebras of dimension 2, and so are embedded in 2 dimensional Euclidian space. This is actually *every* rank 2 root system, as shall be seen shortly. If we now introduce a hyperplane, or, as normal people say, a line, which intersects with no roots and passes through the origin, then we may call all roots above it positive, and all roots below, negative. This may be done arbitrarily. 

Now, call a positive root *simple* if ${} \alpha$ cannot be written as a sum of 2 positive roots. Let $\pi$ the set of simple roots. On these systems, see that the roots highlighted in red are the simple roots. Now clearly $\pi$ spans the roots, and if we have any 2 distinct roots $\alpha$ and $\beta$, then if ${} \alpha-\beta {}$ is a positive root, then ${} \beta+(\alpha-\beta)=\alpha {}$, so $\alpha$ isn't simple. Likewise, if it is negative, then ${} \alpha+(\beta-\alpha)=\beta {}$, so $\beta$ isn't simple. Therefore, $\alpha-\beta {}$ isn't a root. this implies that ${} r=0 {}$ in the $\alpha$ string containing $\beta$, so $n_{\alpha\beta}\leq 0$. Now since ${} (\alpha,\, \alpha)>0 {}$, then ${} (\beta,\, \alpha)\leq 0$. 

Now we observe some properties of the $n_{\alpha\beta}$. First, note that ${} n_{\alpha\alpha}=2 {}$, clearly. Now if $\alpha\neq\beta {}$ are positive roots, then then angle between them, ${} \theta_{\alpha\beta} {}$ is given by ${} 0\leq \cos ^{2}\theta_{\alpha\beta}< 1 {}$, as if the angle is $\pi {}$, then ${} \alpha=-\alpha {}$. Now
$$
n_{\alpha\beta}n_{\beta\alpha}=4\cos ^{2}\theta_{\alpha\beta}\quad \Rightarrow\quad  0\leq n_{\alpha\beta} n_{\beta\alpha}< 4 \quad \Rightarrow  \quad n_{\alpha\beta} n_{\beta\alpha}=0,\, 1,\, 2,3
$$
so one of ns is equal to 1, and the other is equal to 1, 2 or 3, thanks to a simple result from number theory. Therefore, the only angles between roots may be given by this table, as well as the ratios of their lengths, if we assume that ${} \lVert \alpha \rVert \leq \lVert \beta \rVert{} {}$:

| ${} \cos\theta_{\alpha\beta} {}$                                | ${} \sqrt{3} /2 {}$        | ${} \sqrt{2} /2 {}$         | ${} 1/2 {}$                  | 0                           | ${} -1 /2 {}$                | ${} - \sqrt{2} /2 {}$          | ${} -\sqrt{3} /2 {}$           |
| --------------------------------------------------------------- | -------------------------- | --------------------------- | ---------------------------- | --------------------------- | ---------------------------- | ------------------------------ | ------------------------------ |
| $\theta_{\alpha\beta}$                                          | ${} \pi /6=30^{\circ } {}$ | ${} \pi /4 =45^{\circ } {}$ | ${} \pi /3 =60 ^{\circ } {}$ | ${} \pi /2 =90^{\circ } {}$ | ${} 2\pi /3=120^{\circ } {}$ | ${} 3\pi /4 = 135^{\circ } {}$ | ${} 5 \pi /6 =150^{\circ } {}$ |
| $n_{\alpha\beta}$                                               | $3$                        | $2 {}$                      | $1 {}$                       | $0$                         | $-1 {}$                      | $-2 {}$                        | ${} -3 {}$                     |
| ${} n_{\beta\alpha} {}$                                         | $1 {}$                     | $1 {}$                      | $1 {}$                       | $0 {}$                      | ${} -1 {}$                   | ${} -1 {}$                     | ${} -1 {}$                     |
| ${} \frac{ \lVert \beta \rVert }{ \lVert \alpha \rVert  }   {}$ | ${} \sqrt{3}$              | ${} \sqrt{2}$               | $1$                          | $*$                         | $1$                          | ${} \sqrt{2}$                  | ${} \sqrt{3} {}$               |
Since if $\alpha,\, \beta {}$ are simple then ${} (\alpha,\, \beta)\leq 0 {}$, then the angle between any 2 simple roots is obtuse. 

Now we establish Dynkin diagrams. First we normalise the simple roots by setting ${} u_{i}=k\alpha_{i} {}$ for every root ${} \alpha_{i}$ such that ${} \lVert u_{i} \rVert =(u_{i},\, u_{i})=1 {}$. Take some set of simple roots, and notate them as points on a plane. Now connect them by lines corresponding to the angles between them;
$$
0 \text{ lines if } \theta_{ij} = \frac{\pi}{2}\qquad 1 \text{ line if } \theta_{ij} =\frac{2\pi}{3} \qquad 2 \text{ lines if } \theta_{ij}= \frac{3\pi}{4}\qquad 4 \text{ lines if } \theta_{ij}=\frac{5\pi}{6}
$$
that is, ${} 4(u_{i},\, u_{j})^{2} {}$ is the number of incident lines. When we have ${} 2$ lines or $3 {}$ lines, then we draw an arrow pointing from the shorter root to the longer root. Since the simple roots generate the entirety of the roots, then a Dynkin diagram describes exactly every root system. 

Now suppose we have a Dynkin diagram like so which has 2 disconnected components. Then every vector in the first is orthogonal to the second, and so the associated root systems can be described as the direct product of 2 different lie algebras. Therefore, a semisimple lie algebra is simple iff it's Dynkin diagram is connected. Now we may classify every connected dynkin diagram in their entirety. First, we may ignore the arrows and focus only on the lines. These are known as conway diagrams. Consider an arbitrary dynkin diagram. First, it is clear that if we delete a root and all of it's incident nodes, then we get a dykin diagram. 

Now suppose we have a diagram with a loop in it. Then we have simple roots ${} \alpha_{i} {}$ with ${} (u_{i},\, u_{i+1})\neq 0 {}$, and ${} (u_{k}, u_{1})\neq 0 {}$. Then let ${} u=\sum_{i} u_{i} {}$, and by noting that ${} 2(u_{i},\, u_{j})\leq-1 {}$ if $i\neq j {}$, then
$$
0<(u,\, u)=\sum_{i}(u_{i},\, u_{i})+\sum_{i<j} 2(u_{i},\, u_{j})\leq l-l=0
$$
which is a contradiction. Therefore, we cannot have any loops. In a similar vein, we may show that the number of lines incident to any point may not be greater than $3$. 

In particular, consider a vector $u$ with $k$ ${} v_{i}$ incident to $u$ like so. No ${} v_{i}$ may be connected as that would be a loop. Therefore, the ${} v_{i} {}$ form an orthonormal basis for their span $S {}$, but ${} u$ is not in $S {}$, as it is simple. Therefore a well known theorem says that the projection ${} u' {}$ of ${} u$ onto $S$ has squared norm equal to ${} \sum_{i} (u',\, v_{i})^{2} {}$, which is strictly less than the norm of ${} v {}$, which is ${} 1 {}$. Therefore, 
$$
\sum_{i}(u,\, v_{i})^{2} <1\Rightarrow \sum 4(u,\, v_{i})^{2} <4
$$
which is exactly the number of lines incident on $u$. Therefore, diagrams like this may be discarded. Finally, we discuss compressing of diagrams.

In particular, if a diagram has a string of roots connected by only 1 line like so, then we may merge those roots into a single root and end up with another dynkin diagram. In particular, if we havr roots ${} u_{i}$ with ${} 4(u_{i},\, u_{i+1})^{2}=1 {}$, then ${} u=\sum_{i} u_{i} {}$ is a unit vector, as
$$
(u,\, u)=\sum_{i}(u_{i}, u_{i})+2\sum_{i<j} (u_{i},\, u_{j})=l-(l-1)=1
$$
and if a vector $a$ is incident on $u_{1}$ or ${} u_{k} {}$, then it is incident on $u$, as every other ${} u_{i} {}$ is necessarily disconnected. This rules out Dynkin diagrams like the following. This leaves us with only the following diagrams. This, this and this may be ruled out using the same methods as before, albeit slightly more sophisticated and time consuming. Every other diagram is actually admissible, and is named and classified as so. The explicit construction of their corresponding simple lie algebras is possible, time consuming, and not worth the trouble. However the ${} A {}$ family corresponds to lie algebras of matrices of dimension ${} \ell \times \ell$ with trace $0$, that is,${} \mathfrak{sl}_{l}(\mathbb{C}) {}$, the $B$ family corresponds to lie algebras of matrices of dimension ${} \ell \times  \ell {}$ where $\ell {}$ is even, and the matrices are orthogonal, that is ${} A = -A^{\mathrm{T}} {}$, also known as ${} \mathfrak{so}_{2\ell}(\mathbb{C}) {}$.

The $C$ family corrasppon







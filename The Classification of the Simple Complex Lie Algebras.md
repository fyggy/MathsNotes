First, we define Lie Groups. A *smooth manifold* is essentially a shape in space with a topology, and appears *locally smooth*, with smooth here being analogous to a function being infinitely differentiable. A Lie group is a smooth manifold with group structure, such that group multiplication and inversion are also smooth maps. The prototypical example is ${} \mathrm{SO}(2) {}$, the group of rotations in $2 {}$-D. It can be represented as a circle, and it is clear to see that the group operation is smooth. 

A Lie *algebra* is an algebra defined tangent to the identity of a Lie Group. The formal construction is fairly technical, but it can be surmised by the idea of creating a "map" or "projection" of your manifold onto a flat space; specifically a vector space. It turns out, when you do this, you get a multiplication of sorts from the group operation. This is called the *lie bracket*. 

In particular, given a vector space ${} \mathfrak{g} {}$ over some field $F$, we call $\mathfrak{g} {}$ a *Lie Algebra* if we have a bilinear map ${} [{}\cdot{} ,{}\cdot{} ]:\mathfrak{g}\times \mathfrak{g}\to{}\mathfrak{g} {}$ satisfying, for all ${} x,\, y,\, z \in \mathfrak{g} {}$, 
$$
\begin{align}
[x,\, x] & =0\\
 [x,\, y] & =-[y,\, x]   \\
[x,\, [y,\, z]]+[z,\, [x,\, y]]+[y,\, [z,\, x]] & =0
 \end{align}
$$
Note that ${} [x,\, 0]=0 {}$, as it is bilinear. In this talk we will only be concerned with finite dimensional Complex Lie algebras, that is, those with ${} F=\mathbb{C} {}$. Now you may recognise these relations as exactly those satisfied by a commutator, which is a map from an associative algebra $A$, ${} [{}\cdot {},\, {}\cdot {}]:A \times A\to{}A {}$ defined by ${} [X,\, Y]=XY-YX {}$. Indeed, the Lie bracket is a generalisation of this idea. In fact, any associative algebra may be made into a lie algebra by taking multiplication to be the commutator. 

Now define ${} \ad :\mathfrak{g}\to{}\operatorname{End}(\mathfrak{g}) {}$ as ${} \ad (x)(y)=[x,\, y] {}$. That is, $\ad x$ is simply $\mathfrak{g}$ acting on itself from the left. This seems silly, but it turns out to have lovely properties. In particular, it is a *representation* of $\mathfrak{g} {}$, called the adjoint representation of ${} \mathfrak{g} {}$. In particular, if we take ${} x,\, y,\, z \in \mathfrak{g} {}$, we see that
$$
\begin{align}
\ad ([x,\, y])(z) & =[[x,\, y],\, z] \\
 & =-[z,\, [x,\, y]] \\
 & =[x,\, [y,\, z]]+[y,\, [z,\, x]] \\
 & =[x,\, [y,\, z]]-[y,\, [x,\, z]] \\
 & =(\ad (x)\ad (y)-\ad (y)\ad (x) )(z) \\
 & =[\ad (x),\, \ad (y)](x)
\end{align}
$$
Where the bracket at the end is the standard commutator. We see then, that ${} \ad {}$ is actually a *Lie homomorphism*, that is, it preserves the structure of the Lie bracket. However, it also acts on the lie algebra itself. This property will be very useful.

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

On more types, an abelian lie algebra is one where every bracket is zero, that is ${} [x,\, y]=0 {}$ for all ${} x,\, y \in \mathfrak{g} {}$. The name comes from the fact that if the commutator is zero for all elements in an associative algebra, then all the elements commute. Furthermore, a *simple* lie algebra is a non-abelian Lie algebra, that is, there exists some ${} x,\, y \in \mathfrak{g} {}$ with ${} [x,\, y]\neq 0 {}$ with no non-trivial ideals, that is, other than ${} 0 {}$ and itself. These are special as they cannot be expressed as a direct product of any other lie algebras; in a sense, they are *prime*. They are also the central object of study for this talk. Finally, for our purposes, a *semisimple* lie algebra is one which is a direct product of simple lie algebras. If you know lie algebras, you may know that this is not the typical definition, however, this is fine, since it turns out over $\mathbb{C}$, this definition and the traditional one is equivalent. 

All these terms may seem bewildering, but don't worry, we will constantly be recounting the definitions. Just remember: simple = prime, semisimple = product of primes, abelian = almost 0, nilpotent = eventually 0. It's also important to note that not every lie algebra is semisimple. This is ok, as we can decompose any arbitrary lie algebra into a semisimple one and it's *radical*, which is beyond the scope of this talk.

Before we proceed, it's a 
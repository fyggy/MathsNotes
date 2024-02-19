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

We now define the import concepts of solubility, nilpotency, and simplicity. We start with an *ideal*. Ideals are analogous to normal subgroups, and are simply the subalgebras of a Lie algebra which are invariant under the action of the lie group. In particular, if $\mathfrak{h} {}$ is an ideal of ${} \mathfrak{g}, {}$ then ${} [\mathfrak{g},\, \mathfrak{h}]=\mathfrak{g}\mathfrak{h}=\{ [x,\, y] \mid x \in \mathfrak{g},\, y \in \mathfrak{h} \} {}$. Thanks to this invariance, we may quotient by ideals, and
---
tags:
  - homework
  - advalg1
date: 2024-09-23
pset: 1
completed: true
---
[[Directory]], [[University/Undergraduate/Second Year/Advanced Algebra 1/Advanced Algebra 1|Subject Directory]]
[[University/Undergraduate/Second Year/Advanced Algebra 1/Homework/Homework 1|🞀🞀]] [[|◀]] [[University/Undergraduate/Second Year/Advanced Algebra 1/Homework/Homework 2|▶]] [[University/Undergraduate/Second Year/Advanced Algebra 1/Homework/Homework 11|🞂🞂]]

[[University/Undergraduate/Second Year/Advanced Algebra 1/Homework/Worksheets/advanced_algebra_1.pdf|Worksheet]]
1. Let $G {}$ be a group and let ${} S \subseteq G {}$
a)
Let $\mathcal{A} {}$ be a non-empty set of subgroups of $G {}$. Set
$$
A=\bigcap_{H\in \mathcal{A}}H 
$$
Now let ${} x,\, y \in A {}$. Then ${} x,\, y \in H {}$ for all ${} H \in \mathcal{A} {}$. Since all the $H {}$ are subgroups, then ${} xy^{-1} \in H {}$, and therefore ${} xy^{-1} \in A {}$. Therefore, $A {}$ is a subgroup of $G {}$
b)
Let ${} \mathcal{A}_{S}=\{ H\leq G \mid S \subseteq H \} {}$, and set
$$
\langle S \rangle =\bigcap_{H\in \mathcal{A}_{S}} H 
$$
First note that since ${} S \subseteq H {}$ for all ${} H \in  \mathcal{A}_{S} {}$, then ${} S \subseteq  \langle S \rangle  {}$. Now suppose that ${} H\leq G {}$ with ${} S\subseteq H {}$. Since ${} H \in  \mathcal{A}_{S} {}$, then ${} \langle S \rangle \subseteq H {}$. Therefore, ${} \langle S \rangle  {}$ is the smallest subgroup of $G {}$ containing $S {}$.
c)
Since ${} \varnothing \subseteq H {}$ for all subgroups ${} H\leq G {}$, then ${} A_{\varnothing}=\{ S \subseteq G \mid  S\leq  G \} {}$. Therefore, ${} \langle \varnothing \rangle=\bigcup_{S\leq  G}  S=\{ 1 \}=1 {}$ 
d)
Clearly, ${} \langle S \rangle \leq  \mathrm{SL}_{2}(\mathbb{R}) {}$. Now let ${} A \in  \mathrm{GL}_{2}(\mathbb{R}) {}$. Since ${} \mathrm{GL}_{2}(\mathbb{R}) {}$ is generated by the elementary matrices, then we may assume that $A {}$ is a product of elementary matrices. Therefore, we may assume that $A {}$ is an elementary matrix for the sequel. First, if $A {}$ is a row switching matrix, then
$$
A=\begin{pmatrix}0 & 1 \\ 1 & 0 \end{pmatrix} =A^{-1}
$$
and
$$
\begin{pmatrix}0 & 1 \\ 1 & 0 \end{pmatrix} \begin{pmatrix}r & 0 \\ 0 & r^{-1} \end{pmatrix} \begin{pmatrix}0 & 1 \\ 1 & 0 \end{pmatrix} =\begin{pmatrix}0 & r^{-1} \\ r & 0 \end{pmatrix} \begin{pmatrix}0 & 1 \\ 1 & 0 \end{pmatrix} =\begin{pmatrix}r^{-1} & 0 \\ 0 & r \end{pmatrix} \in S
$$
and
$$
\begin{pmatrix}0 & 1 \\ 1 & 0 \end{pmatrix} \begin{pmatrix}1 & 1 \\ 0 & 1 \end{pmatrix} \begin{pmatrix}0 & 1 \\ 1 & 0 \end{pmatrix} =\begin{pmatrix}0 & 1 \\ 1 & 1 \end{pmatrix} \begin{pmatrix}0 & 1 \\ 1 & 0 \end{pmatrix} =\begin{pmatrix} 1& 0 \\ 1 & 1 \end{pmatrix} \in S
$$
and likewise with ${} \begin{pmatrix}1 & 0 \\ 1 & 1 \end{pmatrix}  {}$. Therefore, 
$$
ASA^{-1} \subseteq \langle S \rangle 
$$
Now if $A {}$ is a multiplication matrix, then 
$$
A=\begin{pmatrix}m & 0 \\ 0 & 1 \end{pmatrix} \qquad A^{-1}=\begin{pmatrix}m^{-1} & 0 \\ 0 & 1 \end{pmatrix} 
$$
and so since diagonal matrices commute
$$
A \begin{pmatrix}r & 0 \\ 0 & r^{-1} \end{pmatrix} A^{-1}=\begin{pmatrix}r & 0 \\ 0 & r^{-1} \end{pmatrix} 
$$
likewise, 
$$
A \begin{pmatrix}1 & 1 \\ 0 & 1 \end{pmatrix} A^{-1}=\begin{pmatrix}m & m \\ 0 & 1 \end{pmatrix} A^{-1}=\begin{pmatrix}1 & m \\ 0 & 1 \end{pmatrix} =\begin{pmatrix}\sqrt{m} & 0 \\ 0 & \sqrt{ m }^{\;-1} \end{pmatrix} \begin{pmatrix} 1& 1 \\ 0 & 1 \end{pmatrix} \begin{pmatrix}\sqrt{m} ^{\;-1} & 0 \\ 0 & \sqrt{ m } \end{pmatrix}\in \langle S \rangle 
$$
and likewise for ${} \begin{pmatrix} 1 & 0 \\ 1 & 1 \end{pmatrix}  {}$ or if ${} A=\begin{pmatrix}1 & 0 \\ 0 & m \end{pmatrix}  {}$.
Finally, if $A {}$ is an addition matrix, then 
$$
A=\begin{pmatrix}1 & m \\ 0 & 1 \end{pmatrix} \text{ or } A=\begin{pmatrix}1 & 0 \\ m & 1 \end{pmatrix}  
$$
Since ${} A \in \langle S \rangle  {}$ as established above, then ${} ASA^{-1} \subseteq \langle S \rangle  {}$. Therefore, for any ${} A \in \mathrm{GL}_{2}(\mathbb{R}) {}$, then ${} A \langle S \rangle A^{-1} \subseteq  \langle S \rangle  {}$, and ${} \langle S \rangle  {}$ is normal in ${} \mathrm{GL}_{2}(\mathbb{R}) {}$. In particular, this gives us that if any matrix is similar to a matrix in ${} \langle S \rangle$, then it is also an element of ${} \langle S \rangle  {}$. 

Now let ${} A \in  \mathrm{SL}_{2}(\mathbb{R}) {}$. Then, it's eigenvalues are either of the form ${} r,\, r^{-1} {}$, ${} r \in \mathbb{R}^{\times } {}$, or they are complex. If they are complex, then since they are roots of a real polynomial, then they must be conjugate. So if ${} r_{1}=a+bi {}$ is a eigenvalue, then the other, ${} r_{2} {}$, must be equal to
$$
r_{2}=\frac{1}{r_{1}}=\frac{1}{a+bi}=\frac{ a-bi }{ a^{2}+b^{2} }
$$
but 
$$
r_{2}=a-bi
$$
so ${} a^{2}+b^{2}=1 {}$. Therefore, ${} |r_{1}|=|r_{2}|=1 {}$. In particular, set ${} r_{1}=e^{i\theta} {}$. Then ${} r_{2}=e^{-i\theta} {}$. 

Now if the eigenvalues of $A {}$ are real but distinct, then it is similar to a diagonal matrix of the form
$$
\begin{pmatrix}r & 0 \\ 0 & r^{-1} \end{pmatrix} 
$$
which is an element of $S {}$. If they are real but indistinct, then it is similar to 
$$
\begin{pmatrix} 1 & 1 \\ 0 & 1 \end{pmatrix} 
$$
and if they are complex, then it is similar to
$$
\begin{align}
\begin{pmatrix}\cos\theta & -\sin\theta \\ \sin\theta & \cos\theta \end{pmatrix}  & =\begin{pmatrix}1 & -\tan\left( \frac{\theta}{2} \right) \\ 0 & 1 \end{pmatrix} \begin{pmatrix}1 & 0 \\ \cos\theta & 1 \end{pmatrix} \begin{pmatrix}1 & -\tan\left( \frac{\theta}{2} \right) \\ 0 & 1 \end{pmatrix} \in \langle S \rangle 
\end{align}
$$
Therefore, ${} A \in \langle S \rangle  {}$, so ${} \langle S \rangle =\mathrm{SL}_{2}(\mathbb{R}) {}$.
2. 
a)
Let ${} g \in G {}$, ${} z \in Z(G) {}$. Then ${} gzg^{-1}=zgg^{-1}=z \in Z(G) {}$, therefore ${} Z(G)\trianglelefteq G {}$
b)
Let ${} h \in G {}$. Suppose that ${} H\leq  G {}$, and that ${} h \in Z(H) {}$. Then for all ${} k \in H {}$, ${} hk=kh {}$, Therefore, ${} H \subseteq Z_{G}(h) {}$.
c)
Let ${} K \leq G {}$ such that ${} H\trianglelefteq K {}$. Therefore, for all ${} k \in K {}$, ${} kHk^{-1} =H {}$. Therefore, ${} K \leq  N_{G}(H) {}$
d)
Suppose that ${} A =\begin{pmatrix}a & b \\ c & d \end{pmatrix} \in  Z(G) {}$. Then 
$$
\begin{align}
 \begin{pmatrix}a & b \\ c & d \end{pmatrix} \begin{pmatrix}0 & 1 \\ 1 & 0 \end{pmatrix}   & = \begin{pmatrix}b & a \\ d & c \end{pmatrix}  \\
 & =\begin{pmatrix}c & d \\ a & b \end{pmatrix}  \\
 & =\begin{pmatrix}0 & 1 \\ 1 & 0  \end{pmatrix} \begin{pmatrix}a & b \\ c & d \end{pmatrix} 
 \end{align}
$$
and so ${} a=d {}$ and ${} b=c {}$. Now
$$
\begin{align}
\begin{pmatrix}a & b \\ c & d \end{pmatrix} \begin{pmatrix}0 & 1 \\ -1 & 0 \end{pmatrix}  & =\begin{pmatrix}-b & a \\ -d & c \end{pmatrix}  \\
 & =\begin{pmatrix}c & d \\ -a & -b \end{pmatrix}  \\
 & =\begin{pmatrix}0 & 1 \\ 1 & 0 \end{pmatrix} \begin{pmatrix}a & b \\ c & d \end{pmatrix} 
\end{align}
$$
and so ${} b=c=-c=-b=0 {}$, and ${} A=\begin{pmatrix}a & 0 \\ 0 & a \end{pmatrix}  {}$. Note that ${} A=aI {}$ where $I {}$ is the ${} 2\times 2 {}$ identity, and that for some matrix $B {}$
$$
AB=aIB=aB=B(aI)=BA
$$
and so every such matrix commutes. Therefore
$$
Z(G)=\{ aI \mid a \in \mathbb{R} \}
$$
Now Let ${} A=\begin{pmatrix}a & b \\ c & d \end{pmatrix}  \in Z_{G}(h) {}$. Then
$$
\begin{align}
 \begin{pmatrix}a & b \\ c & d \end{pmatrix}  \begin{pmatrix}1 & 1 \\ 0 & 1 \end{pmatrix}   & =\begin{pmatrix}a & a+b \\ c & c+d \end{pmatrix}  \\
 & =\begin{pmatrix} a+c&b+d  \\ c & d \end{pmatrix}   \\
 & =\begin{pmatrix}1 & 1 \\ 0 & 1 \end{pmatrix} \begin{pmatrix}a & b \\ c & d \end{pmatrix} 
 \end{align}
$$
and so ${} a=a+c {}$, so ${} c=0 {}$, ${} a+b=b+d {}$, so ${} a=d {}$, ${} c+d=d {}$, so ${} c=0 {}$. Therefore, 
$$
A=\begin{pmatrix}a & b \\ 0 & a \end{pmatrix} 
$$
and so ${} Z_{G}(h)=\left\{ \begin{pmatrix}a & b \\ 0 & a \end{pmatrix} \mid a,\, b \in \mathbb{R} \right\} {}$

Finally, Let ${} A=\begin{pmatrix}a & b \\ c & d \end{pmatrix} \in N_{G}(\langle h \rangle ) {}$. Then for all ${} n \in \mathbb{Z} {}$, then 
$$
Ah^{n}A^{-1}=h^{k}
$$
for some ${} k \in \mathbb{Z} {}$. First, note that 
$$
\begin{pmatrix}1 & a \\ 0 & 1 \end{pmatrix} \begin{pmatrix}1 & b \\ 0 & 1 \end{pmatrix} =\begin{pmatrix}1 & a+b \\ 0 & 1 \end{pmatrix} 
$$
Then ${} h^{n}=\begin{pmatrix}1 & n \\ 0 & 1 \end{pmatrix}  {}$. Now
$$
\begin{align}
\frac{1}{ad-bc}\begin{pmatrix}a & b \\ c & d \end{pmatrix} \begin{pmatrix}1 & n \\ 0 & 1 \end{pmatrix} \begin{pmatrix} d& -b \\ -c & a \end{pmatrix}  & =\frac{1}{a d-bc} \begin{pmatrix}ad-bc-nac  & na^{2} \\  -nc^{2}& ad-bc+nac \end{pmatrix}  \\
 & =\begin{pmatrix}1 & k \\ 0 & 1 \end{pmatrix} 
\end{align}
$$
and so ${} c=0 {}$, and we have
$$
\begin{align}
\frac{1}{a d-bc} \begin{pmatrix}ad-bc-nac  & na^{2} \\  -nc^{2}& ad-bc+nac \end{pmatrix}  & =\begin{pmatrix}1 & \frac{na}{d} \\ 0 & 1 \end{pmatrix} 
\end{align}
$$
so ${} \frac{na}{d} \in \mathbb{Z} {}$. In particular, since this holds for all ${} n \in Z {}$, we have ${} \frac{a}{d} \in \mathbb{Z} {}$. Therefore, 
$$
N_{G}(\langle h \rangle )=\left\{ \begin{pmatrix}a & b \\ 0 & d \end{pmatrix} \mid a,\, b,\, d \in \mathbb{R},\, d\neq 0,\, \frac{a}{d} \in \mathbb{Z} \right\} 
$$
3. 
a)
We have that ${} \im f=\{ f(n)\mid n \in \mathbb{Z} \}=\{ g^{n} \mid  n \in \mathbb{Z} \}=\langle g \rangle  {}$.
b)
We have 2 cases: 
Case 1: if ${} |g| {}$ is finite, then 
$$
\ker f=\{ n|g|  \mid n \in \mathbb{Z} \}=[n]
$$
Case 2: if ${} |g| {}$ is infinite, then
$$
\ker f=\{ 0 \}
$$
c)
Let $C {}$ be a cyclic group. Then there exists some element ${} c \in C {}$ such that ${} \langle c \rangle =C {}$. Define ${} f:\mathbb{Z} \to{}C {}$ to be ${} f(n)=c^{n}$. It is clear that ${} f {}$ is surjective. We have 2 cases:

Case 1: if ${} |g|=n {}$ is finite, then ${} \ker f=[n]=n\mathbb{Z} {}$, and so $f {}$ factors through a unique isomorphism ${} \theta:\mathbb{Z} / n\mathbb{Z} \to{}C {}$, and $C {}$ is isomorphic to ${} \mathbb{Z} /n\mathbb{Z} {}$.

Case 2: if ${} |g| {}$ is infinite, then ${} \ker f=\{ 0 \} {}$ is trivial, and so $f {}$ is injective. Since $f {}$ is surjective, then $f {}$ is an isomorphism
4. 
a)
First note that composition is associative. Now we have the identity automorphism, ${} \mathrm{id}:G\to{}G {}$ defined by ${} x \mapsto x {}$. Note that given an automorphism ${} \alpha \in \aut(G) {}$, then ${} \mathrm{id} \circ  \alpha=\alpha=\alpha \circ  \mathrm{id} {}$. Finally, since each automorphism ${} \alpha {}$ is bijective, then there exists a inverse isomorphism ${} \alpha ^{-1} {}$, with the property ${} \alpha\alpha ^{-1}=\mathrm{id}=\alpha ^{-1} \alpha {}$. Therefore, ${} \aut(G) {}$ is a group. 
b)
Let ${} h \in G {}$. First note that ${} \varphi_{h}(ab)=habh^{-1}=hah^{-1} hbh^{-1}=\varphi_{h}(a) \varphi_{h}(b) {}$, so ${} \varphi_{h} {}$ is a homomorphism. Now simply note that ${} \psi_{h}:G\to{}G {}$ defined by ${} \psi_{h}(x)=h^{-1} xh {}$ is an inverse of ${} \varphi_{h} {}$. In particular, 
$$
\varphi_{h}(\psi_{h}(x))=hh^{-1} xh h^{-1}=x=h^{-1}hxh^{-1}h=\psi_{h}(\varphi_{h}(x))
$$
Therefore, ${} \varphi_{h} {}$ is bijective and an isomorphism, so therefore an automorphism, so ${} \varphi_{h} \in \aut(G) {}$
c)
First, note that $\varphi(xy)=\varphi_{xy} {}$, and that ${} \varphi_{xy}(g)=xygy^{-1}x=(\varphi_{x}\circ \varphi_{y})(g) {}$, so ${} \varphi(xy)=\varphi(x)\varphi(y) {}$, and ${} \varphi {}$ is a homomorphism. 

Now let ${} g \in \ker \varphi {}$. Now ${} \varphi_{g}=\mathrm{id} {}$, and ${} gxg^{-1}=x {}$ for all ${} x \in G {}$. Therefore, ${} gx=xg {}$ for all ${} x \in G {}$, so ${} g \in Z(G) {}$. 

Finally, let ${} \varphi_{g} \in  \im \varphi {}$, and ${} \alpha \in \aut(G) {}$. Now note that
$$
\begin{align}
 (\alpha \circ  \varphi_{g} \circ  \alpha ^{-1})(x)  & =\alpha(g\alpha ^{-1}(x)g^{-1}) \\
  & =\alpha(g)x\alpha (g^{-1}) \\
 & =\varphi_{\alpha(g)}(x)
 \end{align}
$$
and so ${} \alpha \circ \varphi_{g}\circ  \alpha ^{-1} \in \im \varphi {}$, and that ${} \im \varphi \trianglelefteq \aut(G) {}$
d)
Since ${} \mathbb{Z} /n\mathbb{Z} = \langle 1 \rangle  {}$, then automorphisms are determined entirely by their value at 1. In particular, if ${} \alpha \in  \aut(G) {}$, then if ${} \alpha(1)=k {}$, then ${} \alpha(x)=kx {}$, since ${} x=x\cdot 1 {}$. Let ${} \alpha :G\to{}G {}$ defined by ${} \alpha(x)=kx {}$ for some $k {}$. Now if ${} d=\gcd(n,\, k)\neq 1 {}$, then we have 
$$
\alpha(n/d)=\frac{kn}{d}=\frac{k}{d}n=0
$$
and so ${} \alpha {}$ is not injective. However, if ${} d=1 {}$, then ${} \alpha(x)=0 \Rightarrow kx=n\Rightarrow n \mid x {}$, so ${} x=mn=0 {}$, and ${} \ker \alpha=\{ 0 \} {}$, and ${} \alpha {}$ is injective. Since it is an endomorphism of a finite group, then ${} \alpha {}$ is surjective, and ${} \alpha {}$ is an automorphism. 

Now, consider ${} \alpha,\, \beta \in \aut(G) {}$ defined by ${} \alpha(x)=ax {}$ and ${} \beta(x)=bx {}$. Then
$$
\begin{align}
 (\alpha \circ  \beta )  & =abx
 \end{align}
$$
since ${} a,\, b {}$ are coprime to $n {}$, then ${} ab {}$ is coprime to $n {}$, and ${} \gamma(x)=abx {}$ is an automorphism.

Therefore, define ${} \theta:(\mathbb{Z} /n \mathbb{Z})^{\times }\to{}\aut(G) {}$ by ${} \theta(k)=\alpha_{k} {}$, where ${} \alpha_{k}:G\to{}G {}$ is defined by ${} \alpha_{k}(x)=kx {}$. Since every ${} k \in (\mathbb{Z} /n\mathbb{Z})^{\times } {}$ has ${} \gcd(k,\, n)=1 {}$, then this is well defined. As proved above, ${} \theta(ab)=\theta(a)\theta(b) {}$. Furthermore, if ${} \theta(a)=\theta(b) {}$, then ${} ax=bx {}$ for all ${} x \in G {}$, so ${} a=b {}$. Finally, if ${} \alpha \in \aut(G) {}$, then there exists some ${} k=\alpha(1) {}$ such that ${} \alpha(x)=kx {}$. Therefore, ${} \theta(k)=\alpha {}$, so ${} \theta {}$ is bijective and is an isomorphism.
5. 
a)
Let ${} \theta:\mathcal{A}\to{}\mathcal{B} {}$ where ${} \mathcal{B}=\{ \conj{A} \subseteq \conj{G} \mid \conj{A} \leq  \conj{G} \} {}$ defined by ${} \theta(H)=\conj{H} {}$. First, suppose that ${} H,\, K\in \mathcal{A} {}$ such that ${} \theta(H)=\theta(K) {}$. Therefore, ${} H /N = K / N {}$. Therefore, for each element ${} \conj{h} \in \conj{H} {}$, ${} \conj{h} \in \conj{K} {}$. Therefore, since ${} H=\bigcup \conj{H} {}$, then ${} H \subseteq K=\bigcup \conj{K} {}$. Likewise for ${} \conj{K} {}$, so ${} H=K {}$, and ${} \theta {}$ is surjective.

Now if ${} \conj{H} \in \mathcal{B} {}$, then let ${} H=\bigcup \conj{H} {}$. Note that, since ${} N \in  \conj{H} {}$, then ${} N \subseteq H {}$. Furthermore, if ${} x,\, y \in H {}$, then ${} \conj{xy^{-1}} \in \conj{H} {}$, so ${} xy^{-1} \in H {}$, and ${} H\leq G {}$, so ${} H \in \mathcal{A} {}$. Finally, given some $\conj{x} \in \conj{H} {}$, and some ${} x \in \conj{x} {}$, then ${} xN=\conj{x} {}$ by definition, and so ${} H/N=\conj{H} {}$. Therefore, ${} \theta(H)=\conj{H} {}$, and ${} \theta {}$ is bijective. 
b)
Let $xH {}$ be a coset of ${} G {}$. Now consider ${} \theta {}$ mapping from the cosets of $H {}$ to the cosets of ${} \conj{H} {}$ by ${} xH \mapsto \conj{x} \conj{H} {}$. First, suppose that ${} xH=yH {}$, so ${} xy^{-1} \in H {}$. Then ${} \conj{x}\conj{y}^{-1}=xy^{-1}N \in \conj{H} {}$. Therefore, ${} \conj{x}\conj{H}=\conj{y}\conj{H} {}$, and ${} \theta {}$ is well defined. Now let ${} \theta(xH)=\theta(yH) {}$. Then by above, ${} xH=yH {}$. Finally, given ${} \conj{x}\conj{H} {}$, let ${} x \in \conj{x} {}$, and ${} \theta(xH)=xN\conj{H}=\conj{x}\conj{H} {}$, and so ${} \theta {}$ is surjective. Therefore, ${} \theta {}$ is a bijection between the cosets, and ${} [G:H]=[\conj{G}:\conj{H}] {}$. 

Just for kicks, let ${} x,\, y \in G {}$. Then ${} \theta(xyH)=\conj{x}\conj{y} \conj{H}=\conj{x} \conj{H} \conj{y}\conj{H}=\theta(xH)\theta(yH) {}$. Therefore, ${} \theta {}$ is a homomorphism if $H {}$ is normal in $G {}$
c)
Let ${} H \in \mathcal{A} {}$. First, suppose that ${} H\trianglelefteq G {}$. Then, given ${} \conj{g} \in \conj{G} {}$, we have that
$$
\begin{align}
\conj{g}\conj{H}\conj{g}^{-1} & =\{ gxg^{-1}N \mid x \in H \} \\
 & =\{ yN \mid y \in H \} \\
 & =\conj{H}
\end{align}
$$
and so ${} \conj{H} \trianglelefteq \conj{G} {}$. 

Conversely, suppose that ${} \conj{H} \trianglelefteq \conj{G} {}$. Then, given ${} g \in G {}$, we have that ${} gxg^{-1}N \in \conj{H} {}$, and so there exists some ${} h \in H {}$ with ${} hN=gxg^{-1}N {}$, so ${} hgxg^{-1} \in N \subseteq H {}$. Therefore, ${} hgxg^{-1}=n {}$ for some ${} n \in N {}$, and ${} gxg^{-1}=h^{-1}n \in H {}$, and ${} gHg^{-1}=H {}$, so ${} H \trianglelefteq G {}$.
d)
(already proved in 5. b)

6. 
a)
First, let ${} g \in G {}$. Then if ${} x=aba^{-1}b^{-1} \in [G,\, G] {}$, then
$$
\begin{align}
 gxg^{-1} & =gaba^{-1}b^{-1}g^{-1} \\
 & =(gag^{-1})(gbg^{-1})(gb^{-1}g^{-1})(ga^{-1} g^{-1}) \in [G,\, G]
 \end{align}
$$
Therefore, ${} [G,\, G]\trianglelefteq G {}$. Let ${} N\trianglelefteq G {}$ such that ${} G /N {}$ is abelian. Then ${} xyN=yxN {}$, so ${} xyx^{-1}y^{-1} \in N {}$, and ${} [G, G]\leq  N {}$.
b)
Note the following:
If ${} A=\begin{pmatrix}1 & \frac{1}{2} \\ 0 & 1 \end{pmatrix}  {}$ and ${} B=\begin{pmatrix}1 & -\frac{1}{2} \\ 0 & -1 \end{pmatrix}  {}$, then ${} ABA^{-1}B^{-1}=\begin{pmatrix}1 & 1 \\ 0 & 1 \end{pmatrix} {}$.
If ${} A=\begin{pmatrix}1 & 0\\ \frac{1}{2}  & 1 \end{pmatrix}  {}$ and ${} B=\begin{pmatrix}1 & 0 \\ -\frac{1}{2} & -1 \end{pmatrix}  {}$, then ${} ABA^{-1}B^{-1}=\begin{pmatrix}1 & 0 \\ 1 & 1 \end{pmatrix} {}$.
If ${} A=\begin{pmatrix}0 & r \\ 1 & 0 \end{pmatrix}  {}$ and ${} B=\begin{pmatrix}0 & 1 \\ 1 & 0 \end{pmatrix}  {}$, then ${} ABA^{-1}B^{-1}=\begin{pmatrix}r & 0 \\ 0 & r^{-1} \end{pmatrix}  {}$.
Therefore, ${} \mathrm{SL}_{2}(\mathbb{R}) \subseteq [\mathrm{GL}_{2}(\mathbb{R}),\, \mathrm{GL}_{2}(\mathbb{R})] {}$. Now note that if ${} A=XYX^{-1}Y^{-1} \in [G,\, G] {}$, we have
$$
\begin{align}
 \det(A)=\det  (XYX^{-1}Y^{-1}) & =\det  (X)\det  (Y)\det  (X^{-1})\det  (Y^{-1})   \\
 & =1
 \end{align}  
$$
and so ${} [G, G] \subseteq \mathrm{SL}_{2}(\mathbb{R}) {}$.




Now let ${} G=\mathrm{PGL}_{2}(\mathbb{R})=\mathrm{GL}_{2}(\mathbb{R}) / Z {}$ where ${} Z=\mathbb{R} I=\{ xI \mid x \in \mathbb{R}^{\times } \} {}$, and $I {}$ is the ${} 2\times 2 {}$ identity matrix. Given ${} X, Y \in \mathrm{PGL}_{2}(\mathbb{R}) {}$, then ${} XYX^{-1}Y^{-1}=xyx^{-1}y^{-1} Z {}$ for some ${} x,\, y \in \mathrm{GL}_{2}(\mathbb{R}) {}$. Therefore, since ${} s=xyx^{-1}y^{-1} \in \mathrm{SL}_{2}(\mathbb{R}) {}$, then ${} sZ=XYX^{-1}Y^{-1} {}$. Since the only elements in $Z {}$ with determinant $1 {}$ are
$$
\begin{pmatrix}1 & 0 \\ 0 & 1 \end{pmatrix} ,\, \begin{pmatrix}-1 & 0 \\ 0 & -1 \end{pmatrix}  \in Z
$$
Set ${} Q=\{ I,\, -I \}\subset Z {}$. Then if we take ${} \mathrm{PSL}_{2}(\mathbb{R})=\mathrm{SL}_{2}(\mathbb{R}) / Z(\mathrm{SL}_{2}(\mathbb{R}))=\mathrm{SL}_{2}(\mathbb{R}) / {}Q {}$, then the map ${} \theta:[G,\,  G]\to{}\mathrm{PSL}_{2}(\mathbb{R}) {}$ defined by ${} \theta(pZ)=pQ {}$, where ${} p \in \mathrm{SL}_{2}(\mathbb{R}) {}$ is well defined.

Now let ${} pZ,\, qZ \in  [G,\, G] {}$ such that ${} \theta(pZ)=\theta(qZ) {}$. Then ${} pQ=qQ {}$, and either ${} p=q {}$ or ${} p=-q {}$. In either case, since ${} -I \in Z {}$, then ${} pZ=qZ {}$, and so ${} \theta {}$ is injective.

Now Let ${} pQ \in \mathrm{PSL}_{2}(\mathbb{R}) {}$. Then ${} p=xyx^{-1}y^{-1} {}$ for some ${} x,\, y \in \mathrm{GL}_{2}(\mathbb{R}) {}$, and setting ${} X=xZ {}$ and ${} Y=yZ {}$, we get ${} P=XYX^{-1}Y^{-1} \in [G,\, G] {}$ with ${} p \in P {}$, and so ${} \theta(pZ)=pQ {}$, and ${} \theta {}$ is bijective and an isomorphism. 

Therefore, ${} [\mathrm{PGL}_{2}(\mathbb{R}),\, \mathrm{PGL}_{2}(\mathbb{R})]\cong \mathrm{PSL}_{2}(\mathbb{R}){} {}$, in particular, since ${} QZ=Z {}$
$$
[\mathrm{PGL}_{2}(\mathbb{R}),\, \mathrm{PGL}_{2}(\mathbb{R})] = \mathrm{PSL}_{2}(\mathbb{R}) Z=\{ pQZ \mid pQ \in \mathrm{PSL}_{2}(\mathbb{R}) \}=\{ pZ \mid pQ \in \mathrm{PSL}_{2}(\mathbb{R}) \}
$$

c)
Note that ${} C=[\mathrm{GL}_{2}(\mathbb{R}),\, \mathrm{GL}_{2}(\mathbb{R})]=\mathrm{SL}_{2}(\mathbb{R}) {}$, but that 
$$
\begin{align}
 D & =[\mathbb{R}^{\times } \times  \mathrm{PGL}_{2}(\mathbb{R}),\, \mathbb{R}^{\times } \times  \mathrm{PGL}_{2}(\mathbb{R})]   \\
 & =\{ (xyx^{-1}y^{-1},\, XYX^{-1}Y^{-1}) \mid x,\, y \in \mathbb{R}^{\times },\, X,\, Y \in \mathrm{PGL}_{2}(\mathbb{R}) \} \\
 & =\{ xyx^{-1}y^{-1} \mid x,\, y \in \mathbb{R}^{\times } \}\times \{ XYX^{-1}Y^{-1} \mid  \mathrm{PGL}_{2}(\mathbb{R}) \} \\
 & \cong \{ 1 \} \times  \mathrm{PSL}_{2}(\mathbb{R})\cong \mathrm{PSL}_{2}(\mathbb{R})
 \end{align}
$$
and that ${} \mathrm{PSL}_{2}(\mathbb{R}) \not\cong \mathrm{SL}_{2}(\mathbb{R})  {}$, and so ${} \mathrm{GL}_{2}(\mathbb{R}) \not\cong \mathbb{R}^{\times } \times  \mathrm{PGL}_{2}(\mathbb{R}) {}$.
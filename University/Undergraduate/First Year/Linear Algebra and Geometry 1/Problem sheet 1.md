---
tags:
  - linear_algebra1
  - homework
pset: 1
date: 2023-09-27
completed: true
---
[[Directory]], [[Linear Algebra and Geometry 1|Subject Directory]]
1.  a)
    1. i)
$$
\begin{align}
 \sum_{k=5}^{9} 4(k-5)&=4\sum_{k=0}^{4}k    \\
 & =4 \sum_{k=1}^{4} k \\
 & =4 \frac{4(4+1)}{2} \\
 & =8\cdot5 \\
 & =40
 \end{align}
$$
2. ii)
$$
\begin{align}
 \sum_{j=0}^{3} \sum_{k=0}^{5}(j-k)  & = \sum_{j=0}^{3}\left( \sum_{k=0}^{5} j - \sum_{k=0}^{5} k \right) \\
 & = \sum_{j=0}^{3} \left( 5j-\frac{5(5+1)}{2} \right) \\
 & =5\sum_{j=0}^{3} j-15 \\
 & =5 \frac{3(3+1)}{2}-15 \\
 & =15
 \end{align} 
$$
3. iii)
$$
\begin{align}
 \sum_{k=1}^{n} \sum_{j=1}^{n} 2j & = \sum_{k=1}^{n} 2\cdot \frac{n(n+1)}{2} \\
 &     =n\cdot n(n+1) \\
 & = n^{2} (n+1)
 \end{align}
$$
1. b) 
$$
\sum_{j=-1}^{12} \sqrt{ 2j+7 }=\sum_{j=5}^{18} \sqrt{ 2j+(-5) }=\sum_{j=1}^{14} \sqrt{ 2j+3 }
$$
1. c)
$$
\begin{align}
 \frac{1}{2}\sum_{k=0}^{n} \sum_{j=0}^{n} (j+k)^{2}  & =\frac{1}{2}\sum_{k=0}^{n} \sum_{j=0}^{n} (j^{2}+2jk+k^{2}) \\
 & =\frac{1}{2} \sum_{k=0}^{n} \left( \sum_{j=0}^{n} j^{2}+2k \sum_{j=0}^{n} j+ k^{2} \sum_{j=0}^{n} 1 \right)  \\
 & =\frac{1}{2} \left( \sum_{j=0}^{n} \sum_{k=0}^{n} j^{2} +2\left( \sum_{j=0}^{n} j  \right)\left( \sum_{k=0}^{n} k \right) +(n+1)\sum_{k=0}^{n} k^{2}\right) \\
 & =\frac{1}{2} \left( (n+1)\sum_{j=0}^{n} j^{2} +(n+1)\sum_{k=0}^{n} k^{2} +2\left( \sum_{j=0}^{n} j \right)\left( \sum_{k=0}^{n} k \right)\right) \\
 & =\frac{1}{2}\left( 2(n+1)\sum_{k=0}^{n} k^{2}+2\left( \sum_{k=0}^{n} k \right)^{2} \right) \\
 & =(n+1) \sum_{k=0}^{k^{2}}k^{2}+\left( \sum_{k=0}^{n} k  \right)^{2} \qquad \text{as required}
\end{align}
$$
2.  a)
    1. i)
$$
\begin{align}
(-3+4i)+(6+7i) & =(-3+6)+(4+7)i \\
 & =3+11i
\end{align}
$$
2. ii)
$$
\begin{align}
(2+5i)(3-2i) & =2(3-2i)+5i(3-2i) \\
 & =6-4i+15i-10i^{2} \\
 & =6+10 +11i \\
 & =16+11i
\end{align}
$$
3. iii)
$$
\begin{align}
\frac{1}{-2+3i} & =\frac{-2-3i}{(-2+3i)(-2-3i)} \\
 & =\frac{ -2-3i }{ 4+9 } \\
 & =-\frac{2+3i}{13} \\
 & =-\frac{2}{13}-\frac{3}{13}i
\end{align}
$$
4. iv)
$$
\begin{align}
 (i+\sqrt{ 5 })^{2}  & =5+2\sqrt{ 5 } i+i^{2} \\
 & =5+2\sqrt{ 5 }i-1 \\
 & =4+2\sqrt{ 5 }i \\
 \end{align}
$$
5. v)
$$
\begin{align}
(1+i)(1+2i)(1+3i) & =(1+2i)(1+3i)+i(1+2i)(1+3i) \\
 & =1+3i+2i+6i^{2}+i+3i^{2}+2i+6i^{2} \\
 & =1+3i+2i+i+2i+6i^{2}+3i^{2}+6i^{2} \\
 & =1+8i-15 \\
 & =-14+8i
\end{align}
$$
6. vi)
$$
\begin{align}
 \left( \frac{1+i}{1-i} \right)^{2}  & = \left( \frac{(1+i)^{2}}{(1-i)(1+i)} \right)^{2} \\
 & =\left( \frac{(1+i)^{2}}{2} \right)^{2} \\
 & =\frac{ (1+i)^{4} }{ 4 } \\
 & =\frac{1+4i+6i^{2}+4i^{3}+i^{4}}{4} \\
 & =\frac{1+4i-6-4i+1}{4} \\
 & =\frac{-4}{4} \\
 & =-1 
 \end{align}
$$
2. b)
    1. i)
$$
\begin{align}
 \left( \frac{1+i}{\sqrt{ 2 }} \right)^{2}  & = \frac{1+2i+i^{2}}{2} \\
 & =\frac{1-1+2i}{2} \\
 & =\frac{2i}{2} \\
 & =i 
 \end{align}
$$
This means that $\frac{1+i}{\sqrt{ 2 }}=\sqrt{ i }=i^{0.5}$. This will come in handy
    2. ii)
$$
z^{3}=(i^{0.5})^{3}=i^{1.5}=\frac{i(1+i)}{\sqrt{ 2 }}=\frac{-1+i}{\sqrt{ 2 }}
$$
3. iii)
$$
z^{4}=(i^{0.5})^{4}=i^{2}=-1
    $$
4. iv)
$$
z^{6}=(i^{0.5})^{6}=i^{3}=-i
$$
5. v)
$$
z^{8}=(i^{0.5})^{8}=i^{4}=1 
$$
6. vi)
$$
z^{100}=(i^{0.5})^{100}=i^{50}=(-1)^{25}=-1
$$
3. 
    1. a) False: take $z=i$, $w=-i$. Now we have $z+w=0\in \mathbb{R}$.
    2. b) False: take $z=1+i$, $w=1-i$. Now we have $zw=1-i^{2}=2 \in \mathbb{R}$
    3. c) True: given that $z=a+bi,\, a,\, b \in \mathbb{R}$, and that $\overline{z}=a-bi$, if $\overline{z}$ is real, then since $a,\, b$ are real, $-b=0$. Therefore, $b=0$, so $z=a+0i=a\in\mathbb{R}$ as required
    4. d) True: given $z=a+bi,\, a,\, b \in \mathbb{R}$, we have $z-\overline{z}=a+bi-a+bi=2bi$. If $2bi$ is real, then $b=0$, so $z=a+0i=a\in\mathbb{R}$
2. 
    1. a) $\left| z+1 \right|=2$ means the set of points that are a distance of $2$ away from $-1$. 
    ![[Problem sheet 1 2023-09-27 14.59.42.excalidraw]]
    2. b) $z=\overline{z}+2i$ is set of all points with imaginary part $1$, as, given $z=a+bi,\, a,\, b \in \mathbb{R}$, 
$$
\frac{ z-\overline{z} }{ 2i }=\frac{ a+bi-a+bi }{ 2i }=\frac{ 2bi }{ 2i }=b=\mathrm{Im}(z)
$$
    So the set of points looks like this:
    ![[Problem sheet 1 2023-09-27 15.27.09.excalidraw]]
3. c)
$$
\begin{align}
z^{2} & =(\overline{z})^{2} \\
\left(  \frac{z}{\overline{z}}  \right)^{2} & =1 \\
\left(  \frac{z^{2}}{|z|^{2}}  \right)^{2} & =1 \\
\left(  \frac{z}{\left| z \right| }  \right)^{4} & =1
\end{align}
$$ 
The expression in the brackets gives a point on the unit circle with the argument of $z$. In order to be raised to a power of 4 and be equal to 1, it must have an argument that is a multiple of $\frac{\pi}{2}$. This means that the set contains every point with an argument that is an integer multiple of $\frac{\pi}{2}$. It also contains $0$, as $0^{2}=0^{2}$. Therefore the set looks like this:
![[Problem sheet 1 2023-09-27 15.40.58.excalidraw]]
 in this diagram I have coloured the set red, so that it can be differentiated against the gridlines
 
5. 
    1. a) 
$$
\begin{align}
 \overline{\left( \frac{z}{w} \right)} & =\overline{z}\cdot \overline{\left( \frac{1}{w} \right)} \\
 & =\overline{z}\cdot\overline{  \left( \frac{\overline{w}}{|w|^{2}} \right)} \\
 & =\overline{z} \cdot \frac{1}{|w|^{2}}\cdot \overline{\overline{w}} \\
 & =\overline{z}\cdot \frac{w}{|w|^{2}} \\
 & =\overline{z} \cdot \frac{w}{w\overline{w}} \\
 & =\overline{z}\cdot \frac{1}{\overline{w}} \\
 & =\frac{\overline{z}}{\overline{w}}
 \end{align}
$$
2. b)
$$
\begin{align}
 \left| \frac{z}{w} \right|  & = \sqrt{\frac{z}{w} \overline{\left( \frac{z}{w} \right)}  }   \\
     & =\sqrt{ \frac{ z\overline{z} }{ w\overline{w} } } \\
 & =\frac{\sqrt{ z\overline{z} }}{\sqrt{ w\overline{w} }} \\
 & =\frac{\left| z \right| }{|w|}
 \end{align}
$$

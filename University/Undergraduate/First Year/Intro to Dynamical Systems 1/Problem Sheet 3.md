---
tags:
  - dynamical_systems1
  - homework
date: 2024-02-02
pset: 3
completed:
---
[[Directory]], [[Intro to Dynamical Systems 1|Subject Directory]]
[[Dynamics HW3.pdf|Problem Sheet]]
1. 
a)
$$
\frac{dx}{dt} =e^{x/t}
$$
b)
$$
\frac{dx}{dt} =\frac{x}{t^{2}}
$$
c)
$$
\frac{dx}{dt} =\frac{x}{t}
$$
2. 
a)
We see that
$$
\begin{align}
t^{2} \frac{dx}{dt}  & =(t+x)^{2}+tx \\
\frac{dx}{dt}  & =\frac{(t+x)^{2}}{t^{2}}+\frac{tx}{t^{2}} \\
 & =\frac{t^{2}+2tx+x^{2}+tx}{t^{2}}  \\
 & =1+3\frac{x}{t}+\frac{x^{2}}{t^{2}} \\
\end{align}
$$
Now we see that if ${} G(y)=y^{2}+3y+1 {}$, then
$$
\begin{align}
\frac{dx}{dt} =G\left( \frac{x}{t} \right)
\end{align}
$$
Now let ${} v=x /t {}$. We now have
$$
\frac{dx}{dt}=G(v)
$$
as required.
b)
We see that
$$
\begin{align}
\frac{dv}{dt} &  =\frac{d}{dt} \frac{x}{t} \\
&= \frac{ \frac{dx}{dt} t-x }{ t^{2} } \\ \\

t^{2} \frac{dv}{dt} +x  & =\frac{dx}{dt} t \\
t \frac{dv}{dt} +\frac{x}{t} & =\frac{dx}{dt}  \\
 \\
\frac{dx}{dt}  & =t \frac{dv}{dt} +v
\end{align}
$$
Now
$$
\begin{align}
t \frac{dv}{dt} +v & =v^{2}+3v+1 \\
 t\frac{dv}{dt} & =(v+1)^{2} \\
\frac{1}{(v+1)^{2}} \frac{dv}{dt}  & =\frac{1}{t} \\
\int \frac{1}{(v+1)^{2}} \ud v  & =\int \frac{1}{t} \ud t \\
 -\frac{1}{v+1} & =\ln |t|+C \\
-(v+1) & =\frac{1}{\ln |t|+C} \\
v & =-\frac{1}{\ln |t|+C}-1
\end{align}
$$
Now solving for $x$ we get that ${} \frac{x}{t}=v {}$, so
$$
\begin{align}
 \frac{x}{t}  & = -\frac{1}{\ln |t|+C}-1 \\
x & =-\frac{t}{\ln |t|+C}-t 
 \end{align}
$$
as required
3. 
a)
If ${} x(1)=0 {}$, then we have 
$$
\begin{align}
-\frac{1}{\ln |1|+C}-1 & =\phantom{-}0 \\
\frac{1}{\ln(1)+C} & =-1 \\
\ln(1)+C & =-1 \\
C&=  -1
\end{align}
$$
b)
Note that, around ${} t_{0}=1 {}$, ${} f(x,\, t)=\frac{ (t+x)^{2}+tx }{ t^{2} } {}$ is continuous for all ${} x\in \mathbb{R} {}$ and for all ${} t \in (0,\, \infty) {}$, and ${} \frac{ \partial f }{ \partial x } =\frac{2x}{t^{2}}+\frac{3}{t} {}$ is continuous for all ${} x \in \mathbb{R} {}$, and for all ${} t \in (0,\, \infty) {}$. Therefore, by Picard's theorem, there exists an open interval ${} (1-\delta,\, 1+\delta) {}$ on which there exists a unique solution. Now note the particular solution is 
$$
x(t)=-\frac{t}{\ln |t|-1}-t
$$
which is not defined for ${} t=\pm e {}$. Therefore, we hate that at most, ${} \delta=e-1 {}$, and the interval on which it is defined is
$$
(e-2,\, e)
$$
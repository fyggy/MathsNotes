---
tags:
  - homework
  - calculus1
date: 2023-10-17
pset: 3
---
[[Directory]], [[Calculus 1|Subject Directory]]
15. a) ${} c=\sqrt{1+1}=\sqrt{2} {}$${} \sin\alpha=\frac{1}{\sqrt{2}} {}$, ${} \cos\alpha=\frac{1}{\sqrt{2}} {}$. Therefore, we have ${} \alpha=\frac{\pi}{4} {}$, and ${} c=\sqrt{2} {}$. ${} \sin\theta+\cos\theta=\sqrt{2}\sin\left( \theta+\frac{\pi}{4} \right) {}$
b) ${} c=\sqrt{3+1}=2$, so ${} \cos\alpha=\frac{\sqrt{3}}{2} {}$, and $\sin\alpha=-\frac{1}{2}$. Therefore, ${} \alpha=-\frac{\pi}{6} {}$, and ${} \sqrt{3}\sin\theta-\cos\theta=2\sin\left( \theta-\frac{\pi}{6} \right) {}$
c)${} c=\sqrt{1+\tan ^{2}\beta}=\sec\beta {}$, so ${} \cos\alpha=\cos\beta {}$ and ${} \sin\alpha=-\sin\beta {}$. Therefore, ${} \alpha=-\beta {}$, and ${} \sin\theta-\tan\beta \cos\theta=\sec\beta \sin(\theta-\beta)$

16. 
$$
\begin{align}
\arcsinh(\sinh(x)) & =\ln\left(\sinh(x)+\sqrt{\sinh ^{2}(x)+1}\right) \\
 & = \ln \left( \sinh(x)+\sqrt{\cosh ^{2}(x)} \right) \\
 & =\ln(\sinh x+\cosh x) \\
 & =\ln\left( \frac{e^{x}-e^{-x}}{2}+\frac{e^{x}+e^{-x}}{2} \right) \\
 & =\ln(e^{x}) \\
 & =x
\end{align}
$$
and 
$$
\begin{align}
\sinh(\arcsinh(x)) & =\frac{ e^{\ln\left( x+\sqrt{x^{2}+1} \right)}-e^{-\ln\left( x+\sqrt{x^{2}+1} \right)} }{ 2 } \\
 & =\frac{x+\sqrt{x^{2}+1}-\frac{1}{x+\sqrt{x^{2}+1}}}{2} \\
 & =\frac{\frac{x^{2}+x^{2}+1+2x\sqrt{x^{2}+1}}{x+\sqrt{x^{2}+1}}-\frac{1}{x+\sqrt{x^{2}+1}}}{2} \\
 & =\frac{2x\frac{x+\sqrt{x^{2}+1}}{x+\sqrt{x^{2}+1}}}{2} \\
 & =x
\end{align}
$$

17. $\sinh x=\frac{e^{x}-e^{-x}}{2}$ and ${} \cosh x=\frac{e^{x}+e^{-x}}{2}$. So
$$
\begin{align}
\tanh x & =\frac{\sinh x}{\cosh x} \\
 & = \frac{e^{x}-e^{-x}}{e^{x}+e^{-x}} \\
 & =\frac{e^{2x}-1}{e^{2x}+1}
\end{align}
$$
18. Note that ${} \cos(x/2)=\sqrt{ \frac{1}{2}(\cos x+1) } {}$
$$
\begin{align}
\cos \left( \frac{\pi}{12} \right) & = \sqrt{\frac{1}{2}\left( \cos \frac{\pi}{6}+1 \right)} \\
 & =\sqrt{\frac{1}{2}\left( \frac{\sqrt{3}}{2}+1 \right)} \\
 & =\sqrt{\frac{1}{4}\left( \sqrt{3}+2 \right)} \\
 & =\frac{1}{2}\sqrt{\sqrt{3}+2} \\
\end{align}
$$
As required

19.  Let ${} t=\tanh(x/2)$. First note that
$$
\begin{align}
\cosh ^{2} \left( \frac{x}{2} \right) & =\frac{1}{\sech ^{2} \left( \frac{x}{2} \right)} \\
 & =\frac{1}{1-\tanh ^{2} \left( \frac{x}{2} \right)} \\
 & =\frac{1}{1-t^{2}} \tag{1}
\end{align}
$$
Now for ${} \sinh {}$ we have
$$
\begin{align}
\sinh x & =2\sinh\left( \frac{x}{2} \right)\cosh\left( \frac{x}{2} \right) \\
 & =2\left( \frac{\sinh \left( \frac{x}{2} \right)}{\cosh \left( \frac{x}{2} \right)} \right) \cosh ^{2}\left( \frac{x}{2} \right) \\
 & =2\tanh \left( \frac{x}{2} \right) \cosh ^{2}\left( \frac{x}{2} \right) \\
 & =\frac{2t}{1-t^{2}}
\end{align}
$$
By ${} (1) {}$

For ${} \cosh {}$, we have
$$
\begin{align}
\cosh x & =2\cosh ^{2}\left( \frac{x}{2} \right)+1 \\
 & =\frac{2}{1-t^{2}}-1 \\
 & =\frac{2-1+t^{2}}{1-t^{2}} \\
 & =\frac{ 1+t^{2} }{ 1-t^{2} } \\
\end{align}
$$
Finally, we have
$$
\begin{align}
\tanh x & =\frac{ \sinh x }{ \cosh x } \\
 & =\frac{\frac{2t}{1-t^{2}}}{\frac{1+t^{2}}{1-t^{2}}} \\
 & =\frac{2t}{1+t^{2}}
\end{align}
$$

20. 
a) ${} \cot\theta+\tan\theta=1 {}$. Then we have
$$
\begin{align}
\frac{1}{\tan\theta}+\tan\theta & =1 \\
 \frac{ 1+\tan ^{2}\theta }{ \tan\theta } & =1 \\
\frac{\sec ^{2}\theta}{\tan\theta} & =1 \\
\frac{\cos\theta}{\cos ^{2}\theta \sin\theta } & =1 \\
\frac{2}{\sin 2\theta} & =1 \\
\sin 2\theta & =2
\end{align}
$$
Which is impossible

b) ${} \cot\theta+\tan\theta=2 {}$. Then we have
$$
\begin{align}
 2\sin 2\theta & =2  \\
 \sin2\theta  & =1
 \end{align}
$$
Therefore, ${} 2\theta=\frac{\pi}{2}+2k\pi$, so 
$$
\theta=\frac{\pi}{4}+k\pi \qquad\forall k \in  \mathbb{Z}
$$

c) we have
$$
\begin{align}
 4\sin 2\theta  & = 2   \\
 \sin 2\theta & =\frac{1}{2} \\
 \end{align}
$$
Therefore, ${} 2\theta=\frac{\pi}{6}+2\pi k {}$ or ${} 2\theta=\frac{5\pi}{6}+2\pi k {}$, so we have
$$
\theta=\frac{\pi}{4}\pm \frac{\pi}{6} +k\pi \qquad\forall k \in  \mathbb{Z}
$$
21. 
a)
$$
\begin{align}
 \sin(\alpha-\beta)+\sin(\alpha+\beta)  & =\phantom{+{}}\sin\alpha \cos\beta-\cos\alpha \sin\beta \\
 & \phantom{={}}+\sin\alpha \cos\beta+\cos\alpha \sin\beta \\
 & = 2\sin\alpha \cos\beta
 \end{align}
$$
b)
$$
\begin{align}
\cos(\alpha-\beta)-\cos(\alpha+\beta) & =\phantom{-}\cos\alpha \cos\beta+\sin\alpha \sin\beta \\
 & \phantom{={}}-\cos\alpha \cos\beta+\sin\alpha \sin\beta \\
 & =2\sin\alpha \sin\beta
\end{align}
$$
22. 
a) ${} \arcsin(\sin(5\pi/6))=\arcsin(1 /2)=\pi /6 {}$
b) ${} \arcsin(\sin(7\pi/6))=\arcsin(\sin(-\pi /6))=\arcsin(-1 /2)=-\pi/6 {}$
c) ${} \arccos(\cos(7\pi /6))=\arccos(-\cos(\pi/6))=\arccos\left( \cos(5\pi/6)\right)=5\pi / 6 {}$
d) ${} \arccos(\cos(11\pi /6))=\arccos(\cos(-5\pi /6))=\arccos(\cos(\pi /6))=\pi /6 {}$

23. 
i) ${} (f\circ g)(x)=(x+2)^{3}=x^{3}+6x^{2}+12x+8 {}$ 
ii) ${} (g\circ f)(x)=x^{3}+2$
iii) 
$$
\begin{align}
(f\circ g)(x) & =(g \circ f)(x) \\
x^{3}+6x^{2}+12x+8 & =x^{3}+2 \\
6x^{2}+12x+6 & =0 \\
x^{2}+2x+1 & =0 \\
x & =-1 \\
\end{align}
$$
iv) No. Note that ${} (f\circ g)(0)=8\neq 2=(g\circ f)(0) {}$
v) If we just consider the functions above we have a counterexample. Note the answer to iv). This is sufficient to disprove the statement.

24. 
i) The image of ${} y(\phi)$ is $\mathbb{R} {}$. As it gets closer to the poles, it stretches exponentially more and more.
ii) First we obtain a half angle formula for ${} \tan {}$
$$
\begin{align}
 \tan\left( \frac{\theta}{2} \right) & =\frac{\sin\left( \frac{\theta}{2} \right)}{\cos\left( \frac{\theta}{2} \right)} \\
 & = \frac{\sqrt{\frac{\cos\theta-1}{2}}}{\sqrt{\frac{\cos\theta+1}{2}}} \\
 & =\sqrt{\frac{1-\cos\theta}{1+\cos\theta}}  \tag{1}\\
 & =\frac{1- \cos\theta}{ \sqrt{\cos ^{2}\theta-1} } \\
 & =\frac{1-\cos\theta}{\sqrt{\sin ^{2}\theta}} \\
 & =\frac{1- \cos\theta}{ \sin\theta }
 \end{align}
$$

So now we have
$$
\begin{align}
 \tan\left( \frac{\phi}{2}+\frac{\pi}{4} \right)  & =\frac{ 1-\cos\left( \phi+\frac{\pi}{2} \right) }{ \sin\left( \phi+\frac{\pi}{2} \right) }  \\
 & =\frac{ 1+\sin\phi }{  \cos\phi}
 \end{align}
$$
as required. Note from entry ${} (1)$, then we have
$$
\begin{align}
\tan\left( \frac{\theta}{2} \right)=\sqrt{\frac{1-\cos\theta}{1+\cos\theta}}
\end{align}
$$
So we can show that
$$
\begin{align}
\tan\left( \frac{\phi}{2}+\frac{\pi}{4} \right) & =\sqrt{\frac{1-\cos(\phi+\pi /2)}{1+\cos(\phi+\pi /2)}} \\
 & =\sqrt{\frac{1+\sin\phi}{1-\sin\phi}}
\end{align}
$$
We can now show that
$$
\begin{align}
 y(\phi) & =\ln\left( \tan\left( \frac{\phi}{2}+\frac{\pi}{4} \right) \right)   \\
 & =\ln\left( \sqrt{\frac{ 1+\sin\phi }{ 1-\sin\phi }} \right) \\
 & =\frac{1}{2}\ln\left( \frac{1+\sin\phi}{1-\sin\phi} \right)
 \end{align}
$$
As required

iii)
$$
\begin{align}
 \sinh(y(\phi))  & =\frac{ e^{1 /2 \ln\left( \frac{1+\sin\phi}{1-\sin\phi} \right)} -e^{-1 /2 \ln\left( \frac{1+\sin\phi}{1-\sin\phi} \right)} }{ 2 } \\
 & =\frac{1}{2}\left(  \sqrt{\frac{ 1+\sin\phi }{ 1-\sin\phi }}-\sqrt{\frac{1-\sin\phi}{1+\sin\phi}} \right) \\
 & =\frac{1}{2}\left( \frac{1+\sin\phi-1+\sin\phi}{\sqrt{1-\sin ^{2}\phi}} \right) \\
 & =\frac{1}{2}\left( \frac{2\sin\phi}{\cos\phi} \right) \\
 & =\tan(\phi) \\
 \\
 y(\phi) & =\arcsinh(\tan(\phi))
 \end{align}
$$
Therefore
$$
\begin{align}
\arcsinh(\tan(\phi)) & =y(\phi) \\
\phi & =\arctan(\sinh(y(\phi))) \\
 & =\operatorname{gd}(y(\phi))
\end{align}
$$
As requried.
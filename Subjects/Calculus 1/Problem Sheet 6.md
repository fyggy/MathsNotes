# Tutors example
Let ${} f(x)=\sqrt{1+\sin x} {}$, with $x \in  [-\pi,\, \pi]$. We calculate
$$
\begin{align}
 \frac{df}{dx}  & =\frac{d}{dx} g(h(x))   \\
 & =g'(h(x))h'(x) \\
 & =\frac{\cos x}{2\sqrt{1+\sin x}}
 \end{align}
$$
Note that when ${} x=-\pi /2 {}$, this function does not exist. So we want to know if the derivative exists at all at $-\pi / 2$.
so we have
$$
\lim_{h\tto 0^{+}} \frac{f(x_{0}+h)-f(x_{0})}{h}\qquad \text{ where }x_{0}=-\frac{\pi}{2}
$$
So we have
$$
\begin{align}
 \lim_{h\tto 0^{+}} \frac{\sqrt{1+\sin\left( -\frac{\pi}{2}+h \right)}-\sqrt{1+\sin\left( -\frac{\pi}{2} \right)}}{h}  & =\lim_{h\tto 0^{+}} \frac{\sqrt{1+\sin\left( h-\frac{\pi}{2} \right)}}{h}  \\
	 & =\lim_{h\tto 0^{+}} \frac{\sqrt{1+\sin(h)\cos\left( -\frac{\pi}{2} \right)+\cos(h)\sin\left( -\frac{\pi}{2} \right)}}{h} \\
 & =\lim_{h\tto 0^{+}} \frac{\sqrt{1-\cos(h)}}{h} \\
 & =\lim_{h\tto 0^{+}} \frac{\sqrt{1-\left( 1-\frac{h^{2}}{2}+\frac{h^{4}}{24}-\frac{h^{6}}{6!}+\dots \right)}}{h}
 \end{align}
$$
This is a *prime* time to use big O notation.
so we have
$$
\lim_{h\tto 0^{+}} \frac{\sqrt{1-\left( 1-\frac{h^{2}}{2}+O(h^{4}) \right)}}{h}
$$
Since ${} h>0 {}$, then ${} h=\sqrt{h^{2}} {}$, then
$$
\begin{align}
 \lim_{h\tto 0^{+}}\frac{ \sqrt{\frac{h^{2}}{2}+O(h^{4})}  }{ \sqrt{h^{2}} }  & =\lim_{h\tto 0^{+}} \sqrt{\frac{1}{2}+O(h^{2})}=\frac{1}{\sqrt{2}} 
 \end{align}
$$
We see that if ${} \lim_{h\tto 0^{-}} {}$, then the only difference is that ${} -h=\sqrt{h^{2}} {}$, so we have
$$
\lim_{h\tto 0^{-}} \frac{f(x_{0}+h)+f(x_{0})}{h}=-\frac{1}{\sqrt{2}}
$$
So the limit does not exist, mean girls style

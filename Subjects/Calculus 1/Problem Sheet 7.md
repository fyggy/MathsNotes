---
tags:
  - calculus1
  - homework
date: 2023-11-21
---
[[Directory]], [[Calculus 1|Subject Directory]]
[[Calculus 1 HW7.pdf|Problem Sheet]]
# Tutors example:
$$
y^{2}=x^{3}+x^{2}
$$
then
$$
\begin{align}
 2y \frac{dy}{dx}  & =3x^{2}+2x   \\
\frac{dy}{dx}  & =\frac{3x^2+2x}{2y}
 \end{align}
$$
62. 
If we can solve ${} \left( \frac{ \partial  }{ \partial x } +\frac{ \partial  }{ \partial y }  \right)^{n}(f(x)g(y)) {}$ and then substitute ${} y=x {}$. then we will get the same answer, as 
$$
\left( \frac{ \partial  }{ \partial x } +\frac{ \partial  }{ \partial y }  \right)(f(x)g(y))=f'(x)g(y)+f(x)g'(y)
$$
Now we use the binomial theorem:
$$
\left( \frac{ \partial y }{ \partial x } +\frac{ \partial  }{ \partial y }  \right)^{n}=\sum_{k=0}^{n} \binom{n}{k}\frac{ \partial^{k}  }{ \partial x^{k} } \frac{ \partial^{k} }{ \partial y^{k} } 
$$
Applying this to $fg {}$, we get
$$
\left( \frac{ \partial y }{ \partial x } +\frac{ \partial  }{ \partial y }  \right)^{n}(fg)=\sum_{k=0}^{n} \binom{n}{k}\frac{ \partial^{k}  }{ \partial x^{k} } \frac{ \partial^{k} }{ \partial y^{k} } (fg)=\sum_{k=0}^{n} \binom{n}{k}\frac{ \partial^{k}f  }{ \partial x^{k} } \frac{ \partial^{k}g }{ \partial y^{k} }
$$
Finally, substituting $y$ for $x$ we get
$$
	\frac{d^{n}}{dx^{n}}(fg)=\sum_{k=0}^{n} \binom{n}{k}\frac{ d^{k}f  }{ d x^{k} } \frac{ d^{k}g }{ d x^{k} }
$$
as required

---
tags:
  - homework
  - classdyn1
date: 2024-09-23
pset: 1
completed: false
---
[[Directory]], [[University/Undergraduate/Second Year/Classical Dynamics 1/Classical Dynamics 1|Subject Directory]]
[[University/Undergraduate/Second Year/Classical Dynamics 1/Homework/Homework 1|🞀🞀]] [[|◀]] [[University/Undergraduate/Second Year/Classical Dynamics 1/Homework/Homework 2|▶]] [[University/Undergraduate/Second Year/Classical Dynamics 1/Homework/Homework 11|🞂🞂]]

[[University/Undergraduate/Second Year/Classical Dynamics 1/Homework/Worksheets/classic_dyn_1.pdf|Worksheet]]
1. 
a)
Recall that the area of a triangle can be calculated as ${} A=\frac{1}{2}ab \sin C {}$. 
![[Pasted image 20241001160342.png]]
Then, since ${} B=A {}$, then the area of this parallelogram is ${} A+B=2A=\lVert \mathbf{r}_{2}  \rVert \lVert \mathbf{r}_{3} \rVert \sin\varphi=\lVert \mathbf{r}_{2} \times \mathbf{r}_{3} \rVert  {}$
b)
${}  \vec{v}=\mathbf{r}_{2} \times  \mathbf{r}_{3}  {}$
c)
We have ${} \mathbf{r}_{1} \cdot \vec{v}=\lVert \mathbf{r}_{1} \rVert \lVert \vec{v} \rVert \cos\theta {}$
![[Pasted image 20241001155635.png]]
d)
The height of the parallelepiped is ${} \lVert \mathbf{r}_{1} \rVert \sin\left( \frac{\pi}{2} - \theta \right)=\lVert \mathbf{r}_{1} \rVert \cos\theta {}$, and so the volume of the parallelepiped is
$$
V=\lVert \mathbf{r}_{1} \rVert \lVert \mathbf{r}_{2} \rVert \lVert \mathbf{r}_{3} \rVert \sin \varphi \cos\theta=\mathbf{r}_{1} \cdot (\mathbf{r}_{2} \times  \mathbf{r}_{3})
$$
e)
We have
$$
\begin{align}
\mathbf{r}_{1} \cdot (\mathbf{r}_{2} \times  \mathbf{r}_{3})=\mathbf{r}_{2} \cdot (\mathbf{r}_{3} \times  \mathbf{r}_{1})=\mathbf{r}_{3} \cdot (\mathbf{r}_{1} \times  \mathbf{r}_{2})
\end{align}
$$
2. 
a) We have
$$
\begin{align}
 \frac{ \partial F }{ \partial x }  & =2x+2y   \\
  \frac{ \partial F }{ \partial y }  & =2x+2y \\
 \frac{ \partial F }{ \partial t }  & =-3
 \end{align}
$$
b)
We have
$$
\begin{align}
f(t) & =F(x(t),\, y(t),\, t) \\
  & =( \sin 3t )^{2}+2\sin(3t)(t-\sin 3t)+(t-\sin 3t)^{2}-3t \\
  & =\sin ^{2}3t+2t\sin 3t-2\sin ^{2}3t+t^{2}-2t\sin 3t+\sin 3t^{2}-3t \\
  & =t^{2}-3t
\end{align}
$$
and so
$$
\frac{df}{dt}=2t-3
$$
c)
We have
$$
\begin{align}
 \frac{ \partial F }{ \partial x } \frac{dx}{dt}  +\frac{ \partial F }{ \partial y } \frac{dy}{dt} +\frac{ \partial F }{ \partial t }  & =(2x+2y)(3\cos 3t+1-3\cos 3t)-3 \\
  & =(2\sin 3t+2t-2\sin 3t)(1)-3 \\
  & =2t-3 =\frac{df}{dt} 
 \end{align}
$$
3. 
We have that
$$
\begin{align}
 \sqrt{x^{2}+y^{2}+z^{2}}  & =\sqrt{r^{2}(\cos ^{2} \theta +\sin ^{2} \theta ( \cos ^{2} \phi +\sin ^{2} \phi))}  \\
  & =r\sqrt{\cos ^{2}\theta+\sin ^{2}\theta} \\
  & =r
 \end{align}
$$
Now
$$
\begin{align}
\frac{y}{x} & =\frac{r \sin \theta \sin \phi}{r \sin \theta \cos \phi}  \\
  & =\tan \phi
\end{align}
$$
and so ${} \phi=\arctan (y /x) {}$. Finally, 
$$
\begin{align}
 \left(  \frac{x}{z}  \right)^{2}+\left(  \frac{y}{z}  \right)^{2}  & =\left(  \frac{r \sin \theta \cos \phi}{r \cos \theta}    \right)^{2}+\left(  \frac{r \sin \theta \sin \phi}{r \cos \theta}    \right)^{2} \\
  & =\tan ^{2}\theta \cos ^{2} \phi+\tan ^{2}\theta \sin ^{2}\phi \\
  & =\tan ^{2}\theta
 \end{align}
$$
and so 
$$
\theta=\arctan \left( \sqrt{\left(  \frac{x}{z}  \right)^{2}+\left(  \frac{y}{z}  \right)^{2}} \right) 
$$
Therefore, 
$$
\begin{align}
r & =\sqrt{x^{2}+y^{2}+z^{2}} \\
 \theta & =\arctan \left( \sqrt{\left( \frac{x}{z} \right)^{2}+\left( \frac{y}{z} \right)^{2}} \right) \\
 \phi & =\arctan \left( \frac{y}{x} \right)
\end{align}
$$
4. 
We have
$$
\begin{align}
 \nabla  & =\begin{pmatrix} \frac{ \partial  }{ \partial x }  \\ \frac{ \partial  }{ \partial y }  \\ \frac{ \partial  }{ \partial z }  \end{pmatrix} \\
 
  & = \begin{pmatrix} \frac{ \partial  }{ \partial r } \frac{ \partial r }{ \partial x } +\frac{ \partial  }{ \partial \theta } \frac{ \partial \theta }{ \partial x } +\frac{ \partial  }{ \partial \phi } \frac{ \partial \phi }{ \partial x }  \\ \frac{ \partial  }{ \partial r } \frac{ \partial r }{ \partial y } +\frac{ \partial  }{ \partial \theta } \frac{ \partial \theta }{ \partial y } +\frac{ \partial  }{ \partial \phi } \frac{ \partial \phi }{ \partial y }  \\ \frac{ \partial  }{ \partial r } \frac{ \partial r }{ \partial z } +\frac{ \partial  }{ \partial \theta } \frac{ \partial \theta }{ \partial z } +\frac{ \partial  }{ \partial \phi } \frac{ \partial \phi }{ \partial z }  \end{pmatrix}  \\
  & =\begin{pmatrix} 2x /2r \frac{ \partial  }{ \partial r }  +2x / z^{2} \cdot 1 /2\sqrt{(x /z)^{2}+(y /z)^{2}} \cdot  \left( \frac{1}{1+( x /z )^{2}+(y /z)^{2}} \right) \frac{ \partial  }{ \partial \theta } -\frac{y}{x^{2}}\cdot \frac{1}{1+( y /x )^{2}} \frac{ \partial  }{ \partial \phi } \\ 2y /2r\frac{ \partial  }{ \partial r } +2y / z^{2} \cdot 1 /2\sqrt{(x /z)^{2}+(y /z)^{2}} \cdot  \left( \frac{1}{1+( x /z )^{2}+(y /z)^{2}} \right) \frac{ \partial  }{ \partial \theta } +\frac{1}{x}\cdot \frac{1}{1+ ( y/x )^{2}}\frac{ \partial  }{ \partial \phi } \\ 2z /2r \frac{ \partial  }{ \partial r } - \frac{1}{z^{2} \sqrt{x^{2}+y^{2}}}\cdot\left( \frac{1}{1+( x /z )^{2}+(y /z)^{2}} \right)\frac{ \partial  }{ \partial \theta } +0 \cdot \frac{ \partial  }{ \partial \phi }   \end{pmatrix}  \\
  & =\begin{pmatrix} \sin \theta \cos  \phi \frac{ \partial  }{ \partial r } + \\  \\  \end{pmatrix} 
 \end{align}
$$


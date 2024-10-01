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



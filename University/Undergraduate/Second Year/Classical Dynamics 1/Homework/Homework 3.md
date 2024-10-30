---
tags:
  - homework
  - classdyn1
date: 2024-10-07
pset: 3
completed: false
---
[[Directory]], [[University/Undergraduate/Second Year/Classical Dynamics 1/Classical Dynamics 1|Subject Directory]]
[[University/Undergraduate/Second Year/Classical Dynamics 1/Homework/Homework 1|🞀🞀]] [[University/Undergraduate/Second Year/Classical Dynamics 1/Homework/Homework 2|◀]] [[University/Undergraduate/Second Year/Classical Dynamics 1/Homework/Homework 4|▶]] [[University/Undergraduate/Second Year/Classical Dynamics 1/Homework/Homework 11|🞂🞂]]

[[University/Undergraduate/Second Year/Classical Dynamics 1/Homework/Worksheets/classic_dyn_3.pdf|Worksheet]]
1. 
a)
The kinetic energy of this particle is
$$
E_{k}=\frac{m}{2} \mathbf{\dot{r}} \cdot \mathbf{\dot{r}}
$$
and it's potential energy is simply ${} V(\mathbf{r}) {}$. Then the total energy has
$$
\begin{align}
 \frac{dE}{dt}  & =m \ddot{\mathbf{r}}\cdot {\dot{\mathbf{r}}}+\frac{d}{dt} V(\mathbf{r}(t))   \\
 & =m \ddot{\mathbf{r}}\cdot {\dot{\mathbf{r}}}+\dot{\mathbf{r}}\cdot \nabla V \\
 & =m \ddot{\mathbf{r}}\cdot {\dot{\mathbf{r}}} + \dot{\mathbf{r}}\cdot (-\mathbf{F}) \\
& =m \ddot{\mathbf{r}}\cdot {\dot{\mathbf{r}}} + \dot{\mathbf{r}}\cdot (-m\ddot{\mathbf{r}}) \\
 & =0
 \end{align}
$$
b)
1) 
We have that
$$
\begin{align}
\nabla \times \mathbf{F} & =\begin{pmatrix} \frac{ \partial  }{ \partial x }  \\ \frac{ \partial  }{ \partial y }  \\ \frac{ \partial  }{ \partial z }  \end{pmatrix} \times \begin{pmatrix} zx \\ yz \\ z^{2} \end{pmatrix}  \\
 & =\begin{pmatrix} 0-y \\ 0-x \\ 0 \end{pmatrix} \neq \begin{pmatrix} 0 \\0 \\ 0 \end{pmatrix} 
\end{align}
$$
and so the curl of $\mathbf{F}$ is non-zero, and $\mathbf{F} {}$ is not conservative. 
2) 
We have that 
$$
\begin{align}
\nabla \times \mathbf{F} & =\begin{pmatrix} \frac{ \partial  }{ \partial x }  \\
\frac{ \partial  }{ \partial y }  \\
\frac{ \partial  }{ \partial z } \end{pmatrix} \times \begin{pmatrix} yz^{2} \\ xz^{2} \\ 2xyz \end{pmatrix}  \\
  & =\begin{pmatrix} 2xz-2xz \\ 2yz-2yz \\ z^{2}-z^{2} \end{pmatrix}  =\begin{pmatrix} 0 \\ 0 \\ 0 \end{pmatrix} 
\end{align}
$$
and so $\mathbf{F} {}$ is conservative. Furthermore, if we set
$$
V=-xyz^{2}
$$
then we get that
$$
-\nabla V=\begin{pmatrix} yz^{2} \\ xz^{2} \\ 2xyz \end{pmatrix} 
$$
c)
The torque of a particle is 
$$
\mathbf{N}=\mathbf{r} \times \mathbf{F}
$$
and the angular momentum is
$$
\mathbf{L}=\mathbf{r} \times \mathbf{p}
$$
Now we compute
$$
\mathbf{N}=\begin{pmatrix} x \\ y \\ z \end{pmatrix} \times \begin{pmatrix} xz \\ yz \\ z^{2} \end{pmatrix} =\begin{pmatrix} 0 \\ 0 \\ 0 \end{pmatrix} 
$$
This is clear since ${} \mathbf{F}=z\mathbf{r} {}$. 
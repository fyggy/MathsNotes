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
\mathbf{L}=\mathbf{r} \times \mathbf{p}=m\mathbf{r}\times \dot{\mathbf{r}}
$$
Now we compute
$$
\mathbf{N}=\begin{pmatrix} x \\ y \\ z \end{pmatrix} \times \begin{pmatrix} xz \\ yz \\ z^{2} \end{pmatrix} =\begin{pmatrix} 0 \\ 0 \\ 0 \end{pmatrix} 
$$
This is clear since ${} \mathbf{F}=z\mathbf{r} {}$. 

Now since $\mathbf{N} {}$ is $\mathbf{0} {}$, then $\mathbf{L} {}$ is a constant w.r.t. to time. Therefore, 
$$
\mathbf{L}=m(\mathbf{r}(0) \times  \dot{\mathbf{r}}(0))=m \begin{pmatrix} 0 \\ 0 \\ 6-4 \end{pmatrix} =\begin{pmatrix} 0 \\ 0 \\ 2m \end{pmatrix} 
$$

Now let ${} \mathbf{r}=\mathbf{v}t+\mathbf{r}(0) {}$. Now ${} \mathbf{p}=m\dot{\mathbf{r}}=m\mathbf{v} {}$, and so ${} \dot{\mathbf{p}}=0 {}$, and so momentum is conserved. Likewise, 
$$
\begin{align}
\mathbf{L} & =m\mathbf{r} \times  \dot{\mathbf{r}} \\
 & =m( t\mathbf{v}+\mathbf{r}(0)) \times \mathbf{v} \\
 & =m(t\mathbf{v} \times  \mathbf{v}+\mathbf{r}(0) \times  \mathbf{v}) \\
 & =m\mathbf{r}(0) \times  \mathbf{v}
\end{align}
$$
which is constant, as both $\mathbf{v}$ and ${} \mathbf{r}(0) {}$ are constant. 
2. 
Let ${} r'=\frac{dr}{d\theta}  {}$, so that ${} \dot{r}=r' \dot{\theta}=\frac{\ell r'}{mr^{2}} {}$. Now
$$
E=\frac{m}{2} \frac{ \ell^{2}r'^{2} }{ m^{2}r^{4} }+\frac{\ell^{2}}{2mr^{2}}=\frac{\ell^{2}(r')^{2}}{2mr^{4}}+\frac{\ell^{2}}{2mr^{2}}=\frac{\ell^{2}}{2m}\left( \frac{(r')^{2}}{r^{4}}+\frac{1}{r^{2}} \right)
$$
Now let ${} u=\frac{1}{r} {}$. Then ${} u'=-\frac{1}{r^{2}}r' {}$, and
$$
E=\frac{\ell^{2}}{2m}((u')^{2}+u^{2})
$$
Now we have the solution ${} u=A\cos (\theta-\theta_{0}) {}$. If we substitute it in, then
$$
E=\frac{\ell^{2}}{2m}A^{2}
$$
and so 
$$
A=\sqrt{\frac{2mE}{\ell^{2}}}=\frac{\sqrt{2mE}}{\ell}
$$
Now finally
$$
\frac{1}{r}=A\cos (\theta-\theta_{0})
$$
which is the polar form of a straight line. If ${} \ell=0 {}$, then
$$
\dot{r}=\sqrt{\frac{2E}{m}}
$$
and so ${} r=\sqrt{\frac{2E}{m}}t {}$. Now since ${} \dot{\theta}=\frac{\ell}{mr^{2}}=0 {}$, then ${} \theta=c {}$ for some constant. Therefore, the path of the particle is a straight line passing through the origin. 
3. 
a)
$$
\begin{align}
\mathbf{F} &=-\nabla V \\
 & =-\begin{pmatrix} \frac{ \partial  }{ \partial x } V \\ \frac{ \partial  }{ \partial y } V \\ \frac{ \partial  }{ \partial z } V \end{pmatrix}  \\
 & =-\frac{k}{2}  \begin{pmatrix} 2x \\2y\\2z \end{pmatrix}  \\
 & =-k \begin{pmatrix} x \\ y \\ z \end{pmatrix} =-k\mathbf{r}
\end{align}
$$
We have that
$$
\mathbf{F}=m\ddot{\mathbf{r}}
$$
in particular, 
$$
-k\mathbf{r}=m\ddot{\mathbf{r}}
$$
Since this is a 2nd order linear differential equation, we have that
$$
r=
$$
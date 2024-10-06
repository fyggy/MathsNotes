---
tags:
  - homework
  - classdyn1
date: 2024-09-30
pset: 2
completed: true
---
[[Directory]], [[University/Undergraduate/Second Year/Classical Dynamics 1/Classical Dynamics 1|Subject Directory]]
[[University/Undergraduate/Second Year/Classical Dynamics 1/Homework/Homework 1|🞀🞀]] [[University/Undergraduate/Second Year/Classical Dynamics 1/Homework/Homework 1|◀]] [[University/Undergraduate/Second Year/Classical Dynamics 1/Homework/Homework 3|▶]] [[University/Undergraduate/Second Year/Classical Dynamics 1/Homework/Homework 11|🞂🞂]]

[[University/Undergraduate/Second Year/Classical Dynamics 1/Homework/Worksheets/classic_dyn_2.pdf|Worksheet]]
1. 
a)
We have that]
$$
\begin{align}
v_{x} & =\frac{dx}{dt} =35 \mathrm{ms}^{-1} \\
v_{y} & =\frac{dy}{dt}  =-2 \mathrm{ms}^{-1} \\
v_{z} & =\frac{dz}{dt}  =(10-9.8t)\mathrm{ms}^{-1}
\end{align}
$$
so at ${} t=0 {}\mathrm{s} {}$, then the momentum of the football is
$$
\mathbf{p}=\begin{pmatrix} 35\cdot 0.5 \\ -2 \cdot 0.5 \\ 10 \cdot  0.5 \end{pmatrix} \mathrm{kgms}^{-1}=\begin{pmatrix} 17.5 \\ -1 \\ 5 \end{pmatrix} \mathrm{kgms^{-1}}
$$
b)
${} x=35\mathrm{m} {}$ when ${} t=1\mathrm{s} {}$, and so 
$$
\begin{align}
 x & =35\mathrm{m}   \\
 y & =5-2=3\mathrm{m} <3.66 \mathrm{m}\\
z & =1.5+10-9.8=1.7 \mathrm{m} <2.44 \mathrm{m}
 \end{align}
$$
and she scores a goal
c)
At ${} t=0 \mathrm{s} {}$, the momentum of the football is
$$
\mathbf{p}=\begin{pmatrix} 35 \cdot 0.5 \\ -2 \cdot 0.5 \\ (10-9.8)\cdot 0.5 \end{pmatrix} \mathrm{kgms^{-1}}=\begin{pmatrix} 17.5 \\ -1 \\ 0.1 \end{pmatrix} \mathrm{kgms^{-1}}
$$
2. 
a)
We have that 
$$
\begin{align}
0& =r(t) \\
 & =r(0)-\frac{1}{2}gt^{2}+v(0)t \\
 & =1000-5t^{2}+0t \\
5t^{2} & =1000 \\
t^{2} & =200 \\
t & =10\sqrt{2}=14.14 \mathrm{s}
\end{align}
$$
b)
$$
\begin{align}
 v  & =\frac{dr}{dt}  \\
 & =-gt+v(0) \\
 & =-10t \;\mathrm{s} \\
 \end{align}
$$
and
$$
p=mv=0.001\cdot -10t=-0.01t \;\mathrm{kgms^{-1}}
$$
c)
@$t=10\sqrt{2}=14.14 \mathrm{s} {}$
$$
v =-10 \cdot 10 \sqrt{2}=-100 \sqrt{2} =-141.4 \mathrm{ms}^{-1} 
$$
and
$$
p=-0.01\cdot 10\sqrt{2}=-0.1414\mathrm{kgms}^{-1}
$$
d)
We see that
$$
\begin{align}
0 & =r(t) \\
 & =1-\frac{1}{2}gt^{2}+0t \\
  5t^{2} & =1 \\
t  & =\frac{1}{\sqrt{5}}=0.4472\mathrm{s}
\end{align}
$$
and so
$$
v=-gt+v(0)=-4.472\mathrm{ms^{-1}}
$$
and
$$
p=mv=-4.472 \mathrm{kgms^{-1}}
$$
Since the momentum of the brick is ${} 10 \sqrt{10}=31.6 {}$ times more momentum than the rain drop I predict it will probably hurt quite a lot comparatively.
3. 
a)
We have that
$$
\dot{\mathbf{r}}(t)=\frac{d}{dt} (t^{2}\mathbf{e}_{x}+\mathbf{e}_{y}-(\sin t)\mathbf{e}_{z})=2t\mathbf{e}_{x}+0\mathbf{e}_{y}-(\cos t)\mathbf{e}_{z}
$$
and
$$
\ddot{\mathbf{r}}=\frac{d}{dt} \dot{\mathbf{r}}(t)=\frac{d}{dt} (2t\mathbf{e}_{x}-(\cos t)\mathbf{e}_{z})=2\mathbf{e}_{x}+(\sin t)\mathbf{e}_{z}
$$
Finally, 
$$
\mathbf{p}(t)=m\dot{\mathbf{r}}(t)=2 mt \mathbf{e}_{x}-m(\cos t)\mathbf{e}_{z}
$$
b)
Since ${} \mathbf{F}(t)=m\ddot{\mathbf{r}}(t) {}$, then
$$
\mathbf{F}(t)=2m \mathbf{e}_{x}+m(\sin t)\mathbf{e}_{z} 
$$
c)
We have
$$
\begin{align}
 \mathbf{L}(t) & =\mathbf{r}(t) \times  \mathbf{p}(t) \\
 & =m\left( \begin{pmatrix} t^{2} \\ 1 \\ -\sin t \end{pmatrix} \times  \begin{pmatrix} 2t \\ 0 \\ -\cos t \end{pmatrix}  \right)  \\
 & =m \begin{pmatrix} -\cos t \\ -t^{2} \cos t+2t \sin t \\ -2t \end{pmatrix}   
 \end{align}
$$
and
$$
\begin{align}
\mathbf{N}(t) & =\mathbf{r}(t) \times  \mathbf{F}(t) \\
 & =m \left(  \begin{pmatrix} t^{2} \\ 1 \\ -\sin t \end{pmatrix} \times  \begin{pmatrix} 2 \\ 0 \\ \sin t \end{pmatrix}  \right)  \\
 & =m \begin{pmatrix} \sin t \\ (t^{2}+2) \sin t  \\  -2\end{pmatrix} 
\end{align}
$$
4. 
Let ${} {} |{\mathbf{r}}(t)|=f(t) {}$, and let ${} \dot{\mathbf{\theta}}(t)=2\pi f {}$. Then 
$$
\begin{align}
\mathbf{L} (t)& =\mathbf{r}\times  m\dot{\mathbf{r}} \\
 & =m \begin{pmatrix} r\cos \theta \\  r\sin  \theta\\  0\end{pmatrix} \times  \begin{pmatrix} \dot{r} \cos \theta-r \dot{\theta} \sin \theta\\  \dot{r} \sin \theta+r \dot{\theta}\cos \theta\\  0\end{pmatrix}  \\
 & =m\begin{pmatrix} 0 \\ 0 \\ r \dot{r} \sin \theta \cos \theta+r \dot{}\dot{\theta} \cos ^{2}\theta-r\dot{r}\sin \theta \cos \theta+r^{2} \theta^{2}\sin ^{2}\theta \end{pmatrix}  \\
 & =\begin{pmatrix} 0 \\ 0 \\m r^{2} \dot{\theta} \end{pmatrix} 
\end{align}
$$
and 
$$
\begin{align}
\mathbf{N} & = \mathbf{r} \times  m\ddot{\mathbf{r}} \\
 & =m \begin{pmatrix} r\cos  \theta \\ r\sin \theta \\ 0 \end{pmatrix} \times \begin{pmatrix} \ddot{r} \cos \theta-\dot{r} \dot{\theta} \sin \theta-\dot{r}\dot{\theta}\sin \theta-r \ddot{\theta}\sin \theta-r \dot{\theta}^{2} \cos \theta \\  \ddot{r}\sin \theta+\dot{r}\dot{\theta}\cos \theta+\dot{r} \dot{\theta} \cos \theta+r  \ddot{\theta}\cos \theta-r\dot{\theta}^{2} \sin \theta\\ 0 \end{pmatrix}  \\
 & =m \begin{pmatrix} r\cos \theta \\ r \sin \theta \\ 0 \end{pmatrix} \times \begin{pmatrix} \ddot{r} \cos \theta-2\dot{r} \dot{\theta} \sin \theta-r \dot{\theta}^{2} \cos \theta \\ \ddot{r} \sin \theta+2\dot{r} \dot{\theta} \cos \theta-r\dot{\theta}^{2} \sin \theta \\ 0 \end{pmatrix}  \\
 & =m \begin{pmatrix} 0 \\ 0 \\ r \ddot{r}\sin \theta \cos \theta+2r\dot{r}\dot{\theta}\cos ^{2}\theta-r^{2}\dot{\theta}^{2} \sin \theta \cos \theta-r\ddot{r} \sin \theta \cos \theta+ 2r \dot{r} \dot{\theta} \sin ^{2}\theta+r^{2} \dot{\theta}^{2} \sin \theta \cos \theta\end{pmatrix} \\
 & =m \begin{pmatrix} 0 \\ 0 \\ 2r \dot{r}\dot{\theta} \end{pmatrix}   \\
 & =\begin{pmatrix} 0 \\ 0 \\ 2mr\dot{r}\dot{\theta} \end{pmatrix} 
\end{align}

$$
Now we have
$$
\begin{align}
 \frac{d}{dt} \mathbf{L}  & = \begin{pmatrix} 0 \\ 0 \\ \frac{d}{dt} mr^{2}\dot{\theta} \end{pmatrix}  \\
 & =\begin{pmatrix} 0 \\ 0 \\ 2mr\dot{r} \dot{\theta}+mr^{2} \ddot{\theta}  \end{pmatrix}  \\
 & =\begin{pmatrix} 0 \\ 0 \\ 2m r \dot{r} \dot{\theta} \end{pmatrix} =\mathbf{N}
 \end{align}
$$
#todo finish when i know what the last section means
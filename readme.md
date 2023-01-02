# Generalized Max-Median Filtering
## Group member
Bùi Khánh Huyền - 1902137

Dương Đức Duy - 20020287 

Vũ Thị Thi - 20020313 
## Inspriration
Our work was to implement and enhance the performance of the paper https://ieeexplore.ieee.org/document/647798.

## Theoretical basis
The basic idea of **max/median** filtering is to combine the output of some basic subfilters each of which is good for preserving a feature in a specific direction. The max/median filtering can preserve image details such as bright lines. 
**Generalized max/median filter** is an extended max/median filter. The essential idea is to define order statistics over the line segments without the common centre point.

<img style="display: block; 
           margin-left: auto;
           margin-right: auto;
           width: 40%;"
     src="https://github.com/huyenbui117/Generalized-Max-Median-Filtering/blob/main/images/BasicIdea.png" 
     alt="Basic idea"> 
- $x(.  , . )$ is a two-dimensional sequence
- $x(i,j)$ is the $(i,j)^{th}$ pixel.
- $W(i,j)$ is a $(2n + 1) \times (2n + 1)$ square window centered at the $(i,j)^{th}$ pixel. 
We define the following line segments of $W$:  ${W_k(i,j) (1 \leqslant k \leqslant 4)}$
  - ${ W^0_1 (i,j) = \\{ x(i,j+k), -n \leqslant k \leqslant n, k \neq 0 \\} }$
  - ${W^0_2 (i,j) = \\{ x(i+k,j+k), -n \leqslant k \leqslant n, k \neq 0 \\} }$
  - ${W^0_3 (i,j) = \\{ x(i+k,j), -n \leqslant k \leqslant n, k \neq 0 \\} }$
  - ${W^0_4 (i,j) = \\{ x(i-k,j+k), -n \leqslant k \leqslant n, k \neq 0 \\} }$
 
- Let ${x^k_{(1)} (i,j) \leqslant x^k_{(2)} (i,j) \leqslant ... \leqslant x^k_{(2n)}(i,j), (1 \leqslant k \leqslant 4)}$ be the order statistics in ${W^0_k(i,j) (1 \leqslant k \leqslant 4)}$ 
- The output of generalized max/median filtering is defined as ${y (i,j) = med(S_1 (i,j) , S_2(i,j) , x(i,j))}$, where:
  - ${S_1 (i,j) = \max (x^k_{(r)} (i,j), 1 \leqslant k \leqslant 4)}$
  - ${S_2 (i,j) = \max (x^k_{(2n - r + 1)} (i,j), 1 \leqslant k \leqslant 4)}$
- When r = n, the output of the generalized max/median filtering is identical to that of the max/median filtering. 
## Run
To run, access the notebook [Generalized_Max_Median_Filtering.ipynb](https://github.com/huyenbui117/Generalized-Max-Median-Filtering/blob/main/Generalized_Max_Median_Filtering.ipynb)
The results of various experiments conducted is saved in [experiments.csv](https://github.com/huyenbui117/Generalized-Max-Median-Filtering/blob/main/experiments.csv)
## Our results
- Original input image 
  ![Original input image](https://github.com/huyenbui117/Generalized-Max-Median-Filtering/blob/main/images/experiment-input.png)
- Filtered with median filter
  ![Filtered with median filter](https://github.com/huyenbui117/Generalized-Max-Median-Filtering/blob/main/images/experiment-median-filter.png)
- Filtered with GMM (ours) and compare
  ![Filtered with GMM (ours) and compare](https://github.com/huyenbui117/Generalized-Max-Median-Filtering/blob/main/images/experiment-gmm.png)

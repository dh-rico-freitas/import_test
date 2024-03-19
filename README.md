Simple sample with multiple levels of subpackages. 

- sample_1 calls the most external function, that import all the chain.
- sample_2 calls directly the subsubpackage function.
- sample_3 calls both.

sample_1 and sample_2 made exactly the same imports,
there is no improvment calling directly the deeply burried package.

Finally, sample_3 show that the imports are done only once.

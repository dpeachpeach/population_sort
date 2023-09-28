# The Population (formerly Malthusian) Sorting Algorithm.

Inspired by other whimsical sorting algorithms such as [bogosort](https://yaav.leonardini.dev/algorithms/sorting/bogo-sort.html), [bogobogosort](https://yaav.leonardini.dev/algorithms/sorting/bogobogo-sort.html), and [Stalinsort](https://www.youtube.com/watch?v=hyOlWQ9MLPI). I wrote and designed Popsort (formerly Malthusian_Sort). 

As the former name implies, I was inspired to design this sorting algorithm off of [Malthusian Population Theory](https://en.wikipedia.org/wiki/Malthusianism), which states that population increases geometrically past it's theoretical 'max bound' until it collapses geometrically back to its bound, after which it gradually hovers around the bound in a pseudo-equilibrium.

I was apprehensive to publish the initial Malthusian algorithm due to its incredible inefficiency. I want to return a sorted list with the length of it resembling the 'population bound' provided by the user, however the initial algorithm was far too inefficient.

Population sort aims to reach the population bound provided by either culling the population or by birthing new members. After reaching the bound, the population sorts itself through continuous life cycles until it is sorted. 

Although this algorithm was initially designed as a complete joke, it has some cool properties. The most interesting of which I found being: Just like a population of people / animals isolated from the outside world, both genotype and phenotype of the population of the organisms will gradually become more and more alike, just like the values in Popsort.

The algorithm isn't completely finished, I'd like to wrap up some unit tests and then publish it onto PyPi, maybe post it on hackernews or something and get a meme video formed from it. 

I also plan to post Malthusian Sort shortly after completing this project in a different language, preferably C++ or Rust, one that can handle the performance requirements.

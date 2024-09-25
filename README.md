## Stiefel Manifolds and Polygons ##

### Overview ###

This is an implementation of the ideas exposed in the article [Stiefel Manifolds and Polygons](https://arxiv.org/abs/1902.01486) (SMP) published by Clayton Shonkwiller in 2019. The goal is to describe an identification of polygons with points in $\text{St}_k(\mathbb R^2)$. With that identification in hand, in this project we will:

- Use the tools in SMP to define what a random polygon is 
- Generate random polygons
- Make random polygons convex



### Installation ### 
To install the package, navigate to the project root and run:

`pip install -e .`

`pip install -r requirements.txt`

### Requirements ###
- `numpy == 1.16.4`
- `matplotlib==1.3.1`
- `scipy==3.1.1`

### How to Run ###
1. Clone this repository
2. Install the necessary dependencies
3. Run the examples provided in the `examples/` directory to test the functionality

### Next Steps ###
Potential future developments for this project include:
- Implementing the algorithm for finding paths in the polygon space 
- Implementing the algorithm for the generation of random planar tilings

### Contributing ###

Feel free to contribute by opening a pull request. If you find any issues, please report them!
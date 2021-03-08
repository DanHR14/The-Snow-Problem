# The Snow Problem

In this exercise we have and image where we can see walls and the snow that have fall between there.

![Imafe of graphic](https://github.com/DanHR14/The-Snow-Problem/blob/main/static/snow.png)

Given a list of height wall, make a function that calculate how many snow have been stored between walls. For example, the solution of our picture is 12.

## Cuadratic Solution O(n * m)

We can see that with our array we can do a matrix with wall positions and they height. One solution can be given the higher height, try to find the next higher height, and if we find one, we can put snow between both until the height of the snow it is the same than the height of the wall less higher. When we put the snow, we store the height from the less higher wall and continue doing the same.


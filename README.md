# Challenge 2 (I forgot the name)

## Getting Started

### Using Linear Regression and SGD Regression to evaluate

I started applying the data to the regression method.
With only preconfigure data a little bit(selecting data with  correlation coefficient greater than 0.27 and dropping all of the discrete data)
![self test on local](images/image-1.png)
![0.73 on kaggle](images/image.png)

### dealing with discrete data

I looked deep into the column description.
![Discrete tags](images/image-2.png)
There are too many columns.

So, I use dummy function to create more columns for discrete value.

![correlation coefficient remain 0.27](images/image-3.png)
And, the result get worse
![correlation coefficient updated to gte 0.5](images/image-4.png)
![correlation coefficient updated to gte 0.65](images/image-5.png)

Still got bad results.

=> Remove abs
![correlation coefficient updated to gte 0.65](images/image-6.png)
![correlation coefficient updated to gte 0.5](images/image-7.png)

=> split continuous data and discrete data
![discrete gte 0.2; continous gte 0.5](images/image-8.png)
![discrete gte 0.2; continuous gte 0.5;abs](images/image-11.png)
![discrete gte 0.5; continous gte 0.2](images/image-9.png)
![discrete gte 0.5; continous gte 0.2;abs](images/image-10.png)

### abs on

continous gte 0.7

![discrete gte 0.7; continuous gte 0.7](images/image-12.png)
![discrete gte 0.6; continous gte 0.7](images/image-13.png)
![discrete gte 0.5; continous gte 0.7](images/image-14.png)
![discrete gte 0.4; continous gte 0.7](images/image-15.png)
![discrete gte 0.3; continous gte 0.7](images/image-16.png)
![discrete gte 0.2; continous gte 0.7](images/image-17.png)

continous gte 0.6

![discrete gte 0.7; continuous gte 0.6](images/image-18.png)
![discrete gte 0.6; continuous gte 0.6](images/image-19.png)
![discrete gte 0.5; continuous gte 0.6](images/image-20.png)
![discrete gte 0.4; continuous gte 0.6](images/image-21.png)
![discrete gte 0.3; continuous gte 0.6](images/image-22.png)
![discrete gte 0.2; continuous gte 0.6](images/image-23.png)

continous gte 0.5

![discrete gte 0.7; continuous gte 0.5](images/image-24.png)
![discrete gte 0.6; continuous gte 0.5](images/image-25.png)
![discrete gte 0.5; continuous gte 0.5](images/image-26.png)
![discrete gte 0.4; continuous gte 0.5](images/image-28.png)
![discrete gte 0.3; continuous gte 0.5](images/image-29.png)

continous gte 0.4

![discrete gte 0.7; continuous gte 0.4](images/image-30.png)
![discrete gte 0.6; continuous gte 0.4](images/image-31.png)
![discrete gte 0.5; continuous gte 0.4](images/image-32.png)
![discrete gte 0.4; continuous gte 0.4](images/image-33.png)
![discrete gte 0.3; continuous gte 0.4](images/image-34.png)

continous gte 0.3

![discrete gte 0.7; continuous gte 0.3](images/image-35.png)
![discrete gte 0.6; continuous gte 0.3](images/image-36.png)
![discrete gte 0.5; continuous gte 0.3](images/image-37.png)
![discrete gte 0.4; continuous gte 0.3](images/image-38.png)
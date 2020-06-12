# CloudProject
About the project
----------------------
This is the project developed for the **Development of Aplications in the Cloud** class of January-June 2020.
<p>It is an algorithm written in Python to use parallel computig with MPI in the Cloud, using GCP. The algorithm uses the Monte Carlo method to calculate an aproximation of Pi.
<p>The program was packaged in a Docker container image that was then used in a Kubernetes cluster in Google Kubernete Engine to create a deployment of pods running this image. The results where then published in JSON format to a FireStore also in GCP.

Monte Carlo explanation
-------------------------
<p>The idea of Monte Carlo is to generate a series of random points in the first quartile of a circle, and calculate the hipotenuse of said point. Considering a radius of the circle of 1, if the hipotenuse is less than 1, the point is considered to be inside the circle. To get the aproximation of Pi, the total number inside the circle is counted, multiplied by 4 because of the four quartiles of the circle, and then divided between the total number of generated random points. 

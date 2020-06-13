# CloudProject
About the project
----------------------
This is the project developed for the **Development of Aplications in the Cloud** class of January-June 2020.
<p>It is an algorithm written in Python to use parallel computig with MPI in the Cloud, using GCP. The algorithm uses the Monte Carlo method to calculate an aproximation of Pi.
<p>The program was packaged in a Docker container image that was then used in a Kubernetes cluster in Google Kubernete Engine to create a deployment of pods running this image. The results where then published in JSON format to a FireStore also in GCP.

Monte Carlo explanation
-------------------------
<p>The idea of Monte Carlo is to generate a series of random points in the first quartile of a circle, and calculate the hipotenuse of said point. Considering a radius of the circle of 1, if the hipotenuse is less than 1, the point is considered to be inside the circle. To get the aproximation of Pi, the total number inside the circle is counted, multiplied by 4 because of the four quartiles of the circle, and then divided between the total number of generated random points. 
  
Test in Kubernetes
--------------------
<p>The environment in which the following commands were run is in the Cloud Shell of Google Cloud Platform.
  
```
git clone https://github.com/ggonzaleze/CloudProject.git
gcloud config set compute/zone us-west1-a
gcloud container clusters create project-cluster
cd CloudProject
cd
ssh-keygen
```

When prompted to entere file **Enter file in which to save the key** enter **./CloudProject/project_cluster**
<p>Press enter two times to not create a passphrase
  
```
cd CloudProject
```

Create file named **ssh_config** with the following content:

```
Host *    
  StrictHostKeyChecking no
```

```
docker build -t project-mpi .
docker tag project-mpi gcr.io/<google-cloud-project-id>/project-mpi
docker push gcr.io/<google-cloud-project-id>/project-mpi
```
Enter **deployment.yaml** and in **image**, change **google-cloud-project-id**

```
kubectl apply -f deployment.yaml
kubectl get pods
```

You should now see your pods in STATUS Running.

```
touch hosts
for podIP in $(kubectl get pods -o json| jq -r '.items[].status.podIP'); do echo "${podIP}" >> hosts; done
for podname in $(kubectl get pods -o json| jq -r '.items[].metadata.name'); do kubectl cp hosts "${podname}":/mpi/hosts; done
```

```
kubectl get pods
```

Get the name of the first pod

```
kubectl exec <pod-name> -- mpiexec -f hosts -n 4 python3 projectNoFirestore.py
```

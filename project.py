from mpi4py import MPI
import random
import math
import uuid
from google.cloud import firestore
import os

t4 = MPI.Wtime()
comm = MPI.COMM_WORLD
size = comm.size #number of processors
rank = comm.rank #calling process rank
npoints = 1000000

def quarterCircle():
        circle_count = 0
        for i in range(npoints//size):
                x = random.random()
                y = random.random()
                x2 = pow(x,2)
                y2 = pow(y,2)
                h = math.sqrt(x2+y2)
                if h < 1:
                        circle_count = circle_count+1
        print (rank," rank computed ",npoints/size,"points")
        return circle_count

cc = quarterCircle()
circle_count = comm.gather(cc,root=0)
if rank==0:
    t5 = MPI.Wtime()
    print("Time:",t5-t4)
    tiempo = t5-t4
    print(circle_count)
    pi = (4.0 * sum(circle_count)) / npoints
    print("Pi aprox. value:",pi)
    os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "/mpi/mpi_auth.json"
    name_test = u''+str(uuid.uuid4())
    db = firestore.Client()
    doc_ref = db.collection(u'montecarlo').document(name_test)
    doc_ref.set({
    u'time': tiempo,
    u'pi': pi,
    u'points': npoints,
    u'processors': size
    })

FROM python

RUN apt-get update

RUN yes | apt install mpich
RUN yes | pip3 install mpi4py
RUN yes | pip3 install google-cloud-firestore

ADD projectNoFirestore.py /mpi/projectNoFirestore.py
RUN apt-get install -y openssh-server

RUN mkdir /var/run/sshd

RUN echo 'root:7p?Db#N_>k=de2pp' | chpasswd
RUN sed -i 's/PermitRootLogin prohibit-password/PermitRootLogin yes/' /etc/ssh/sshd_config

RUN sed 's@session\s*required\s*pam_loginuid.so@session optional pam_loginuid.so@g' -i /etc/pam.d/sshd
WORKDIR /mpi

RUN mkdir -p /root/.ssh/
ADD project_cluster.pub project_cluster.pub
ADD project_cluster project_cluster

RUN cat project_cluster.pub >> /root/.ssh/authorized_keys
RUN cp project_cluster /root/.ssh/id_rsa
RUN cp project_cluster.pub /root/.ssh/id_rsa.pub

RUN chmod 600 /root/.ssh/id_rsa

COPY ssh_config /etc/ssh/ssh_config

EXPOSE 22
RUN service ssh restart
CMD ["/usr/sbin/sshd", "-D"]

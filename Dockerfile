FROM ubuntu
RUN apt update
RUN apt install --yes python3 python3-pip
RUN pip3 install requests
COPY dynamic_dns.py /home
CMD python3 /home/dynamic_dns.py

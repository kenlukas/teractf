FROM ubuntu:latest AS app  
RUN apt-get update && apt-get install -y gcc-multilib make file

WORKDIR /app

COPY admin.c flag.txt ./  
RUN gcc -o admin admin.c  
RUN rm admin.c

FROM pwn.red/jail  
COPY --from=app / /srv  
ENV JAIL_TIME=30  
RUN mv /srv/app/admin /srv/app/run

FROM ubuntu:latest AS app  
RUN apt-get update && apt-get install -y gcc-multilib make file

WORKDIR /app

COPY youdontownme.c flag.txt ./  
RUN gcc youdontownme.c -o youdontownme -fno-stack-protector  -no-pie -m32
RUN rm youdontownme.c  

FROM pwn.red/jail  
COPY --from=app / /srv  
ENV JAIL_TIME=30  
RUN mv /srv/app/youdontownme /srv/app/run

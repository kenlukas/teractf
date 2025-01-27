FROM ubuntu:latest AS app
RUN apt-get update && apt-get install -y gcc-multilib make 

WORKDIR /app

COPY maths.c flag.txt ./
RUN gcc -o maths maths.c
RUN rm maths.c

FROM pwn.red/jail
COPY --from=app / /srv
ENV JAIL_TIME=30
RUN mv /srv/app/maths /srv/app/run

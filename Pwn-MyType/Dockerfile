FROM ubuntu:latest AS app
RUN apt-get update && apt-get install -y gcc-multilib make cowsay file

WORKDIR /app

#COPY Makefile mytype.c flag.txt ./
COPY mytype.c flag.txt ./
RUN gcc -o mytype mytype.c
#RUN rm Makefile mytype.c
RUN rm mytype.c
RUN ln -s /usr/games/cowsay /bin/cowsay

FROM pwn.red/jail
COPY --from=app / /srv
ENV JAIL_TIME=30
RUN mv /srv/app/mytype /srv/app/run

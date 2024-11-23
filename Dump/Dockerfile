FROM ubuntu:16.04
RUN apt-get update && apt-get install -y openssh-server
RUN mkdir /var/run/sshd

RUN useradd -M jailer # Add a user for ssh
RUN echo 'jailer:keyissecret' | chpasswd # Assign a password to the user for ssh

# Prohibit someone to ssh as root
RUN sed -i 's/PermitRootLogin prohibit-password/PermitRootLogin yes/' /etc/ssh/sshd_config

# SSH login fix. Otherwise user is kicked off after login
RUN sed 's@session\s*required\s*pam_loginuid.so@session optional pam_loginuid.so@g' -i /etc/pam.d/sshd

# Remove read and executable permissions for the user.
RUN chmod go-rx /usr/bin/passwd

WORKDIR /jailed
COPY ./jailed .
RUN chown -R root:root /jailed
RUN chmod -R 755 .
RUN chmod 1733 /tmp /var/tmp /dev/shm

# Configure default ssh shell as bash
RUN chsh -s /bin/bash jailer
# Define jailer as a recognised ssh user
RUN echo "Match User jailer" >> /etc/ssh/sshd_config
# Define the chroot directory to be sshed into
RUN echo "  ChrootDirectory /jailed" >> /etc/ssh/sshd_config
EXPOSE 22
CMD ["/usr/sbin/sshd", "-D"]

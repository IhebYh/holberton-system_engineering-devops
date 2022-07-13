# Postmortem

## Issue Summary:
On 4/14/22 at 9:23 pm, connection to my servers provided by holberton school failed for a total of 1h and 43min, with the connection reinstated successfully at 11:06 pm. The root cause of the connection failure was because of the nginx service working in the background of my computer prohibiting me from connecting the servers.

## Timeline:
**9:23 pm:** After typing the command in the terminal trying to connect to the server, an error message was displayed showing either a timeout or an rsa key not found.

**9:25 pm:** Rsa key re-checked for many times and "ssh key-gen" re-used to be sure of the main cause.

**9:45 pm:** Contacting the staff to see if there's a problem in the servers.

**10:14 pm:** A response recieved from the staff telling me that the servers are working fine. SSH command log checked to locate the problem.

**10:55 pm:** After reading the logs, a brief research in google with the results I have from the logs. Checking the working processes using ps command.

**11:03 pm:** Nginx found working in the background. Using 'pkill' command to kill it.

**11:06 pm:** Trying to reconnect and connection was successful.

## Root cause and resolution:
The root cause of this connection failure was because of the Nginx service working in the background listening at the same port of the ssh connection. Killing the service, since it is not needed, was the perfect solution for this problem.

## Corrective and preventative measures:
to prevent an issue like this from occuring in the future, services should not be automatically started or try to provide for each service a specific port so there will be no confusion.


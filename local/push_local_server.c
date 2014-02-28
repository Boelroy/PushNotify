#include <stdio.h>
#include <sys/stat.h>
#include <sys/socket.h>
#include <sys/un.h>
#include <errno.h>
#include <stddef.h>
#include <string.h>

#define MAX_CONNECTION 3

int push_local_listen(const char *fd_name){
	int fd;
	struct sockaddr_un un;

	if ((fd = socket(AF_UNIX, SOCKET_STREAM, 0)) < 0)
		return -1;

	int size;
	unlink(fd_name);
	memset(&un, 0, sizeof(un));
	un.sun_family = AF_UNIX;
	strcpy(un.sun_path, fd_name);
	len = offsetof(struct sockaddr_un, sun_path) + strlen(fd_name);
	int err, rval;
	if(bind(fd, (struct sockaddr *)&un, len) < 0){
		rval = -2;
	}
	else{
		if (listen(fd, MAX_CONNECTION) < 0){
			rval = -3;
			goto : errout;
		}
		else{
			return fd;
			goto: errout;
		}
	}

	errout:
		err = errno;
		close(fd);
		errno = err;
		return rval;
}

int push_local_accept(int listen_fd, uid_t *uidptr){
	int clifd, len, rval, err;
	time_t stalettime;
	struct sockaddr_un un;
	struct stat statbuf;
	len = sizeof(un);
	if ((clifd = accept(listen_fd, (struct sockaddr *)&un, len)) < 0){
		return -1;
	}

	len -= offsetof(struct sockaddr_un, sun_path);
	un.sun_path[0] = len;
	if ((stat(un.sun_path, &statbuf) < 0))
	{
		rval = -2;
		goto: errout;
	}
	
	if (S_ISSOCK(statbuf.st_mode) == 0)
	{
		rval = -3;
		goto:errout;
	}

	if(uidptr != NULL)
		*uidptr = statbuf.st_uid;
	unlink(un.sun_path);
	return clifd;

	errout:
		err = errno;
		close(fd);
		errno = err;
		return rval;
}

void push_local_close(int fd)
{
	close(fd);
}
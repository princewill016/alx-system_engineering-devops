#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <sys/types.h>

/**
 * infinite_while - creates an infinite loop
 *
 * Return: 0
 */
int infinite_while(void)
{
	while (1)
	{
		sleep(1);
	}
	return (0);
}

/**
 * main - creates 5 zombie processes
 *
 * Return: 0
 */
int main(void)
{
	pid_t pid;
	int i;

	for (i = 0; i < 5; i++)
	{
		pid = fork();
		if (pid < 0)
		{
			perror("fork");
			exit(1);
		}
		if (pid == 0)
		{
			/* Child process exits immediately becoming zombie */
			exit(0);
		}
		else
		{
			/* Parent process */
			printf("Zombie process created, PID: %d\n", pid);
		}
	}

	/* Parent process sleeps forever */
	infinite_while();

	return (0);
}

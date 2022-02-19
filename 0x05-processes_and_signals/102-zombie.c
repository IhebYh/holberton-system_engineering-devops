#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>

/**
 * infinite_while - infinite loop
 *
 * Return: int
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
 * main - create 5 zombie processes
 *
 * Return: int
 */
int main(void)
{
	pid_t zombie;
	int i = 0;

	for (; i < 5; i++)
	{
		zombie = fork();
		if (!zombie)
			return (0);
		printf("Zombie process created, PID:%d\n", zombie);
	}
	infinite_while();
	return (0);
}

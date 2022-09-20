#include "lists.h"
/**
  * check_cycle - checks if a singly linked list has a cycle in it
  * @list: the list to be checked
  * Return: check code
  */
int check_cycle(listint_t *list)
{
	int i = 0;
	listint_t *head, *nexting;

	head = list;
	nexting = list;
	while(nexting != NULL)
	{
		if (nexting->next == head)
			return(1);
		i++;
		nexting = nexting->next;
	}

	return(0);
}

#include "lists.h"
#include <stdio.h>
#include <stdlib.h>

int compare(listint_t *head, listint_t *head2);
listint_t *reverse_list(listint_t *head);
listint_t *duplicate_list(listint_t *head);

/**
  * duplicate_list - Duplicates a list
  * @head: list to be puplicated
  * Return: duplicated list
  */
listint_t *duplicate_list(listint_t *head)
{
	listint_t *h = head, *dup = NULL, *tail = NULL;

	while (h != NULL)
	{
		if (dup == NULL)
		{
			dup = malloc(sizeof(listint_t));
			dup->n = h->n;
			dup->next = NULL;
			tail = dup;
		}
		else
		{
			tail->next = malloc(sizeof(listint_t));
			tail = tail->next;
			tail->n = h->n;
			tail->next = NULL;
		}
		h = h->next;
	}

	return (dup);
}
/**
  * reverse_list - reverse a list
  * @head: list to be reversed
  * Return: reversed list
  */
listint_t *reverse_list(listint_t *head)
{
	listint_t *current, *prev = NULL, *next = NULL;

	current = head;
	while (current != NULL)
	{
		next = current->next;
		current->next = prev;
		prev = current;
		current = next;
	}

	return (prev);
}
/**
  * compare - compares two lists
  * @head: 1st list
  * @head2: 2nd list
  * Return: 0 or 1
  */
int compare(listint_t *head, listint_t *head2)
{
	listint_t *h;

	h = head;
	while (h != NULL && head2 != NULL)
	{
		if (h->n != head2->n)
			return (0);

		h = h->next;
		head2 = head2->next;
	}
	if (h == NULL && head2 == NULL)
		return (1);
	else
		return (0);
}
/**
  * is_palindrome - checks if a list is a palindrome
  * @head: list
  * Return: 0 or 1
  */
int is_palindrome(listint_t **head)
{
	listint_t *head2, *h;
	int res;

	h = *head;
	if (h == NULL)
		return (1);
	head2 = duplicate_list(h);
	head2 = reverse_list(head2);
	res = compare((*head), head2);
	free_listint(head2);

	return (res);
}

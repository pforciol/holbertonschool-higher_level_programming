#include "lists.h"

/**
 * check_cycle - checks if a singly linked list has a cycle in it
 *
 * @head: the listint_t argument (head)
 *
 * Return: 0 if there is  cycle, 1 if there is a cycle
 */

int check_cycle(listint_t *head)
{
	listint_t *slow_p = head, *fast_p = head;

	if (head && head->next)
	{
		while (slow_p && fast_p && fast_p->next)
		{
			slow_p = slow_p->next;
			fast_p = fast_p->next->next;

			if (slow_p == fast_p)
			{
				slow_p = head;
				while (slow_p != fast_p)
				{
					slow_p = slow_p->next;
					fast_p = fast_p->next;
				}
				return (1);
			}
		}
	}
	return (0);
}

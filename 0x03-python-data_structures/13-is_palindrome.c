#include "lists.h"

/**
 * is_palindrome - checks if a linked list is a palindrome
 *
 * @head: the head address of the linked list
 *
 * Return: 1 if it's a palindrome, 0 else
 */

int is_palindrome(listint_t **head)
{
	listint_t *cur = *head;
	int len = 0, *tab = NULL, i, j;

	if (*head)
	{
		while (cur)
		{
			len++;
			cur = cur->next;
		}

		tab = malloc(sizeof(int) * len);
		if (!tab)
			return (0);

		cur = *head;
		i = 0;
		while (i < len)
		{
			tab[i] = cur->n;
			cur = cur->next;
			i++;
		}

		while (j < len / 2)
		{
			if (tab[j] == tab[i - j - 1])
				j++;
			else
			{
				return (0);
				free(tab);
			}
		}
		free(tab);
	}
	return (1);
}

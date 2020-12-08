#include "lists.h"
#include <stdio.h>
#include <stdlib.h>

/**
 * insert_node - insert node at right space
 *
 * @head: the head of the list
 * @number: the value of the node
 *
 * Return: pointer to the new node
 */

listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new;
	listint_t *current;

	current = *head;

	new = malloc(sizeof(listint_t));
	if (new == NULL)
		return (NULL);

	new->n = number;

	if (*head == NULL)
		*head = new;
	else
	{
		if (number < current->n)
		{
			new->next = current;
			*head = new;
		}
		else
		{
			while (current->next && number > current->next->n)
				current = current->next;

			new->next = current->next;
			current->next = new;
		}
	}
	return (new);
}

#include "lists.h"

/**
 * check_cycle - checks if a linked list contains a cycle
 * @list: linked list to check
 *
 * Return: 1 if the list has a cycle, 0 if it doesn't
 */
int check_cycle(listint_t *list)
{
	listint_t *this = list;
	listint_t *that = list;

	if (list == NULL)
		return (0);

	while (this && that && that->next)
	{
		this = this->next;
		that = that->next->next;
		if (this == that)
			return (1);
	}

	return (0);
}


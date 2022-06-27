#include "lists.h"
/**
 * check_cycle - checks if a singly linked
 * list has a cycle in it
 * @list: pointer to singly linked lists
 * Return: 0 if there is no cycle, 1 if there is a cycle
 */
int check_cycle(listint_t *list)
{
	listint_t *i;
	listint_t *j;

	i = list;
	j = list;
	while (list && i &&  i->next)
	{
		list = list->next;
		i = i->next->next;

		if (list == i)
		{
			list = j;
			j = i;
			while (1)
			{
				i = j;
				while (i->next != list && i->next != j)
				{
					i = i->next;
				}
				if (i->next == list)
					break;
				list = list->next;
			}
			return (1);
		}
	}
	return (0);
}

#include <Python.h>
#include <stdio.h>

/**
 * print_python_list_info - gives data of the PyListObject
 *
 * @p: the PyObject
 */

void print_python_list_info(PyObject *p)
{
	Py_ssize_t size = 0;
	int i = 0;

	if (PyList_CheckExact(p))
	{
		size = PyList_Size(p);

		printf("[*] Size of the Python List = %zd\n", size);
		printf("[*] Allocated = %lu\n", ((PyListObject *)p)->allocated);

		while (i < size)
		{
			printf("Element %d: %s\n",
					i, Py_TYPE(PyList_GetItem(p, i))->tp_name);
			i++;
		}
	}
}

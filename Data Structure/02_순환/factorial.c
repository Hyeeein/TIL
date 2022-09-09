// 01. ��ȯ���� ���丮�� ��� ���α׷�

int factorial(int n) {
	if (n <= 1) return (1);
	else return (n * factorial(n - 1));
}

// 02. ��¹��� �߰��� ��ȯ���� ���丮�� ��� ���α׷�

int factorial(int n) {
	printf("factorial(%d) \n", n);
	if (n <= 1) return (1);
	else return (n * factorial(n - 1));
}

// 03. �ݺ����� ���丮�� ��� ���α׷�

int factorial_iter(int n) {
	int i, result = 1;
	for (i = 1; i <= n; i++)
		result = result * i;
	return (result);
}
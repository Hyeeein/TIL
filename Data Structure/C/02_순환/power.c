// 01. �ݺ����� �ŵ����� ��� ���α׷�

double slow_power(double x, int n) {
	int i;
	double result 1.0;

	for (i = 0; i < n; i++)
		result = result * x;
	return (result);
}

// 02. ��ȯ���� �ŵ����� ��� ���α׷�

double power(double x, int n) {
	if (n == 0) return 1;
	else if ((n % 2) == 0)
		return power(x * x, n / 2);
	else return x * power(x * x, (n - 1) / 2);
}
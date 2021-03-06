// 01. 순환적인 팩토리얼 계산 프로그램

int factorial(int n) {
	if (n <= 1) return (1);
	else return (n * factorial(n - 1));
}

// 02. 출력문이 추가된 순환적인 팩토리얼 계산 프로그램

int factorial(int n) {
	printf("factorial(%d) \n", n);
	if (n <= 1) return (1);
	else return (n * factorial(n - 1));
}

// 03. 반복적인 팩토리얼 계산 프로그램

int factorial_iter(int n) {
	int i, result = 1;
	for (i = 1; i <= n; i++)
		result = result * i;
	return (result);
}
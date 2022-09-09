// �Ǻ���ġ ���� : ��ȯȣ���� ����ϸ� ��ȿ������ ����

// 01. ��ȯ���� �Ǻ���ġ ���� ��� ���α׷� -> ��ȿ������
//     ��ȿ������ ����: ���� �� �ߺ��Ǽ� ����. n�� Ŀ������ �� ������

int fib(int n) {
	if (n == 0) return 0;
	if (n == 1) return 1;
	return (fib(n - 1) + fib(n - 2));
}

// 02. �ݺ����� �Ǻ���ġ ���� ��� ���α׷�

int fib_iter(int n) {
	if (n == 0) return 0;
	if (n == 1) return 1;

	int pp = 0;
	int p = 1;
	int result = 0;

	for (int i = 2; i <= n; i++) {
		result = p + pp;
		pp = p;
		p = result;
	}
	return result;
}

// (���� ����ε� �ٸ� ������� �ڵ�)
// int fib_iter(int n) {
//  	if (n < 2) return n;
//	else {
//		int i, tmp, current = 1, last = 0;
//		for (i = 2; i <= n; i++) {
//			tmp = current;
//			current += last;
//			last = tmp;
//		}
//		return tmp;
//	}
//}
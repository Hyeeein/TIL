// 피보나치 수열 : 순환호출을 사용하면 비효율적인 예시

// 01. 순환적인 피보나치 수열 계산 프로그램 -> 비효율적임
//     비효율적인 이유: 같은 항 중복되서 계산됨. n이 커질수록 더 심해짐

int fib(int n) {
	if (n == 0) return 0;
	if (n == 1) return 1;
	return (fib(n - 1) + fib(n - 2));
}

// 02. 반복적인 피보나치 수열 계산 프로그램

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

// (같은 결과인데 다른 방법으로 코딩)
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
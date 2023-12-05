// 1번
public class Soojebi {
    public static void main(String[] args) {
        int i;
        int []a = {0, 1, 2, 3};

        for (i=0; i<4; i++) {
            System.out.print(a[i]+" ");
        }
    }
}

// 2번
public class Soojebi {
    public static void main(String[] args) {
        int i = 3;
        int k = 1;

        switch(i) {
            case 0:
            case 1:
            case 2:
            case 3: k=0;
            case 4: k+=3;
            case 5: k-=10;
            default: k--;
        }

        System.out.print(k)
    }
}


// 3번
class Parent{
    public void show() {
        System.out.println("Parent");
    }
}
class Child extends Parent {
    public void show() {
        System.out.println("Child");
    }
}
public class Soojebi {
    public static void main(String[] args){
        Parent pa=____Child();
        pa.show()
    }
}

// 4번
class A {
    private int a;
    public A(int a) {
        this.a = a;
    }
    public void display(){
        System.out.println("a="+a);
    }
}

class B {
    public B(int a) {
        super(a);
        super.display( );
    }
}

public class Main {
    public static void main(String[] args) {
        B obj = new B(10);
    }
}


// 5번
public class Soojebi {
    public static void main(String[] args) {
        int i=0;
        int sum=0;

        while (i<10) {
            i++;
            if (i%2==1)
                continue;
            sum += i;
        }
        System.out.println(sum);
    }
}

// 6번
abstract class Vehicle {
    private String name;
    abstract public String getName(String val);
    public String getName() {
        return "Vehicle name:" + name;
    }
    public void setName(String val) {
        name = val;
    }
}
class Car extends Vehicle {
    public Car(String val) {
        setName(val);
    }
    public String getName(String val) {
        return "Car name :" + val
    }
}
public class Soojebi {
    public static void main(String[] args) {
        Vehicle obj = new Car("Spark");
        System.out.println(obj.getName());
    }
}

// 7번
class Soojebi {
    public static void main (String[] args) {
        int []a = new int[8];
        int i=0;
        int n=10;

        while ( ) {
            a[i++] = ();
            n /= 2;
        }
        
        for (i=7; i>=0; i--) {
            System.out.print(a[i]);
        }
    }
}

// 8번
public class Soojebi {
    public static void main(String[] args) {
        int[][] a = new int[][];
        for (int i=0; i<3; i++) {
            for (int j=0; j<5; j++) {
                a[i][j] = j*3+(j+1);
                System.out.print(a[i][j] + " ");
            }
            System.out.println();
        }
    }
}

// 9번
class Parent {
    public int compute (int num) {
        if (num <= 1) return num;
        return compute(num-1)+compute(num-2);
    }
}
class Child extends Parent{
    public int compute(int num) {
        if (num <= 1) return num;
        return compute(num-1)+compute(num-3);
    }
}
class Soojebi {
    public static void main(String[] args) {
        Parent obj = new Child();
        System.out.print(obj.compute(4)):
    }
}

// 10번
public class Soojebi {
    public static void main(String[] args) {
        int[][] arr = new int[][]{{45, 50, 75}, {89}};
        System.out.println(arr[0].length);
        System.out.println(arr[1].length);
        System.out.println(arr[0][0]);
        System.out.println(arr[0][1]);
        System.out.println(arr[1][0]);
    }
}

// 11번
public class Soojebi {
    public static void main(String[] args) {
        int i, j;
        for (j=0, i=0; i<=5; i++) {
            j+=i;
            System.out.print(i);
            if (i==5) {
                System.out.print("=");
                System.out.print(j);
            }
            else {
                System.out.print("+");
            }
        }
    }
}

// 12번
class ovr1 {
    public static void main (Stringp[ args]) {
        ovr1 a1 = new ovr1();
        ovr2 a2 = new ovr2();
    
        System.out.print(a1.san(3, 2) + a2.san(3, 2));
    }
    int san(int x, int y) {
        return x + y;
    }
}
class ovr2 extends ovr1 {
    int san(int x, int y) {
        return x-y + super.san(x, y);
    }
}

// 13번
class Soojebi {
    static private Soojebi instance = null;
    private int count = 0;
    static public Soojebi get() {
        if (instance == null) {
            instance = new Soojebi();
        }
        return instance;
    }
    public void count(){ count++; }
    public int getCount(){ return count; }
}
public class Soojebi2 {
    public static void main(String[] args) {
        Soojebi s1 = Soojebi.get();
        s1.count();
        Soojebi s2 = Soojebi.get();
        s2.count();
        Soojebi s3 = Soojebi.get();
        s3.count();
        System.out.print(s1.getCount());
    }
}

// 14번
public class Soojebi {
    public static void main(String[] args) {
        System.out.print(Soojebi.check(1));
    }
    ______ String check(int num) {
        return (num >= 0) ? "positive" : "negative";
    }
}

// 15번
public class Soojebi {
    public static void main(String[] args) {
        int a = 3, b = 4, c = 3, d = 5;
        if ((a==2 | a==c) & !(c>d) & (1==b^c!=d)) {
            a = b + c;
            if (7 == b ^ c != a) {
                System.out.println(a);
            }
            else {
                System.out.println(b);
            }
        }
        else {
            a = c + d;
            if (7 == c ^ d != a) {
                System.out.println(a);
            }
            else {
                System.out.println(d);
            }
        }
    }
}


// =============
// 16번
public class Soojebi{
    public static void main(String[] args) {
        int k = 10;
        int a = 3;

        switch (k++) {
            case 10 : a += 2;
            case 11 : a *= k;
            case 8 : break;
            case 9 : a %= 2;
        }
        System.out.println(a);
        System.out.println(k);
    }
}

// 17번
public class Soojebi{
    public static void main(String[] args) {
        for (int m=0; m<10; m++) {
            if (m%2 == 0)
                continue;
            System.out.print(m);
        }
    }
}

// 18번
public class Soojebi {
    public static void main(String[] args) {
        int x=5, y=0, z=0;
        y = x++;
        z = --x;
        System.out.println(x + "," + y + "," + z);
    }
}

// 19번
class A {
    private String s;
    A(){}
    A(String s) {
        this.s = s + "A";
    }
    public void fn(String s) {
        System.out.println(this.s + s);
    }
}

class B {
    private String s;
    B(String s) {
        this.s = s + "B";
    }
    public void fn(String s) {
        System.out.println(this.s + s);
    }
}

public class Soojebi {
    public static void main(String[] args) {
        A a = new B("Hello");
        a.fn("Hi");
    }
}

// 20번
public class Soojebi {
    public static void main(String args[]) {
        String s = "red";
        boolean [] b = new boolean[1];
        if(b[0]) s = "blue";
        System.out.println(s);
    }
}
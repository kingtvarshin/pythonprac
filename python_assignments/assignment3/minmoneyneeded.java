import java.util.*;
public class Main {
    public static void main(String args[]) {
        int[] price = { 1, 2, 3, 4, 5};
		System.out.println(minimumMoneyBU(price));
    }

    public static int minimumMoneyBU(int[] price) {

		int[] strg = new int[price.length];

		strg[0] = 0;
		if (price[1] == -1) {
			strg[1] = Integer.MAX_VALUE;
		} else {
			strg[1] = price[1];
		}
		for (int i = 2; i < price.length; i++) {
			int min;
			if (price[i] == -1) {
				min = Integer.MAX_VALUE;
			} else {
				min = price[i];
			}
			int left = 1;
			int right = i - 1;
			while (left <= right) {
				int lc = strg[left];
				int rc = strg[right];
				int tw;
				if (lc != Integer.MAX_VALUE && rc != Integer.MAX_VALUE) {
					tw = lc + rc;
					if (tw < min) {
						min = tw;
					}
				}
				left++;
				right--;
			}
			strg[i] = min;
		} 
		if (strg[strg.length - 1] == Integer.MAX_VALUE) {
			return -1;
		} else {
			return strg[strg.length - 1];
		}
	}
}

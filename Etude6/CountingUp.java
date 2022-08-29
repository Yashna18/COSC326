
/** 
 * @author Remin Reji Mathew
 * @author Yashna Shetty
 * this program takes two numbers from
 * the user and returns NCK
 * first it takes the smallest value
 * then manually multiples, taking the gcd of 
 * ans and i - which hold the numerator
 * and denominator, respectively. 
*/
import java.util.Scanner;

public class CountingUp {

  /**
   * @param n user input1
   * @param k user input2
   * @return the answer
   *         func returns the final product
   *         via nCk
   */

  public static long nCk(long n, long k) {
    long ans = 1;

    if (n - k < k) {
      k = n - k;
    }
    if (k == 1) {
      ans = n;
    } else if (k != 0 && n != 0) {
      long i = 1;
      while (i <= k) {
        // for overflow and simplifying
        long gcd_num = gcd(ans, i);
        ans /= gcd_num;
        ans *= n / (i / gcd_num);

        n--;
        i++;
      }
    } else {
      ans = 0;
    }

    return ans;
  }

  /**
   * 
   * @param n1 top line holder var
   * @param n2 bottom line holder var
   * @return gcd of current ans and i
   */
  // for overflow and simplifying
  static long gcd(long a, long b) {
    long gcd = 1;

    for (int i = 1; i <= a && i <= b; ++i) {
      if (a % i == 0 && b % i == 0) {
        gcd = i;
      }
    }
    return gcd;
  }

  public static void main(String[] args) {
    Scanner input = new Scanner(System.in);

    System.out.print("Enter the value of N: ");
    long n = input.nextLong();
    System.out.print("Enter the value of K: ");
    long k = input.nextLong();

    System.out.println(nCk(n, k));
    input.close();
  }
}

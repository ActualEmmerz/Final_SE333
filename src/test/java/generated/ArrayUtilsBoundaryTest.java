package generated;

import org.junit.Test;
import static org.junit.Assert.*;
import org.apache.commons.lang3.ArrayUtils;

public class ArrayUtilsBoundaryTest {

    @Test
    public void testIndexOfBoundaryValues() {
        int[] sizes = {0, 1, 5, 10};
        int[] searchValues = {-1, 0, 1};

        for (int s : sizes) {
            int[] arr = new int[s];
            for (int i = 0; i < s; i++) {
                arr[i] = i;
            }

            for (int v : searchValues) {
                int expected = (v >= 0 && v < s) ? v : -1;
                int actual = ArrayUtils.indexOf(arr, v);
                assertEquals("size=" + s + " value=" + v, expected, actual);
            }
        }
    }

}

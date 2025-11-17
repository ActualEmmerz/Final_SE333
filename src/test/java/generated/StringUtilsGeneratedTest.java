package generated;

import org.junit.Test;
import static org.junit.Assert.*;
import org.apache.commons.lang3.StringUtils;

public class StringUtilsGeneratedTest {

    @Test
    public void testIsBlank() {
        // meaningful assertions for StringUtils.isBlank
        assertTrue(StringUtils.isBlank(null));
        assertTrue(StringUtils.isBlank(""));
        assertTrue(StringUtils.isBlank("   "));
        assertFalse(StringUtils.isBlank("a"));
        assertFalse(StringUtils.isBlank(" a "));
    }

}

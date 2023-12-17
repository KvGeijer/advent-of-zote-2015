use std::collections::HashSet;

fn main() {
    let mut r1: u64;
    let mut r4: u64 = 123;
    let mut seen_r4_values = HashSet::new();
    let mut last = 0;

    // Initial steps
    loop {
        r4 &= 456;
        if r4 == 72 {
            break;
        }
    }

    r4 = 0;
    loop {
        // Main program
        r1 = r4 | 65536;
        r4 = 16031208;

        // Operations
        loop {
            r4 += r1 & 255;
            r4 = (r4 & 16777215) * 65899 & 16777215;

            if 256 > r1 {
                break;
            }

            r1 = r1 / 256; // Optimized version of the inner loop
        }

        // Check for new or seen r4 values
        if seen_r4_values.contains(&r4) {
            println!("Part 2: {last}");
            break;
        } else {
            last = r4;
            seen_r4_values.insert(r4);
        }
    }
}

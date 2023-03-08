import perl

print("We're in Python now.")

# Compile some C code through Perl.
perl.compile_c(r"""
    void high_performance_loop(int count)
    {
        puts("We're in C now.");
        for(int i = 0; i < count; ++i) {
            printf("High-performance loop %d\n", i);
        }
    }
""")

# Call the C function for blazing fast looping code.
perl.high_performance_loop(10)

print("Back in Python.")

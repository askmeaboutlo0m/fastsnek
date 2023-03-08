#!/usr/bin/env perl
use 5.020;
use warnings;
use Inline;
use Inline::Python qw(py_eval);

say "We're in Perl now.";

sub compile_c {
    my ($code) = @_;
    Inline->bind(C => $code);
}

py_eval('import fastsnek');

say "Back in Perl.";

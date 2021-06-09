static pointer (*ftab[7])();

#define QUOTE_STRINGS_SIZE 43
static char *quote_strings[QUOTE_STRINGS_SIZE]={
    "quote",
    "|,|",
    "|,@|",
    "append",
    "list",
    "cons",
    "\"01\"",
    "find",
    "(8)",
    ":element-type",
    ":bit",
    ":fill-pointer",
    "make-array",
    "\"01\"",
    "fill-pointer",
    "pathname",
    "deg2rad",
    "rad2deg",
    "\"@(#)$Id: readmacro.l,v 1.1.1.1 2003/11/20 07:46:31 eus Exp $\"",
    "\"LISP\"",
    "\"LISP\"",
    "*package*",
    "\"no such package\"",
    "(newline space rubout page tab backspace return linefeed)",
    "read-backquote",
    "\"(file &optional ch)\"",
    "conv-bq",
    "\"(x)\"",
    "conscons",
    "\"(x y)\"",
    "read-comma",
    "\"(file &optional ch)\"",
    "read-binary",
    "\"(f ch n)\"",
    "read-bit-vector",
    "\"(f ch n)\"",
    "get-macro-character",
    "read-pathname",
    "\"(f ch n)\"",
    "read-radian",
    "\"(strm char num)\"",
    "read-degree",
    "\"(strm char num)\"",
  };
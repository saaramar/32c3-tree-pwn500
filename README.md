# 32c3-tree-pwn500
Exploit pwn challenge from 32c3 ctf. The vulnerability is classic dangling pointer from the clipboard, points to a string node.
Updating this node cause realloc --> free old chunk, which is still referenced from the clipboard symbol.
The exploit is really simple and trivial - first, I exploit the dangling pointer to info disc, read the address of my chunk
in the heap, get from this the address of libc, and then forge the vtable of my object for code execution.
Instead of doing a classic rop (mprotect and jump to shellcode), I jump to system (Not important, both ways extremely easy).
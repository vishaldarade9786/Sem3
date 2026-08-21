section .data
    msg db 'Hello, World!', 10   ; 10 is the ASCII code for newline (\n)
    len equ $ - msg             ; Calculates string length automatically

section .text
    global _start

_start:
    ; --- sys_write (print to screen) ---
    mov rax, 1          ; System call number 1 = sys_write
    mov rdi, 1          ; File descriptor 1 = stdout (screen)
    mov rsi, msg        ; Address of string to print
    mov rdx, len        ; Number of bytes to print
    syscall

    ; --- sys_exit (exit program) ---
    mov rax, 60         ; System call number 60 = sys_exit
    xor rdi, rdi        ; Exit code 0 (success)
    syscall

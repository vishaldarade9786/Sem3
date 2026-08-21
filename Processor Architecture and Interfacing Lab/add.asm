section .data
    fmt db "Result: %d", 10, 0   ; Format string like printf in C ("Result: %d\n")

section .text
    global main
    extern printf                ; Tell NASM we'll use C's printf function

main:
    ; --- 1. Perform Addition ---
    mov rax, 12                  ; Load first number (12) into RAX
    add rax, 25                  ; Add second number (25) to RAX (RAX is now 37)

    ; --- 2. Print with printf ---
    mov rsi, rax                 ; 2nd argument for printf: the integer value (37)
    mov rdi, fmt                 ; 1st argument for printf: the format string address
    mov rax, 0                   ; 0 floating-point arguments used
    call printf

    ; --- 3. Return from main ---
    mov rax, 0                   ; Return status 0
    ret
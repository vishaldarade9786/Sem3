section .data
	num1 dq 12
	num2 dq 12
	newline db 10	;
section .bss
	buffer resb 20	;

section .text
	global _start
_start:
	mov rax, [num1] ;
	imul qword [num2] ;
	mov rbx, 10	;
	mov rdi, buffer + 19	;
	mov byte [rdi],0	;
.convert_loop:
	xor rdx, rdx	;
	div rbx 		;
	add dl, '0'		;
	dec rdi			;
	mov [rdi], dl	;
	test rax, rax	;
	jnz .convert_loop ;
	mov rdx, buffer + 19
	sub rdx, rdi	;
	mov rax, 1		;
	mov rsi, rdi	;
	mov rdi, 1		;
	syscall

	mov rax, 1 			;
	mov rdi, 1 			;
	mov rsi, newline 	;
	mov rdx, 1 			;
	syscall

	mov rax, 60 	;
	xor rdi, rdi 	;
	syscall
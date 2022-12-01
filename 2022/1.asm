; nasm -f elf64 1.asm; ld -s -o 1 1.o; rm 1.o

section .rodata
file_name:
    db "1.txt", 0

section .bss
elf_sums:
    resq 0x1000
buffer:
    resb 0x10
buffer_end:
    resb 1

section .text

global _start

_start:
    mov rax, 2
    mov rdi, file_name
    mov rsi, 0
    mov rdx, 0
    syscall  ; fd = open("1.txt", 0, 0)

    mov r8, rax
    mov rax, 9
    mov rdi, 0
    mov rsi, 0x4000
    mov rdx, 1
    mov r10, 2
    mov r9, 0
    syscall  ; file = mmap(NULL, 0x4000, PROT_READ, MAP_PRIVATE, fd, 0)
    
    mov r11, rax  ; file
    dec r11
    xor r12, r12  ; file[i]
    xor r13, r13  ; new_lines
    xor r14, r14  ; sum
    xor rax, rax  ; integer
    mov r15, elf_sums  ; elf_sums

file_loop:
    inc r11
    mov r12b, byte [r11]  ; file[i]
    test r12b, r12b
    jz file_loop_exit
    cmp r12b, 10  ; \n
    je file_loop_new_line
    cmp r12b, 0x30  ; 0
    jb file_loop
    cmp r12b, 0x39  ; 9
    ja file_loop
    cmp r13, 1
    je file_loop_one_new_line
    cmp r13, 2
    je file_loop_two_new_line
file_loop_process_character:
    sub r12b, 0x30
    imul rax, rax, 10
    add rax, r12
    jmp file_loop
file_loop_new_line:
    inc r13
    jmp file_loop
file_loop_one_new_line:
    xor r13, r13
    add r14, rax
    xor rax, rax
    jmp file_loop_process_character
file_loop_two_new_line:
    xor r13, r13
    add r14, rax
    xor rax, rax
    mov qword [r15], r14
    xor r14, r14
    add r15, 8
    jmp file_loop_process_character
file_loop_exit:
    add r14, rax
    mov qword [r15], r14

    mov r11, elf_sums  ; elf_sums
    sub r11, 8
    xor r12, r12  ; best_1
    xor r13, r13, ; best_2
    xor r14, r14  ; best_3

best_loop:
    add r11, 8
    cmp r11, r15
    ja best_loop_exit
    mov rax, qword [r11]
best_loop_comparason:
    cmp rax, r12
    ja best_loop_1
    cmp rax, r13
    ja best_loop_2
    cmp rax, r14
    ja best_loop_3
    jmp best_loop
best_loop_1:
    xchg r12, rax
    jmp best_loop_comparason
best_loop_2:
    xchg r13, rax
    jmp best_loop_comparason
best_loop_3:
    xchg r14, rax
    jmp best_loop_comparason

best_loop_exit:
    mov rax, r12
    call output_int

    mov rax, r12
    add rax, r13,
    add rax, r14
    call output_int

    mov rax, 60
    mov rdi, 0
    syscall  ; exit(0)

output_int:
    mov rbx, buffer_end
    mov byte [rbx], 10  ; \n
    mov rcx, 10

output_int_loop:
    dec rbx
    xor rdx, rdx
    div rcx
    add dl, 0x30
    mov byte [rbx], dl
    test rax, rax
    jnz output_int_loop

    mov rax, 1
    mov rdi, 1
    mov rsi, rbx
    mov rdx, buffer_end
    sub rdx, rbx
    inc rdx
    syscall
    ret

